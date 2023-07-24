
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class PingSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    server_address: (str | None) = Field(default=None, alias='ServerAddress')

class LatencySettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    server_address: (str | None) = Field(default=None, alias='ServerAddress')

class TcpSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    server_address: (str | None) = Field(default=None, alias='ServerAddress')
    port: (int | None) = Field(default=None, alias='Port')
    data_to_send: (str | None) = Field(default=None, alias='DataToSend')

class UdpSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    server_address: (str | None) = Field(default=None, alias='ServerAddress')
    port: (int | None) = Field(default=None, alias='Port')
    data_to_send: (str | None) = Field(default=None, alias='DataToSend')

class SnmpSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    server_address: (str | None) = Field(default=None, alias='ServerAddress')
    community_string: (str | None) = Field(default=None, alias='CommunityString')
    oid: (str | None) = Field(default=None, alias='Oid')
    should_use_snmp_v2: (bool | None) = Field(default=None, alias='ShouldUseSnmpV2')

class PerformanceCounterSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    performance_object: (str | None) = Field(default=None, alias='PerformanceObject')
    performance_counter: (str | None) = Field(default=None, alias='PerformanceCounter')
    instance: (str | None) = Field(default=None, alias='Instance')

class FileOrDirectorySettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    path: (str | None) = Field(default=None, alias='Path')

class ServiceSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    service_name: (str | None) = Field(default=None, alias='ServiceName')

class DiskSpaceSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    drive_letter: (str | None) = Field(default=None, alias='DriveLetter')

class RegistrySettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    registry_hive_type_id: (int | None) = Field(default=None, alias='RegistryHiveTypeId')
    registry_key: (str | None) = Field(default=None, alias='RegistryKey')
    value_name: (str | None) = Field(default=None, alias='ValueName')

class ProcessSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    process_name: (str | None) = Field(default=None, alias='ProcessName')

class EventLogSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    log_file_name: (str | None) = Field(default=None, alias='LogFileName')
    event_type_id: (int | None) = Field(default=None, alias='EventTypeId')
    source: (str | None) = Field(default=None, alias='Source')
    event_id: (str | None) = Field(default=None, alias='EventId')
    message_regex: (str | None) = Field(default=None, alias='MessageRegex')

class ExecutableSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    executable_invocation: (str | None) = Field(default=None, alias='ExecutableInvocation')

class WmiSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    wmi_query: (str | None) = Field(default=None, alias='WmiQuery')

class BandwidthSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ip_address: (str | None) = Field(default=None, alias='IpAddress')
    snmp_version_id: (int | None) = Field(default=None, alias='SnmpVersionId')
    community_string: (str | None) = Field(default=None, alias='CommunityString')
    data_to_watch_id: (int | None) = Field(default=None, alias='DataToWatchId')
    index_to_watch: (str | None) = Field(default=None, alias='IndexToWatch')
    snmp_v3_user_name: (str | None) = Field(default=None, alias='SnmpV3UserName')
    snmp_v3_auth_password: (str | None) = Field(default=None, alias='SnmpV3AuthPassword')
    snmp_v3_auth_method_id: (int | None) = Field(default=None, alias='SnmpV3AuthMethodId')
    snmp_v3_encryption_password: (str | None) = Field(default=None, alias='SnmpV3EncryptionPassword')
    snmp_v3_encryption_method_id: (int | None) = Field(default=None, alias='SnmpV3EncryptionMethodId')

class SensorSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    sensor_number: (int | None) = Field(default=None, alias='SensorNumber')
    sensor_type_id: (int | None) = Field(default=None, alias='SensorTypeId')
