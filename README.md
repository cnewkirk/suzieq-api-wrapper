# suzieq-api-wrapper

[![PyPI](https://img.shields.io/pypi/v/suzieq-api-wrapper)](https://pypi.org/project/suzieq-api-wrapper/)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An unofficial, dependency-minimal Python 3 client for the
[SuzieQ](https://github.com/netenglabs/suzieq) REST API (v2).

> **SuzieQ resources**: [GitHub](https://github.com/netenglabs/suzieq) ·
> [Documentation](https://suzieq.readthedocs.io/) ·
> [REST API reference](https://suzieq.readthedocs.io/en/latest/rest-server/)

## Features

- Covers all 21 SuzieQ tables with all supported verbs
- One method per table-verb combination — flat, discoverable namespace
- Single runtime dependency: [`requests`](https://docs.python-requests.org/)
- Synchronous and straightforward — no async complexity
- Typed exception hierarchy — catch `AuthenticationError`, `NotFoundError`,
  etc. without importing `requests`
- Full test suite (237 tests, mocked HTTP — no live server required)
- Read-only smoke test for live server validation

## Installation

```bash
pip install suzieq-api-wrapper
```

**From source** (latest development version):

```bash
git clone https://github.com/cnewkirk/suzieq-api-wrapper.git
cd suzieq-api-wrapper
pip install .
```

## Quick start

```python
import suzieq_api_wrapper as suzieq

client = suzieq.SuzieQ(
    url="https://127.0.0.1:8000",
    api_key="your-api-key-here",
)

# Show all devices
devices = client.show_device()
for dev in devices:
    print(dev["hostname"], dev["os"], dev["status"])

# Show only established BGP peers
peers = client.show_bgp(state="Established")

# Assert all BGP sessions pass
failures = client.assert_bgp(result="fail")

# Longest-prefix match
match = client.lpm_route(address="10.0.0.1")

# Find where a MAC lives in the network
location = client.find_network(address=["aa:bb:cc:dd:ee:ff"])

# Show interfaces that are down
down = client.show_interface(state="down")

# Summarize routes by protocol
summary = client.summarize_route()

# Unique operating systems across the network
os_list = client.unique_device(what="os")
```

## Error handling

HTTP errors raise typed exceptions — no need to import `requests`:

```python
import suzieq_api_wrapper as suzieq

try:
    result = client.show_bgp()
except suzieq.AuthenticationError:
    print("Check your API key")
except suzieq.NotFoundError:
    print("Unknown table or verb")
except suzieq.ValidationError:
    print("Invalid parameter value")
except suzieq.SuzieQError:
    print("Unexpected error")
```

Full hierarchy: `SuzieQHTTPError` (base, exposes `.status_code` and
`.response`) → `AuthenticationError` (401), `NotFoundError` (404),
`BadRequestError` (405), `ValidationError` (422), `ServerError` (5xx).

## API coverage

Every table supports `show`, `summarize`, and `top`.  All except `devconfig`
support `unique`.  Special verbs are noted below.

| Table | Verbs | Description |
|---|---|---|
| `address` | show, summarize, unique, top | IP address assignments |
| `arpnd` | show, summarize, unique, top | ARP / IPv6 Neighbor Discovery |
| `bgp` | show, summarize, unique, top, **assert** | BGP peer state |
| `device` | show, summarize, unique, top | Device inventory |
| `devconfig` | show, summarize, top | Raw device configurations |
| `evpnVni` | show, summarize, unique, top, **assert** | EVPN VNI |
| `fs` | show, summarize, unique, top | Filesystem usage |
| `interface` | show, summarize, unique, top, **assert** | Interface state |
| `inventory` | show, summarize, unique, top | Hardware inventory |
| `lldp` | show, summarize, unique, top | LLDP neighbors |
| `mac` | show, summarize, unique, top | MAC address table |
| `mlag` | show, summarize, unique, top | MLAG status |
| `namespace` | show, summarize, unique, top | Namespace summary |
| `network` | **find**, show\*, summarize\*, unique\*, top\* | Network-wide search |
| `ospf` | show, summarize, unique, top, **assert** | OSPF neighbor state |
| `path` | show, summarize, unique, top | L3 path trace |
| `route` | show, summarize, unique, top, **lpm** | Routing table |
| `sqPoller` | show, summarize, unique, top | Poller health |
| `table` | show, summarize, unique, top | Meta: available tables |
| `topology` | show, summarize, unique, top | Multi-protocol topology |
| `vlan` | show, summarize, unique, top | VLAN table |

\* Deprecated — redirects to `namespace` on the server side.

## Authentication

SuzieQ uses API key authentication.  Generate a key with
`openssl rand -hex 20` and set it as `rest.API_KEY` in
`~/.suzieq/suzieq.cfg`.

Pass `verify_ssl=False` to disable certificate verification (useful for
self-signed certs in lab environments):

```python
client = suzieq.SuzieQ(
    url="https://127.0.0.1:8000",
    api_key="your-api-key-here",
    verify_ssl=False,
)
```

## Smoke testing

`smoke_test.py` exercises the wrapper against a real SuzieQ REST server.
Since SuzieQ's API is read-only, the smoke test is always safe to run
against any server, including production.

Tests for optional features (EVPN, MLAG, OSPF, etc.) are reported as
**WARN** (non-fatal) rather than FAIL.

```bash
export SUZIEQ_URL="https://127.0.0.1:8000"
export SUZIEQ_API_KEY="your-api-key-here"
export SUZIEQ_VERIFY_SSL="false"   # omit or set to "true" for valid certs
export SUZIEQ_TIMEOUT="60"         # per-request timeout in seconds (default 60)

python smoke_test.py
python smoke_test.py --no-color                   # plain output for log files
python smoke_test.py --skip show_path,show_fs     # skip specific tests
```

## Development

```bash
git clone https://github.com/cnewkirk/suzieq-api-wrapper.git
cd suzieq-api-wrapper
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest tests/ -v
```

## Contributing

Bug reports and pull requests are welcome on
[GitHub](https://github.com/cnewkirk/suzieq-api-wrapper).
See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Acknowledgements

This library was designed and tested by a human, with implementation
assistance from [Claude Code](https://claude.ai/code) (Anthropic). All API
shapes are derived from the [SuzieQ](https://github.com/netenglabs/suzieq)
open-source project.

[requests](https://docs.python-requests.org/) handles all HTTP communication.
