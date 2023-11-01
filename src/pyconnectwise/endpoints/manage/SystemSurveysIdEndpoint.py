from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemSurveysIdCopyEndpoint import (
    SystemSurveysIdCopyEndpoint,
)
from pyconnectwise.endpoints.manage.SystemSurveysIdInfoEndpoint import (
    SystemSurveysIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.SystemSurveysIdQuestionsEndpoint import (
    SystemSurveysIdQuestionsEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import Survey
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemSurveysIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[Survey, ConnectWiseManageRequestParams],
    IPuttable[Survey, ConnectWiseManageRequestParams],
    IPatchable[Survey, ConnectWiseManageRequestParams],
    IPaginateable[Survey, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, Survey)
        IPuttable.__init__(self, Survey)
        IPatchable.__init__(self, Survey)
        IPaginateable.__init__(self, Survey)

        self.copy = self._register_child_endpoint(
            SystemSurveysIdCopyEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            SystemSurveysIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.questions = self._register_child_endpoint(
            SystemSurveysIdQuestionsEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Survey]:
        """
        Performs a GET request against the /system/surveys/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Survey]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Survey,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Survey:
        """
        Performs a GET request against the /system/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Survey: The parsed response data.
        """
        return self._parse_one(
            Survey, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /system/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Survey:
        """
        Performs a PUT request against the /system/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Survey: The parsed response data.
        """
        return self._parse_one(
            Survey, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Survey:
        """
        Performs a PATCH request against the /system/surveys/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Survey: The parsed response data.
        """
        return self._parse_one(
            Survey, super()._make_request("PATCH", data=data, params=params).json()
        )
