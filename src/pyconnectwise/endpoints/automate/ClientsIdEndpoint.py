from typing import Any

from pyconnectwise.endpoints.automate.ClientsIdDocumentsEndpoint import ClientsIdDocumentsEndpoint
from pyconnectwise.endpoints.automate.ClientsIdLicensesEndpoint import ClientsIdLicensesEndpoint
from pyconnectwise.endpoints.automate.ClientsIdPermissionsEndpoint import ClientsIdPermissionsEndpoint
from pyconnectwise.endpoints.automate.ClientsIdProductkeysEndpoint import ClientsIdProductkeysEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.automate import LabTechClient
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ClientsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[LabTechClient, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechClient, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, LabTechClient)
        IPaginateable.__init__(self, LabTechClient)

        self.permissions = self._register_child_endpoint(ClientsIdPermissionsEndpoint(client, parent_endpoint=self))
        self.licenses = self._register_child_endpoint(ClientsIdLicensesEndpoint(client, parent_endpoint=self))
        self.documents = self._register_child_endpoint(ClientsIdDocumentsEndpoint(client, parent_endpoint=self))
        self.productkeys = self._register_child_endpoint(ClientsIdProductkeysEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseAutomateRequestParams | None = None
    ) -> PaginatedResponse[LabTechClient]:
        """
        Performs a GET request against the /Clients/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechClient]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechClient, self, page, page_size, params
        )

    def get(self, data: JSON | None = None, params: ConnectWiseAutomateRequestParams | None = None) -> LabTechClient:
        """
        Performs a GET request against the /Clients/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechClient: The parsed response data.
        """
        return self._parse_one(LabTechClient, super()._make_request("GET", data=data, params=params).json())
