from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdProducttypeexemptionsCountEndpoint import \
    FinanceTaxcodesIdProducttypeexemptionsCountEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxcodesIdProducttypeexemptionsIdEndpoint import \
    FinanceTaxcodesIdProducttypeexemptionsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ProductTypeExemption
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class FinanceTaxcodesIdProducttypeexemptionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ProductTypeExemption], ConnectWiseManageRequestParams],
    IPostable[ProductTypeExemption, ConnectWiseManageRequestParams],
    IPaginateable[ProductTypeExemption, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "productTypeExemptions", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ProductTypeExemption])
        IPostable.__init__(self, ProductTypeExemption)
        IPaginateable.__init__(self, ProductTypeExemption)

        self.count = self._register_child_endpoint(
            FinanceTaxcodesIdProducttypeexemptionsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> FinanceTaxcodesIdProducttypeexemptionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxcodesIdProducttypeexemptionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxcodesIdProducttypeexemptionsIdEndpoint: The initialized FinanceTaxcodesIdProducttypeexemptionsIdEndpoint object.
        """
        child = FinanceTaxcodesIdProducttypeexemptionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ProductTypeExemption]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/productTypeExemptions endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProductTypeExemption]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ProductTypeExemption, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ProductTypeExemption]:
        """
        Performs a GET request against the /finance/taxCodes/{id}/productTypeExemptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ProductTypeExemption]: The parsed response data.
        """
        return self._parse_many(ProductTypeExemption, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ProductTypeExemption:
        """
        Performs a POST request against the /finance/taxCodes/{id}/productTypeExemptions endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProductTypeExemption: The parsed response data.
        """
        return self._parse_one(ProductTypeExemption, super()._make_request("POST", data=data, params=params).json())
