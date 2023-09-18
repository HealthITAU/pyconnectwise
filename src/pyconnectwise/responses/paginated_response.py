from __future__ import annotations
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.utils.helpers import parse_link_headers
from typing import TYPE_CHECKING, Generic, TypeVar, Type, Iterable
from pydantic import BaseModel
from requests import Response

TModel = TypeVar("TModel", bound="BaseModel")

if TYPE_CHECKING:
    from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class PaginatedResponse(Generic[TModel]):
    """
    PaginatedResponse is a wrapper class for handling paginated responses from the
    ConnectWise API. It provides methods for navigating through the pages of the response
    and accessing the data contained within each page.

    The class is designed to work with ConnectWiseEndpoint and its derived classes to
    parse the API response into model instances. It also supports iteration, allowing
    the user to loop through the items within the paginated response.

    PaginatedResponse uses a generic type variable TModel, which represents the
    expected model type for the response data. This allows for type-safe handling
    of model instances throughout the class.
    """

    def __init__(
        self,
        response: Response,
        response_model: Type[TModel],
        endpoint: ConnectWiseEndpoint,
        page: int,
        page_size: int,
        params: dict[str, int | str] = {},
    ):
        """
        PaginatedResponse is a wrapper class for handling paginated responses from the
        ConnectWise API. It provides methods for navigating through the pages of the response
        and accessing the data contained within each page.

        The class is designed to work with ConnectWiseEndpoint and its derived classes to
        parse the API response into model instances. It also supports iteration, allowing
        the user to loop through the items within the paginated response.

        PaginatedResponse uses a generic type variable TModel, which represents the
        expected model type for the response data. This allows for type-safe handling
        of model instances throughout the class.
        """
        self._initialize(response, response_model, endpoint, page, page_size, params)

    def _initialize(
        self,
        response: Response,
        response_model: Type[TModel],
        endpoint: ConnectWiseEndpoint,
        page: int,
        page_size: int,
        params: dict[str, int | str] = {},
    ):
        """
        Initialize the instance variables using the provided response, endpoint, and page size.

        Args:
            response: The raw response object from the API.
            endpoint (ConnectWiseEndpoint[TModel]): The endpoint associated with the response.
            page_size (int): The number of items per page.
        """
        self.response = response
        self.response_model = response_model
        self.endpoint = endpoint
        self.page_size = page_size
        self.parsed_link_headers = parse_link_headers(response.headers)
        self.params = params
        if self.parsed_link_headers is not None:
            # ConnectWise Manage API gives us handy headers to parse for Pagination
            self.has_next_page: bool = self.parsed_link_headers.get(
                "has_next_page", False
            )
            self.has_prev_page: bool = self.parsed_link_headers.get(
                "has_prev_page", False
            )
            self.first_page: int = self.parsed_link_headers.get("first_page", None)
            self.prev_page: int = self.parsed_link_headers.get("prev_page", None)
            self.next_page: int = self.parsed_link_headers.get("next_page", None)
            self.last_page: int = self.parsed_link_headers.get("last_page", None)
        else:
            # ConnectWise Automate doesn't...
            # So, we'll brute force it, with some guesses.
            self.has_next_page: bool = True
            self.has_prev_page: bool = page > 1
            self.first_page: int = 1
            self.prev_page = page - 1 if page > 1 else 1
            self.next_page = page + 1
            self.last_page = 999999
        self.data: list[TModel] = endpoint._parse_many(response_model, response.json())
        self.has_data = self.data and len(self.data) > 0
        self.index = 0

    def get_next_page(self) -> PaginatedResponse[TModel]:
        """
        Fetch the next page of the paginated response.

        Returns:
            PaginatedResponse[TModel]: The updated PaginatedResponse instance
            with the data from the next page or None if there is no next page.
        """
        if not self.has_next_page or not self.next_page:
            self.has_data = False
            return self

        next_response = self.endpoint.paginated(
            self.next_page, self.page_size, self.params
        )
        self._initialize(
            next_response.response,
            next_response.response_model,
            next_response.endpoint,
            self.next_page,
            next_response.page_size,
            self.params,
        )
        return self

    def get_previous_page(self) -> PaginatedResponse[TModel]:
        """
        Fetch the next page of the paginated response.

        Returns:
            PaginatedResponse[TModel]: The updated PaginatedResponse instance
            with the data from the next page or None if there is no next page.
        """
        if not self.has_prev_page or not self.prev_page:
            self.has_data = False
            return self

        prev_response = self.endpoint.paginated(
            self.prev_page, self.page_size, self.params
        )
        self._initialize(
            prev_response.response,
            prev_response.response_model,
            prev_response.endpoint,
            self.prev_page,
            prev_response.page_size,
            self.params,
        )
        return self

    def all(self) -> Iterable[TModel]:
        """
        Iterate through all items in the paginated response, across all pages.

        Yields:
            TModel: An instance of the model class for each item in the paginated response.
        """
        while self.has_data:
            for item in self.data:
                yield item
            self.get_next_page()

    def __iter__(self):
        """
        Implement the iterator protocol for the PaginatedResponse class.

        Returns:
            PaginatedResponse[TModel]: The current instance of the PaginatedResponse.
        """
        return self

    def __dict__(self):
        """
        Implement the iterator protocol for the PaginatedResponse class.

        Returns:
            PaginatedResponse[TModel]: The current instance of the PaginatedResponse.
        """
        return self.data

    def __next__(self):
        """
        Implement the iterator protocol by getting the next item in the data.

        Returns:
            TModel: The next item in the data.

        Raises:
            StopIteration: If there are no more items in the data.
        """
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
