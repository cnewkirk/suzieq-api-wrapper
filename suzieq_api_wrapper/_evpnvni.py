"""EVPN VNI REST API – /api/v2/evpnVni."""


class EvpnVniMixin:
    """Methods for the ``evpnVni`` SuzieQ table."""

    def show_evpnvni(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        vni=None,
        priVtepIp=None,
    ):
        """Return EVPN VNI records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            vni: Filter by VNI number(s).
            priVtepIp: Filter by primary VTEP IP(s).

        Returns:
            List of EVPN VNI record dicts.
        """
        return self._get("evpnVni", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            vni=vni, priVtepIp=priVtepIp,
        ))

    def summarize_evpnvni(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        vni=None,
        priVtepIp=None,
    ):
        """Return summary statistics for the ``evpnVni`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            vni: Filter by VNI number(s).
            priVtepIp: Filter by primary VTEP IP(s).

        Returns:
            Column-oriented summary dict.
        """
        return self._get("evpnVni", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            vni=vni, priVtepIp=priVtepIp,
        ))

    def unique_evpnvni(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        vni=None,
        priVtepIp=None,
    ):
        """Return unique values and counts for a column in the ``evpnVni`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            vni: Filter by VNI number(s).
            priVtepIp: Filter by primary VTEP IP(s).

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("evpnVni", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            vni=vni, priVtepIp=priVtepIp,
        ))

    def top_evpnvni(
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
        vni=None,
        priVtepIp=None,
    ):
        """Return the top N records sorted by a column in the ``evpnVni`` table.

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
            vni: Filter by VNI number(s).
            priVtepIp: Filter by primary VTEP IP(s).

        Returns:
            List of top-N EVPN VNI record dicts.
        """
        return self._get("evpnVni", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            vni=vni, priVtepIp=priVtepIp,
        ))

    def assert_evpnvni(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        vni=None,
        priVtepIp=None,
        result=None,
    ):
        """Run EVPN VNI assertions and return pass/fail results.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            vni: Filter by VNI number(s).
            priVtepIp: Filter by primary VTEP IP(s).
            result: Assertion result filter — ``"pass"``, ``"fail"``,
                or ``"all"`` (default).

        Returns:
            List of EVPN VNI assertion result dicts.
        """
        return self._get("evpnVni", "assert", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            vni=vni, priVtepIp=priVtepIp, result=result,
        ))
