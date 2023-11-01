from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMycompanyCrmCountEndpoint import (
    SystemMycompanyCrmCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemMycompanyCrmIdEndpoint import (
    SystemMycompanyCrmIdEndpoint,
)
from pyconnectwise.endpoints.manage.SystemMycompanyCrmInfoEndpoint import (
    SystemMycompanyCrmInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import Crm
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemMycompanyCrmEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Crm], ConnectWiseManageRequestParams],
    IPaginateable[Crm, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "crm", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[Crm])
        IPaginateable.__init__(self, Crm)

        self.count = self._register_child_endpoint(
            SystemMycompanyCrmCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            SystemMycompanyCrmInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemMycompanyCrmIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized SystemMycompanyCrmIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMycompanyCrmIdEndpoint: The initialized SystemMycompanyCrmIdEndpoint object.
        """
        child = SystemMycompanyCrmIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[Crm]:
        """
        Performs a GET request against the /system/myCompany/crm endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Crm]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            Crm,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[Crm]:
        """
        Performs a GET request against the /system/myCompany/crm endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Crm]: The parsed response data.
        """
        return self._parse_many(
            Crm, super()._make_request("GET", data=data, params=params).json()
        )
