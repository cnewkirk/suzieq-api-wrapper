# TODO

Items deferred for a future session.

## Live smoke test validation

`smoke_test.py` has not yet been validated against a live SuzieQ REST server.
Run it against a dev instance and update the README validation note once
confirmed.

## CI workflow

Add `.github/workflows/ci.yml` to run the test suite on push/PR against
Python 3.8–3.13.

## PyPI publishing workflow

Add `.github/workflows/publish.yml` triggered on GitHub releases, using
OIDC trusted publishing (same pattern as opennms-api-wrapper).

## Pre-commit config

Add `.pre-commit-config.yaml` with ruff:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.9.0
    hooks:
      - id: ruff
```

Update `CONTRIBUTING.md` to mention `pre-commit install` as an optional
setup step.

## Codecov integration

Add coverage reporting to CI and a Codecov badge to `README.md`.

## Documentation site

Consider adding mkdocs-material + mkdocstrings for a hosted API reference
(same pattern as opennms-api-wrapper with Read the Docs).

## GitHub remote

Create the `cnewkirk/suzieq-api-wrapper` repo on GitHub, push, and update
badge URLs in `README.md`.
