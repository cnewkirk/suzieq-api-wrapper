"""ARP/ND REST API – /api/v2/arpnd."""


class ArpndMixin:
    """Methods for the ``arpnd`` SuzieQ table (ARP and IPv6 Neighbor Discovery)."""

    def show_arpnd(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        ipAddress=None,
        prefix=None,
        macaddr=None,
        oif=None,
    ):
        """Return ARP/ND table records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            ipAddress: Filter by IP address(es).
            prefix: Filter by prefix(es).
            macaddr: Filter by MAC address(es).
            oif: Filter by outgoing interface(s).

        Returns:
            List of ARP/ND record dicts.
        """
        return self._get("arpnd", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ipAddress=ipAddress, prefix=prefix,
            macaddr=macaddr, oif=oif,
        ))

    def summarize_arpnd(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        ipAddress=None,
        prefix=None,
        macaddr=None,
        oif=None,
    ):
        """Return summary statistics for the ``arpnd`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            ipAddress: Filter by IP address(es).
            prefix: Filter by prefix(es).
            macaddr: Filter by MAC address(es).
            oif: Filter by outgoing interface(s).

        Returns:
            Column-oriented summary dict.
        """
        return self._get("arpnd", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ipAddress=ipAddress, prefix=prefix,
            macaddr=macaddr, oif=oif,
        ))

    def unique_arpnd(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        ipAddress=None,
        prefix=None,
        macaddr=None,
        oif=None,
    ):
        """Return unique values and counts for a column in the ``arpnd`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            ipAddress: Filter by IP address(es).
            prefix: Filter by prefix(es).
            macaddr: Filter by MAC address(es).
            oif: Filter by outgoing interface(s).

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("arpnd", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ipAddress=ipAddress, prefix=prefix,
            macaddr=macaddr, oif=oif,
        ))

    def top_arpnd(
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
        ipAddress=None,
        prefix=None,
        macaddr=None,
        oif=None,
    ):
        """Return the top N records sorted by a column in the ``arpnd`` table.

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
            ipAddress: Filter by IP address(es).
            prefix: Filter by prefix(es).
            macaddr: Filter by MAC address(es).
            oif: Filter by outgoing interface(s).

        Returns:
            List of top-N ARP/ND record dicts.
        """
        return self._get("arpnd", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ipAddress=ipAddress, prefix=prefix,
            macaddr=macaddr, oif=oif,
        ))
