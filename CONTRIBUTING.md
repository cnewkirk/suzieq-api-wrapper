# Contributing

Bug reports and pull requests are welcome.

## Development setup

```bash
git clone https://github.com/cnewkirk/suzieq-api-wrapper.git
cd suzieq-api-wrapper
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Running the tests

```bash
pytest tests/ -v
```

All tests should pass.

## Adding a new table

1. Create `suzieq_api_wrapper/_newtable.py` with a mixin class following the
   existing pattern (`_bgp.py` is a good template for tables with `assert`;
   `_mlag.py` is the simplest example).
2. Each method takes the universal query params (`namespace`, `hostname`,
   `start_time`, `end_time`, `view`, `columns`, `query_str`) plus any
   table-specific params.
3. Import and add the mixin to the inheritance list in `client.py`.
4. Add response fixture shapes to `tests/fixtures.py`.
5. Add a corresponding test file `tests/test_newtable.py`. Mock the HTTP
   call with `@responses.activate` and verify params, auth header, and
   None-omission.

## Style

- PEP 8 throughout: 79-character line limit, 4-space indentation.
- Google-style docstrings with `Args:` and `Returns:` sections.
- No new runtime dependencies beyond `requests`.
- camelCase parameter names preserved to match the SuzieQ API exactly.

## Submitting a pull request

1. Fork the repo and create a branch from `main`.
2. Make your changes and ensure all local checks pass:
   ```bash
   pytest tests/ -v
   ruff check suzieq_api_wrapper/
   ```
3. Open a pull request — CI will run all checks automatically.
