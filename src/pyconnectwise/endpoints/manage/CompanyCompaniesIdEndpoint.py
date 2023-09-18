from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdCustomstatusnotesEndpoint import \
    CompanyCompaniesIdCustomstatusnotesEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdGroupsEndpoint import CompanyCompaniesIdGroupsEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdManagementreportnotificationsEndpoint import \
    CompanyCompaniesIdManagementreportnotificationsEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdManagementreportsetupEndpoint import \
    CompanyCompaniesIdManagementreportsetupEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdManagementsummaryreportsEndpoint import \
    CompanyCompaniesIdManagementsummaryreportsEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdMergeEndpoint import CompanyCompaniesIdMergeEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdNotesEndpoint import CompanyCompaniesIdNotesEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdSitesEndpoint import CompanyCompaniesIdSitesEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdSurveysEndpoint import CompanyCompaniesIdSurveysEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTeamsEndpoint import CompanyCompaniesIdTeamsEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTracksEndpoint import CompanyCompaniesIdTracksEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTypeassociationsEndpoint import \
    CompanyCompaniesIdTypeassociationsEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdUsagesEndpoint import CompanyCompaniesIdUsagesEndpoint
from pyconnectwise.models.manage import Company
from pyconnectwise.responses.paginated_response import PaginatedResponse


class CompanyCompaniesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.sites = self._register_child_endpoint(CompanyCompaniesIdSitesEndpoint(client, parent_endpoint=self))
        self.usages = self._register_child_endpoint(CompanyCompaniesIdUsagesEndpoint(client, parent_endpoint=self))
        self.groups = self._register_child_endpoint(CompanyCompaniesIdGroupsEndpoint(client, parent_endpoint=self))
        self.management_report_notifications = self._register_child_endpoint(
            CompanyCompaniesIdManagementreportnotificationsEndpoint(client, parent_endpoint=self)
        )
        self.merge = self._register_child_endpoint(CompanyCompaniesIdMergeEndpoint(client, parent_endpoint=self))
        self.teams = self._register_child_endpoint(CompanyCompaniesIdTeamsEndpoint(client, parent_endpoint=self))
        self.tracks = self._register_child_endpoint(CompanyCompaniesIdTracksEndpoint(client, parent_endpoint=self))
        self.custom_status_notes = self._register_child_endpoint(
            CompanyCompaniesIdCustomstatusnotesEndpoint(client, parent_endpoint=self)
        )
        self.notes = self._register_child_endpoint(CompanyCompaniesIdNotesEndpoint(client, parent_endpoint=self))
        self.management_summary_reports = self._register_child_endpoint(
            CompanyCompaniesIdManagementsummaryreportsEndpoint(client, parent_endpoint=self)
        )
        self.type_associations = self._register_child_endpoint(
            CompanyCompaniesIdTypeassociationsEndpoint(client, parent_endpoint=self)
        )
        self.management_report_setup = self._register_child_endpoint(
            CompanyCompaniesIdManagementreportsetupEndpoint(client, parent_endpoint=self)
        )
        self.surveys = self._register_child_endpoint(CompanyCompaniesIdSurveysEndpoint(client, parent_endpoint=self))

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Company]:
        """
        Performs a GET request against the /company/companies/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Company]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Company, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Company:
        """
        Performs a GET request against the /company/companies/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Company: The parsed response data.
        """
        return self._parse_one(Company, super()._make_request("GET", data=data, params=params).json())

    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> None:
        """
        Performs a DELETE request against the /company/companies/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Company:
        """
        Performs a PUT request against the /company/companies/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Company: The parsed response data.
        """
        return self._parse_one(Company, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Company:
        """
        Performs a PATCH request against the /company/companies/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Company: The parsed response data.
        """
        return self._parse_one(Company, super()._make_request("PATCH", data=data, params=params).json())
