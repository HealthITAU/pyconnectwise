from typing import Mapping, Any, Literal, TypeAlias
from typing_extensions import TypedDict, Required, NotRequired

Literals: TypeAlias = str | int | float | bool
JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | Literals | None

Patch = TypedDict(
    "Patch",
    {
        "op": Literal["add"] | Literal["replace"] | Literal["remove"],
        "path": str,
        "value": JSON,
    },
)

ConnectWiseManageRequestParams = TypedDict(
    "ConnectWiseManageRequestParams",
    {
        "conditions": NotRequired[str],
        "childConditions": NotRequired[str],
        "customFieldConditions": NotRequired[str],
        "orderBy": NotRequired[str],
        "page": NotRequired[int],
        "pageSize": NotRequired[int],
        "fields": NotRequired[str],
        "columns": NotRequired[str],
    },
)

GenericRequestParams: TypeAlias = Mapping[str, Literals]
RequestParams: TypeAlias = ConnectWiseManageRequestParams | GenericRequestParams
PatchRequestData: TypeAlias = list[Patch]
RequestData: TypeAlias = JSON | PatchRequestData
RequestMethod: TypeAlias = Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
