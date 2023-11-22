from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdBoarddefaultsEndpoint import (
    FinanceAgreementtypesIdBoarddefaultsEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorkroleexclusionsEndpoint import (
    FinanceAgreementtypesIdWorkroleexclusionsEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorkrolesEndpoint import (
    FinanceAgreementtypesIdWorkrolesEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorktypeexclusionsEndpoint import (
    FinanceAgreementtypesIdWorktypeexclusionsEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAgreementtypesIdWorktypesEndpoint import (
    FinanceAgreementtypesIdWorktypesEndpoint,
)

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class FinanceAgreementtypesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)

        self.board_defaults = self._register_child_endpoint(
            FinanceAgreementtypesIdBoarddefaultsEndpoint(client, parent_endpoint=self)
        )
        self.work_role_exclusions = self._register_child_endpoint(
            FinanceAgreementtypesIdWorkroleexclusionsEndpoint(client, parent_endpoint=self)
        )
        self.work_type_exclusions = self._register_child_endpoint(
            FinanceAgreementtypesIdWorktypeexclusionsEndpoint(client, parent_endpoint=self)
        )
        self.workroles = self._register_child_endpoint(
            FinanceAgreementtypesIdWorkrolesEndpoint(client, parent_endpoint=self)
        )
        self.worktypes = self._register_child_endpoint(
            FinanceAgreementtypesIdWorktypesEndpoint(client, parent_endpoint=self)
        )
