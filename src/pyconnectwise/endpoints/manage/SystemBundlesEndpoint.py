from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemBundlesCountEndpoint import SystemBundlesCountEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import BundleResultsCollection
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemBundlesEndpoint(ConnectWiseEndpoint, IPostable[BundleResultsCollection, ConnectWiseManageRequestParams]):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "bundles", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, BundleResultsCollection)

        self.count = self._register_child_endpoint(SystemBundlesCountEndpoint(client, parent_endpoint=self))

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> BundleResultsCollection:
        """
        Performs a POST request against the /system/bundles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BundleResultsCollection: The parsed response data.
        """
        return self._parse_one(BundleResultsCollection, super()._make_request("POST", data=data, params=params).json())
