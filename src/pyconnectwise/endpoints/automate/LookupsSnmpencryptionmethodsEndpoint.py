from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.automate import LabTechEncryptionMethod
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class LookupsSnmpencryptionmethodsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechEncryptionMethod], ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechEncryptionMethod, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Snmpencryptionmethods", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechEncryptionMethod])
        IPaginateable.__init__(self, LabTechEncryptionMethod)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechEncryptionMethod]:
        """
        Performs a GET request against the /Lookups/Snmpencryptionmethods endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechEncryptionMethod]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechEncryptionMethod,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechEncryptionMethod]:
        """
        Performs a GET request against the /Lookups/Snmpencryptionmethods endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechEncryptionMethod]: The parsed response data.
        """
        return self._parse_many(
            LabTechEncryptionMethod,
            super()._make_request("GET", data=data, params=params).json(),
        )
