from typing import Any

from pyconnectwise.endpoints.automate.ClientsIdDocumentsEndpoint import ClientsIdDocumentsEndpoint
from pyconnectwise.endpoints.automate.ClientsIdLicensesEndpoint import ClientsIdLicensesEndpoint
from pyconnectwise.endpoints.automate.ClientsIdPermissionsEndpoint import ClientsIdPermissionsEndpoint
from pyconnectwise.endpoints.automate.ClientsIdProductkeysEndpoint import ClientsIdProductkeysEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate.LabTech.Models import Client
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ClientsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.licenses = self._register_child_endpoint(ClientsIdLicensesEndpoint(client, parent_endpoint=self))
        self.permissions = self._register_child_endpoint(ClientsIdPermissionsEndpoint(client, parent_endpoint=self))
        self.documents = self._register_child_endpoint(ClientsIdDocumentsEndpoint(client, parent_endpoint=self))
        self.productkeys = self._register_child_endpoint(ClientsIdProductkeysEndpoint(client, parent_endpoint=self))

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Client]:
        """
        Performs a GET request against the /Clients/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Client]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Client,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Client:
        """
        Performs a GET request against the /Clients/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Client: The parsed response data.
        """
        return self._parse_one(Client, super()._make_request("GET", data=data, params=params).json())
