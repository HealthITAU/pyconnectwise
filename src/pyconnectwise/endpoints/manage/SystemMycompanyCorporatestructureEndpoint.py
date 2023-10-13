from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyCorporatestructureCountEndpoint import \
    SystemMycompanyCorporatestructureCountEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyCorporatestructureIdEndpoint import \
    SystemMycompanyCorporatestructureIdEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyCorporatestructureInfoEndpoint import \
    SystemMycompanyCorporatestructureInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import CorporateStructure
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemMycompanyCorporatestructureEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CorporateStructure], ConnectWiseManageRequestParams],
    IPaginateable[CorporateStructure, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "corporateStructure", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[CorporateStructure])
        IPaginateable.__init__(self, CorporateStructure)

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
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
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
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), CorporateStructure, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[CorporateStructure]:
        """
        Performs a GET request against the /system/myCompany/corporateStructure endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CorporateStructure]: The parsed response data.
        """
        return self._parse_many(CorporateStructure, super()._make_request("GET", data=data, params=params).json())
