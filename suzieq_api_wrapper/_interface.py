"""Interface REST API – /api/v2/interface."""


class InterfaceMixin:
    """Methods for the ``interface`` SuzieQ table."""

    def show_interface(
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
        type=None,
        mtu=None,
        master=None,
        vrf=None,
        portmode=None,
        vlan=None,
        macaddr=None,
        bond=None,
        ifindex=None,
    ):
        """Return interface records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            ifname: Filter by interface name(s).
            state: Interface state filter — ``"up"``, ``"down"``,
                ``"errDisabled"``, ``"notConnected"``, or negations
                like ``"!down"``.
            type: Filter by interface type(s).
            mtu: Filter by MTU with a comparison operator, e.g. ``">1500"``.
            master: Filter by master/parent interface(s).
            vrf: Filter by VRF(s).
            portmode: Filter by port mode(s).
            vlan: Filter by VLAN(s).
            macaddr: Filter by MAC address(es).
            bond: Filter by bond interface(s).
            ifindex: Filter by interface index(es).

        Returns:
            List of interface record dicts.
        """
        return self._get("interface", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ifname=ifname, state=state, type=type, mtu=mtu,
            master=master, vrf=vrf, portmode=portmode, vlan=vlan,
            macaddr=macaddr, bond=bond, ifindex=ifindex,
        ))

    def summarize_interface(
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
        type=None,
        mtu=None,
        master=None,
        vrf=None,
        portmode=None,
        vlan=None,
        macaddr=None,
        bond=None,
        ifindex=None,
    ):
        """Return summary statistics for the ``interface`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            ifname: Filter by interface name(s).
            state: Interface state filter.
            type: Filter by interface type(s).
            mtu: Filter by MTU with a comparison operator.
            master: Filter by master/parent interface(s).
            vrf: Filter by VRF(s).
            portmode: Filter by port mode(s).
            vlan: Filter by VLAN(s).
            macaddr: Filter by MAC address(es).
            bond: Filter by bond interface(s).
            ifindex: Filter by interface index(es).

        Returns:
            Column-oriented summary dict.
        """
        return self._get("interface", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ifname=ifname, state=state, type=type, mtu=mtu,
            master=master, vrf=vrf, portmode=portmode, vlan=vlan,
            macaddr=macaddr, bond=bond, ifindex=ifindex,
        ))

    def unique_interface(
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
        type=None,
        mtu=None,
        master=None,
        vrf=None,
        portmode=None,
        vlan=None,
        macaddr=None,
        bond=None,
        ifindex=None,
    ):
        """Return unique values and counts for a column in the ``interface`` table.

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
            state: Interface state filter.
            type: Filter by interface type(s).
            mtu: Filter by MTU with a comparison operator.
            master: Filter by master/parent interface(s).
            vrf: Filter by VRF(s).
            portmode: Filter by port mode(s).
            vlan: Filter by VLAN(s).
            macaddr: Filter by MAC address(es).
            bond: Filter by bond interface(s).
            ifindex: Filter by interface index(es).

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("interface", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ifname=ifname, state=state, type=type, mtu=mtu,
            master=master, vrf=vrf, portmode=portmode, vlan=vlan,
            macaddr=macaddr, bond=bond, ifindex=ifindex,
        ))

    def top_interface(
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
        type=None,
        mtu=None,
        master=None,
        vrf=None,
        portmode=None,
        vlan=None,
        macaddr=None,
        bond=None,
        ifindex=None,
    ):
        """Return the top N records sorted by a column in the ``interface`` table.

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
            state: Interface state filter.
            type: Filter by interface type(s).
            mtu: Filter by MTU with a comparison operator.
            master: Filter by master/parent interface(s).
            vrf: Filter by VRF(s).
            portmode: Filter by port mode(s).
            vlan: Filter by VLAN(s).
            macaddr: Filter by MAC address(es).
            bond: Filter by bond interface(s).
            ifindex: Filter by interface index(es).

        Returns:
            List of top-N interface record dicts.
        """
        return self._get("interface", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ifname=ifname, state=state, type=type, mtu=mtu,
            master=master, vrf=vrf, portmode=portmode, vlan=vlan,
            macaddr=macaddr, bond=bond, ifindex=ifindex,
        ))

    def assert_interface(
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
        type=None,
        mtu=None,
        master=None,
        vrf=None,
        value=None,
        what=None,
        result=None,
        ignore_missing_peer=None,
    ):
        """Run interface assertions and return pass/fail results.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            ifname: Filter by interface name(s).
            state: Interface state filter.
            type: Filter by interface type(s).
            mtu: Filter by MTU with a comparison operator.
            master: Filter by master/parent interface(s).
            vrf: Filter by VRF(s).
            value: Threshold value(s) for the assertion check.
            what: What to assert (e.g. ``"mtu"``, ``"speed"``).
            result: Assertion result filter — ``"pass"``, ``"fail"``,
                or ``"all"`` (default).
            ignore_missing_peer: If ``True``, skip failures for
                interfaces with no matching peer.

        Returns:
            List of interface assertion result dicts.
        """
        return self._get("interface", "assert", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            ifname=ifname, state=state, type=type, mtu=mtu,
            master=master, vrf=vrf, value=value, what=what,
            result=result, ignore_missing_peer=ignore_missing_peer,
        ))
