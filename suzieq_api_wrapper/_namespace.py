"""Namespace REST API – /api/v2/namespace."""


class NamespaceMixin:
    """Methods for the ``namespace`` SuzieQ table (namespace summary)."""

    def show_namespace(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        version=None,
        os=None,
        model=None,
        vendor=None,
    ):
        """Return namespace summary records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            version: Filter by OS version.
            os: Filter by operating system(s).
            model: Filter by model(s).
            vendor: Filter by vendor(s).

        Returns:
            List of namespace record dicts.
        """
        return self._get("namespace", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            version=version, os=os, model=model, vendor=vendor,
        ))

    def summarize_namespace(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        version=None,
        os=None,
        model=None,
        vendor=None,
    ):
        """Return summary statistics for the ``namespace`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            version: Filter by OS version.
            os: Filter by operating system(s).
            model: Filter by model(s).
            vendor: Filter by vendor(s).

        Returns:
            Column-oriented summary dict.
        """
        return self._get("namespace", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            version=version, os=os, model=model, vendor=vendor,
        ))

    def unique_namespace(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        version=None,
        os=None,
        model=None,
        vendor=None,
    ):
        """Return unique values and counts for a column in the ``namespace`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            version: Filter by OS version.
            os: Filter by operating system(s).
            model: Filter by model(s).
            vendor: Filter by vendor(s).

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("namespace", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            version=version, os=os, model=model, vendor=vendor,
        ))

    def top_namespace(
        self,
        what,
        count=None,
        reverse=None,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        version=None,
        os=None,
        model=None,
        vendor=None,
    ):
        """Return the top N records sorted by a column in the ``namespace`` table.

        Args:
            what: Column name to sort by.
            count: Number of rows to return.
            reverse: If truthy, reverse the sort order.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            version: Filter by OS version.
            os: Filter by operating system(s).
            model: Filter by model(s).
            vendor: Filter by vendor(s).

        Returns:
            List of top-N namespace record dicts.
        """
        return self._get("namespace", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            version=version, os=os, model=model, vendor=vendor,
        ))
