from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsIdValuesIdEndpoint import \
    ConfigurationsTypesIdQuestionsIdValuesIdEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsIdValuesInfoEndpoint import \
    ConfigurationsTypesIdQuestionsIdValuesInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ConfigurationsTypesIdQuestionsIdValuesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "values", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(
            ConfigurationsTypesIdQuestionsIdValuesInfoEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ConfigurationsTypesIdQuestionsIdValuesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ConfigurationsTypesIdQuestionsIdValuesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ConfigurationsTypesIdQuestionsIdValuesIdEndpoint: The initialized ConfigurationsTypesIdQuestionsIdValuesIdEndpoint object.
        """
        child = ConfigurationsTypesIdQuestionsIdValuesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
