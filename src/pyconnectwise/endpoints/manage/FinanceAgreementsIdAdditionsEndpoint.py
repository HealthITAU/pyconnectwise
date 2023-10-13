from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdAdditionsCountEndpoint import \
    FinanceAgreementsIdAdditionsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdAdditionsIdEndpoint import FinanceAgreementsIdAdditionsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Addition
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceAgreementsIdAdditionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Addition], ConnectWiseManageRequestParams],
    IPostable[Addition, ConnectWiseManageRequestParams],
    IPaginateable[Addition, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "additions", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[Addition])
        IPostable.__init__(self, Addition)
        IPaginateable.__init__(self, Addition)

        self.count = self._register_child_endpoint(
            FinanceAgreementsIdAdditionsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceAgreementsIdAdditionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsIdAdditionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsIdAdditionsIdEndpoint: The initialized FinanceAgreementsIdAdditionsIdEndpoint object.
        """
        child = FinanceAgreementsIdAdditionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Addition]:
        """
        Performs a GET request against the /finance/agreements/{id}/additions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Addition]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Addition, self, page, page_size, params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> list[Addition]:
        """
        Performs a GET request against the /finance/agreements/{id}/additions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Addition]: The parsed response data.
        """
        return self._parse_many(Addition, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Addition:
        """
        Performs a POST request against the /finance/agreements/{id}/additions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Addition: The parsed response data.
        """
        return self._parse_one(Addition, super()._make_request("POST", data=data, params=params).json())
