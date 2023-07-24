
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class MonitorRoutineParametersFormat(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class UnformattedMonitorRoutineParameters(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    where: (str | None) = Field(default=None, alias='Where')
    what: (str | None) = Field(default=None, alias='What')
    data_out: (str | None) = Field(default=None, alias='DataOut')
    id_field: (str | None) = Field(default=None, alias='IdField')

class InternalDatabaseQueryParameters(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    field_to_check: (str | None) = Field(default=None, alias='FieldToCheck')
    table_or_view_to_query: (str | None) = Field(default=None, alias='TableOrViewToQuery')
    additional_conditions: (str | None) = Field(default=None, alias='AdditionalConditions')
    identity_field: (str | None) = Field(default=None, alias='IdentityField')

class GetNetworkResponseParameters(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    target: (str | None) = Field(default=None, alias='Target')
    port: (str | None) = Field(default=None, alias='Port')
    payload: (str | None) = Field(default=None, alias='Payload')

class PerformanceCounterQueryParameters(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    performance_object: (str | None) = Field(default=None, alias='PerformanceObject')
    performance_counter: (str | None) = Field(default=None, alias='PerformanceCounter')
    instance: (str | None) = Field(default=None, alias='Instance')

class NetworkDeviceWbemQueryParameters(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    namespace: (str | None) = Field(default=None, alias='Namespace')
    query: (str | None) = Field(default=None, alias='Query')

class GetPluginCommandResultParameters(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    command_number: (int | None) = Field(default=None, alias='CommandNumber')
    data: (str | None) = Field(default=None, alias='Data')

class FileOrDirectoryQueryParameters(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    directory: (str | None) = Field(default=None, alias='Directory')
    file: (str | None) = Field(default=None, alias='File')

class GetExecutableResultParameters(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    fully_qualified_executable_string: (str | None) = Field(default=None, alias='FullyQualifiedExecutableString')
    result_transform_regular_expression: (str | None) = Field(default=None, alias='ResultTransformRegularExpression')

class SnmpOidQuerySnmpVersion(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class SnmpOidQueryEncryptionMethod(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class SnmpOidQueryAuthenticationMethod(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class HardwareSensorQuerySensor(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class RegistryValueQueryRegistryHive(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class EventLogQueryEventLevelFilter(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    match_verbose: (bool | None) = Field(default=None, alias='MatchVerbose')
    match_informational: (bool | None) = Field(default=None, alias='MatchInformational')
    match_warning: (bool | None) = Field(default=None, alias='MatchWarning')
    match_error: (bool | None) = Field(default=None, alias='MatchError')
    match_critical: (bool | None) = Field(default=None, alias='MatchCritical')

class SnmpOidQueryParameters(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ip_address: (str | None) = Field(default=None, alias='IpAddress')
    snmp_version: (SnmpOidQuerySnmpVersion | None) = Field(default=None, alias='SnmpVersion')
    community: (str | None) = Field(default=None, alias='Community')
    username: (str | None) = Field(default=None, alias='Username')
    encryption_method: (SnmpOidQueryEncryptionMethod | None) = Field(default=None, alias='EncryptionMethod')
    encryption_password: (str | None) = Field(default=None, alias='EncryptionPassword')
    authentication_method: (SnmpOidQueryAuthenticationMethod | None) = Field(default=None, alias='AuthenticationMethod')
    authentication_password: (str | None) = Field(default=None, alias='AuthenticationPassword')
    object_identifier: (str | None) = Field(default=None, alias='ObjectIdentifier')

class HardwareSensorQueryParameters(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    sensor: (HardwareSensorQuerySensor | None) = Field(default=None, alias='Sensor')
    sensor_number: (str | None) = Field(default=None, alias='SensorNumber')

class RegistryValueQueryParameters(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    hive: (RegistryValueQueryRegistryHive | None) = Field(default=None, alias='Hive')
    key: (str | None) = Field(default=None, alias='Key')
    value: (str | None) = Field(default=None, alias='Value')

class EventLogQueryParameters(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    log: (str | None) = Field(default=None, alias='Log')
    level_filter: (EventLogQueryEventLevelFilter | None) = Field(default=None, alias='LevelFilter')
    keywords: (int | None) = Field(default=None, alias='Keywords')
    source: (str | None) = Field(default=None, alias='Source')
    event_id: (int | None) = Field(default=None, alias='EventId')
    regular_expression_filter: (str | None) = Field(default=None, alias='RegularExpressionFilter')

class MonitorRoutineParameters(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    format: (MonitorRoutineParametersFormat | None) = Field(default=None, alias='Format')
    unformatted_monitor_parameters: (UnformattedMonitorRoutineParameters | None) = Field(default=None, alias='UnformattedMonitorParameters')
    internal_database_query_parameters: (InternalDatabaseQueryParameters | None) = Field(default=None, alias='InternalDatabaseQueryParameters')
    latency_target: (str | None) = Field(default=None, alias='LatencyTarget')
    get_network_response_parameters: (GetNetworkResponseParameters | None) = Field(default=None, alias='GetNetworkResponseParameters')
    snmp_oid_query_parameters: (SnmpOidQueryParameters | None) = Field(default=None, alias='SnmpOidQueryParameters')
    performance_counter_query_parameters: (PerformanceCounterQueryParameters | None) = Field(default=None, alias='PerformanceCounterQueryParameters')
    hardware_sensor_query_parameters: (HardwareSensorQueryParameters | None) = Field(default=None, alias='HardwareSensorQueryParameters')
    network_device_wbem_query_parameters: (NetworkDeviceWbemQueryParameters | None) = Field(default=None, alias='NetworkDeviceWbemQueryParameters')
    get_plugin_command_result_parameters: (GetPluginCommandResultParameters | None) = Field(default=None, alias='GetPluginCommandResultParameters')
    file_or_directory_query_parameters: (FileOrDirectoryQueryParameters | None) = Field(default=None, alias='FileOrDirectoryQueryParameters')
    service_name: (str | None) = Field(default=None, alias='ServiceName')
    volume_mountpoint: (str | None) = Field(default=None, alias='VolumeMountpoint')
    registry_value_query_parameters: (RegistryValueQueryParameters | None) = Field(default=None, alias='RegistryValueQueryParameters')
    process_name: (str | None) = Field(default=None, alias='ProcessName')
    event_log_listener_parameters: (EventLogQueryParameters | None) = Field(default=None, alias='EventLogListenerParameters')
    get_executable_result_parameters: (GetExecutableResultParameters | None) = Field(default=None, alias='GetExecutableResultParameters')
    wmi_query: (str | None) = Field(default=None, alias='WmiQuery')
