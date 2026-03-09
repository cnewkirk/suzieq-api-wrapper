"""BGP REST API – /api/v2/bgp."""


class BgpMixin:
    """Methods for the ``bgp`` SuzieQ table."""

    def show_bgp(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        peer=None,
        state=None,
        vrf=None,
        asn=None,
        afiSafi=None,
    ):
        """Return BGP peer records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            peer: Filter by BGP peer address(es) or name(s).
            state: Peer state filter, e.g. ``"Established"``,
                ``"NotEstd"``, or ``"!Established"`` to negate.
            vrf: Filter by VRF(s).
            asn: Filter by AS number(s).
            afiSafi: Address family filter (e.g. ``"ipv4Unicast"``).

        Returns:
            List of BGP peer record dicts.
        """
        return self._get("bgp", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            peer=peer, state=state, vrf=vrf, asn=asn, afiSafi=afiSafi,
        ))

    def summarize_bgp(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        peer=None,
        state=None,
        vrf=None,
        asn=None,
        afiSafi=None,
    ):
        """Return summary statistics for the ``bgp`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            peer: Filter by peer address(es) or name(s).
            state: Peer state filter.
            vrf: Filter by VRF(s).
            asn: Filter by AS number(s).
            afiSafi: Address family filter.

        Returns:
            Column-oriented summary dict.
        """
        return self._get("bgp", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            peer=peer, state=state, vrf=vrf, asn=asn, afiSafi=afiSafi,
        ))

    def unique_bgp(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        peer=None,
        state=None,
        vrf=None,
        asn=None,
        afiSafi=None,
    ):
        """Return unique values and counts for a column in the ``bgp`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            peer: Filter by peer address(es) or name(s).
            state: Peer state filter.
            vrf: Filter by VRF(s).
            asn: Filter by AS number(s).
            afiSafi: Address family filter.

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("bgp", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            peer=peer, state=state, vrf=vrf, asn=asn, afiSafi=afiSafi,
        ))

    def top_bgp(
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
        peer=None,
        state=None,
        vrf=None,
        asn=None,
        afiSafi=None,
    ):
        """Return the top N records sorted by a column in the ``bgp`` table.

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
            peer: Filter by peer address(es) or name(s).
            state: Peer state filter.
            vrf: Filter by VRF(s).
            asn: Filter by AS number(s).
            afiSafi: Address family filter.

        Returns:
            List of top-N BGP peer record dicts.
        """
        return self._get("bgp", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            peer=peer, state=state, vrf=vrf, asn=asn, afiSafi=afiSafi,
        ))

    def assert_bgp(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        peer=None,
        state=None,
        vrf=None,
        asn=None,
        afiSafi=None,
        result=None,
    ):
        """Run BGP assertions and return pass/fail results.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            peer: Filter by peer address(es) or name(s).
            state: Peer state filter.
            vrf: Filter by VRF(s).
            asn: Filter by AS number(s).
            afiSafi: Address family filter.
            result: Assertion result filter — ``"pass"``, ``"fail"``,
                or ``"all"`` (default).

        Returns:
            List of BGP assertion result dicts.
        """
        return self._get("bgp", "assert", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            peer=peer, state=state, vrf=vrf, asn=asn, afiSafi=afiSafi,
            result=result,
        ))
