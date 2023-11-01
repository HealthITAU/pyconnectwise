from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.automate import LabTechComputerEffectivePatchingPolicy
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class ComputersIdEffectivepatchingpolicyEndpoint(
    ConnectWiseEndpoint,
    IGettable[LabTechComputerEffectivePatchingPolicy, ConnectWiseAutomateRequestParams],
    IPaginateable[
        LabTechComputerEffectivePatchingPolicy, ConnectWiseAutomateRequestParams
    ],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Effectivepatchingpolicy", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, LabTechComputerEffectivePatchingPolicy)
        IPaginateable.__init__(self, LabTechComputerEffectivePatchingPolicy)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechComputerEffectivePatchingPolicy]:
        """
        Performs a GET request against the /Computers/{id}/Effectivepatchingpolicy endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechComputerEffectivePatchingPolicy]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechComputerEffectivePatchingPolicy,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechComputerEffectivePatchingPolicy:
        """
        Performs a GET request against the /Computers/{id}/Effectivepatchingpolicy endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechComputerEffectivePatchingPolicy: The parsed response data.
        """
        return self._parse_one(
            LabTechComputerEffectivePatchingPolicy,
            super()._make_request("GET", data=data, params=params).json(),
        )
