from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.CompanyCompaniesIdMergeEndpoint import CompanyCompaniesIdMergeEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdUsagesEndpoint import CompanyCompaniesIdUsagesEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdCustomStatusNotesEndpoint import CompanyCompaniesIdCustomStatusNotesEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdGroupsEndpoint import CompanyCompaniesIdGroupsEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdManagementReportNotificationsEndpoint import CompanyCompaniesIdManagementReportNotificationsEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdManagementReportSetupEndpoint import CompanyCompaniesIdManagementReportSetupEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdManagementSummaryReportsEndpoint import CompanyCompaniesIdManagementSummaryReportsEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdNotesEndpoint import CompanyCompaniesIdNotesEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdSitesEndpoint import CompanyCompaniesIdSitesEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTeamsEndpoint import CompanyCompaniesIdTeamsEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTracksEndpoint import CompanyCompaniesIdTracksEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdTypeAssociationsEndpoint import CompanyCompaniesIdTypeAssociationsEndpoint
from pyconnectwise.models.manage.CompanyModel import CompanyModel

class CompanyCompaniesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.merge = self.register_child_endpoint(
            CompanyCompaniesIdMergeEndpoint(client, parent_endpoint=self)
        )
        self.usages = self.register_child_endpoint(
            CompanyCompaniesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.customStatusNotes = self.register_child_endpoint(
            CompanyCompaniesIdCustomStatusNotesEndpoint(client, parent_endpoint=self)
        )
        self.groups = self.register_child_endpoint(
            CompanyCompaniesIdGroupsEndpoint(client, parent_endpoint=self)
        )
        self.managementReportNotifications = self.register_child_endpoint(
            CompanyCompaniesIdManagementReportNotificationsEndpoint(client, parent_endpoint=self)
        )
        self.managementReportSetup = self.register_child_endpoint(
            CompanyCompaniesIdManagementReportSetupEndpoint(client, parent_endpoint=self)
        )
        self.managementSummaryReports = self.register_child_endpoint(
            CompanyCompaniesIdManagementSummaryReportsEndpoint(client, parent_endpoint=self)
        )
        self.notes = self.register_child_endpoint(
            CompanyCompaniesIdNotesEndpoint(client, parent_endpoint=self)
        )
        self.sites = self.register_child_endpoint(
            CompanyCompaniesIdSitesEndpoint(client, parent_endpoint=self)
        )
        self.teams = self.register_child_endpoint(
            CompanyCompaniesIdTeamsEndpoint(client, parent_endpoint=self)
        )
        self.tracks = self.register_child_endpoint(
            CompanyCompaniesIdTracksEndpoint(client, parent_endpoint=self)
        )
        self.typeAssociations = self.register_child_endpoint(
            CompanyCompaniesIdTypeAssociationsEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[CompanyModel]:
        """
        Performs a GET request against the /company/companies/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[CompanyModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            CompanyModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyModel:
        """
        Performs a GET request against the /company/companies/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyModel: The parsed response data.
        """
        return self._parse_one(CompanyModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /company/companies/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyModel:
        """
        Performs a PUT request against the /company/companies/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyModel: The parsed response data.
        """
        return self._parse_one(CompanyModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> CompanyModel:
        """
        Performs a PATCH request against the /company/companies/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            CompanyModel: The parsed response data.
        """
        return self._parse_one(CompanyModel, super().make_request("PATCH", params=params).json())
        