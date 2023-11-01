from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.automate import LabTechProductKey
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class ClientsIdProductkeysEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechProductKey], ConnectWiseAutomateRequestParams],
    IPostable[LabTechProductKey, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechProductKey, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Productkeys", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechProductKey])
        IPostable.__init__(self, LabTechProductKey)
        IPaginateable.__init__(self, LabTechProductKey)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechProductKey]:
        """
        Performs a GET request against the /Clients/{id}/Productkeys endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechProductKey]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechProductKey,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechProductKey]:
        """
        Performs a GET request against the /Clients/{id}/Productkeys endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechProductKey]: The parsed response data.
        """
        return self._parse_many(
            LabTechProductKey,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechProductKey:
        """
        Performs a POST request against the /Clients/{id}/Productkeys endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechProductKey: The parsed response data.
        """
        return self._parse_one(
            LabTechProductKey,
            super()._make_request("POST", data=data, params=params).json(),
        )
