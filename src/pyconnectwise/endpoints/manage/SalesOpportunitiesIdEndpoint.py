from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdContactsEndpoint import SalesOpportunitiesIdContactsEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdConverttoagreementEndpoint import \
    SalesOpportunitiesIdConverttoagreementEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdConverttoprojectEndpoint import \
    SalesOpportunitiesIdConverttoprojectEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdConverttosalesorderEndpoint import \
    SalesOpportunitiesIdConverttosalesorderEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdConverttoserviceticketEndpoint import \
    SalesOpportunitiesIdConverttoserviceticketEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdForecastEndpoint import SalesOpportunitiesIdForecastEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdNotesEndpoint import SalesOpportunitiesIdNotesEndpoint
from pyconnectwise.endpoints.manage.SalesOpportunitiesIdTeamEndpoint import SalesOpportunitiesIdTeamEndpoint
from pyconnectwise.models.manage import Opportunity
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesOpportunitiesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.team = self._register_child_endpoint(SalesOpportunitiesIdTeamEndpoint(client, parent_endpoint=self))
        self.convert_to_agreement = self._register_child_endpoint(
            SalesOpportunitiesIdConverttoagreementEndpoint(client, parent_endpoint=self)
        )
        self.convert_to_project = self._register_child_endpoint(
            SalesOpportunitiesIdConverttoprojectEndpoint(client, parent_endpoint=self)
        )
        self.convert_to_sales_order = self._register_child_endpoint(
            SalesOpportunitiesIdConverttosalesorderEndpoint(client, parent_endpoint=self)
        )
        self.notes = self._register_child_endpoint(SalesOpportunitiesIdNotesEndpoint(client, parent_endpoint=self))
        self.contacts = self._register_child_endpoint(
            SalesOpportunitiesIdContactsEndpoint(client, parent_endpoint=self)
        )
        self.convert_to_service_ticket = self._register_child_endpoint(
            SalesOpportunitiesIdConverttoserviceticketEndpoint(client, parent_endpoint=self)
        )
        self.forecast = self._register_child_endpoint(
            SalesOpportunitiesIdForecastEndpoint(client, parent_endpoint=self)
        )

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Opportunity]:
        """
        Performs a GET request against the /sales/opportunities/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Opportunity]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), Opportunity, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Opportunity:
        """
        Performs a GET request against the /sales/opportunities/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Opportunity: The parsed response data.
        """
        return self._parse_one(Opportunity, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /sales/opportunities/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Opportunity:
        """
        Performs a PUT request against the /sales/opportunities/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Opportunity: The parsed response data.
        """
        return self._parse_one(Opportunity, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Opportunity:
        """
        Performs a PATCH request against the /sales/opportunities/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Opportunity: The parsed response data.
        """
        return self._parse_one(Opportunity, super()._make_request("PATCH", data=data, params=params).json())
