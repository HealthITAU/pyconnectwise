from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsIdInfoEndpoint import \
    ConfigurationsTypesIdQuestionsIdInfoEndpoint
from pyconnectwise.endpoints.manage.ConfigurationsTypesIdQuestionsIdValuesEndpoint import \
    ConfigurationsTypesIdQuestionsIdValuesEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ConfigurationsTypesIdQuestionsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "{id}", parent_endpoint=parent_endpoint)

        self.values = self._register_child_endpoint(
            ConfigurationsTypesIdQuestionsIdValuesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ConfigurationsTypesIdQuestionsIdInfoEndpoint(client, parent_endpoint=self)
        )
