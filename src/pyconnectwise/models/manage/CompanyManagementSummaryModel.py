from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.ManagementSolutionReferenceModel import ManagementSolutionReferenceModel
from enum import Enum
from pyconnectwise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
class DeviceType(str, Enum):
    WorkstationsAndServers = 'WorkstationsAndServers'
    BackupStats = 'BackupStats'
    Servers = 'Servers'
    Workstations = 'Workstations'

class CompanyManagementSummaryModel(ConnectWiseModel):
    id: int
    management_solution: ManagementSolutionReferenceModel
    group_identifier: str
    device_type: DeviceType
    agreement: AgreementReferenceModel
    snmp_machines: int
    total_workstations: int
    total_servers: int
    total_windows_servers: int
    total_windows_workstations: int
    total_managed_machines: int
    servers_offline: int
    servers_disk_space_low: int
    failed_backup_jobs: int
    total_notifications: int
    successful_backup_jobs: int
    server_availability: int
    viruses_removed: int
    spyware_items_removed: int
    windows_patches_installed: int
    disk_cleanups: int
    disk_defragmentations: int
    fully_patched_machines: int
    missing_one_two_patches_machines: int
    missing_three_five_patches_machines: int
    missing_more_five_patches_machines: int
    missing_unscanned_patches_machines: int
    alerts_generated: str
    internet_connectivity: float
    disk_space_cleaned_mb: int
    missing_security_patches: str
    cpu_utilization: float
    memory_utilization: float
    company: CompanyReferenceModel
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True