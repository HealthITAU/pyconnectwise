from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementUnitofmeasuresCountEndpoint import (
    ProcurementUnitofmeasuresCountEndpoint,
)
from pyconnectwise.endpoints.manage.ProcurementUnitofmeasuresIdEndpoint import (
    ProcurementUnitofmeasuresIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import UnitOfMeasure
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ProcurementUnitofmeasuresEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[UnitOfMeasure], ConnectWiseManageRequestParams],
    IPostable[UnitOfMeasure, ConnectWiseManageRequestParams],
    IPaginateable[UnitOfMeasure, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "unitOfMeasures", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[UnitOfMeasure])
        IPostable.__init__(self, UnitOfMeasure)
        IPaginateable.__init__(self, UnitOfMeasure)

        self.count = self._register_child_endpoint(
            ProcurementUnitofmeasuresCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> ProcurementUnitofmeasuresIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementUnitofmeasuresIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementUnitofmeasuresIdEndpoint: The initialized ProcurementUnitofmeasuresIdEndpoint object.
        """
        child = ProcurementUnitofmeasuresIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[UnitOfMeasure]:
        """
        Performs a GET request against the /procurement/unitOfMeasures endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnitOfMeasure]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            UnitOfMeasure,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[UnitOfMeasure]:
        """
        Performs a GET request against the /procurement/unitOfMeasures endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UnitOfMeasure]: The parsed response data.
        """
        return self._parse_many(
            UnitOfMeasure, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> UnitOfMeasure:
        """
        Performs a POST request against the /procurement/unitOfMeasures endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            UnitOfMeasure: The parsed response data.
        """
        return self._parse_one(
            UnitOfMeasure,
            super()._make_request("POST", data=data, params=params).json(),
        )
