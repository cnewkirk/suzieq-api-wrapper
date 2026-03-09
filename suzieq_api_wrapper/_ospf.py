"""OSPF REST API – /api/v2/ospf."""


class OspfMixin:
    """Methods for the ``ospf`` SuzieQ table."""

    def show_ospf(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        ifname=None,
        state=None,
        area=None,
        vrf=None,
    ):
        """Return OSPF neighbor and interface records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            ifname: Filter by interface name(s).
            state: OSPF state filter — ``"full"``, ``"passive"``,
                ``"other"``, or negations like ``"!full"``.
            area: Filter by OSPF area(s).
            vrf: Filter by VRF(s).

        Returns:
            List of OSPF record dicts.
        """
        return self._get("ospf", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ifname=ifname, state=state, area=area, vrf=vrf,
        ))

    def summarize_ospf(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        ifname=None,
        state=None,
        area=None,
        vrf=None,
    ):
        """Return summary statistics for the ``ospf`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            ifname: Filter by interface name(s).
            state: OSPF state filter.
            area: Filter by OSPF area(s).
            vrf: Filter by VRF(s).

        Returns:
            Column-oriented summary dict.
        """
        return self._get("ospf", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ifname=ifname, state=state, area=area, vrf=vrf,
        ))

    def unique_ospf(
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
        state=None,
        area=None,
        vrf=None,
    ):
        """Return unique values and counts for a column in the ``ospf`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            ifname: Filter by interface name(s).
            state: OSPF state filter.
            area: Filter by OSPF area(s).
            vrf: Filter by VRF(s).

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("ospf", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ifname=ifname, state=state, area=area, vrf=vrf,
        ))

    def top_ospf(
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
        state=None,
        area=None,
        vrf=None,
    ):
        """Return the top N records sorted by a column in the ``ospf`` table.

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
            ifname: Filter by interface name(s).
            state: OSPF state filter.
            area: Filter by OSPF area(s).
            vrf: Filter by VRF(s).

        Returns:
            List of top-N OSPF record dicts.
        """
        return self._get("ospf", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ifname=ifname, state=state, area=area, vrf=vrf,
        ))

    def assert_ospf(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        ifname=None,
        state=None,
        area=None,
        vrf=None,
        result=None,
    ):
        """Run OSPF assertions and return pass/fail results.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            ifname: Filter by interface name(s).
            state: OSPF state filter.
            area: Filter by OSPF area(s).
            vrf: Filter by VRF(s).
            result: Assertion result filter — ``"pass"``, ``"fail"``,
                or ``"all"`` (default).

        Returns:
            List of OSPF assertion result dicts.
        """
        return self._get("ospf", "assert", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ifname=ifname, state=state, area=area, vrf=vrf,
            result=result,
        ))
