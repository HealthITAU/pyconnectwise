from typing import Any

from pyconnectwise.endpoints.automate.ScriptingRunningscriptsEndpoint import ScriptingRunningscriptsEndpoint
from pyconnectwise.endpoints.automate.ScriptingScriptschedulesEndpoint import ScriptingScriptschedulesEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ScriptingEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "Scripting", parent_endpoint=parent_endpoint)

        self.scriptschedules = self._register_child_endpoint(
            ScriptingScriptschedulesEndpoint(client, parent_endpoint=self)
        )
        self.runningscripts = self._register_child_endpoint(
            ScriptingRunningscriptsEndpoint(client, parent_endpoint=self)
        )
