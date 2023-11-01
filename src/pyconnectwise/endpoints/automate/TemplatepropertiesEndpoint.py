from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.automate import LabTechTemplateProperty
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class TemplatepropertiesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechTemplateProperty], ConnectWiseAutomateRequestParams],
    IPostable[LabTechTemplateProperty, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechTemplateProperty, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "Templateproperties", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechTemplateProperty])
        IPostable.__init__(self, LabTechTemplateProperty)
        IPaginateable.__init__(self, LabTechTemplateProperty)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechTemplateProperty]:
        """
        Performs a GET request against the /Templateproperties endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechTemplateProperty]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechTemplateProperty,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechTemplateProperty]:
        """
        Performs a GET request against the /Templateproperties endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechTemplateProperty]: The parsed response data.
        """
        return self._parse_many(
            LabTechTemplateProperty,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechTemplateProperty:
        """
        Performs a POST request against the /Templateproperties endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechTemplateProperty: The parsed response data.
        """
        return self._parse_one(
            LabTechTemplateProperty,
            super()._make_request("POST", data=data, params=params).json(),
        )
