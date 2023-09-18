from typing import Any

from pyconnectwise.endpoints.automate.ComputersIdAlertsEndpoint import ComputersIdAlertsEndpoint
from pyconnectwise.endpoints.automate.ComputersIdAlertsuspensionsEndpoint import ComputersIdAlertsuspensionsEndpoint
from pyconnectwise.endpoints.automate.ComputersIdBiosEndpoint import ComputersIdBiosEndpoint
from pyconnectwise.endpoints.automate.ComputersIdCommandexecuteEndpoint import ComputersIdCommandexecuteEndpoint
from pyconnectwise.endpoints.automate.ComputersIdCommandhistoryEndpoint import ComputersIdCommandhistoryEndpoint
from pyconnectwise.endpoints.automate.ComputersIdComputerpatchingpoliciesEndpoint import \
    ComputersIdComputerpatchingpoliciesEndpoint
from pyconnectwise.endpoints.automate.ComputersIdDevicesEndpoint import ComputersIdDevicesEndpoint
from pyconnectwise.endpoints.automate.ComputersIdDriversEndpoint import ComputersIdDriversEndpoint
from pyconnectwise.endpoints.automate.ComputersIdDrivesEndpoint import ComputersIdDrivesEndpoint
from pyconnectwise.endpoints.automate.ComputersIdEffectivepatchingpolicyEndpoint import \
    ComputersIdEffectivepatchingpolicyEndpoint
from pyconnectwise.endpoints.automate.ComputersIdMicrosoftupdatesEndpoint import ComputersIdMicrosoftupdatesEndpoint
from pyconnectwise.endpoints.automate.ComputersIdMonitoralertsuspensionsEndpoint import \
    ComputersIdMonitoralertsuspensionsEndpoint
from pyconnectwise.endpoints.automate.ComputersIdMonitorsEndpoint import ComputersIdMonitorsEndpoint
from pyconnectwise.endpoints.automate.ComputersIdOperatingsystemEndpoint import ComputersIdOperatingsystemEndpoint
from pyconnectwise.endpoints.automate.ComputersIdPatchingstatsEndpoint import ComputersIdPatchingstatsEndpoint
from pyconnectwise.endpoints.automate.ComputersIdPatchjobsEndpoint import ComputersIdPatchjobsEndpoint
from pyconnectwise.endpoints.automate.ComputersIdPrintersEndpoint import ComputersIdPrintersEndpoint
from pyconnectwise.endpoints.automate.ComputersIdProcessorsEndpoint import ComputersIdProcessorsEndpoint
from pyconnectwise.endpoints.automate.ComputersIdRunningscriptsEndpoint import ComputersIdRunningscriptsEndpoint
from pyconnectwise.endpoints.automate.ComputersIdScheduledscriptsEndpoint import ComputersIdScheduledscriptsEndpoint
from pyconnectwise.endpoints.automate.ComputersIdScheduledtasksEndpoint import ComputersIdScheduledtasksEndpoint
from pyconnectwise.endpoints.automate.ComputersIdScripthistoryEndpoint import ComputersIdScripthistoryEndpoint
from pyconnectwise.endpoints.automate.ComputersIdSensorsEndpoint import ComputersIdSensorsEndpoint
from pyconnectwise.endpoints.automate.ComputersIdServicesEndpoint import ComputersIdServicesEndpoint
from pyconnectwise.endpoints.automate.ComputersIdSoftwareEndpoint import ComputersIdSoftwareEndpoint
from pyconnectwise.endpoints.automate.ComputersIdSystemslotsEndpoint import ComputersIdSystemslotsEndpoint
from pyconnectwise.endpoints.automate.ComputersIdThirdpartypatchesEndpoint import ComputersIdThirdpartypatchesEndpoint
from pyconnectwise.endpoints.automate.ComputersIdUpsEndpoint import ComputersIdUpsEndpoint
from pyconnectwise.endpoints.automate.ComputersIdVideocardsEndpoint import ComputersIdVideocardsEndpoint
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.models.automate import LabTechComputer
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ComputersIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.ups = self._register_child_endpoint(ComputersIdUpsEndpoint(client, parent_endpoint=self))
        self.services = self._register_child_endpoint(ComputersIdServicesEndpoint(client, parent_endpoint=self))
        self.alerts = self._register_child_endpoint(ComputersIdAlertsEndpoint(client, parent_endpoint=self))
        self.software = self._register_child_endpoint(ComputersIdSoftwareEndpoint(client, parent_endpoint=self))
        self.printers = self._register_child_endpoint(ComputersIdPrintersEndpoint(client, parent_endpoint=self))
        self.microsoftupdates = self._register_child_endpoint(
            ComputersIdMicrosoftupdatesEndpoint(client, parent_endpoint=self)
        )
        self.scheduledscripts = self._register_child_endpoint(
            ComputersIdScheduledscriptsEndpoint(client, parent_endpoint=self)
        )
        self.commandhistory = self._register_child_endpoint(
            ComputersIdCommandhistoryEndpoint(client, parent_endpoint=self)
        )
        self.thirdpartypatches = self._register_child_endpoint(
            ComputersIdThirdpartypatchesEndpoint(client, parent_endpoint=self)
        )
        self.drives = self._register_child_endpoint(ComputersIdDrivesEndpoint(client, parent_endpoint=self))
        self.videocards = self._register_child_endpoint(ComputersIdVideocardsEndpoint(client, parent_endpoint=self))
        self.commandexecute = self._register_child_endpoint(
            ComputersIdCommandexecuteEndpoint(client, parent_endpoint=self)
        )
        self.effectivepatchingpolicy = self._register_child_endpoint(
            ComputersIdEffectivepatchingpolicyEndpoint(client, parent_endpoint=self)
        )
        self.alertsuspensions = self._register_child_endpoint(
            ComputersIdAlertsuspensionsEndpoint(client, parent_endpoint=self)
        )
        self.sensors = self._register_child_endpoint(ComputersIdSensorsEndpoint(client, parent_endpoint=self))
        self.bios = self._register_child_endpoint(ComputersIdBiosEndpoint(client, parent_endpoint=self))
        self.monitoralertsuspensions = self._register_child_endpoint(
            ComputersIdMonitoralertsuspensionsEndpoint(client, parent_endpoint=self)
        )
        self.processors = self._register_child_endpoint(ComputersIdProcessorsEndpoint(client, parent_endpoint=self))
        self.systemslots = self._register_child_endpoint(ComputersIdSystemslotsEndpoint(client, parent_endpoint=self))
        self.runningscripts = self._register_child_endpoint(
            ComputersIdRunningscriptsEndpoint(client, parent_endpoint=self)
        )
        self.operatingsystem = self._register_child_endpoint(
            ComputersIdOperatingsystemEndpoint(client, parent_endpoint=self)
        )
        self.devices = self._register_child_endpoint(ComputersIdDevicesEndpoint(client, parent_endpoint=self))
        self.monitors = self._register_child_endpoint(ComputersIdMonitorsEndpoint(client, parent_endpoint=self))
        self.patchjobs = self._register_child_endpoint(ComputersIdPatchjobsEndpoint(client, parent_endpoint=self))
        self.computerpatchingpolicies = self._register_child_endpoint(
            ComputersIdComputerpatchingpoliciesEndpoint(client, parent_endpoint=self)
        )
        self.scripthistory = self._register_child_endpoint(
            ComputersIdScripthistoryEndpoint(client, parent_endpoint=self)
        )
        self.drivers = self._register_child_endpoint(ComputersIdDriversEndpoint(client, parent_endpoint=self))
        self.scheduledtasks = self._register_child_endpoint(
            ComputersIdScheduledtasksEndpoint(client, parent_endpoint=self)
        )
        self.patchingstats = self._register_child_endpoint(
            ComputersIdPatchingstatsEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[LabTechComputer]:
        """
        Performs a GET request against the /Computers/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechComputer]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params), LabTechComputer, self, page, page_size, params
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> LabTechComputer:
        """
        Performs a GET request against the /Computers/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechComputer: The parsed response data.
        """
        return self._parse_one(LabTechComputer, super()._make_request("GET", data=data, params=params).json())
