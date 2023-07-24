
from __future__ import annotations
from datetime import datetime
from enum import Enum
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class ComputerDriver(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    computer_id: (int | None) = Field(default=None, alias='ComputerId')
    name: (str | None) = Field(default=None, alias='Name')
    description: (str | None) = Field(default=None, alias='Description')
    state: (str | None) = Field(default=None, alias='State')
    startup: (str | None) = Field(default=None, alias='Startup')
    path_name: (str | None) = Field(default=None, alias='PathName')
    service_type: (str | None) = Field(default=None, alias='ServiceType')
    username: (str | None) = Field(default=None, alias='Username')
    date_last_inventoried: (datetime | None) = Field(default=None, alias='DateLastInventoried')
    run_levels: (str | None) = Field(default=None, alias='RunLevels')

class DriveStats(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    drive_id: (int | None) = Field(default=None, alias='DriveId')
    free_space_percentage: (int | None) = Field(default=None, alias='FreeSpacePercentage')
    fragmented_space_percentage: (int | None) = Field(default=None, alias='FragmentedSpacePercentage')
    event_date: (datetime | None) = Field(default=None, alias='EventDate')
    sample_count: (int | None) = Field(default=None, alias='SampleCount')
    week: (int | None) = Field(default=None, alias='Week')
    month: (int | None) = Field(default=None, alias='Month')
    year: (int | None) = Field(default=None, alias='Year')

class DeviceClassification(Enum):
    UNKNOWN = 'Unknown'
    COMPUTER = 'Computer'
    NETWORK_DEVICE = 'NetworkDevice'
    INTERNET_CONNECTION = 'InternetConnection'
    BLACK_BOX = 'BlackBox'

class NetworkMapNode(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    device_id: (int | None) = Field(default=None, alias='DeviceId')
    device_name: (str | None) = Field(default=None, alias='DeviceName')
    device_friendly_name: (str | None) = Field(default=None, alias='DeviceFriendlyName')
    description: (str | None) = Field(default=None, alias='Description')
    device_type: (str | None) = Field(default=None, alias='DeviceType')
    child_node_list: (list[NetworkMapNode] | None) = Field(default=None, alias='ChildNodeList')
    device_mac_address: (str | None) = Field(default=None, alias='DeviceMacAddress')
    ip_address: (str | None) = Field(default=None, alias='IpAddress')
    status: (str | None) = Field(default=None, alias='Status')
    device_classification: (DeviceClassification | None) = Field(default=None, alias='DeviceClassification')

class NetworkMapNodeDetails(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    device_id: (int | None) = Field(default=None, alias='DeviceId')
    device_type: (str | None) = Field(default=None, alias='DeviceType')
    uptime: (int | None) = Field(default=None, alias='Uptime')
    ignore_device_scan: (bool | None) = Field(default=None, alias='IgnoreDeviceScan')
    asset_date: (datetime | None) = Field(default=None, alias='AssetDate')
    date_last_inventoried: (datetime | None) = Field(default=None, alias='DateLastInventoried')
    last_contact_date: (datetime | None) = Field(default=None, alias='LastContactDate')
    ip_address: (str | None) = Field(default=None, alias='IpAddress')
    device_mac_address: (str | None) = Field(default=None, alias='DeviceMacAddress')
    operating_system: (str | None) = Field(default=None, alias='OperatingSystem')
    model: (str | None) = Field(default=None, alias='Model')
    location_probe: (str | None) = Field(default=None, alias='LocationProbe')
    manufacturer: (str | None) = Field(default=None, alias='Manufacturer')
    uplink_port: (str | None) = Field(default=None, alias='UplinkPort')
    uplink_name: (str | None) = Field(default=None, alias='UplinkName')
    uplink_ip_address: (str | None) = Field(default=None, alias='UplinkIpAddress')

class ProbeEventLevel(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')

class MonitorDataCollectionSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    monitor_id: (int | None) = Field(default=None, alias='MonitorId')
    computer_id: (int | None) = Field(default=None, alias='ComputerId')
    unit_label: (str | None) = Field(default=None, alias='UnitLabel')
    graph_title: (str | None) = Field(default=None, alias='GraphTitle')
    graph_vertical_limit: (int | None) = Field(default=None, alias='GraphVerticalLimit')

class MonitorStatistic(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    monitor_id: (int | None) = Field(default=None, alias='MonitorId')
    last_fail_time: (datetime | None) = Field(default=None, alias='LastFailTime')
    last_fail_message: (str | None) = Field(default=None, alias='LastFailMessage')
    last_success_time: (datetime | None) = Field(default=None, alias='LastSuccessTime')
    last_success_message: (str | None) = Field(default=None, alias='LastSuccessMessage')
    last_warning_time: (datetime | None) = Field(default=None, alias='LastWarningTime')
    last_warning_message: (str | None) = Field(default=None, alias='LastWarningMessage')
    monitor_start_time: (datetime | None) = Field(default=None, alias='MonitorStartTime')
    computer_id: (int | None) = Field(default=None, alias='ComputerId')

class ProbeEvent(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    probe_id: (int | None) = Field(default=None, alias='ProbeId')
    event_level: (ProbeEventLevel | None) = Field(default=None, alias='EventLevel')
    message: (str | None) = Field(default=None, alias='Message')
    event_time: (datetime | None) = Field(default=None, alias='EventTime')

class DriveStatistics(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    drive_id: (int | None) = Field(default=None, alias='DriveId')
    percentage_used_difference: (float | None) = Field(default=None, alias='PercentageUsedDifference')
