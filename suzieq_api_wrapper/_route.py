"""Route REST API – /api/v2/route."""


class RouteMixin:
    """Methods for the ``route`` SuzieQ table (routing table)."""

    def show_route(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        prefix=None,
        vrf=None,
        protocol=None,
        prefixlen=None,
        ipvers=None,
        add_filter=None,
    ):
        """Return routing table records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            prefix: Filter by route prefix(es).
            vrf: Filter by VRF(s).
            protocol: Filter by routing protocol(s) (e.g. ``"bgp"``,
                ``"ospf"``, ``"static"``).
            prefixlen: Filter by prefix length with a comparison operator,
                e.g. ``"<24"`` or ``">=16"``.
            ipvers: IP version, ``"4"`` or ``"6"``.
            add_filter: Additional Pandas filter expression.

        Returns:
            List of route record dicts.
        """
        return self._get("route", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            prefix=prefix, vrf=vrf, protocol=protocol,
            prefixlen=prefixlen, ipvers=ipvers, add_filter=add_filter,
        ))

    def summarize_route(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        prefix=None,
        vrf=None,
        protocol=None,
        prefixlen=None,
        ipvers=None,
        add_filter=None,
    ):
        """Return summary statistics for the ``route`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            prefix: Filter by route prefix(es).
            vrf: Filter by VRF(s).
            protocol: Filter by routing protocol(s).
            prefixlen: Filter by prefix length with a comparison operator.
            ipvers: IP version, ``"4"`` or ``"6"``.
            add_filter: Additional Pandas filter expression.

        Returns:
            Column-oriented summary dict.
        """
        return self._get("route", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            prefix=prefix, vrf=vrf, protocol=protocol,
            prefixlen=prefixlen, ipvers=ipvers, add_filter=add_filter,
        ))

    def unique_route(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        prefix=None,
        vrf=None,
        protocol=None,
        prefixlen=None,
        ipvers=None,
        add_filter=None,
    ):
        """Return unique values and counts for a column in the ``route`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            prefix: Filter by route prefix(es).
            vrf: Filter by VRF(s).
            protocol: Filter by routing protocol(s).
            prefixlen: Filter by prefix length with a comparison operator.
            ipvers: IP version, ``"4"`` or ``"6"``.
            add_filter: Additional Pandas filter expression.

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("route", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            prefix=prefix, vrf=vrf, protocol=protocol,
            prefixlen=prefixlen, ipvers=ipvers, add_filter=add_filter,
        ))

    def top_route(
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
        prefix=None,
        vrf=None,
        protocol=None,
        prefixlen=None,
        ipvers=None,
        add_filter=None,
    ):
        """Return the top N records sorted by a column in the ``route`` table.

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
            prefix: Filter by route prefix(es).
            vrf: Filter by VRF(s).
            protocol: Filter by routing protocol(s).
            prefixlen: Filter by prefix length with a comparison operator.
            ipvers: IP version, ``"4"`` or ``"6"``.
            add_filter: Additional Pandas filter expression.

        Returns:
            List of top-N route record dicts.
        """
        return self._get("route", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            prefix=prefix, vrf=vrf, protocol=protocol,
            prefixlen=prefixlen, ipvers=ipvers, add_filter=add_filter,
        ))

    def lpm_route(
        self,
        address,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        vrf=None,
        ipvers=None,
    ):
        """Perform a longest-prefix match for an address in the routing table.

        Args:
            address: IP address to perform the LPM lookup on (required).
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: List of columns to return.
            query_str: Pandas query string for post-filter.
            vrf: VRF to search within.
            ipvers: IP version, ``"4"`` or ``"6"``.

        Returns:
            List of matching route record dicts (one per device).
        """
        return self._get("route", "lpm", self._build_params(
            address=address,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            vrf=vrf, ipvers=ipvers,
        ))
