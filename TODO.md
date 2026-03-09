# TODO

Items deferred for a future session.

## PyPI trusted publisher setup

Blocked on PyPI account access. Once restored:

1. Go to https://pypi.org/manage/account/publishing/
2. Add a pending publisher:
   - **Project**: `suzieq-api-wrapper`
   - **Owner**: `cnewkirk`
   - **Repository**: `suzieq-api-wrapper`
   - **Workflow**: `publish.yml`
   - **Environment**: `pypi`
3. In `publish.yml`, replace `on: workflow_dispatch` with:
   ```yaml
   on:
     release:
       types: [published]
   ```
4. Create a release to verify the pipeline end-to-end.

## Live smoke test validation

`smoke_test.py` has not yet been validated against a live SuzieQ REST server.
Run it against a dev instance and update the README validation note once
confirmed.

