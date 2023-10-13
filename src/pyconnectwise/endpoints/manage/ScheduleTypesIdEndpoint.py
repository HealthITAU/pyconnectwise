from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleTypesIdInfoEndpoint import ScheduleTypesIdInfoEndpoint
from pyconnectwise.endpoints.manage.ScheduleTypesIdUsagesEndpoint import ScheduleTypesIdUsagesEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ScheduleType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ScheduleTypesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ScheduleType, ConnectWiseManageRequestParams],
    IPuttable[ScheduleType, ConnectWiseManageRequestParams],
    IPatchable[ScheduleType, ConnectWiseManageRequestParams],
    IPaginateable[ScheduleType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, ScheduleType)
        IPuttable.__init__(self, ScheduleType)
        IPatchable.__init__(self, ScheduleType)
        IPaginateable.__init__(self, ScheduleType)

        self.usages = self._register_child_endpoint(ScheduleTypesIdUsagesEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(ScheduleTypesIdInfoEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ScheduleType]:
        """
        Performs a GET request against the /schedule/types/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ScheduleType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ScheduleType, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ScheduleType:
        """
        Performs a GET request against the /schedule/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScheduleType: The parsed response data.
        """
        return self._parse_one(ScheduleType, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /schedule/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> ScheduleType:
        """
        Performs a PUT request against the /schedule/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScheduleType: The parsed response data.
        """
        return self._parse_one(ScheduleType, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> ScheduleType:
        """
        Performs a PATCH request against the /schedule/types/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ScheduleType: The parsed response data.
        """
        return self._parse_one(ScheduleType, super()._make_request("PATCH", data=data, params=params).json())
