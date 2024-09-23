from typing import Literal, TypeAlias

from typing_extensions import NotRequired, TypedDict

Literals: TypeAlias = str | int | float | bool
JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | Literals | None


class Patch(TypedDict):
    op: Literal["add"] | Literal["replace"] | Literal["remove"]
    path: str
    value: JSON


class ConnectWiseManageRequestParams(TypedDict):
    conditions: NotRequired[str]
    childConditions: NotRequired[str]
    customFieldConditions: NotRequired[str]
    orderBy: NotRequired[str]
    page: NotRequired[int]
    pageSize: NotRequired[int]
    fields: NotRequired[str]
    columns: NotRequired[str]


class ConnectWiseChangeApprovalRequestParams(TypedDict):
    # TODO - Clarify what these are?
    perColConditions: NotRequired[dict[str, str]]


class ConnectWiseAutomateRequestParams(TypedDict):
    condition: NotRequired[str]
    customFieldConditions: NotRequired[str]
    orderBy: NotRequired[str]
    page: NotRequired[int]
    pageSize: NotRequired[int]
    ids: NotRequired[str]
    includeFields: NotRequired[str]
    excludeFields: NotRequired[str]
    expand: NotRequired[str]


GenericRequestParams: TypeAlias = dict[str, Literals]
RequestParams: TypeAlias = ConnectWiseManageRequestParams | ConnectWiseAutomateRequestParams | GenericRequestParams
PatchRequestData: TypeAlias = list[Patch]
RequestData: TypeAlias = JSON | PatchRequestData
RequestMethod: TypeAlias = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
