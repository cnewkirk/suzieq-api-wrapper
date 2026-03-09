"""SqPoller REST API – /api/v2/sqPoller."""


class SqPollerMixin:
    """Methods for the ``sqPoller`` SuzieQ table (internal poller health)."""

    def show_sqpoller(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        service=None,
        status=None,
        pollExcdPeriodCount=None,
    ):
        """Return SuzieQ poller health records.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window (ISO 8601 or relative).
            end_time: End of time window.
            view: One of ``"latest"`` (default), ``"all"``, or ``"changes"``.
            columns: List of columns to return; use ``["*"]`` for all.
            query_str: Pandas query string for post-filter.
            service: Filter by service/table name being polled.
            status: Poller status — ``"pass"``, ``"fail"``, or ``"all"``.
            pollExcdPeriodCount: Filter by number of times the poll
                period was exceeded (e.g. ``">0"``).

        Returns:
            List of poller health record dicts.
        """
        return self._get("sqPoller", "show", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            service=service, status=status,
            pollExcdPeriodCount=pollExcdPeriodCount,
        ))

    def summarize_sqpoller(
        self,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        service=None,
        status=None,
        pollExcdPeriodCount=None,
    ):
        """Return summary statistics for the ``sqPoller`` table.

        Args:
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include in summary.
            query_str: Pandas query string for post-filter.
            service: Filter by service/table name.
            status: Poller status — ``"pass"``, ``"fail"``, or ``"all"``.
            pollExcdPeriodCount: Filter by poll period exceeded count.

        Returns:
            Column-oriented summary dict.
        """
        return self._get("sqPoller", "summarize", self._build_params(
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            service=service, status=status,
            pollExcdPeriodCount=pollExcdPeriodCount,
        ))

    def unique_sqpoller(
        self,
        what,
        namespace=None,
        hostname=None,
        start_time=None,
        end_time=None,
        view=None,
        columns=None,
        query_str=None,
        service=None,
        status=None,
        pollExcdPeriodCount=None,
    ):
        """Return unique values and counts for a column in the ``sqPoller`` table.

        Args:
            what: Column name to compute unique values for.
            namespace: Filter by namespace(s).
            hostname: Filter by device hostname(s).
            start_time: Start of time window.
            end_time: End of time window.
            view: One of ``"latest"``, ``"all"``, or ``"changes"``.
            columns: Columns to include.
            query_str: Pandas query string for post-filter.
            service: Filter by service/table name.
            status: Poller status — ``"pass"``, ``"fail"``, or ``"all"``.
            pollExcdPeriodCount: Filter by poll period exceeded count.

        Returns:
            List of dicts with ``"entry"`` and ``"count"`` keys.
        """
        return self._get("sqPoller", "unique", self._build_params(
            what=what,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            service=service, status=status,
            pollExcdPeriodCount=pollExcdPeriodCount,
        ))

    def top_sqpoller(
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
        service=None,
        status=None,
        pollExcdPeriodCount=None,
    ):
        """Return the top N records sorted by a column in the ``sqPoller`` table.

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
            service: Filter by service/table name.
            status: Poller status — ``"pass"``, ``"fail"``, or ``"all"``.
            pollExcdPeriodCount: Filter by poll period exceeded count.

        Returns:
            List of top-N poller health record dicts.
        """
        return self._get("sqPoller", "top", self._build_params(
            what=what, count=count, reverse=reverse,
            namespace=namespace, hostname=hostname,
            start_time=start_time, end_time=end_time,
            view=view, columns=columns, query_str=query_str,
            service=service, status=status,
            pollExcdPeriodCount=pollExcdPeriodCount,
        ))
