"""Network REST API – /api/v2/network."""


class NetworkMixin:
    """Methods for the ``network`` SuzieQ table.

    The primary verb for this table is ``find``, which performs a
    network-wide search for an IP or MAC address.  The ``show``,
    ``summarize``, ``unique``, and ``top`` verbs are deprecated aliases
    that redirect to the ``namespace`` table on the server side.
    """

    def find_network(
        self,
        address,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        vlan=None,
        vrf=None,
    ):
        """Search the network for an IP or MAC address.

        Args:
            address: IP or MAC address(es) to locate.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            vlan: VLAN context for the search.
            vrf: VRF context for the search.

        Returns:
            List of dicts describing where the address was found.
        """
        return self._get("network", "find", self._build_params(
            address=address,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            vlan=vlan, vrf=vrf,
        ))

    def show_network(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
    ):
        """Return network/namespace records.

        .. deprecated::
            This verb is deprecated on the SuzieQ server and redirects to
            the ``namespace`` table.  Use :meth:`show_namespace` instead.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: List of columns to return.
            query_str: Pandas query string for post-filter.

        Returns:
            List of namespace record dicts.
        """
        return self._get("network", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
        ))

    def summarize_network(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
    ):
        """Return summary statistics for the ``network`` table.

        .. deprecated::
            This verb is deprecated on the SuzieQ server.
            Use :meth:`summarize_namespace` instead.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.

        Returns:
            Column-oriented summary dict.
        """
        return self._get("network", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
        ))

    def unique_network(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
    ):
        """Return unique values and counts for a column in the ``network`` table.

        .. deprecated::
            This verb is deprecated on the SuzieQ server.
            Use :meth:`unique_namespace` instead.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("network", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
        ))

    def top_network(
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
    ):
        """Return the top N records sorted by a column in the ``network`` table.

        .. deprecated::
            This verb is deprecated on the SuzieQ server.
            Use :meth:`top_namespace` instead.

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

        Returns:
            List of top-N namespace record dicts.
        """
        return self._get("network", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
        ))
