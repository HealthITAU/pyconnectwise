from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdBoarddefaultsEndpoint import \
    FinanceAgreementtypesIdBoarddefaultsEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorkroleexclusionsEndpoint import \
    FinanceAgreementtypesIdWorkroleexclusionsEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorkrolesEndpoint import \
    FinanceAgreementtypesIdWorkrolesEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorktypeexclusionsEndpoint import \
    FinanceAgreementtypesIdWorktypeexclusionsEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorktypesEndpoint import \
    FinanceAgreementtypesIdWorktypesEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class FinanceAgreementtypesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.work_type_exclusions = self._register_child_endpoint(
            FinanceAgreementtypesIdWorktypeexclusionsEndpoint(client, parent_endpoint=self)
        )
        self.workroles = self._register_child_endpoint(
            FinanceAgreementtypesIdWorkrolesEndpoint(client, parent_endpoint=self)
        )
        self.worktypes = self._register_child_endpoint(
            FinanceAgreementtypesIdWorktypesEndpoint(client, parent_endpoint=self)
        )
        self.work_role_exclusions = self._register_child_endpoint(
            FinanceAgreementtypesIdWorkroleexclusionsEndpoint(client, parent_endpoint=self)
        )
        self.board_defaults = self._register_child_endpoint(
            FinanceAgreementtypesIdBoarddefaultsEndpoint(client, parent_endpoint=self)
        )
