# suzieq-api-wrapper

[![CI](https://github.com/cnewkirk/suzieq-api-wrapper/actions/workflows/ci.yml/badge.svg)](https://github.com/cnewkirk/suzieq-api-wrapper/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/suzieq-api-wrapper)](https://pypi.org/project/suzieq-api-wrapper/)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/cnewkirk/suzieq-api-wrapper/blob/main/LICENSE)

An unofficial, dependency-minimal Python 3 client for the
[SuzieQ](https://github.com/netenglabs/suzieq) REST API (v2).

## Installation

```bash
pip install suzieq-api-wrapper
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
```

## Features

- Covers all 21 SuzieQ tables with all supported verbs
- One method per table-verb combination — flat, discoverable namespace
- Single runtime dependency: [`requests`](https://docs.python-requests.org/)
- Synchronous and straightforward — no async complexity
- Typed exception hierarchy — catch `AuthenticationError`, `NotFoundError`,
  etc. without importing `requests`
- Full test suite (237 tests, mocked HTTP — no live server required)
- Read-only smoke test for live server validation

## Error handling

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

## Authentication

SuzieQ uses API key authentication.  Configure your API key via the
SuzieQ web UI or in `~/.suzieq/suzieq.cfg`.

Pass `verify_ssl=False` to disable certificate verification (useful for
self-signed certs in lab environments):

```python
client = suzieq.SuzieQ(
    url="https://127.0.0.1:8000",
    api_key="your-api-key-here",
    verify_ssl=False,
)
```

## Acknowledgements

This library was designed and tested by a human, with implementation
assistance from [Claude Code](https://claude.ai/code) (Anthropic). All API
shapes are derived from the [SuzieQ](https://github.com/netenglabs/suzieq)
open-source project.
