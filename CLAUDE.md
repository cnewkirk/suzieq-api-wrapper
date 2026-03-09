# CLAUDE.md — suzieq-api-wrapper

This file gives Claude Code the context needed to work on this project
without prior conversation history.

## Project purpose

A thin, synchronous Python 3 wrapper for the SuzieQ REST API (v2).
Users `import suzieq_api_wrapper as suzieq` and get a single `SuzieQ`
client class with methods covering all 21 SuzieQ tables.

## Repository layout

```
suzieq_api_wrapper/     # installable package
    __init__.py         # exports SuzieQ, exceptions, __version__
    client.py           # SuzieQ class (combines all mixins)
    _base.py            # _SuzieQBase: HTTP helpers (_get, _parse, _build_params)
    _exceptions.py      # Exception hierarchy
    _address.py         # AddressMixin
    _arpnd.py           # ArpndMixin
    _bgp.py             # BgpMixin
    _device.py          # DeviceMixin
    _devconfig.py       # DevconfigMixin  (no unique verb)
    _evpnvni.py         # EvpnVniMixin
    _fs.py              # FsMixin
    _interface.py       # InterfaceMixin
    _inventory.py       # InventoryMixin
    _lldp.py            # LldpMixin
    _mac.py             # MacMixin
    _mlag.py            # MlagMixin
    _namespace.py       # NamespaceMixin
    _network.py         # NetworkMixin  (find verb; show/summarize/unique/top deprecated)
    _ospf.py            # OspfMixin
    _path.py            # PathMixin
    _route.py           # RouteMixin  (includes lpm verb)
    _sqpoller.py        # SqPollerMixin
    _table.py           # TablesMixin
    _topology.py        # TopologyMixin
    _vlan.py            # VlanMixin

tests/
    conftest.py         # client fixture, API URL constant, qs() helper
    fixtures.py         # accurate SuzieQ response shapes
    test_bgp.py         # complete test file (use as template)
    test_*.py           # one file per mixin

pyproject.toml          # build config + project metadata
smoke_test.py           # live-server smoke test (read-only, always safe)
                        #   python smoke_test.py
                        #   python smoke_test.py --no-color
                        #   python smoke_test.py --skip show_path,show_fs
                        #   env vars: SUZIEQ_URL, SUZIEQ_API_KEY,
                        #            SUZIEQ_VERIFY_SSL, SUZIEQ_TIMEOUT
CHANGELOG.md
CLAUDE.md
LICENSE
```

## Architecture decisions (do not change without good reason)

- **Mixin pattern**: each table lives in its own `_<name>.py` mixin.
  `client.py` combines them all via multiple inheritance into `SuzieQ`.
- **GET only**: all SuzieQ REST API calls are `GET`. No POST/PUT/DELETE.
- **Synchronous only**: no async. `requests.Session` is used throughout.
  One runtime dependency: `requests>=2.28`.
- **API version**: all endpoints are at `/api/v2/{table}/{verb}`.
  v1 is deprecated server-side and not supported in this wrapper.
- **Authentication**: API key passed as a request header
  (`access_token: <key>`), not as a query parameter.
- **`_build_params()`**: static method on `_SuzieQBase` that strips `None`
  values from kwargs. Used in every mixin method.
- **`_parse()`**: handles JSON responses and raises typed exceptions on
  HTTP errors. SuzieQ always returns JSON when `format=json` (the default).
- **`format` param not exposed**: the wrapper always receives JSON. Users
  who need CSV output should use the API directly.
- **Timeout**: `_SuzieQBase.__init__` accepts `timeout=30` (seconds).
  Connect timeout is `min(timeout, 10)` seconds.
- **Retries**: same pattern as opennms-api-wrapper — urllib3 `Retry` with
  0.5 s backoff on 500/502/503/504. Pass `retries=0` to disable.
- **SSL**: defaults to `verify_ssl=True`. Set to `False` for dev/self-signed
  certs. Never hard-code `verify=False` in production.
- **camelCase params preserved**: SuzieQ uses camelCase for some parameter
  names (`ipAddress`, `peerMacaddr`, `afiSafi`, etc.). These are preserved
  as-is in Python method signatures to match the API exactly.

## SuzieQ API verb reference

| Verb | Available on |
|------|-------------|
| `show` | All 21 tables |
| `summarize` | All 21 tables |
| `unique` | All tables except `devconfig` |
| `top` | All 21 tables |
| `assert` | `bgp`, `evpnVni`, `interface`, `ospf` |
| `lpm` | `route` only |
| `find` | `network` only |

## Universal query parameters (all methods)

`namespace`, `hostname`, `start_time`, `end_time`, `view`
(`latest`/`all`/`changes`), `columns`, `query_str`

## Development environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"   # installs requests + pytest + responses
pytest tests/ -v
```

Always activate the `.venv` before running any commands.

## Test conventions

- HTTP mocking: `responses` library with `@responses.activate` decorator.
- `conftest.py` constants:
  - `BASE_URL = "http://suzieq:8000"`
  - `API = "http://suzieq:8000/api/v2"`
  - `API_KEY = "test-api-key"`
  - `qs(url)` parses query params into a dict of lists.
- Fixture shapes in `tests/fixtures.py` mirror real SuzieQ responses.
- `test_bgp.py` is the canonical template for all other test files.
- Verify the `access_token` header is present on requests.
- Verify None params are not included in the query string.
- List params (`namespace`, `hostname`, etc.) repeat the key:
  `?namespace=dc1&namespace=dc2` → use `responses` + `qs()` to verify.

## Build / release

Release checklist:
1. Bump `version` in `pyproject.toml`.
2. Add a changelog entry in `CHANGELOG.md`.
3. Commit on a branch, open a PR, merge to `main`.
4. `gh release create vX.Y.Z`.

## Git workflow

- **Never push directly to `main`.**  All changes go through a branch + PR.
- Branch naming: `feature/<topic>`, `fix/<topic>`, `docs/<topic>`, etc.

## Style

- PEP 8: 79-character line limit, 4-space indentation.
- Every public method has a Google-style docstring with `Args:` and
  `Returns:` sections.
- No inline comments on self-evident code.
