"""Path REST API – /api/v2/path."""


class PathMixin:
    """Methods for the ``path`` SuzieQ table (Layer 3 path trace)."""

    def show_path(
        self,
        src,
        dest,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        vrf=None,
    ):
        """Compute and return the Layer 3 path between two IP addresses.

        Args:
            src: Source IP address (required).
            dest: Destination IP address (required).
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            vrf: VRF to use for path computation.

        Returns:
            List of path hop record dicts describing each hop from
            *src* to *dest*.
        """
        return self._get("path", "show", self._build_params(
            src=src, dest=dest,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            vrf=vrf,
        ))

    def summarize_path(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        src=None,
        dest=None,
        vrf=None,
    ):
        """Return summary statistics for the ``path`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            src: Source IP address.
            dest: Destination IP address.
            vrf: VRF context.

        Returns:
            Column-oriented summary dict.
        """
        return self._get("path", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            src=src, dest=dest, vrf=vrf,
        ))

    def unique_path(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        src=None,
        dest=None,
        vrf=None,
    ):
        """Return unique values and counts for a column in the ``path`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            src: Source IP address.
            dest: Destination IP address.
            vrf: VRF context.

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("path", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            src=src, dest=dest, vrf=vrf,
        ))

    def top_path(
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
        src=None,
        dest=None,
        vrf=None,
    ):
        """Return the top N records sorted by a column in the ``path`` table.

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
            src: Source IP address.
            dest: Destination IP address.
            vrf: VRF context.

        Returns:
            List of top-N path record dicts.
        """
        return self._get("path", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            src=src, dest=dest, vrf=vrf,
        ))
