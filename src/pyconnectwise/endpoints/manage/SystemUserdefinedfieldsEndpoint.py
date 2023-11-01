from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemUserdefinedfieldsCountEndpoint import (
    SystemUserdefinedfieldsCountEndpoint,
)
from pyconnectwise.endpoints.manage.SystemUserdefinedfieldsIdEndpoint import (
    SystemUserdefinedfieldsIdEndpoint,
)
from pyconnectwise.endpoints.manage.SystemUserdefinedfieldsInfoEndpoint import (
    SystemUserdefinedfieldsInfoEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import UserDefinedField
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemUserdefinedfieldsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[UserDefinedField], ConnectWiseManageRequestParams],
    IPostable[UserDefinedField, ConnectWiseManageRequestParams],
    IPaginateable[UserDefinedField, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "userDefinedFields", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[UserDefinedField])
        IPostable.__init__(self, UserDefinedField)
        IPaginateable.__init__(self, UserDefinedField)

        self.count = self._register_child_endpoint(
            SystemUserdefinedfieldsCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            SystemUserdefinedfieldsInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> SystemUserdefinedfieldsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemUserdefinedfieldsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemUserdefinedfieldsIdEndpoint: The initialized SystemUserdefinedfieldsIdEndpoint object.
        """
        child = SystemUserdefinedfieldsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[UserDefinedField]:
        """
        Performs a GET request against the /system/userDefinedFields endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UserDefinedField]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            UserDefinedField,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[UserDefinedField]:
        """
        Performs a GET request against the /system/userDefinedFields endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UserDefinedField]: The parsed response data.
        """
        return self._parse_many(
            UserDefinedField,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> UserDefinedField:
        """
        Performs a POST request against the /system/userDefinedFields endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            UserDefinedField: The parsed response data.
        """
        return self._parse_one(
            UserDefinedField,
            super()._make_request("POST", data=data, params=params).json(),
        )
