from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeAccrualsEndpoint import TimeAccrualsEndpoint
from pyconnectwise.endpoints.manage.TimeActivitystopwatchesEndpoint import TimeActivitystopwatchesEndpoint
from pyconnectwise.endpoints.manage.TimeChargecodesEndpoint import TimeChargecodesEndpoint
from pyconnectwise.endpoints.manage.TimeEntriesEndpoint import TimeEntriesEndpoint
from pyconnectwise.endpoints.manage.TimeInfoEndpoint import TimeInfoEndpoint
from pyconnectwise.endpoints.manage.TimeSchedulestopwatchesEndpoint import TimeSchedulestopwatchesEndpoint
from pyconnectwise.endpoints.manage.TimeSheetsEndpoint import TimeSheetsEndpoint
from pyconnectwise.endpoints.manage.TimeTicketstopwatchesEndpoint import TimeTicketstopwatchesEndpoint
from pyconnectwise.endpoints.manage.TimeTimeperiodsetupsEndpoint import TimeTimeperiodsetupsEndpoint
from pyconnectwise.endpoints.manage.TimeWorkrolesEndpoint import TimeWorkrolesEndpoint
from pyconnectwise.endpoints.manage.TimeWorktypesEndpoint import TimeWorktypesEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class TimeEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "time", parent_endpoint=parent_endpoint)

        self.work_types = self._register_child_endpoint(TimeWorktypesEndpoint(client, parent_endpoint=self))
        self.schedulestopwatches = self._register_child_endpoint(
            TimeSchedulestopwatchesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(TimeInfoEndpoint(client, parent_endpoint=self))
        self.accruals = self._register_child_endpoint(TimeAccrualsEndpoint(client, parent_endpoint=self))
        self.activitystopwatches = self._register_child_endpoint(
            TimeActivitystopwatchesEndpoint(client, parent_endpoint=self)
        )
        self.entries = self._register_child_endpoint(TimeEntriesEndpoint(client, parent_endpoint=self))
        self.time_period_setups = self._register_child_endpoint(
            TimeTimeperiodsetupsEndpoint(client, parent_endpoint=self)
        )
        self.charge_codes = self._register_child_endpoint(TimeChargecodesEndpoint(client, parent_endpoint=self))
        self.sheets = self._register_child_endpoint(TimeSheetsEndpoint(client, parent_endpoint=self))
        self.ticketstopwatches = self._register_child_endpoint(
            TimeTicketstopwatchesEndpoint(client, parent_endpoint=self)
        )
        self.work_roles = self._register_child_endpoint(TimeWorkrolesEndpoint(client, parent_endpoint=self))
