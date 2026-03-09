"""Address REST API – /api/v2/address."""


class AddressMixin:
    """Methods for the ``address`` SuzieQ table (IP address assignments)."""

    def show_address(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        address=None,
        prefix=None,
        ipvers=None,
        vrf=None,
        type=None,
        ifname=None,
    ):
        """Return IP address assignment records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter
                (e.g. ``"state == 'up'``).
            address: Filter by IP address(es).
            prefix: Filter by prefix(es).
            ipvers: IP version, ``"4"`` or ``"6"``.
            vrf: Filter by VRF(s).
            type: Filter by address type(s).
            ifname: Filter by interface name(s).

        Returns:
            List of address record dicts.
        """
        return self._get("address", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            address=address, prefix=prefix, ipvers=ipvers,
            vrf=vrf, type=type, ifname=ifname,
        ))

    def summarize_address(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        address=None,
        prefix=None,
        ipvers=None,
        vrf=None,
        type=None,
        ifname=None,
    ):
        """Return summary statistics for the ``address`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            address: Filter by IP address(es).
            prefix: Filter by prefix(es).
            ipvers: IP version, ``"4"`` or ``"6"``.
            vrf: Filter by VRF(s).
            type: Filter by address type(s).
            ifname: Filter by interface name(s).

        Returns:
            Column-oriented summary dict.
        """
        return self._get("address", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            address=address, prefix=prefix, ipvers=ipvers,
            vrf=vrf, type=type, ifname=ifname,
        ))

    def unique_address(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        address=None,
        prefix=None,
        ipvers=None,
        vrf=None,
        type=None,
        ifname=None,
    ):
        """Return unique values and counts for a column in the ``address`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            address: Filter by IP address(es).
            prefix: Filter by prefix(es).
            ipvers: IP version, ``"4"`` or ``"6"``.
            vrf: Filter by VRF(s).
            type: Filter by address type(s).
            ifname: Filter by interface name(s).

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("address", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            address=address, prefix=prefix, ipvers=ipvers,
            vrf=vrf, type=type, ifname=ifname,
        ))

    def top_address(
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
        address=None,
        prefix=None,
        ipvers=None,
        vrf=None,
        type=None,
        ifname=None,
    ):
        """Return the top N records sorted by a column in the ``address`` table.

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
            address: Filter by IP address(es).
            prefix: Filter by prefix(es).
            ipvers: IP version, ``"4"`` or ``"6"``.
            vrf: Filter by VRF(s).
            type: Filter by address type(s).
            ifname: Filter by interface name(s).

        Returns:
            List of top-N address record dicts.
        """
        return self._get("address", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            address=address, prefix=prefix, ipvers=ipvers,
            vrf=vrf, type=type, ifname=ifname,
        ))
