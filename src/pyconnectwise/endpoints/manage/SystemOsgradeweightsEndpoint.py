from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemOsgradeweightsCountEndpoint import (
    SystemOsgradeweightsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemOsgradeweightsIdEndpoint import (
    SystemOsgradeweightsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import OsGradeWeight
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class SystemOsgradeweightsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[OsGradeWeight], ConnectWiseManageRequestParams],
    IPaginateable[OsGradeWeight, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "osgradeweights", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[OsGradeWeight])
        IPaginateable.__init__(self, OsGradeWeight)

        self.count = self._register_child_endpoint(
            SystemOsgradeweightsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemOsgradeweightsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemOsgradeweightsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemOsgradeweightsIdEndpoint: The initialized SystemOsgradeweightsIdEndpoint object.
        """
        child = SystemOsgradeweightsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[OsGradeWeight]:
        """
        Performs a GET request against the /system/osgradeweights endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OsGradeWeight]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            OsGradeWeight,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[OsGradeWeight]:
        """
        Performs a GET request against the /system/osgradeweights endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OsGradeWeight]: The parsed response data.
        """
        return self._parse_many(
            OsGradeWeight, super()._make_request("GET", data=data, params=params).json()
        )
