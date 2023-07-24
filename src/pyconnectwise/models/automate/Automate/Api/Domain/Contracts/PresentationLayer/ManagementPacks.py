
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class ManagementPackQuickSettingsRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_core_services_enabled: (bool | None) = Field(default=None, alias='IsCoreServicesEnabled')
    is_database_enabled: (bool | None) = Field(default=None, alias='IsDatabaseEnabled')
    is_messaging_services_enabled: (bool | None) = Field(default=None, alias='IsMessagingServicesEnabled')
    is_network_ports_enabled: (bool | None) = Field(default=None, alias='IsNetworkPortsEnabled')
    is_websites_and_proxies_enabled: (bool | None) = Field(default=None, alias='IsWebsitesAndProxiesEnabled')
    alert_level: (str | None) = Field(default=None, alias='AlertLevel')

class ManagementPackStatus(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_installed: (bool | None) = Field(default=None, alias='IsInstalled')
    is_enabled: (bool | None) = Field(default=None, alias='IsEnabled')
    alert_level: (str | None) = Field(default=None, alias='AlertLevel')

class ManagementPackQuickSettingsResponse(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    core_services_status: (ManagementPackStatus | None) = Field(default=None, alias='CoreServicesStatus')
    database_status: (ManagementPackStatus | None) = Field(default=None, alias='DatabaseStatus')
    messaging_services_status: (ManagementPackStatus | None) = Field(default=None, alias='MessagingServicesStatus')
    network_port_status: (ManagementPackStatus | None) = Field(default=None, alias='NetworkPortStatus')
    websites_and_proxies_status: (ManagementPackStatus | None) = Field(default=None, alias='WebsitesAndProxiesStatus')
