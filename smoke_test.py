#!/usr/bin/env python3
"""
smoke_test.py – Exercise the SuzieQ API wrapper against a live server.

SuzieQ's REST API is read-only (GET only), so this smoke test is always
safe to run against any server, including production.

Environment variables:
    SUZIEQ_URL          Base URL, e.g. "https://127.0.0.1:8000"  (required)
    SUZIEQ_API_KEY      API key configured in ~/.suzieq/suzieq.cfg  (required)
    SUZIEQ_VERIFY_SSL   Set to "false" to disable SSL verification (default: true)
    SUZIEQ_TIMEOUT      Request timeout in seconds (default: 60)

Usage:
    python smoke_test.py                              # run all tests
    python smoke_test.py --no-color                   # plain output for log files
    python smoke_test.py --skip show_path,show_fs     # skip specific tests
"""

import argparse
import os
import sys
import time

import suzieq_api_wrapper as suzieq


# ── Output ────────────────────────────────────────────────────────────────

_passed = _failed = _skipped = _warned = 0
_failures: list = []
_warnings: list = []
_skip_prefixes: list = []
_use_color = True


def _section(title: str):
    print(f"\n[{title}]")


def _ok(label: str, detail: str = ""):
    global _passed
    _passed += 1
    if _use_color:
        suffix = f"  \033[2m{detail}\033[0m" if detail else ""
        print(f"  \033[32mPASS\033[0m  {label}{suffix}")
    else:
        suffix = f"  {detail}" if detail else ""
        print(f"  PASS  {label}{suffix}")


def _fail(label: str, err):
    global _failed
    _failed += 1
    _failures.append((label, str(err)))
    if _use_color:
        print(f"  \033[31mFAIL\033[0m  {label}  \033[2m{err}\033[0m")
    else:
        print(f"  FAIL  {label}  {err}")


def _skip(label: str, reason: str = ""):
    global _skipped
    _skipped += 1
    suffix = f"  ({reason})" if reason else ""
    if _use_color:
        print(f"  \033[33mSKIP\033[0m  {label}{suffix}")
    else:
        print(f"  SKIP  {label}{suffix}")


def _warn_msg(label: str, err, note: str = None):
    global _warned
    _warned += 1
    suffix = f"  ({note})" if note else ""
    _warnings.append((label, f"{err}{suffix}"))
    if _use_color:
        print(f"  \033[33mWARN\033[0m  {label}  \033[2m{err}{suffix}\033[0m")
    else:
        print(f"  WARN  {label}  {err}{suffix}")


def _should_skip(label: str) -> bool:
    return any(label.startswith(p) for p in _skip_prefixes)


_FAILED = object()


def run(label: str, fn, *args, detail_fn=None, **kwargs):
    """Call *fn* and record PASS or FAIL.

    Returns the call's return value, or ``_FAILED`` on exception.
    """
    if _should_skip(label):
        _skip(label, "--skip")
        return _FAILED
    try:
        result = fn(*args, **kwargs)
        detail = ""
        if detail_fn is not None and result is not None:
            try:
                detail = str(detail_fn(result))
            except Exception:
                pass
        _ok(label, detail)
        return result
    except Exception as exc:
        _fail(label, exc)
        return _FAILED


def warn(label: str, fn, *args, note: str = None,
         detail_fn=None, **kwargs):
    """Call *fn*; record PASS or WARN (non-fatal)."""
    if _should_skip(label):
        _skip(label, "--skip")
        return _FAILED
    try:
        result = fn(*args, **kwargs)
        detail = ""
        if detail_fn is not None and result is not None:
            try:
                detail = str(detail_fn(result))
            except Exception:
                pass
        _ok(label, detail)
        return result
    except Exception as exc:
        _warn_msg(label, exc, note)
        return _FAILED


# ── helpers ───────────────────────────────────────────────────────────────

def _count(result):
    """Return a short count description."""
    if isinstance(result, list):
        return f"{len(result)} record(s)"
    if isinstance(result, dict):
        return f"{len(result)} key(s)"
    return str(result)


# ── Smoke tests ───────────────────────────────────────────────────────────

def main():
    global _use_color, _skip_prefixes

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-color", action="store_true",
                        help="Disable ANSI color output")
    parser.add_argument("--skip", default="",
                        help="Comma-separated prefixes to skip")
    args = parser.parse_args()
    _use_color = not args.no_color and sys.stdout.isatty()
    if args.skip:
        _skip_prefixes.extend(
            s.strip() for s in args.skip.split(",") if s.strip()
        )

    url = os.environ.get("SUZIEQ_URL")
    api_key = os.environ.get("SUZIEQ_API_KEY")
    if not url or not api_key:
        print("Error: SUZIEQ_URL and SUZIEQ_API_KEY must be set.")
        sys.exit(2)

    verify_ssl = os.environ.get("SUZIEQ_VERIFY_SSL", "true").lower() != "false"
    timeout = int(os.environ.get("SUZIEQ_TIMEOUT", "60"))

    client = suzieq.SuzieQ(
        url=url,
        api_key=api_key,
        verify_ssl=verify_ssl,
        timeout=timeout,
    )

    start = time.monotonic()
    print(f"SuzieQ smoke test – {url}")
    print(f"  verify_ssl={verify_ssl}  timeout={timeout}s")

    # ── device ────────────────────────────────────────────────────────
    _section("device")
    devices = run("show_device", client.show_device, detail_fn=_count)
    run("summarize_device", client.summarize_device, detail_fn=_count)
    run("unique_device (os)", client.unique_device, what="os",
        detail_fn=_count)
    run("top_device (version)", client.top_device, what="version",
        count="5", detail_fn=_count)

    # ── namespace ─────────────────────────────────────────────────────
    _section("namespace")
    ns = run("show_namespace", client.show_namespace, detail_fn=_count)
    run("summarize_namespace", client.summarize_namespace, detail_fn=_count)

    # ── bgp ───────────────────────────────────────────────────────────
    _section("bgp")
    run("show_bgp", client.show_bgp, detail_fn=_count)
    run("summarize_bgp", client.summarize_bgp, detail_fn=_count)
    run("unique_bgp (state)", client.unique_bgp, what="state",
        detail_fn=_count)
    run("top_bgp (numChanges)", client.top_bgp, what="numChanges",
        count="5", detail_fn=_count)
    warn("assert_bgp", client.assert_bgp, detail_fn=_count,
         note="requires active BGP peers")

    # ── ospf ──────────────────────────────────────────────────────────
    _section("ospf")
    warn("show_ospf", client.show_ospf, detail_fn=_count,
         note="requires OSPF config")
    warn("summarize_ospf", client.summarize_ospf, detail_fn=_count,
         note="requires OSPF config")
    warn("assert_ospf", client.assert_ospf, detail_fn=_count,
         note="requires OSPF config")

    # ── interface ─────────────────────────────────────────────────────
    _section("interface")
    run("show_interface", client.show_interface, detail_fn=_count)
    run("summarize_interface", client.summarize_interface,
        detail_fn=_count)
    run("unique_interface (state)", client.unique_interface,
        what="state", detail_fn=_count)
    run("top_interface (mtu)", client.top_interface, what="mtu",
        count="5", detail_fn=_count)
    warn("assert_interface", client.assert_interface, detail_fn=_count,
         note="may report failures if peers disagree on MTU")

    # ── route ─────────────────────────────────────────────────────────
    _section("route")
    run("show_route", client.show_route, detail_fn=_count)
    run("summarize_route", client.summarize_route, detail_fn=_count)
    run("unique_route (protocol)", client.unique_route, what="protocol",
        detail_fn=_count)
    warn("lpm_route (10.0.0.1)", client.lpm_route, address="10.0.0.1",
         detail_fn=_count, note="needs routes in default VRF")

    # ── address ───────────────────────────────────────────────────────
    _section("address")
    run("show_address", client.show_address, detail_fn=_count)
    run("summarize_address", client.summarize_address, detail_fn=_count)

    # ── arpnd ─────────────────────────────────────────────────────────
    _section("arpnd")
    run("show_arpnd", client.show_arpnd, detail_fn=_count)
    run("summarize_arpnd", client.summarize_arpnd, detail_fn=_count)

    # ── lldp ──────────────────────────────────────────────────────────
    _section("lldp")
    run("show_lldp", client.show_lldp, detail_fn=_count)
    run("summarize_lldp", client.summarize_lldp, detail_fn=_count)

    # ── mac ───────────────────────────────────────────────────────────
    _section("mac")
    warn("show_mac", client.show_mac, detail_fn=_count,
         note="requires L2 domain")
    warn("summarize_mac", client.summarize_mac, detail_fn=_count,
         note="requires L2 domain")

    # ── vlan ──────────────────────────────────────────────────────────
    _section("vlan")
    warn("show_vlan", client.show_vlan, detail_fn=_count,
         note="requires VLAN config")

    # ── evpnVni ───────────────────────────────────────────────────────
    _section("evpnVni")
    warn("show_evpnvni", client.show_evpnvni, detail_fn=_count,
         note="requires EVPN config")
    warn("assert_evpnvni", client.assert_evpnvni, detail_fn=_count,
         note="requires EVPN config")

    # ── mlag ──────────────────────────────────────────────────────────
    _section("mlag")
    warn("show_mlag", client.show_mlag, detail_fn=_count,
         note="requires MLAG config")

    # ── inventory ─────────────────────────────────────────────────────
    _section("inventory")
    warn("show_inventory", client.show_inventory, detail_fn=_count,
         note="not all platforms report inventory")

    # ── fs ────────────────────────────────────────────────────────────
    _section("fs")
    warn("show_fs", client.show_fs, detail_fn=_count,
         note="not all platforms report filesystem")

    # ── topology ──────────────────────────────────────────────────────
    _section("topology")
    run("show_topology (lldp)", client.show_topology, via=["lldp"],
        detail_fn=_count)
    run("summarize_topology", client.summarize_topology, detail_fn=_count)

    # ── path ──────────────────────────────────────────────────────────
    _section("path")
    warn("show_path", lambda: "skipped — requires src/dest IPs",
         note="provide specific IPs to test path tracing")

    # ── network (find) ────────────────────────────────────────────────
    _section("network")
    warn("find_network", lambda: "skipped — requires target address",
         note="provide an address to test network find")

    # ── devconfig ─────────────────────────────────────────────────────
    _section("devconfig")
    warn("show_devconfig", client.show_devconfig, detail_fn=_count,
         note="may take time on large networks")

    # ── sqPoller ──────────────────────────────────────────────────────
    _section("sqPoller")
    run("show_sqpoller", client.show_sqpoller, detail_fn=_count)
    run("summarize_sqpoller", client.summarize_sqpoller, detail_fn=_count)

    # ── table (meta) ──────────────────────────────────────────────────
    _section("table")
    run("show_tables", client.show_tables, detail_fn=_count)
    run("summarize_tables", client.summarize_tables, detail_fn=_count)

    # ── Summary ───────────────────────────────────────────────────────
    elapsed = time.monotonic() - start
    print(f"\n{'─' * 60}")
    parts = [f"{_passed} passed"]
    if _failed:
        parts.append(f"{_failed} FAILED")
    if _warned:
        parts.append(f"{_warned} warned")
    if _skipped:
        parts.append(f"{_skipped} skipped")
    print(f"  {', '.join(parts)}  ({elapsed:.1f}s)")

    if _failures:
        print("\nFailures:")
        for label, err in _failures:
            print(f"  {label}: {err}")

    if _warnings:
        print("\nWarnings:")
        for label, err in _warnings:
            print(f"  {label}: {err}")

    sys.exit(1 if _failed else 0)


if __name__ == "__main__":
    main()
