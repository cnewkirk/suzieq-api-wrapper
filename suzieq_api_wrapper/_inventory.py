"""Inventory REST API – /api/v2/inventory."""


class InventoryMixin:
    """Methods for the ``inventory`` SuzieQ table (hardware inventory)."""

    def show_inventory(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        type=None,
        serial=None,
        model=None,
        vendor=None,
        status=None,
    ):
        """Return hardware inventory records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            type: Filter by component type(s).
            serial: Filter by serial number(s).
            model: Filter by model(s).
            vendor: Filter by vendor(s).
            status: Component status — ``"present"`` or ``"absent"``.

        Returns:
            List of inventory record dicts.
        """
        return self._get("inventory", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            type=type, serial=serial, model=model,
            vendor=vendor, status=status,
        ))

    def summarize_inventory(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        type=None,
        serial=None,
        model=None,
        vendor=None,
        status=None,
    ):
        """Return summary statistics for the ``inventory`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            type: Filter by component type(s).
            serial: Filter by serial number(s).
            model: Filter by model(s).
            vendor: Filter by vendor(s).
            status: Component status — ``"present"`` or ``"absent"``.

        Returns:
            Column-oriented summary dict.
        """
        return self._get("inventory", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            type=type, serial=serial, model=model,
            vendor=vendor, status=status,
        ))

    def unique_inventory(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        type=None,
        serial=None,
        model=None,
        vendor=None,
        status=None,
    ):
        """Return unique values and counts for a column in the ``inventory`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            type: Filter by component type(s).
            serial: Filter by serial number(s).
            model: Filter by model(s).
            vendor: Filter by vendor(s).
            status: Component status — ``"present"`` or ``"absent"``.

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("inventory", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            type=type, serial=serial, model=model,
            vendor=vendor, status=status,
        ))

    def top_inventory(
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
        type=None,
        serial=None,
        model=None,
        vendor=None,
        status=None,
    ):
        """Return the top N records sorted by a column in the ``inventory`` table.

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
            type: Filter by component type(s).
            serial: Filter by serial number(s).
            model: Filter by model(s).
            vendor: Filter by vendor(s).
            status: Component status — ``"present"`` or ``"absent"``.

        Returns:
            List of top-N inventory record dicts.
        """
        return self._get("inventory", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            type=type, serial=serial, model=model,
            vendor=vendor, status=status,
        ))
