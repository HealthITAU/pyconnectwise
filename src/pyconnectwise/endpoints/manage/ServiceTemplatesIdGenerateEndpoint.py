from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IPostable
from pyconnectwise.models.manage import TemplateGeneratedCountsModel
from pyconnectwise.types import JSON, ConnectWiseManageRequestParams

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ServiceTemplatesIdGenerateEndpoint(
    ConnectWiseEndpoint, IPostable[TemplateGeneratedCountsModel, ConnectWiseManageRequestParams]
):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "generate", parent_endpoint=parent_endpoint)
        IPostable.__init__(self, TemplateGeneratedCountsModel)

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> TemplateGeneratedCountsModel:
        """
        Performs a POST request against the /service/templates/{id}/generate endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            TemplateGeneratedCountsModel: The parsed response data.
        """
        return self._parse_one(
            TemplateGeneratedCountsModel, super()._make_request("POST", data=data, params=params).json()
        )
