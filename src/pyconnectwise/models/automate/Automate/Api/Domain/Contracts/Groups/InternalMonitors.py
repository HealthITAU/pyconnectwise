
from __future__ import annotations
from datetime import datetime
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class MonitorAlertPolicy(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    effective_policy_type_id: (int | None) = Field(default=None, alias='EffectivePolicyTypeId')
    effective_policy_type_name: (str | None) = Field(default=None, alias='EffectivePolicyTypeName')
    is_alert_template_overridden: (bool | None) = Field(default=None, alias='IsAlertTemplateOverridden')
    alert_template_id: (int | None) = Field(default=None, alias='AlertTemplateId')
    alert_template_name: (str | None) = Field(default=None, alias='AlertTemplateName')
    alert_template_description: (str | None) = Field(default=None, alias='AlertTemplateDescription')
    is_ticket_category_overridden: (bool | None) = Field(default=None, alias='IsTicketCategoryOverridden')
    ticket_category_id: (int | None) = Field(default=None, alias='TicketCategoryId')
    ticket_category_name: (str | None) = Field(default=None, alias='TicketCategoryName')
    inheritance_source_name: (str | None) = Field(default=None, alias='InheritanceSourceName')

class AlertingOverride(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    alert_template: (InternalMonitor.AlertTemplate | None) = Field(default=None, alias='AlertTemplate')
    ticket_category: (InternalMonitor.TicketCategory | None) = Field(default=None, alias='TicketCategory')

class GroupInternalMonitorInfo(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    monitor_id: (int | None) = Field(default=None, alias='MonitorId')
    monitor_name: (str | None) = Field(default=None, alias='MonitorName')
    is_monitor_globally_applied: (bool | None) = Field(default=None, alias='IsMonitorGloballyApplied')
    is_subscription_inherited: (bool | None) = Field(default=None, alias='IsSubscriptionInherited')
    is_group_subscribed: (bool | None) = Field(default=None, alias='IsGroupSubscribed')
    monitor_interval: (str | None) = Field(default=None, alias='MonitorInterval')
    monitor_next_scan_date: (datetime | None) = Field(default=None, alias='MonitorNextScanDate')
    effective_alert_policy: (MonitorAlertPolicy | None) = Field(default=None, alias='EffectiveAlertPolicy')

class UpdateGroupMonitorSubscriptionRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_subscribed: (bool | None) = Field(default=None, alias='IsSubscribed')
    overrides: (AlertingOverride | None) = Field(default=None, alias='Overrides')
from ...PresentationLayer.ViewModels.Groups import InternalMonitor
