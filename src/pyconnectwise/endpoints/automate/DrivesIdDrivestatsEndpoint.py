from typing import Any

from pyconnectwise.endpoints.automate.DrivesIdDrivestatsDailyEndpoint import DrivesIdDrivestatsDailyEndpoint
from pyconnectwise.endpoints.automate.DrivesIdDrivestatsMonthlyEndpoint import DrivesIdDrivestatsMonthlyEndpoint
from pyconnectwise.endpoints.automate.DrivesIdDrivestatsWeeklyEndpoint import DrivesIdDrivestatsWeeklyEndpoint
from pyconnectwise.endpoints.automate.DrivesIdDrivestatsYearlyEndpoint import DrivesIdDrivestatsYearlyEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class DrivesIdDrivestatsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Drivestats", parent_endpoint=parent_endpoint)

        self.yearly = self._register_child_endpoint(DrivesIdDrivestatsYearlyEndpoint(client, parent_endpoint=self))
        self.weekly = self._register_child_endpoint(DrivesIdDrivestatsWeeklyEndpoint(client, parent_endpoint=self))
        self.daily = self._register_child_endpoint(DrivesIdDrivestatsDailyEndpoint(client, parent_endpoint=self))
        self.monthly = self._register_child_endpoint(DrivesIdDrivestatsMonthlyEndpoint(client, parent_endpoint=self))
