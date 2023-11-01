from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleColorsCountEndpoint import (
    ScheduleColorsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ScheduleColorsIdEndpoint import (
    ScheduleColorsIdEndpoint,
)
from pyconnectwise.endpoints.manage.ScheduleColorsResetEndpoint import (
    ScheduleColorsResetEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import ScheduleColor
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ScheduleColorsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ScheduleColor], ConnectWiseManageRequestParams],
    IPaginateable[ScheduleColor, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "colors", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ScheduleColor])
        IPaginateable.__init__(self, ScheduleColor)

        self.count = self._register_child_endpoint(
            ScheduleColorsCountEndpoint(client, parent_endpoint=self)
        )
        self.reset = self._register_child_endpoint(
            ScheduleColorsResetEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ScheduleColorsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized ScheduleColorsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ScheduleColorsIdEndpoint: The initialized ScheduleColorsIdEndpoint object.
        """
        child = ScheduleColorsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ScheduleColor]:
        """
        Performs a GET request against the /schedule/colors endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleColor]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ScheduleColor,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ScheduleColor]:
        """
        Performs a GET request against the /schedule/colors endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ScheduleColor]: The parsed response data.
        """
        return self._parse_many(
            ScheduleColor, super()._make_request("GET", data=data, params=params).json()
        )
