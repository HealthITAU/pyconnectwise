from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate.LabTech.Models import ComputerEffectivePatchingPolicy
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ComputersIdEffectivepatchingpolicyEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(
            client, "Effectivepatchingpolicy", parent_endpoint=parent_endpoint
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ComputerEffectivePatchingPolicy]:
        """
        Performs a GET request against the /Computers/{id}/Effectivepatchingpolicy endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ComputerEffectivePatchingPolicy]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ComputerEffectivePatchingPolicy,
            self,
            page,
            page_size,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> ComputerEffectivePatchingPolicy:
        """
        Performs a GET request against the /Computers/{id}/Effectivepatchingpolicy endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ComputerEffectivePatchingPolicy: The parsed response data.
        """
        return self._parse_one(
            ComputerEffectivePatchingPolicy,
            super()._make_request("GET", data=data, params=params).json(),
        )
