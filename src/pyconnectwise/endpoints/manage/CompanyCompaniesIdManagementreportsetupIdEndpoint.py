from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IPatchable, IPuttable
from pyconnectwise.models.manage import ManagementReportSetup
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams, PatchRequestData

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class CompanyCompaniesIdManagementreportsetupIdEndpoint(
    ConnectWiseEndpoint,
    IPatchable[ManagementReportSetup, ConnectWiseManageRequestParams],
    IPuttable[ManagementReportSetup, ConnectWiseManageRequestParams],
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)
        IPatchable.__init__(self, ManagementReportSetup)
        IPuttable.__init__(self, ManagementReportSetup)

    def patch(
        self, data: PatchRequestData, params: ConnectWiseManageRequestParams | None = None
    ) -> ManagementReportSetup:
        """
        Performs a PATCH request against the /company/companies/{id}/managementReportSetup/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementReportSetup: The parsed response data.
        """
        return self._parse_one(ManagementReportSetup, super()._make_request("PATCH", data=data, params=params).json())

    def put(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ManagementReportSetup:
        """
        Performs a PUT request against the /company/companies/{id}/managementReportSetup/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagementReportSetup: The parsed response data.
        """
        return self._parse_one(ManagementReportSetup, super()._make_request("PUT", data=data, params=params).json())
