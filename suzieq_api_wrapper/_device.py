"""Device REST API – /api/v2/device."""


class DeviceMixin:
    """Methods for the ``device`` SuzieQ table (device inventory)."""

    def show_device(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        os=None,
        vendor=None,
        model=None,
        version=None,
        status=None,
        ignore_neverpoll=None,
        address=None,
    ):
        """Return device inventory records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            os: Filter by operating system(s).
            vendor: Filter by vendor(s).
            model: Filter by model(s).
            version: Filter by OS version(s).
            status: Device status filter — ``"alive"``, ``"dead"``,
                ``"neverpoll"``, or ``"!alive"`` to negate.
            ignore_neverpoll: If ``True``, exclude devices that have
                never been polled.
            address: Filter by management IP address(es).

        Returns:
            List of device record dicts.
        """
        return self._get("device", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            os=os, vendor=vendor, model=model, version=version,
            status=status, ignore_neverpoll=ignore_neverpoll,
            address=address,
        ))

    def summarize_device(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        os=None,
        vendor=None,
        model=None,
        version=None,
        status=None,
        ignore_neverpoll=None,
        address=None,
    ):
        """Return summary statistics for the ``device`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            os: Filter by operating system(s).
            vendor: Filter by vendor(s).
            model: Filter by model(s).
            version: Filter by OS version(s).
            status: Device status filter.
            ignore_neverpoll: If ``True``, exclude never-polled devices.
            address: Filter by management IP address(es).

        Returns:
            Column-oriented summary dict.
        """
        return self._get("device", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            os=os, vendor=vendor, model=model, version=version,
            status=status, ignore_neverpoll=ignore_neverpoll,
            address=address,
        ))

    def unique_device(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        os=None,
        vendor=None,
        model=None,
        version=None,
        status=None,
        ignore_neverpoll=None,
        address=None,
    ):
        """Return unique values and counts for a column in the ``device`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            os: Filter by operating system(s).
            vendor: Filter by vendor(s).
            model: Filter by model(s).
            version: Filter by OS version(s).
            status: Device status filter.
            ignore_neverpoll: If ``True``, exclude never-polled devices.
            address: Filter by management IP address(es).

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("device", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            os=os, vendor=vendor, model=model, version=version,
            status=status, ignore_neverpoll=ignore_neverpoll,
            address=address,
        ))

    def top_device(
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
        os=None,
        vendor=None,
        model=None,
        version=None,
        status=None,
        ignore_neverpoll=None,
        address=None,
    ):
        """Return the top N records sorted by a column in the ``device`` table.

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
            os: Filter by operating system(s).
            vendor: Filter by vendor(s).
            model: Filter by model(s).
            version: Filter by OS version(s).
            status: Device status filter.
            ignore_neverpoll: If ``True``, exclude never-polled devices.
            address: Filter by management IP address(es).

        Returns:
            List of top-N device record dicts.
        """
        return self._get("device", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            os=os, vendor=vendor, model=model, version=version,
            status=status, ignore_neverpoll=ignore_neverpoll,
            address=address,
        ))
