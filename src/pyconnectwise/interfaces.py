from abc import ABC, abstractmethod
from pyconnectwise.types import (
    RequestParams,
    ConnectWiseManageRequestParams,
    ConnectWiseAutomateRequestParams,
    JSON,
    PatchRequestData,
)
from typing import TypeVar, Type, TYPE_CHECKING, Generic
from pyconnectwise.responses.paginated_response import PaginatedResponse

if TYPE_CHECKING:
    from pydantic import BaseModel

TModel = TypeVar("TModel", bound="BaseModel")
TRequestParams = TypeVar(
    "TRequestParams",
    bound=ConnectWiseManageRequestParams | ConnectWiseAutomateRequestParams,
)


class IPaginateable(ABC, Generic[TModel, TRequestParams]):
    @abstractmethod
    def paginated(
        self,
        page: int,
        page_size: int,
        params: TRequestParams | None = None,
    ) -> PaginatedResponse[TModel]:
        pass


class IGettable(ABC, Generic[TModel, TRequestParams]):
    @abstractmethod
    def get(
        self,
        data: JSON | None = None,
        params: TRequestParams | None = None,
    ) -> TModel:
        pass


class IPostable(ABC, Generic[TModel, TRequestParams]):
    @abstractmethod
    def post(
        self,
        data: JSON | None = None,
        params: TRequestParams | None = None,
    ) -> TModel:
        pass


class IPatchable(ABC, Generic[TModel, TRequestParams]):
    @abstractmethod
    def patch(
        self,
        data: PatchRequestData,
        params: TRequestParams | None = None,
    ) -> TModel:
        pass


class IPuttable(ABC, Generic[TModel, TRequestParams]):
    @abstractmethod
    def put(
        self,
        data: JSON | None = None,
        params: TRequestParams | None = None,
    ) -> TModel:
        pass


class IDeleteable(ABC, Generic[TRequestParams]):
    @abstractmethod
    def delete(
        self,
        data: JSON | None = None,
        params: TRequestParams | None = None,
    ) -> None:
        pass
