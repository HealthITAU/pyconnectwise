from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.automate import AutomateGroupPatchingPolicy
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class GrouppatchingpoliciesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AutomateGroupPatchingPolicy], ConnectWiseAutomateRequestParams],
    IPaginateable[AutomateGroupPatchingPolicy, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Grouppatchingpolicies", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[AutomateGroupPatchingPolicy])
        IPaginateable.__init__(self, AutomateGroupPatchingPolicy)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[AutomateGroupPatchingPolicy]:
        """
        Performs a GET request against the /Grouppatchingpolicies endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AutomateGroupPatchingPolicy]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            AutomateGroupPatchingPolicy,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[AutomateGroupPatchingPolicy]:
        """
        Performs a GET request against the /Grouppatchingpolicies endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AutomateGroupPatchingPolicy]: The parsed response data.
        """
        return self._parse_many(
            AutomateGroupPatchingPolicy,
            super()._make_request("GET", data=data, params=params).json(),
        )
