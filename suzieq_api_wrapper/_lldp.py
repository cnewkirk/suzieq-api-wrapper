"""LLDP REST API – /api/v2/lldp."""


class LldpMixin:
    """Methods for the ``lldp`` SuzieQ table (LLDP neighbor table)."""

    def show_lldp(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        ifname=None,
        peerMacaddr=None,
        peerHostname=None,
        use_bond=None,
    ):
        """Return LLDP neighbor records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            ifname: Filter by local interface name(s).
            peerMacaddr: Filter by peer MAC address(es).
            peerHostname: Filter by peer hostname(s).
            use_bond: ``"True"`` or ``"False"`` to filter by bond usage.

        Returns:
            List of LLDP neighbor record dicts.
        """
        return self._get("lldp", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ifname=ifname, peerMacaddr=peerMacaddr,
            peerHostname=peerHostname, use_bond=use_bond,
        ))

    def summarize_lldp(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        ifname=None,
        peerMacaddr=None,
        peerHostname=None,
        use_bond=None,
    ):
        """Return summary statistics for the ``lldp`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            ifname: Filter by local interface name(s).
            peerMacaddr: Filter by peer MAC address(es).
            peerHostname: Filter by peer hostname(s).
            use_bond: ``"True"`` or ``"False"`` to filter by bond usage.

        Returns:
            Column-oriented summary dict.
        """
        return self._get("lldp", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ifname=ifname, peerMacaddr=peerMacaddr,
            peerHostname=peerHostname, use_bond=use_bond,
        ))

    def unique_lldp(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        ifname=None,
        peerMacaddr=None,
        peerHostname=None,
        use_bond=None,
    ):
        """Return unique values and counts for a column in the ``lldp`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            ifname: Filter by local interface name(s).
            peerMacaddr: Filter by peer MAC address(es).
            peerHostname: Filter by peer hostname(s).
            use_bond: ``"True"`` or ``"False"`` to filter by bond usage.

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("lldp", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ifname=ifname, peerMacaddr=peerMacaddr,
            peerHostname=peerHostname, use_bond=use_bond,
        ))

    def top_lldp(
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
        ifname=None,
        peerMacaddr=None,
        peerHostname=None,
        use_bond=None,
    ):
        """Return the top N records sorted by a column in the ``lldp`` table.

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
            ifname: Filter by local interface name(s).
            peerMacaddr: Filter by peer MAC address(es).
            peerHostname: Filter by peer hostname(s).
            use_bond: ``"True"`` or ``"False"`` to filter by bond usage.

        Returns:
            List of top-N LLDP neighbor record dicts.
        """
        return self._get("lldp", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ifname=ifname, peerMacaddr=peerMacaddr,
            peerHostname=peerHostname, use_bond=use_bond,
        ))
