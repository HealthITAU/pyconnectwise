from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServicePrioritiesIdImageEndpoint import (
    ServicePrioritiesIdImageEndpoint,
)
from pyconnectwise.endpoints.manage.ServicePrioritiesIdUsagesEndpoint import (
    ServicePrioritiesIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import Priority
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ServicePrioritiesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[Priority, ConnectWiseManageRequestParams],
    IPuttable[Priority, ConnectWiseManageRequestParams],
    IPatchable[Priority, ConnectWiseManageRequestParams],
    IPaginateable[Priority, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, Priority)
        IPuttable.__init__(self, Priority)
        IPatchable.__init__(self, Priority)
        IPaginateable.__init__(self, Priority)

        self.usages = self._register_child_endpoint(
            ServicePrioritiesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.image = self._register_child_endpoint(
            ServicePrioritiesIdImageEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Priority]:
        """
        Performs a GET request against the /service/priorities/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Priority]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Priority,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Priority:
        """
        Performs a GET request against the /service/priorities/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Priority: The parsed response data.
        """
        return self._parse_one(
            Priority, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /service/priorities/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Priority:
        """
        Performs a PUT request against the /service/priorities/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Priority: The parsed response data.
        """
        return self._parse_one(
            Priority, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> Priority:
        """
        Performs a PATCH request against the /service/priorities/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Priority: The parsed response data.
        """
        return self._parse_one(
            Priority, super()._make_request("PATCH", data=data, params=params).json()
        )
