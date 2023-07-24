from typing import Any

from pyconnectwise.endpoints.automate.UserclassesIdEndpoint import UserclassesIdEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate.Automate.Api.Domain.Contracts.Users import UserClass
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class UserclassesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Userclasses", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> UserclassesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized UserclassesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            UserclassesIdEndpoint: The initialized UserclassesIdEndpoint object.
        """
        child = UserclassesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[UserClass]:
        """
        Performs a GET request against the /Userclasses endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UserClass]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            UserClass,
            self,
            page,
            page_size,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> list[UserClass]:
        """
        Performs a GET request against the /Userclasses endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UserClass]: The parsed response data.
        """
        return self._parse_many(
            UserClass, super()._make_request("GET", data=data, params=params).json()
        )
