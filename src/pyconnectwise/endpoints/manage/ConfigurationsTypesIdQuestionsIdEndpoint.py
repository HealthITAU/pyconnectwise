from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsIdInfoEndpoint import (
    ConfigurationsTypesIdQuestionsIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsIdValuesEndpoint import (
    ConfigurationsTypesIdQuestionsIdValuesEndpoint,
)

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ConfigurationsTypesIdQuestionsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(
            ConfigurationsTypesIdQuestionsIdInfoEndpoint(client, parent_endpoint=self)
        )
        self.values = self._register_child_endpoint(
            ConfigurationsTypesIdQuestionsIdValuesEndpoint(client, parent_endpoint=self)
        )
