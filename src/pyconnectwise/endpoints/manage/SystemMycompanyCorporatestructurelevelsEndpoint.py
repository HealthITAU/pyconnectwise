from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyCorporatestructurelevelsCountEndpoint import (
    SystemMycompanyCorporatestructurelevelsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemMycompanyCorporatestructurelevelsIdEndpoint import (
    SystemMycompanyCorporatestructurelevelsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import CorporateStructureLevel
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemMycompanyCorporatestructurelevelsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[CorporateStructureLevel], ConnectWiseManageRequestParams],
    IPaginateable[CorporateStructureLevel, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "corporateStructureLevels", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[CorporateStructureLevel])
        IPaginateable.__init__(self, CorporateStructureLevel)

        self.count = self._register_child_endpoint(
            SystemMycompanyCorporatestructurelevelsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(self, id: int) -> SystemMycompanyCorporatestructurelevelsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMycompanyCorporatestructurelevelsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMycompanyCorporatestructurelevelsIdEndpoint: The initialized SystemMycompanyCorporatestructurelevelsIdEndpoint object.
        """
        child = SystemMycompanyCorporatestructurelevelsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[CorporateStructureLevel]:
        """
        Performs a GET request against the /system/myCompany/corporateStructureLevels endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CorporateStructureLevel]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            CorporateStructureLevel,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[CorporateStructureLevel]:
        """
        Performs a GET request against the /system/myCompany/corporateStructureLevels endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[CorporateStructureLevel]: The parsed response data.
        """
        return self._parse_many(
            CorporateStructureLevel,
            super()._make_request("GET", data=data, params=params).json(),
        )
