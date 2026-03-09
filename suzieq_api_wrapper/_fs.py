"""Filesystem REST API – /api/v2/fs."""


class FsMixin:
    """Methods for the ``fs`` SuzieQ table (filesystem/disk usage)."""

    def show_fs(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        mountPoint=None,
        usedPercent=None,
    ):
        """Return filesystem usage records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            mountPoint: Filter by mount point(s).
            usedPercent: Filter by used percentage with a comparison
                operator, e.g. ``">80"``.

        Returns:
            List of filesystem record dicts.
        """
        return self._get("fs", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            mountPoint=mountPoint, usedPercent=usedPercent,
        ))

    def summarize_fs(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        mountPoint=None,
        usedPercent=None,
    ):
        """Return summary statistics for the ``fs`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            mountPoint: Filter by mount point(s).
            usedPercent: Filter by used percentage (e.g. ``">80"``).

        Returns:
            Column-oriented summary dict.
        """
        return self._get("fs", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            mountPoint=mountPoint, usedPercent=usedPercent,
        ))

    def unique_fs(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        mountPoint=None,
        usedPercent=None,
    ):
        """Return unique values and counts for a column in the ``fs`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            mountPoint: Filter by mount point(s).
            usedPercent: Filter by used percentage (e.g. ``">80"``).

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("fs", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            mountPoint=mountPoint, usedPercent=usedPercent,
        ))

    def top_fs(
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
        mountPoint=None,
        usedPercent=None,
    ):
        """Return the top N records sorted by a column in the ``fs`` table.

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
            mountPoint: Filter by mount point(s).
            usedPercent: Filter by used percentage (e.g. ``">80"``).

        Returns:
            List of top-N filesystem record dicts.
        """
        return self._get("fs", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            mountPoint=mountPoint, usedPercent=usedPercent,
        ))
