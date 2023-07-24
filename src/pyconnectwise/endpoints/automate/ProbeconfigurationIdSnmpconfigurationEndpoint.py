from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate.LabTech.Repositories.MySQL.Domain.Models.NetworkProbe import (
    ProbeSnmpConfiguration,
)
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProbeconfigurationIdSnmpconfigurationEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Snmpconfiguration", parent_endpoint=parent_endpoint)

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[ProbeSnmpConfiguration]:
        """
        Performs a GET request against the /Probeconfiguration/{id}/Snmpconfiguration endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ProbeSnmpConfiguration]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ProbeSnmpConfiguration,
            self,
            page,
            page_size,
        )

    def get(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> ProbeSnmpConfiguration:
        """
        Performs a GET request against the /Probeconfiguration/{id}/Snmpconfiguration endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProbeSnmpConfiguration: The parsed response data.
        """
        return self._parse_one(
            ProbeSnmpConfiguration,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def patch(
        self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}
    ) -> ProbeSnmpConfiguration:
        """
        Performs a PATCH request against the /Probeconfiguration/{id}/Snmpconfiguration endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ProbeSnmpConfiguration: The parsed response data.
        """
        return self._parse_one(
            ProbeSnmpConfiguration,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
