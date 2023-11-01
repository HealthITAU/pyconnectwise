from typing import Any

from pyconnectwise.endpoints.automate.MonitorsIdCollecteddataDailyaveragesEndpoint import (
    MonitorsIdCollecteddataDailyaveragesEndpoint,
)
from pyconnectwise.endpoints.automate.MonitorsIdCollecteddataMonthlyaveragesEndpoint import (
    MonitorsIdCollecteddataMonthlyaveragesEndpoint,
)
from pyconnectwise.endpoints.automate.MonitorsIdCollecteddataWeeklyaveragesEndpoint import (
    MonitorsIdCollecteddataWeeklyaveragesEndpoint,
)
from pyconnectwise.endpoints.automate.MonitorsIdCollecteddataYearlyaveragesEndpoint import (
    MonitorsIdCollecteddataYearlyaveragesEndpoint,
)
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class MonitorsIdCollecteddataEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Collecteddata", parent_endpoint=parent_endpoint
        )

        self.monthlyaverages = self._register_child_endpoint(
            MonitorsIdCollecteddataMonthlyaveragesEndpoint(client, parent_endpoint=self)
        )
        self.weeklyaverages = self._register_child_endpoint(
            MonitorsIdCollecteddataWeeklyaveragesEndpoint(client, parent_endpoint=self)
        )
        self.dailyaverages = self._register_child_endpoint(
            MonitorsIdCollecteddataDailyaveragesEndpoint(client, parent_endpoint=self)
        )
        self.yearlyaverages = self._register_child_endpoint(
            MonitorsIdCollecteddataYearlyaveragesEndpoint(client, parent_endpoint=self)
        )
