from typing import TYPE_CHECKING

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsIdEndpoint import (
    ConfigurationsTypesIdQuestionsIdEndpoint,
)
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsInfoEndpoint import (
    ConfigurationsTypesIdQuestionsInfoEndpoint,
)

if TYPE_CHECKING:
    from pyconnectwise.clients.connectwise_client import ConnectWiseClient


class ConfigurationsTypesIdQuestionsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client: "ConnectWiseClient", parent_endpoint: ConnectWiseEndpoint = None) -> None:
        ConnectWiseEndpoint.__init__(self, client, "questions", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(
            ConfigurationsTypesIdQuestionsInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, _id: int) -> ConfigurationsTypesIdQuestionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ConfigurationsTypesIdQuestionsIdEndpoint object to move down the chain.

        Parameters:
            _id (int): The ID to set.
        Returns:
            ConfigurationsTypesIdQuestionsIdEndpoint: The initialized ConfigurationsTypesIdQuestionsIdEndpoint object.
        """
        child = ConfigurationsTypesIdQuestionsIdEndpoint(self.client, parent_endpoint=self)
        child._id = _id
        return child
