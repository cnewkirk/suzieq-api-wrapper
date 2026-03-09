"""Topology REST API – /api/v2/topology."""


class TopologyMixin:
    """Methods for the ``topology`` SuzieQ table (multi-protocol topology graph)."""

    def show_topology(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        via=None,
        ifname=None,
        peerHostname=None,
        asn=None,
        area=None,
        vrf=None,
        afiSafi=None,
        polled=None,
    ):
        """Return network topology records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            via: Protocol(s) to include — ``"lldp"``, ``"bgp"``,
                ``"ospf"``, ``"arpnd"``.
            ifname: Filter by interface name(s).
            peerHostname: Filter by peer hostname(s).
            asn: Filter by AS number(s).
            area: Filter by OSPF area(s).
            vrf: Filter by VRF(s).
            afiSafi: BGP address family filter.
            polled: Filter to only polled links.

        Returns:
            List of topology edge record dicts.
        """
        return self._get("topology", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            via=via, ifname=ifname, peerHostname=peerHostname,
            asn=asn, area=area, vrf=vrf, afiSafi=afiSafi, polled=polled,
        ))

    def summarize_topology(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        via=None,
        ifname=None,
        peerHostname=None,
        asn=None,
        area=None,
        vrf=None,
        afiSafi=None,
        polled=None,
    ):
        """Return summary statistics for the ``topology`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            via: Protocol(s) to include.
            ifname: Filter by interface name(s).
            peerHostname: Filter by peer hostname(s).
            asn: Filter by AS number(s).
            area: Filter by OSPF area(s).
            vrf: Filter by VRF(s).
            afiSafi: BGP address family filter.
            polled: Filter to only polled links.

        Returns:
            Column-oriented summary dict.
        """
        return self._get("topology", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            via=via, ifname=ifname, peerHostname=peerHostname,
            asn=asn, area=area, vrf=vrf, afiSafi=afiSafi, polled=polled,
        ))

    def unique_topology(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        via=None,
        ifname=None,
        peerHostname=None,
        asn=None,
        area=None,
        vrf=None,
        afiSafi=None,
        polled=None,
    ):
        """Return unique values and counts for a column in the ``topology`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            via: Protocol(s) to include.
            ifname: Filter by interface name(s).
            peerHostname: Filter by peer hostname(s).
            asn: Filter by AS number(s).
            area: Filter by OSPF area(s).
            vrf: Filter by VRF(s).
            afiSafi: BGP address family filter.
            polled: Filter to only polled links.

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("topology", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            via=via, ifname=ifname, peerHostname=peerHostname,
            asn=asn, area=area, vrf=vrf, afiSafi=afiSafi, polled=polled,
        ))

    def top_topology(
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
        via=None,
        ifname=None,
        peerHostname=None,
        asn=None,
        area=None,
        vrf=None,
        afiSafi=None,
        polled=None,
    ):
        """Return the top N records sorted by a column in the ``topology`` table.

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
            via: Protocol(s) to include.
            ifname: Filter by interface name(s).
            peerHostname: Filter by peer hostname(s).
            asn: Filter by AS number(s).
            area: Filter by OSPF area(s).
            vrf: Filter by VRF(s).
            afiSafi: BGP address family filter.
            polled: Filter to only polled links.

        Returns:
            List of top-N topology edge record dicts.
        """
        return self._get("topology", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            via=via, ifname=ifname, peerHostname=peerHostname,
            asn=asn, area=area, vrf=vrf, afiSafi=afiSafi, polled=polled,
        ))
