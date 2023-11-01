from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeAccrualsIdDetailsCountEndpoint import (
    TimeAccrualsIdDetailsCountEndpoint,
)
from pyconnectwise.endpoints.manage.TimeAccrualsIdDetailsIdEndpoint import (
    TimeAccrualsIdDetailsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import TimeAccrualDetail
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class TimeAccrualsIdDetailsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TimeAccrualDetail], ConnectWiseManageRequestParams],
    IPaginateable[TimeAccrualDetail, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "details", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[TimeAccrualDetail])
        IPaginateable.__init__(self, TimeAccrualDetail)

        self.count = self._register_child_endpoint(
            TimeAccrualsIdDetailsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> TimeAccrualsIdDetailsIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized TimeAccrualsIdDetailsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            TimeAccrualsIdDetailsIdEndpoint: The initialized TimeAccrualsIdDetailsIdEndpoint object.
        """
        child = TimeAccrualsIdDetailsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[TimeAccrualDetail]:
        """
        Performs a GET request against the /time/accruals/{id}/details endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TimeAccrualDetail]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            TimeAccrualDetail,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[TimeAccrualDetail]:
        """
        Performs a GET request against the /time/accruals/{id}/details endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TimeAccrualDetail]: The parsed response data.
        """
        return self._parse_many(
            TimeAccrualDetail,
            super()._make_request("GET", data=data, params=params).json(),
        )
