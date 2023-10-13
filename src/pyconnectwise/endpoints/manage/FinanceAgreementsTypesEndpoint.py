from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsTypesCountEndpoint import FinanceAgreementsTypesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsTypesIdEndpoint import FinanceAgreementsTypesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsTypesInfoEndpoint import FinanceAgreementsTypesInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import AgreementType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceAgreementsTypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[AgreementType], ConnectWiseManageRequestParams],
    IPostable[AgreementType, ConnectWiseManageRequestParams],
    IPaginateable[AgreementType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "types", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[AgreementType])
        IPostable.__init__(self, AgreementType)
        IPaginateable.__init__(self, AgreementType)

        self.count = self._register_child_endpoint(FinanceAgreementsTypesCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(FinanceAgreementsTypesInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> FinanceAgreementsTypesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementsTypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementsTypesIdEndpoint: The initialized FinanceAgreementsTypesIdEndpoint object.
        """
        child = FinanceAgreementsTypesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[AgreementType]:
        """
        Performs a GET request against the /finance/agreements/types endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), AgreementType, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[AgreementType]:
        """
        Performs a GET request against the /finance/agreements/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementType]: The parsed response data.
        """
        return self._parse_many(AgreementType, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> AgreementType:
        """
        Performs a POST request against the /finance/agreements/types endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementType: The parsed response data.
        """
        return self._parse_one(AgreementType, super()._make_request("POST", data=data, params=params).json())
