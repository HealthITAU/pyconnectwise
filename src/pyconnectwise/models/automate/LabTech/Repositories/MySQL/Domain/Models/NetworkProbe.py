
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class EncryptionMethod(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class HashMethod(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class ScanFrequencyCategory(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    category_id: (int | None) = Field(default=None, alias='CategoryId')
    description: (str | None) = Field(default=None, alias='Description')

class StatusScanNetworkPortOption(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    status_scan_network_port_option_id: (int | None) = Field(default=None, alias='StatusScanNetworkPortOptionId')
    description: (str | None) = Field(default=None, alias='Description')

class ProbeConfigurationCredentials(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    probe_configuration_credentials_id: (int | None) = Field(default=None, alias='ProbeConfigurationCredentialsId')
    probe_configuration_id: (int | None) = Field(default=None, alias='ProbeConfigurationId')
    credential_id: (int | None) = Field(default=None, alias='CredentialId')
    attempt_sequence: (int | None) = Field(default=None, alias='AttemptSequence')
    credentials_alias: (str | None) = Field(default=None, alias='CredentialsAlias')
    credential_details: (Models.ExternalSystemCredentials | None) = Field(default=None, alias='CredentialDetails')

class SnmpSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    community_strings_get: (str | None) = Field(default=None, alias='CommunityStringsGet')
    timeout_in_seconds: (int | None) = Field(default=None, alias='TimeoutInSeconds')

class SyslogServerSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    syslog_server_listening_port: (int | None) = Field(default=None, alias='SyslogServerListeningPort')
    syslog_server_ip_filter: (str | None) = Field(default=None, alias='SyslogServerIpFilter')

class TftpServerSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    tftp_server_ip_filter: (str | None) = Field(default=None, alias='TftpServerIpFilter')
    tftp_server_listening_port: (int | None) = Field(default=None, alias='TftpServerListeningPort')
    allow_tftp_uploads: (bool | None) = Field(default=None, alias='AllowTftpUploads')

class ProbeSubnet(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    probe_subnet_id: (int | None) = Field(default=None, alias='ProbeSubnetId')
    probe_configuration_id: (int | None) = Field(default=None, alias='ProbeConfigurationId')
    network: (str | None) = Field(default=None, alias='Network')
    subnet_mask: (str | None) = Field(default=None, alias='SubnetMask')
    label: (str | None) = Field(default=None, alias='Label')

class ProbeExcludedIpAddressRange(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    excluded_ip_range_id: (int | None) = Field(default=None, alias='ExcludedIpRangeId')
    probe_subnet_id: (int | None) = Field(default=None, alias='ProbeSubnetId')
    excluded_ip_range: (str | None) = Field(default=None, alias='ExcludedIpRange')

class ProbeSnmpAuthentication(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    snmp_authentication_id: (int | None) = Field(default=None, alias='SnmpAuthenticationId')
    probe_snmp_configuration_id: (int | None) = Field(default=None, alias='ProbeSnmpConfigurationId')
    authentication_secret: (str | None) = Field(default=None, alias='AuthenticationSecret')
    hash_method: (HashMethod | None) = Field(default=None, alias='HashMethod')

class ProbeSnmpEncryption(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    snmp_encryption_id: (int | None) = Field(default=None, alias='SnmpEncryptionId')
    probe_snmp_configuration_id: (int | None) = Field(default=None, alias='ProbeSnmpConfigurationId')
    encryption_password: (str | None) = Field(default=None, alias='EncryptionPassword')
    encryption_method: (EncryptionMethod | None) = Field(default=None, alias='EncryptionMethod')

class NetMapPluginStatus(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    computer_id: (int | None) = Field(default=None, alias='ComputerId')
    is_net_map_plugin_enabled: (bool | None) = Field(default=None, alias='IsNetMapPluginEnabled')

class ProbeDiscoveryScanStatus(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    probe_discovery_scan_status_id: (int | None) = Field(default=None, alias='ProbeDiscoveryScanStatusId')
    location_id: (int | None) = Field(default=None, alias='LocationId')
    probe_id: (int | None) = Field(default=None, alias='ProbeId')
    is_discovery_scan_running: (bool | None) = Field(default=None, alias='IsDiscoveryScanRunning')
    discovery_scan_start: (datetime | None) = Field(default=None, alias='DiscoveryScanStart')
    last_discovery_scan: (datetime | None) = Field(default=None, alias='LastDiscoveryScan')

class ProbeSummary(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    current_probe_id: (int | None) = Field(default=None, alias='CurrentProbeId')
    total_devices: (int | None) = Field(default=None, alias='TotalDevices')
    offline_devices: (int | None) = Field(default=None, alias='OfflineDevices')
    missing_agents: (int | None) = Field(default=None, alias='MissingAgents')
    last_discovery_scan: (datetime | None) = Field(default=None, alias='LastDiscoveryScan')
    agent_deployment_enabled: (bool | None) = Field(default=None, alias='AgentDeploymentEnabled')
    has_max_tile_permissions: (bool | None) = Field(default=None, alias='HasMaxTilePermissions')
    is_generation_two: (bool | None) = Field(default=None, alias='IsGenerationTwo')

class ScanFrequency(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    scan_frequency_id: (int | None) = Field(default=None, alias='ScanFrequencyId')
    frequency_in_minutes: (int | None) = Field(default=None, alias='FrequencyInMinutes')
    display_name: (str | None) = Field(default=None, alias='DisplayName')
    frequency_category: (ScanFrequencyCategory | None) = Field(default=None, alias='FrequencyCategory')

class DiscoveryScanSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    discovery_scan_frequency: (ScanFrequency | None) = Field(default=None, alias='DiscoveryScanFrequency')
    limit_discovery_to_scan_window: (bool | None) = Field(default=None, alias='LimitDiscoveryToScanWindow')
    discovery_window_start: (str | None) = Field(default=None, alias='DiscoveryWindowStart')
    discovery_window_end: (str | None) = Field(default=None, alias='DiscoveryWindowEnd')
    is_mac_addres_scanning_enabled: (bool | None) = Field(default=None, alias='IsMacAddresScanningEnabled')
    concurrent_thread_count: (int | None) = Field(default=None, alias='ConcurrentThreadCount')

class StatusScanSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    status_scan_frequency: (ScanFrequency | None) = Field(default=None, alias='StatusScanFrequency')
    status_scan_network_port_list: (str | None) = Field(default=None, alias='StatusScanNetworkPortList')
    network_port_option: (StatusScanNetworkPortOption | None) = Field(default=None, alias='NetworkPortOption')

class ProbeConfigurationDefaults(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    probe_default_setting_id: (int | None) = Field(default=None, alias='ProbeDefaultSettingId')
    community_string_get_list: (str | None) = Field(default=None, alias='CommunityStringGetList')
    snmp_timeout_in_seconds: (int | None) = Field(default=None, alias='SnmpTimeoutInSeconds')
    agent_deployment_attempt_maximum: (int | None) = Field(default=None, alias='AgentDeploymentAttemptMaximum')
    discovery_settings: (DiscoveryScanSettings | None) = Field(default=None, alias='DiscoverySettings')
    status_settings: (StatusScanSettings | None) = Field(default=None, alias='StatusSettings')
    snmp_settings: (SnmpSettings | None) = Field(default=None, alias='SnmpSettings')
    is_data_collection_enabled: (bool | None) = Field(default=None, alias='IsDataCollectionEnabled')
    snmp_trap_server_listening_port: (int | None) = Field(default=None, alias='SnmpTrapServerListeningPort')
    syslog_settings: (SyslogServerSettings | None) = Field(default=None, alias='SyslogSettings')
    tftp_settings: (TftpServerSettings | None) = Field(default=None, alias='TftpSettings')

class ProbeSnmpV3Configuration(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    probe_snmp_configuration_id: (int | None) = Field(default=None, alias='ProbeSnmpConfigurationId')
    snmp_v3_username: (str | None) = Field(default=None, alias='SnmpV3Username')
    authentication: (ProbeSnmpAuthentication | None) = Field(default=None, alias='Authentication')
    encryption: (ProbeSnmpEncryption | None) = Field(default=None, alias='Encryption')

class ProbeConfiguration(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    probe_configuration_id: (int | None) = Field(default=None, alias='ProbeConfigurationId')
    location_id: (int | None) = Field(default=None, alias='LocationId')
    agent_deployment_attempt_maximum: (int | None) = Field(default=None, alias='AgentDeploymentAttemptMaximum')
    automated_deployment_enabled: (bool | None) = Field(default=None, alias='AutomatedDeploymentEnabled')
    discovery_settings: (DiscoveryScanSettings | None) = Field(default=None, alias='DiscoverySettings')
    status_settings: (StatusScanSettings | None) = Field(default=None, alias='StatusSettings')
    snmp_settings: (SnmpSettings | None) = Field(default=None, alias='SnmpSettings')
    is_data_collection_enabled: (bool | None) = Field(default=None, alias='IsDataCollectionEnabled')
    snmp_trap_server_listening_port: (int | None) = Field(default=None, alias='SnmpTrapServerListeningPort')
    syslog_settings: (SyslogServerSettings | None) = Field(default=None, alias='SyslogSettings')
    tftp_settings: (TftpServerSettings | None) = Field(default=None, alias='TftpSettings')

class ProbeSnmpConfiguration(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    probe_snmp_configuration_id: (int | None) = Field(default=None, alias='ProbeSnmpConfigurationId')
    probe_configuration_id: (int | None) = Field(default=None, alias='ProbeConfigurationId')
    snmp_timeout_in_seconds: (int | None) = Field(default=None, alias='SnmpTimeoutInSeconds')
    community_string_get_list: (str | None) = Field(default=None, alias='CommunityStringGetList')
    snmp_v3_settings: (ProbeSnmpV3Configuration | None) = Field(default=None, alias='SnmpV3Settings')
from ..... import Models
