
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class SoftwareUninstallInfo(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    uninstall_path: (str | None) = Field(default=None, alias='UninstallPath')

class SoftwareClassificationInfo(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    software_names: (list[str] | None) = Field(default=None, alias='SoftwareNames')

class NewProbeConfiguration(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_agent_push_enabled: (bool | None) = Field(default=None, alias='IsAgentPushEnabled')
    is_automated_deployment_enabled: (bool | None) = Field(default=None, alias='IsAutomatedDeploymentEnabled')
    is_data_collection_enabled: (bool | None) = Field(default=None, alias='IsDataCollectionEnabled')
    is_snmp_trap_server_enabled: (bool | None) = Field(default=None, alias='IsSnmpTrapServerEnabled')
    is_syslog_server_enabled: (bool | None) = Field(default=None, alias='IsSyslogServerEnabled')
    is_tftp_server_enabled: (bool | None) = Field(default=None, alias='IsTftpServerEnabled')
    credentials_list: (list[NetworkProbe.ProbeConfigurationCredentials] | None) = Field(default=None, alias='CredentialsList')
from ..Repositories.MySQL.Domain.Models import NetworkProbe
