"""VLAN REST API – /api/v2/vlan."""


class VlanMixin:
    """Methods for the ``vlan`` SuzieQ table."""

    def show_vlan(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        vlan=None,
        state=None,
        vlanName=None,
    ):
        """Return VLAN table records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            vlan: Filter by VLAN ID(s).
            state: VLAN state — ``"active"`` or ``"suspended"``.
            vlanName: Filter by VLAN name(s).

        Returns:
            List of VLAN record dicts.
        """
        return self._get("vlan", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            vlan=vlan, state=state, vlanName=vlanName,
        ))

    def summarize_vlan(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        vlan=None,
        state=None,
        vlanName=None,
    ):
        """Return summary statistics for the ``vlan`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            vlan: Filter by VLAN ID(s).
            state: VLAN state — ``"active"`` or ``"suspended"``.
            vlanName: Filter by VLAN name(s).

        Returns:
            Column-oriented summary dict.
        """
        return self._get("vlan", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            vlan=vlan, state=state, vlanName=vlanName,
        ))

    def unique_vlan(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        vlan=None,
        state=None,
        vlanName=None,
    ):
        """Return unique values and counts for a column in the ``vlan`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            vlan: Filter by VLAN ID(s).
            state: VLAN state — ``"active"`` or ``"suspended"``.
            vlanName: Filter by VLAN name(s).

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("vlan", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            vlan=vlan, state=state, vlanName=vlanName,
        ))

    def top_vlan(
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
        vlan=None,
        state=None,
        vlanName=None,
    ):
        """Return the top N records sorted by a column in the ``vlan`` table.

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
            vlan: Filter by VLAN ID(s).
            state: VLAN state — ``"active"`` or ``"suspended"``.
            vlanName: Filter by VLAN name(s).

        Returns:
            List of top-N VLAN record dicts.
        """
        return self._get("vlan", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            vlan=vlan, state=state, vlanName=vlanName,
        ))
