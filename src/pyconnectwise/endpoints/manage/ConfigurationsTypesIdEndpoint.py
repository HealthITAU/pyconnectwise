from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsEndpoint import (
    ConfigurationsTypesIdQuestionsEndpoint,
)


class ConfigurationsTypesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )

        self.questions = self._register_child_endpoint(
            ConfigurationsTypesIdQuestionsEndpoint(client, parent_endpoint=self)
        )
