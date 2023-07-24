
from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pydantic import ConfigDict, Field

class SessionViewerUser(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    id: (int | None) = Field(default=None, alias='Id')
    name: (str | None) = Field(default=None, alias='Name')
    permissions: (str | None) = Field(default=None, alias='Permissions')

class WebExtensionPermission(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    web_extension_permission_id: (int | None) = Field(default=None, alias='WebExtensionPermissionId')
    web_extension_id: (int | None) = Field(default=None, alias='WebExtensionId')
    permission_key: (str | None) = Field(default=None, alias='PermissionKey')
    permission_name: (str | None) = Field(default=None, alias='PermissionName')
    description: (str | None) = Field(default=None, alias='Description')

class UserExtensionClaimType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    has_claim: (bool | None) = Field(default=None, alias='HasClaim')
    extension_claim_type_id: (int | None) = Field(default=None, alias='ExtensionClaimTypeId')
    web_extension_id: (int | None) = Field(default=None, alias='WebExtensionId')
    display_name: (str | None) = Field(default=None, alias='DisplayName')
    claim_key: (str | None) = Field(default=None, alias='ClaimKey')
    description: (str | None) = Field(default=None, alias='Description')

class WebExtensionArea(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    web_extension_area_id: (int | None) = Field(default=None, alias='WebExtensionAreaId')
    web_extension_area_name: (str | None) = Field(default=None, alias='WebExtensionAreaName')
    web_extension_screen_id: (int | None) = Field(default=None, alias='WebExtensionScreenId')

class ExtensionClaimType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    extension_claim_type_id: (int | None) = Field(default=None, alias='ExtensionClaimTypeId')
    web_extension_id: (int | None) = Field(default=None, alias='WebExtensionId')
    display_name: (str | None) = Field(default=None, alias='DisplayName')
    claim_key: (str | None) = Field(default=None, alias='ClaimKey')
    description: (str | None) = Field(default=None, alias='Description')

class WebExtensionTileSize(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    tile_size_id: (int | None) = Field(default=None, alias='TileSizeId')
    description: (str | None) = Field(default=None, alias='Description')

class WebExtensionUrlOpenType(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    url_open_type_id: (int | None) = Field(default=None, alias='UrlOpenTypeId')
    description: (str | None) = Field(default=None, alias='Description')

class ExtensionSolution(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    extension_solution_id: (int | None) = Field(default=None, alias='ExtensionSolutionId')
    solution_guid: (UUID | None) = Field(default=None, alias='SolutionGuid', example='00000000-0000-0000-0000-000000000000')
    solution_name: (str | None) = Field(default=None, alias='SolutionName')
    is_installed: (bool | None) = Field(default=None, alias='IsInstalled')
    installed_version: (str | None) = Field(default=None, alias='InstalledVersion')
    latest_version: (str | None) = Field(default=None, alias='LatestVersion')

class ExtensionStatus(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    extension_status_id: (int | None) = Field(default=None, alias='ExtensionStatusId')
    description: (str | None) = Field(default=None, alias='Description')

class SessionViewerSettings(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    domain: (str | None) = Field(default=None, alias='Domain')
    port: (int | None) = Field(default=None, alias='Port')
    api_token: (str | None) = Field(default=None, alias='ApiToken')
    instance_id: (str | None) = Field(default=None, alias='InstanceId')
    extension_id: (str | None) = Field(default=None, alias='ExtensionId')
    enable_wcc_element: (bool | None) = Field(default=None, alias='EnableWccElement')
    user: (SessionViewerUser | None) = Field(default=None, alias='User')

class WebExtensionTile(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    tile_guid: (UUID | None) = Field(default=None, alias='TileGuid', example='00000000-0000-0000-0000-000000000000')
    normal_tile_source_url: (str | None) = Field(default=None, alias='NormalTileSourceUrl')
    normal_tile_header_url: (str | None) = Field(default=None, alias='NormalTileHeaderUrl')
    max_tile_source_url: (str | None) = Field(default=None, alias='MaxTileSourceUrl')
    tile_title: (str | None) = Field(default=None, alias='TileTitle')
    tile_size: (WebExtensionTileSize | None) = Field(default=None, alias='TileSize')
    web_extension_control_id: (int | None) = Field(default=None, alias='WebExtensionControlId')
    web_extension_control_name: (str | None) = Field(default=None, alias='WebExtensionControlName')
    web_extension_guid: (UUID | None) = Field(default=None, alias='WebExtensionGuid', example='00000000-0000-0000-0000-000000000000')
    extension_claim_type: (ExtensionClaimType | None) = Field(default=None, alias='ExtensionClaimType')
    is_core_extension: (bool | None) = Field(default=None, alias='IsCoreExtension')
    web_extension_area_control_type_ids: (list[int] | None) = Field(default=None, alias='WebExtensionAreaControlTypeIds')

class WebExtensionRedirect(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    redirect_guid: (UUID | None) = Field(default=None, alias='RedirectGuid', example='00000000-0000-0000-0000-000000000000')
    source_url: (str | None) = Field(default=None, alias='SourceUrl')
    web_extension_control_id: (int | None) = Field(default=None, alias='WebExtensionControlId')
    web_extension_control_name: (str | None) = Field(default=None, alias='WebExtensionControlName')
    web_extension_guid: (UUID | None) = Field(default=None, alias='WebExtensionGuid', example='00000000-0000-0000-0000-000000000000')
    extension_claim_type: (ExtensionClaimType | None) = Field(default=None, alias='ExtensionClaimType')
    is_core_extension: (bool | None) = Field(default=None, alias='IsCoreExtension')
    web_extension_area_control_type_ids: (list[int] | None) = Field(default=None, alias='WebExtensionAreaControlTypeIds')

class WebExtensionInlineFrame(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    inline_frame_guid: (UUID | None) = Field(default=None, alias='InlineFrameGuid', example='00000000-0000-0000-0000-000000000000')
    source_url: (str | None) = Field(default=None, alias='SourceUrl')
    web_extension_control_id: (int | None) = Field(default=None, alias='WebExtensionControlId')
    web_extension_control_name: (str | None) = Field(default=None, alias='WebExtensionControlName')
    web_extension_guid: (UUID | None) = Field(default=None, alias='WebExtensionGuid', example='00000000-0000-0000-0000-000000000000')
    extension_claim_type: (ExtensionClaimType | None) = Field(default=None, alias='ExtensionClaimType')
    is_core_extension: (bool | None) = Field(default=None, alias='IsCoreExtension')
    web_extension_area_control_type_ids: (list[int] | None) = Field(default=None, alias='WebExtensionAreaControlTypeIds')

class WebExtensionClickAction(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    click_action_id: (int | None) = Field(default=None, alias='ClickActionId')
    url: (str | None) = Field(default=None, alias='Url')
    url_open_type: (WebExtensionUrlOpenType | None) = Field(default=None, alias='UrlOpenType')

class WebExtensionMenuItem(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    web_extension_menu_item_id: (int | None) = Field(default=None, alias='WebExtensionMenuItemId')
    web_extension_menu_item_parent_id: (int | None) = Field(default=None, alias='WebExtensionMenuItemParentId')
    menu_text: (str | None) = Field(default=None, alias='MenuText')
    click_action: (WebExtensionClickAction | None) = Field(default=None, alias='ClickAction')
    menu_items: (list[WebExtensionMenuItem] | None) = Field(default=None, alias='MenuItems')

class WebExtensionClickButton(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    icon_url: (str | None) = Field(default=None, alias='IconUrl')
    button_text: (str | None) = Field(default=None, alias='ButtonText')
    click_action: (WebExtensionClickAction | None) = Field(default=None, alias='ClickAction')
    allows_multi_select: (bool | None) = Field(default=None, alias='AllowsMultiSelect')
    web_extension_control_id: (int | None) = Field(default=None, alias='WebExtensionControlId')
    web_extension_control_name: (str | None) = Field(default=None, alias='WebExtensionControlName')
    web_extension_guid: (UUID | None) = Field(default=None, alias='WebExtensionGuid', example='00000000-0000-0000-0000-000000000000')
    extension_claim_type: (ExtensionClaimType | None) = Field(default=None, alias='ExtensionClaimType')
    is_core_extension: (bool | None) = Field(default=None, alias='IsCoreExtension')
    web_extension_area_control_type_ids: (list[int] | None) = Field(default=None, alias='WebExtensionAreaControlTypeIds')

class WebExtensionMenuButton(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    icon_url: (str | None) = Field(default=None, alias='IconUrl')
    button_text: (str | None) = Field(default=None, alias='ButtonText')
    menu_items: (list[WebExtensionMenuItem] | None) = Field(default=None, alias='MenuItems')
    allows_multi_select: (bool | None) = Field(default=None, alias='AllowsMultiSelect')
    web_extension_control_id: (int | None) = Field(default=None, alias='WebExtensionControlId')
    web_extension_control_name: (str | None) = Field(default=None, alias='WebExtensionControlName')
    web_extension_guid: (UUID | None) = Field(default=None, alias='WebExtensionGuid', example='00000000-0000-0000-0000-000000000000')
    extension_claim_type: (ExtensionClaimType | None) = Field(default=None, alias='ExtensionClaimType')
    is_core_extension: (bool | None) = Field(default=None, alias='IsCoreExtension')
    web_extension_area_control_type_ids: (list[int] | None) = Field(default=None, alias='WebExtensionAreaControlTypeIds')

class WebExtension(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    web_extension_id: (int | None) = Field(default=None, alias='WebExtensionId')
    extension_solution: (ExtensionSolution | None) = Field(default=None, alias='ExtensionSolution')
    extension_status: (ExtensionStatus | None) = Field(default=None, alias='ExtensionStatus')
    web_extension_guid: (UUID | None) = Field(default=None, alias='WebExtensionGuid', example='00000000-0000-0000-0000-000000000000')
    web_extension_name: (str | None) = Field(default=None, alias='WebExtensionName')
    author: (str | None) = Field(default=None, alias='Author')
    description: (str | None) = Field(default=None, alias='Description')
    version: (str | None) = Field(default=None, alias='Version')
    file_url: (str | None) = Field(default=None, alias='FileUrl')
    filename: (str | None) = Field(default=None, alias='Filename')
    file_check_sum: (str | None) = Field(default=None, alias='FileCheckSum')
    has_static_files: (bool | None) = Field(default=None, alias='HasStaticFiles')
    has_graph_files: (bool | None) = Field(default=None, alias='HasGraphFiles')
    is_core_extension: (bool | None) = Field(default=None, alias='IsCoreExtension')
    extension_claim_types: (list[ExtensionClaimType] | None) = Field(default=None, alias='ExtensionClaimTypes')
    redirects: (list[WebExtensionRedirect] | None) = Field(default=None, alias='Redirects')
    tiles: (list[WebExtensionTile] | None) = Field(default=None, alias='Tiles')
    inline_frames: (list[WebExtensionInlineFrame] | None) = Field(default=None, alias='InlineFrames')
    menu_buttons: (list[WebExtensionMenuButton] | None) = Field(default=None, alias='MenuButtons')
    click_buttons: (list[WebExtensionClickButton] | None) = Field(default=None, alias='ClickButtons')

class WebExtensionAreaControls(ConnectWiseModel):
    model_config = ConfigDict(populate_by_name=True)
    web_extension_area: (WebExtensionArea | None) = Field(default=None, alias='WebExtensionArea')
    click_buttons: (list[WebExtensionClickButton] | None) = Field(default=None, alias='ClickButtons')
    menu_buttons: (list[WebExtensionMenuButton] | None) = Field(default=None, alias='MenuButtons')
    tiles: (list[WebExtensionTile] | None) = Field(default=None, alias='Tiles')
    redirects: (list[WebExtensionRedirect] | None) = Field(default=None, alias='Redirects')
    inline_frames: (list[WebExtensionInlineFrame] | None) = Field(default=None, alias='InlineFrames')
from uuid import UUID
