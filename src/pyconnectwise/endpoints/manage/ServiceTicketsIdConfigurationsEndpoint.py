from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceTicketsIdConfigurationsCountEndpoint import (
    ServiceTicketsIdConfigurationsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceTicketsIdConfigurationsIdEndpoint import (
    ServiceTicketsIdConfigurationsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import ConfigurationReference
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceTicketsIdConfigurationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ConfigurationReference], ConnectWiseManageRequestParams],
    IPostable[ConfigurationReference, ConnectWiseManageRequestParams],
    IPaginateable[ConfigurationReference, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "configurations", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ConfigurationReference])
        IPostable.__init__(self, ConfigurationReference)
        IPaginateable.__init__(self, ConfigurationReference)

        self.count = self._register_child_endpoint(
            ServiceTicketsIdConfigurationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ServiceTicketsIdConfigurationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceTicketsIdConfigurationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceTicketsIdConfigurationsIdEndpoint: The initialized ServiceTicketsIdConfigurationsIdEndpoint object.
        """
        child = ServiceTicketsIdConfigurationsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ConfigurationReference]:
        """
        Performs a GET request against the /service/tickets/{id}/configurations endpoint and returns an initialized PaginatedResponse object.

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
            super()._make_request("GET", params=params),
            ConfigurationReference,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ConfigurationReference]:
        """
        Performs a GET request against the /service/tickets/{id}/configurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ConfigurationReference]: The parsed response data.
        """
        return self._parse_many(
            ConfigurationReference,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ConfigurationReference:
        """
        Performs a POST request against the /service/tickets/{id}/configurations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ConfigurationReference: The parsed response data.
        """
        return self._parse_one(
            ConfigurationReference,
            super()._make_request("POST", data=data, params=params).json(),
        )
