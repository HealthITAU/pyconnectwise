from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyCorporatestructureCountEndpoint import \
    SystemMycompanyCorporatestructureCountEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyCorporatestructureIdEndpoint import \
    SystemMycompanyCorporatestructureIdEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyCorporatestructureInfoEndpoint import \
    SystemMycompanyCorporatestructureInfoEndpoint
from pyconnectwise.models.manage import CorporateStructure
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMycompanyCorporatestructureEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "corporateStructure", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(
            SystemMycompanyCorporatestructureCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            SystemMycompanyCorporatestructureInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemMycompanyCorporatestructureIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMycompanyCorporatestructureIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMycompanyCorporatestructureIdEndpoint: The initialized SystemMycompanyCorporatestructureIdEndpoint object.
        """
        child = SystemMycompanyCorporatestructureIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[CorporateStructure]:
        """
        Performs a GET request against the /system/myCompany/corporateStructure endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CorporateStructure]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), CorporateStructure, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[CorporateStructure]:
        """
        Performs a GET request against the /system/myCompany/corporateStructure endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CorporateStructure]: The parsed response data.
        """
        return self._parse_many(CorporateStructure, super()._make_request("GET", data=data, params=params).json())
