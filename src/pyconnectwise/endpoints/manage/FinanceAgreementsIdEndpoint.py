from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdAdditionsEndpoint import FinanceAgreementsIdAdditionsEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdAdjustmentsEndpoint import FinanceAgreementsIdAdjustmentsEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdBoarddefaultsEndpoint import (
    FinanceAgreementsIdBoarddefaultsEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementsIdConfigurationsEndpoint import (
    FinanceAgreementsIdConfigurationsEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementsIdSitesEndpoint import FinanceAgreementsIdSitesEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkroleexclusionsEndpoint import (
    FinanceAgreementsIdWorkroleexclusionsEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorkrolesEndpoint import FinanceAgreementsIdWorkrolesEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorktypeexclusionsEndpoint import (
    FinanceAgreementsIdWorktypeexclusionsEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementsIdWorktypesEndpoint import FinanceAgreementsIdWorktypesEndpoint
from pyconnectwise.interfaces import IGettable, IPaginateable, IPatchable, IPuttable
from pyconnectwise.models.manage import Agreement
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceAgreementsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[Agreement, ConnectWiseManageRequestParams],
    IPatchable[Agreement, ConnectWiseManageRequestParams],
    IPuttable[Agreement, ConnectWiseManageRequestParams],
    IPaginateable[Agreement, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, Agreement)
        IPatchable.__init__(self, Agreement)
        IPuttable.__init__(self, Agreement)
        IPaginateable.__init__(self, Agreement)

        self.additions = self._register_child_endpoint(
            FinanceAgreementsIdAdditionsEndpoint(client, parent_endpoint=self)
        )
        self.adjustments = self._register_child_endpoint(
            FinanceAgreementsIdAdjustmentsEndpoint(client, parent_endpoint=self)
        )
        self.board_defaults = self._register_child_endpoint(
            FinanceAgreementsIdBoarddefaultsEndpoint(client, parent_endpoint=self)
        )
        self.configurations = self._register_child_endpoint(
            FinanceAgreementsIdConfigurationsEndpoint(client, parent_endpoint=self)
        )
        self.sites = self._register_child_endpoint(FinanceAgreementsIdSitesEndpoint(client, parent_endpoint=self))
        self.work_role_exclusions = self._register_child_endpoint(
            FinanceAgreementsIdWorkroleexclusionsEndpoint(client, parent_endpoint=self)
        )
        self.work_type_exclusions = self._register_child_endpoint(
            FinanceAgreementsIdWorktypeexclusionsEndpoint(client, parent_endpoint=self)
        )
        self.workroles = self._register_child_endpoint(
            FinanceAgreementsIdWorkrolesEndpoint(client, parent_endpoint=self)
        )
        self.worktypes = self._register_child_endpoint(
            FinanceAgreementsIdWorktypesEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Agreement]:
        """
        Performs a GET request against the /finance/agreements/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Agreement]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(super()._make_request("GET", params=params), Agreement, self, page, page_size, params)

    def delete(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> None:
        """
        Performs a DELETE request against the /finance/agreements/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def get(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Agreement:
        """
        Performs a GET request against the /finance/agreements/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Agreement: The parsed response data.
        """
        return self._parse_one(Agreement, super()._make_request("GET", data=data, params=params).json())

    def patch(self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None) -> Agreement:
        """
        Performs a PATCH request against the /finance/agreements/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Agreement: The parsed response data.
        """
        return self._parse_one(Agreement, super()._make_request("PATCH", data=data, params=params).json())

    def put(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Agreement:
        """
        Performs a PUT request against the /finance/agreements/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Agreement: The parsed response data.
        """
        return self._parse_one(Agreement, super()._make_request("PUT", data=data, params=params).json())
