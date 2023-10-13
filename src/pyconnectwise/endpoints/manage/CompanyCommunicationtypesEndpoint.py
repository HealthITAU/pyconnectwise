from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCommunicationtypesCountEndpoint import CompanyCommunicationtypesCountEndpoint
from pyconnectwise.endpoints.manage.CompanyCommunicationtypesIdEndpoint import CompanyCommunicationtypesIdEndpoint
from pyconnectwise.endpoints.manage.CompanyCommunicationtypesInfoEndpoint import CompanyCommunicationtypesInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CommunicationType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class CompanyCommunicationtypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CommunicationType], ConnectWiseManageRequestParams],
    IPostable[CommunicationType, ConnectWiseManageRequestParams],
    IPaginateable[CommunicationType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "communicationTypes", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CommunicationType])
        IPostable.__init__(self, CommunicationType)
        IPaginateable.__init__(self, CommunicationType)

        self.count = self._register_child_endpoint(CompanyCommunicationtypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(CompanyCommunicationtypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> CompanyCommunicationtypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyCommunicationtypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyCommunicationtypesIdEndpoint: The initialized CompanyCommunicationtypesIdEndpoint object.
        """
        child = CompanyCommunicationtypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[CommunicationType]:
        """
        Performs a GET request against the /company/communicationTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CommunicationType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CommunicationType, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[CommunicationType]:
        """
        Performs a GET request against the /company/communicationTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CommunicationType]: The parsed response data.
        """
        return self._parse_many(CommunicationType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> CommunicationType:
        """
        Performs a POST request against the /company/communicationTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CommunicationType: The parsed response data.
        """
        return self._parse_one(CommunicationType, super()._make_request("POST", data=data, params=params).json())
