
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class AlertTemplate(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    template_id: (int | None) = Field(default=None, alias='TemplateId')
    template_name: (str | None) = Field(default=None, alias='TemplateName')
