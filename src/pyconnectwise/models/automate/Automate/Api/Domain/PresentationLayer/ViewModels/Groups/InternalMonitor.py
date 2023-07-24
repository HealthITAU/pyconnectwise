
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class AlertTemplate(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    alert_template_id: (int | None) = Field(default=None, alias='AlertTemplateId')
    name: (str | None) = Field(default=None, alias='Name')

class TicketCategory(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    ticket_category_id: (int | None) = Field(default=None, alias='TicketCategoryId')
    name: (str | None) = Field(default=None, alias='Name')

class InternalMonitorSubscriptionViewModel(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    alert_templates: (list[AlertTemplate] | None) = Field(default=None, alias='AlertTemplates')
    ticket_categories: (list[TicketCategory] | None) = Field(default=None, alias='TicketCategories')
    is_group_subscribed: (bool | None) = Field(default=None, alias='IsGroupSubscribed')
    is_subscription_inherited: (bool | None) = Field(default=None, alias='IsSubscriptionInherited')
    is_override_applied: (bool | None) = Field(default=None, alias='IsOverrideApplied')
    monitor_alert_template_id: (int | None) = Field(default=None, alias='MonitorAlertTemplateId')
    monitor_ticket_category_id: (int | None) = Field(default=None, alias='MonitorTicketCategoryId')
    overridden_alert_template_id: (int | None) = Field(default=None, alias='OverriddenAlertTemplateId')
    overridden_ticket_category_id: (int | None) = Field(default=None, alias='OverriddenTicketCategoryId')
