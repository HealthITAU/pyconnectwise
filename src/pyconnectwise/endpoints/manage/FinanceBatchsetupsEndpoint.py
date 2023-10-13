from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceBatchsetupsCountEndpoint import FinanceBatchsetupsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceBatchsetupsIdEndpoint import FinanceBatchsetupsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import AgreementBatchSetup
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceBatchsetupsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AgreementBatchSetup], ConnectWiseManageRequestParams],
    IPaginateable[AgreementBatchSetup, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "batchSetups", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[AgreementBatchSetup])
        IPaginateable.__init__(self, AgreementBatchSetup)

        self.count = self._register_child_endpoint(FinanceBatchsetupsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceBatchsetupsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceBatchsetupsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceBatchsetupsIdEndpoint: The initialized FinanceBatchsetupsIdEndpoint object.
        """
        child = FinanceBatchsetupsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[AgreementBatchSetup]:
        """
        Performs a GET request against the /finance/batchSetups endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementBatchSetup]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), AgreementBatchSetup, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[AgreementBatchSetup]:
        """
        Performs a GET request against the /finance/batchSetups endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementBatchSetup]: The parsed response data.
        """
        return self._parse_many(AgreementBatchSetup, super()._make_request("GET", data=data, params=params).json())
