# Architecture Decision Record — suzieq-api-wrapper

This document captures the significant design decisions made in building
`suzieq-api-wrapper`, the rationale behind each, and their tradeoffs.  It
is intended to serve both as institutional memory and as a guide for
contributors evaluating future changes.

Format loosely follows [Nygard ADRs](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions):
**Context → Decision → Consequences**.

---

## ADR-001 · Mixin-per-table architecture

### Status
Accepted

### Context
The SuzieQ REST API covers 21 tables, each with 4–6 verb methods.  While the
API is more uniform than OpenNMS (every table follows
`GET /api/v2/{table}/{verb}`), placing all ~90 methods in one class would
still produce a large, hard-to-navigate file.  The mixin-per-resource pattern
proved successful in the sibling `opennms-api-wrapper` project.

| Option | Description |
|---|---|
| **One class, one file** | `SuzieQ` with all 90 methods in a single source file |
| **Resource sub-clients** | `client.bgp.show(...)`, `client.route.lpm(...)` |
| **Mixin-per-table** | One mixin class per table, assembled via multiple inheritance |

### Decision
Mixin-per-table.  Each SuzieQ table lives in its own file (`_bgp.py`,
`_route.py`, …).  `client.py` assembles them with multiple inheritance,
exposing a single flat namespace to callers.

### Consequences

**Pros**
- Each mixin is self-contained and covers exactly one table.
- Adding a new table is additive: new file, new mixin, one line in
  `client.py`.
- Tests map 1-to-1: `test_bgp.py` tests only `BgpMixin`.
- Flat namespace: `client.show_bgp()`, not `client.bgp.show()`.

**Cons**
- Python's MRO is non-obvious to new contributors.
- Large inheritance chain can confuse some IDE introspection.

---

## ADR-002 · GET-only client — no write operations

### Status
Accepted

### Context
The SuzieQ REST API is entirely read-only — all endpoints are `GET` requests
with query parameters.  There are no `POST`, `PUT`, `PATCH`, or `DELETE`
endpoints exposed in the REST server.

### Decision
The base class provides only a `_get` helper.  No `_post`, `_put`, `_delete`,
or `_patch` methods exist.  This simplifies the wrapper and removes any risk
of accidental mutation.

### Consequences

**Pros**
- The wrapper is inherently safe — it cannot modify server state.
- The smoke test is always safe to run against production.
- No need for write-mode confirmation prompts or guardrails.

**Cons**
- If SuzieQ adds write endpoints in the future, the base class will need
  new HTTP verb helpers.

---

## ADR-003 · API key authentication via header

### Status
Accepted

### Context
SuzieQ accepts the API key in two ways:
1. Query parameter: `?access_token=<key>`
2. HTTP header: `access_token: <key>`

### Decision
Pass the API key as a session-level header, not as a query parameter.

### Consequences

**Pros**
- The key does not appear in server access logs, proxy logs, or
  `responses.calls[].request.url` — reducing accidental exposure.
- The key is set once on the session and applies to all requests
  automatically.

**Cons**
- Non-standard header name (`access_token` rather than `Authorization`).
  This is dictated by the SuzieQ server and cannot be changed.

---

## ADR-004 · `_build_params` static method

### Status
Accepted

### Context
Every mixin method accepts 7 universal params plus 0–12 table-specific
params.  All params default to `None` and only non-`None` values should
appear in the query string.  Without a helper, each method would contain
a dict comprehension filtering `None` values.

### Decision
A `_build_params(**kwargs)` static method on `_SuzieQBase` strips `None`
values and returns the filtered dict.

```python
return self._get("bgp", "show", self._build_params(
    namespace=namespace, hostname=hostname, state=state, ...
))
```

### Consequences

**Pros**
- DRY: every method is a single `return self._get(...)` statement.
- Explicit: all params are named in the `_build_params` call — no `**kwargs`
  passthrough that hides valid parameters.
- Preserves falsy values (`False`, `0`, `""`) — only `None` is stripped.

**Cons**
- Every param is written twice (once in the method signature, once in the
  `_build_params` call).  This is intentional for clarity but verbose.

---

## ADR-005 · camelCase parameter names preserved

### Status
Accepted

### Context
SuzieQ uses camelCase for many query parameters (`ipAddress`, `peerMacaddr`,
`afiSafi`, `priVtepIp`, `pollExcdPeriodCount`, `remoteVtepIp`, `mountPoint`,
`usedPercent`, `vlanName`, `peerHostname`).  Python convention is snake_case.

### Decision
Preserve the exact SuzieQ parameter names in the Python method signatures.
`client.show_arpnd(ipAddress=["10.0.0.1"])`, not `ip_address=`.

### Consequences

**Pros**
- Zero translation layer between the wrapper and the API docs.
- Parameters are Google-able: `SuzieQ peerMacaddr` finds relevant docs.
- No risk of mapping errors between snake_case and camelCase.

**Cons**
- PEP 8 naming convention is violated for these parameters.
- IDE linters may flag camelCase function arguments.

**Mitigations**
- Every parameter is documented in the Google-style docstring with its
  exact API-side meaning.

---

## ADR-006 · `format` parameter not exposed

### Status
Accepted

### Context
The SuzieQ API accepts `format=json|csv|markdown|text` on every endpoint.
The default is `json`.

### Decision
Do not expose the `format` parameter.  The wrapper always receives JSON
and parses it into Python dicts/lists via `_parse()`.

### Consequences

**Pros**
- Callers always get Python objects, never raw text.
- `_parse()` can rely on `resp.json()` without conditional logic.

**Cons**
- Callers who need CSV output must use the SuzieQ REST API directly.
- This is intentional: the wrapper's purpose is to return Python objects.

---

## ADR-007 · Mocked HTTP unit tests

### Status
Accepted

### Context
Same reasoning as opennms-api-wrapper ADR-008.

### Decision
Use the `responses` library.  Fixture shapes in `tests/fixtures.py` are
derived from real SuzieQ response structures.

### Consequences

**Pros**
- Tests run in ~0.2 s with no external dependencies.
- Fully deterministic; no server state dependency.
- CI requires no SuzieQ instance.

**Cons**
- Fixtures can drift from the live API.

**Mitigation**
`smoke_test.py` runs all methods against a real server.

---

## ADR-008 · Timeout and retry (inherited pattern)

### Status
Accepted

### Context
Same reasoning as opennms-api-wrapper ADRs 009/010.

### Decision
- `timeout=30` default, connect timeout capped at `min(timeout, 10)`.
- `retries=3` default with 0.5 s backoff on 500/502/503/504.

These are identical to the opennms-api-wrapper settings and reuse the
same `urllib3.Retry` + `HTTPAdapter` pattern.

---

## Summary matrix

| ADR | Decision | Primary benefit | Primary cost |
|---|---|---|---|
| 001 | Mixin per table | Incremental, isolated | MRO non-obvious |
| 002 | GET-only | Inherently safe | No write support |
| 003 | API key via header | Key not in logs/URLs | Non-standard header |
| 004 | `_build_params` | DRY, explicit params | Params written twice |
| 005 | camelCase preserved | Zero translation errors | PEP 8 violation |
| 006 | `format` not exposed | Always Python objects | No CSV output |
| 007 | Mocked HTTP tests | Fast, deterministic | Fixtures can drift |
| 008 | Timeout + retry | Robust against transients | Hidden latency on errors |
