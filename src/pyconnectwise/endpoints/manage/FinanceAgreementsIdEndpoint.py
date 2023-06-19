from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementsIdAdditionsEndpoint import FinanceAgreementsIdAdditionsEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdAdjustmentsEndpoint import FinanceAgreementsIdAdjustmentsEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdBoardDefaultsEndpoint import FinanceAgreementsIdBoardDefaultsEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdConfigurationsEndpoint import FinanceAgreementsIdConfigurationsEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdSitesEndpoint import FinanceAgreementsIdSitesEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkRoleExclusionsEndpoint import FinanceAgreementsIdWorkRoleExclusionsEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkrolesEndpoint import FinanceAgreementsIdWorkrolesEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkTypeExclusionsEndpoint import FinanceAgreementsIdWorkTypeExclusionsEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorktypesEndpoint import FinanceAgreementsIdWorktypesEndpoint
from pyconnectwise.models.manage.AgreementModel import AgreementModel

class FinanceAgreementsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.additions = self.register_child_endpoint(
            FinanceAgreementsIdAdditionsEndpoint(client, parent_endpoint=self)
        )
        self.adjustments = self.register_child_endpoint(
            FinanceAgreementsIdAdjustmentsEndpoint(client, parent_endpoint=self)
        )
        self.boardDefaults = self.register_child_endpoint(
            FinanceAgreementsIdBoardDefaultsEndpoint(client, parent_endpoint=self)
        )
        self.configurations = self.register_child_endpoint(
            FinanceAgreementsIdConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.sites = self.register_child_endpoint(
            FinanceAgreementsIdSitesEndpoint(client, parent_endpoint=self)
        )
        self.workRoleExclusions = self.register_child_endpoint(
            FinanceAgreementsIdWorkRoleExclusionsEndpoint(client, parent_endpoint=self)
        )
        self.workroles = self.register_child_endpoint(
            FinanceAgreementsIdWorkrolesEndpoint(client, parent_endpoint=self)
        )
        self.workTypeExclusions = self.register_child_endpoint(
            FinanceAgreementsIdWorkTypeExclusionsEndpoint(client, parent_endpoint=self)
        )
        self.worktypes = self.register_child_endpoint(
            FinanceAgreementsIdWorktypesEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AgreementModel]:
        """
        Performs a GET request against the /finance/agreements/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AgreementModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementModel:
        """
        Performs a GET request against the /finance/agreements/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementModel: The parsed response data.
        """
        return self._parse_one(AgreementModel, super().make_request("GET", params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /finance/agreements/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementModel:
        """
        Performs a PUT request against the /finance/agreements/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementModel: The parsed response data.
        """
        return self._parse_one(AgreementModel, super().make_request("PUT", params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementModel:
        """
        Performs a PATCH request against the /finance/agreements/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementModel: The parsed response data.
        """
        return self._parse_one(AgreementModel, super().make_request("PATCH", params=params).json())
        