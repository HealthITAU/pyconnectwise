from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyCorporatestructureIdInfoEndpoint import (
    SystemMycompanyCorporatestructureIdInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import CorporateStructure
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemMycompanyCorporatestructureIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[CorporateStructure, ConnectWiseManageRequestParams],
    IPuttable[CorporateStructure, ConnectWiseManageRequestParams],
    IPatchable[CorporateStructure, ConnectWiseManageRequestParams],
    IPaginateable[CorporateStructure, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, CorporateStructure)
        IPuttable.__init__(self, CorporateStructure)
        IPatchable.__init__(self, CorporateStructure)
        IPaginateable.__init__(self, CorporateStructure)

        self.info = self._register_child_endpoint(
            SystemMycompanyCorporatestructureIdInfoEndpoint(
                client, parent_endpoint=self
            )
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[CorporateStructure]:
        """
        Performs a GET request against the /system/myCompany/corporateStructure/{id} endpoint and returns an initialized PaginatedResponse object.

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
            super()._make_request("GET", params=params),
            CorporateStructure,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CorporateStructure:
        """
        Performs a GET request against the /system/myCompany/corporateStructure/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CorporateStructure: The parsed response data.
        """
        return self._parse_one(
            CorporateStructure,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CorporateStructure:
        """
        Performs a PUT request against the /system/myCompany/corporateStructure/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CorporateStructure: The parsed response data.
        """
        return self._parse_one(
            CorporateStructure,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> CorporateStructure:
        """
        Performs a PATCH request against the /system/myCompany/corporateStructure/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CorporateStructure: The parsed response data.
        """
        return self._parse_one(
            CorporateStructure,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
