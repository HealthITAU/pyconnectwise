
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class AuditAnalyticsBundle(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    audit_action_id: (int | None) = Field(default=None, alias='AuditActionId')
    external_id: (int | None) = Field(default=None, alias='ExternalId')
    secondary_identifier: (str | None) = Field(default=None, alias='SecondaryIdentifier')
    unsanitized_base_message: (str | None) = Field(default=None, alias='UnsanitizedBaseMessage')
    extra_log_values: (list[String_System.String] | None) = Field(default=None, alias='ExtraLogValues')
    sanitized_analytics_description: (str | None) = Field(default=None, alias='SanitizedAnalyticsDescription')
from .....System.Collections.Generic.KeyValuePair_System import String_System
