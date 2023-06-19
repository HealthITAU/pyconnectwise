from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeAccrualsEndpoint import TimeAccrualsEndpoint
from pyconnectwise.endpoints.manage.TimeActivitystopwatchesEndpoint import TimeActivitystopwatchesEndpoint
from pyconnectwise.endpoints.manage.TimeChargeCodesEndpoint import TimeChargeCodesEndpoint
from pyconnectwise.endpoints.manage.TimeEntriesEndpoint import TimeEntriesEndpoint
from pyconnectwise.endpoints.manage.TimeSchedulestopwatchesEndpoint import TimeSchedulestopwatchesEndpoint
from pyconnectwise.endpoints.manage.TimeSheetsEndpoint import TimeSheetsEndpoint
from pyconnectwise.endpoints.manage.TimeTicketstopwatchesEndpoint import TimeTicketstopwatchesEndpoint
from pyconnectwise.endpoints.manage.TimeTimePeriodSetupsEndpoint import TimeTimePeriodSetupsEndpoint
from pyconnectwise.endpoints.manage.TimeWorkRolesEndpoint import TimeWorkRolesEndpoint
from pyconnectwise.endpoints.manage.TimeWorkTypesEndpoint import TimeWorkTypesEndpoint

class TimeEndpoint(ConnectWiseEndpoint):
    def __init__(self, client):
        super().__init__(client, "time")
        
        self.accruals = self.register_child_endpoint(
            TimeAccrualsEndpoint(client, parent_endpoint=self)
        )
        self.activitystopwatches = self.register_child_endpoint(
            TimeActivitystopwatchesEndpoint(client, parent_endpoint=self)
        )
        self.chargeCodes = self.register_child_endpoint(
            TimeChargeCodesEndpoint(client, parent_endpoint=self)
        )
        self.entries = self.register_child_endpoint(
            TimeEntriesEndpoint(client, parent_endpoint=self)
        )
        self.schedulestopwatches = self.register_child_endpoint(
            TimeSchedulestopwatchesEndpoint(client, parent_endpoint=self)
        )
        self.sheets = self.register_child_endpoint(
            TimeSheetsEndpoint(client, parent_endpoint=self)
        )
        self.ticketstopwatches = self.register_child_endpoint(
            TimeTicketstopwatchesEndpoint(client, parent_endpoint=self)
        )
        self.timePeriodSetups = self.register_child_endpoint(
            TimeTimePeriodSetupsEndpoint(client, parent_endpoint=self)
        )
        self.workRoles = self.register_child_endpoint(
            TimeWorkRolesEndpoint(client, parent_endpoint=self)
        )
        self.workTypes = self.register_child_endpoint(
            TimeWorkTypesEndpoint(client, parent_endpoint=self)
        )