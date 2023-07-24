
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class ExtraFieldDisplayFormat(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    extra_field_display_format_id: (int | None) = Field(default=None, alias='ExtraFieldDisplayFormatId')
    name: (str | None) = Field(default=None, alias='Name')

class ExtraFieldLocation(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    extra_field_location_id: (int | None) = Field(default=None, alias='ExtraFieldLocationId')
    name: (str | None) = Field(default=None, alias='Name')

class ExtraFieldTitleFormat(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    extra_field_title_format_id: (int | None) = Field(default=None, alias='ExtraFieldTitleFormatId')
    name: (str | None) = Field(default=None, alias='Name')

class TextFieldSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_masked: (bool | None) = Field(default=None, alias='IsMasked')
    value: (str | None) = Field(default=None, alias='Value')
    default_value: (str | None) = Field(default=None, alias='DefaultValue')

class DropdownSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    available_options: (dict[(str, str)] | None) = Field(default=None, alias='AvailableOptions')
    selected_value: (str | None) = Field(default=None, alias='SelectedValue')
    default_value: (str | None) = Field(default=None, alias='DefaultValue')

class CheckboxSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    is_checked: (bool | None) = Field(default=None, alias='IsChecked')
    default_value: (bool | None) = Field(default=None, alias='DefaultValue')

class ExtraFieldSectionResetRequest(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    section: (str | None) = Field(default=None, alias='Section')

class ExtraField(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    target_id: (int | None) = Field(default=None, alias='TargetId')
    extra_field_definition_id: (int | None) = Field(default=None, alias='ExtraFieldDefinitionId')
    title: (str | None) = Field(default=None, alias='Title')
    display_format: (ExtraFieldDisplayFormat | None) = Field(default=None, alias='DisplayFormat')
    location: (ExtraFieldLocation | None) = Field(default=None, alias='Location')
    title_format: (ExtraFieldTitleFormat | None) = Field(default=None, alias='TitleFormat')
    section: (str | None) = Field(default=None, alias='Section')
    tooltip: (str | None) = Field(default=None, alias='Tooltip')
    is_read_only: (bool | None) = Field(default=None, alias='IsReadOnly')
    text_field_settings: (TextFieldSettings | None) = Field(default=None, alias='TextFieldSettings')
    dropdown_settings: (DropdownSettings | None) = Field(default=None, alias='DropdownSettings')
    checkbox_settings: (CheckboxSettings | None) = Field(default=None, alias='CheckboxSettings')

class ExtraFieldDefinition(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    sort_oder: (int | None) = Field(default=None, alias='SortOder')
    is_encrypted: (bool | None) = Field(default=None, alias='IsEncrypted')
    is_restricted: (bool | None) = Field(default=None, alias='IsRestricted')
    read_user_classes: (list[Users.UserClass] | None) = Field(default=None, alias='ReadUserClasses')
    edit_user_classes: (list[Users.UserClass] | None) = Field(default=None, alias='EditUserClasses')
    extra_field_definition_id: (int | None) = Field(default=None, alias='ExtraFieldDefinitionId')
    title: (str | None) = Field(default=None, alias='Title')
    display_format: (ExtraFieldDisplayFormat | None) = Field(default=None, alias='DisplayFormat')
    location: (ExtraFieldLocation | None) = Field(default=None, alias='Location')
    title_format: (ExtraFieldTitleFormat | None) = Field(default=None, alias='TitleFormat')
    section: (str | None) = Field(default=None, alias='Section')
    tooltip: (str | None) = Field(default=None, alias='Tooltip')
    is_read_only: (bool | None) = Field(default=None, alias='IsReadOnly')
    text_field_settings: (TextFieldSettings | None) = Field(default=None, alias='TextFieldSettings')
    dropdown_settings: (DropdownSettings | None) = Field(default=None, alias='DropdownSettings')
    checkbox_settings: (CheckboxSettings | None) = Field(default=None, alias='CheckboxSettings')
from . import Users
