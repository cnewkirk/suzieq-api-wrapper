"""MAC REST API – /api/v2/mac."""


class MacMixin:
    """Methods for the ``mac`` SuzieQ table (MAC address table)."""

    def show_mac(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        macaddr=None,
        vlan=None,
        remoteVtepIp=None,
        local=None,
        bd=None,
        moveCount=None,
    ):
        """Return MAC address table records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            macaddr: Filter by MAC address(es).
            vlan: Filter by VLAN ID(s).
            remoteVtepIp: Filter by remote VTEP IP(s) (EVPN).
            local: Filter for local entries.
            bd: Filter by bridge domain.
            moveCount: Filter by MAC move count (e.g. ``">5"``).

        Returns:
            List of MAC address table record dicts.
        """
        return self._get("mac", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            macaddr=macaddr, vlan=vlan, remoteVtepIp=remoteVtepIp,
            local=local, bd=bd, moveCount=moveCount,
        ))

    def summarize_mac(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        macaddr=None,
        vlan=None,
        remoteVtepIp=None,
        local=None,
        bd=None,
        moveCount=None,
    ):
        """Return summary statistics for the ``mac`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            macaddr: Filter by MAC address(es).
            vlan: Filter by VLAN ID(s).
            remoteVtepIp: Filter by remote VTEP IP(s).
            local: Filter for local entries.
            bd: Filter by bridge domain.
            moveCount: Filter by MAC move count (e.g. ``">5"``).

        Returns:
            Column-oriented summary dict.
        """
        return self._get("mac", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            macaddr=macaddr, vlan=vlan, remoteVtepIp=remoteVtepIp,
            local=local, bd=bd, moveCount=moveCount,
        ))

    def unique_mac(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        macaddr=None,
        vlan=None,
        remoteVtepIp=None,
        local=None,
        bd=None,
        moveCount=None,
    ):
        """Return unique values and counts for a column in the ``mac`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            macaddr: Filter by MAC address(es).
            vlan: Filter by VLAN ID(s).
            remoteVtepIp: Filter by remote VTEP IP(s).
            local: Filter for local entries.
            bd: Filter by bridge domain.
            moveCount: Filter by MAC move count.

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("mac", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            macaddr=macaddr, vlan=vlan, remoteVtepIp=remoteVtepIp,
            local=local, bd=bd, moveCount=moveCount,
        ))

    def top_mac(
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
        macaddr=None,
        vlan=None,
        remoteVtepIp=None,
        local=None,
        bd=None,
        moveCount=None,
    ):
        """Return the top N records sorted by a column in the ``mac`` table.

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
            macaddr: Filter by MAC address(es).
            vlan: Filter by VLAN ID(s).
            remoteVtepIp: Filter by remote VTEP IP(s).
            local: Filter for local entries.
            bd: Filter by bridge domain.
            moveCount: Filter by MAC move count.

        Returns:
            List of top-N MAC address table record dicts.
        """
        return self._get("mac", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            macaddr=macaddr, vlan=vlan, remoteVtepIp=remoteVtepIp,
            local=local, bd=bd, moveCount=moveCount,
        ))
