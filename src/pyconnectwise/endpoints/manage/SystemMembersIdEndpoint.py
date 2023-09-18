from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdAccrualsEndpoint import SystemMembersIdAccrualsEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdCertificationsEndpoint import SystemMembersIdCertificationsEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdDeactivateEndpoint import SystemMembersIdDeactivateEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdDelegationsEndpoint import SystemMembersIdDelegationsEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdImageEndpoint import SystemMembersIdImageEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdLinkssouserEndpoint import SystemMembersIdLinkssouserEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdManageddeviceaccountsEndpoint import \
    SystemMembersIdManageddeviceaccountsEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdMycertificationsEndpoint import \
    SystemMembersIdMycertificationsEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdNotificationsettingsEndpoint import \
    SystemMembersIdNotificationsettingsEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdPersonasEndpoint import SystemMembersIdPersonasEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdSkillsEndpoint import SystemMembersIdSkillsEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdSubmitEndpoint import SystemMembersIdSubmitEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdTokensEndpoint import SystemMembersIdTokensEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdUnlinkssouserEndpoint import SystemMembersIdUnlinkssouserEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdUnusedtimesheetsEndpoint import \
    SystemMembersIdUnusedtimesheetsEndpoint
from pyconnectwise.endpoints.manage.SystemMembersIdUsagesEndpoint import SystemMembersIdUsagesEndpoint
from pyconnectwise.models.manage import Member
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemMembersIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.submit = self._register_child_endpoint(SystemMembersIdSubmitEndpoint(client, parent_endpoint=self))
        self.skills = self._register_child_endpoint(SystemMembersIdSkillsEndpoint(client, parent_endpoint=self))
        self.usages = self._register_child_endpoint(SystemMembersIdUsagesEndpoint(client, parent_endpoint=self))
        self.tokens = self._register_child_endpoint(SystemMembersIdTokensEndpoint(client, parent_endpoint=self))
        self.mycertifications = self._register_child_endpoint(
            SystemMembersIdMycertificationsEndpoint(client, parent_endpoint=self)
        )
        self.accruals = self._register_child_endpoint(SystemMembersIdAccrualsEndpoint(client, parent_endpoint=self))
        self.notification_settings = self._register_child_endpoint(
            SystemMembersIdNotificationsettingsEndpoint(client, parent_endpoint=self)
        )
        self.image = self._register_child_endpoint(SystemMembersIdImageEndpoint(client, parent_endpoint=self))
        self.link_sso_user = self._register_child_endpoint(
            SystemMembersIdLinkssouserEndpoint(client, parent_endpoint=self)
        )
        self.unlink_sso_user = self._register_child_endpoint(
            SystemMembersIdUnlinkssouserEndpoint(client, parent_endpoint=self)
        )
        self.managed_device_accounts = self._register_child_endpoint(
            SystemMembersIdManageddeviceaccountsEndpoint(client, parent_endpoint=self)
        )
        self.deactivate = self._register_child_endpoint(SystemMembersIdDeactivateEndpoint(client, parent_endpoint=self))
        self.unused_time_sheets = self._register_child_endpoint(
            SystemMembersIdUnusedtimesheetsEndpoint(client, parent_endpoint=self)
        )
        self.delegations = self._register_child_endpoint(
            SystemMembersIdDelegationsEndpoint(client, parent_endpoint=self)
        )
        self.certifications = self._register_child_endpoint(
            SystemMembersIdCertificationsEndpoint(client, parent_endpoint=self)
        )
        self.personas = self._register_child_endpoint(SystemMembersIdPersonasEndpoint(client, parent_endpoint=self))

    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[Member]:
        """
        Performs a GET request against the /system/members/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Member]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(super()._make_request("GET", params=params), Member, self, page, page_size, params)

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Member:
        """
        Performs a GET request against the /system/members/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Member: The parsed response data.
        """
        return self._parse_one(Member, super()._make_request("GET", data=data, params=params).json())

    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Member:
        """
        Performs a PUT request against the /system/members/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Member: The parsed response data.
        """
        return self._parse_one(Member, super()._make_request("PUT", data=data, params=params).json())

    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> Member:
        """
        Performs a PATCH request against the /system/members/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Member: The parsed response data.
        """
        return self._parse_one(Member, super()._make_request("PATCH", data=data, params=params).json())
