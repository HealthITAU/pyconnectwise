from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsEndpoint import ConfigurationsTypesIdQuestionsEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ConfigurationsTypesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.questions = self._register_child_endpoint(
            ConfigurationsTypesIdQuestionsEndpoint(client, parent_endpoint=self)
        )
