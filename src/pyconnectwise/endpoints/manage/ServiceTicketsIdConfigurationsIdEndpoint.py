from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ConfigurationReference
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceTicketsIdConfigurationsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ConfigurationReference, ConnectWiseManageRequestParams],
    IPaginateable[ConfigurationReference, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, ConfigurationReference)
        IPaginateable.__init__(self, ConfigurationReference)

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ConfigurationReference]:
        """
        Performs a GET request against the /service/tickets/{id}/configurations/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ConfigurationReference]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ConfigurationReference, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ConfigurationReference:
        """
        Performs a GET request against the /service/tickets/{id}/configurations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationReference: The parsed response data.
        """
        return self._parse_one(ConfigurationReference, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /service/tickets/{id}/configurations/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)
