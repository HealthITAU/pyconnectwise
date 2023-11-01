from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.automate import LabTechCommandExecute
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class ComputersIdCommandexecuteEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechCommandExecute], ConnectWiseAutomateRequestParams],
    IPostable[LabTechCommandExecute, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechCommandExecute, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Commandexecute", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechCommandExecute])
        IPostable.__init__(self, LabTechCommandExecute)
        IPaginateable.__init__(self, LabTechCommandExecute)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechCommandExecute]:
        """
        Performs a GET request against the /Computers/{id}/Commandexecute endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechCommandExecute]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechCommandExecute,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechCommandExecute]:
        """
        Performs a GET request against the /Computers/{id}/Commandexecute endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechCommandExecute]: The parsed response data.
        """
        return self._parse_many(
            LabTechCommandExecute,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechCommandExecute:
        """
        Performs a POST request against the /Computers/{id}/Commandexecute endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechCommandExecute: The parsed response data.
        """
        return self._parse_one(
            LabTechCommandExecute,
            super()._make_request("POST", data=data, params=params).json(),
        )
