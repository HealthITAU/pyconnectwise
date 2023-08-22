from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemBundlesCountEndpoint import SystemBundlesCountEndpoint
from pyconnectwise.models.manage import BundleResultsCollection
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SystemBundlesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "bundles", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemBundlesCountEndpoint(client, parent_endpoint=self))

    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> BundleResultsCollection:
        """
        Performs a POST request against the /system/bundles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BundleResultsCollection: The parsed response data.
        """
        return self._parse_one(BundleResultsCollection, super()._make_request("POST", data=data, params=params).json())
