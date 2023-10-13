from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceEmailtemplatesCountEndpoint import ServiceEmailtemplatesCountEndpoint
from pyconnectwise.endpoints.manage.ServiceEmailtemplatesIdEndpoint import ServiceEmailtemplatesIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import ServiceEmailTemplate
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class ServiceEmailtemplatesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ServiceEmailTemplate], ConnectWiseManageRequestParams],
    IPostable[ServiceEmailTemplate, ConnectWiseManageRequestParams],
    IPaginateable[ServiceEmailTemplate, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "emailTemplates", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[ServiceEmailTemplate])
        IPostable.__init__(self, ServiceEmailTemplate)
        IPaginateable.__init__(self, ServiceEmailTemplate)

        self.count = self._register_child_endpoint(ServiceEmailtemplatesCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> ServiceEmailtemplatesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceEmailtemplatesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceEmailtemplatesIdEndpoint: The initialized ServiceEmailtemplatesIdEndpoint object.
        """
        child = ServiceEmailtemplatesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[ServiceEmailTemplate]:
        """
        Performs a GET request against the /service/emailTemplates endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceEmailTemplate]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), ServiceEmailTemplate, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[ServiceEmailTemplate]:
        """
        Performs a GET request against the /service/emailTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ServiceEmailTemplate]: The parsed response data.
        """
        return self._parse_many(ServiceEmailTemplate, super()._make_request("GET", data=data, params=params).json())

    def post(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> ServiceEmailTemplate:
        """
        Performs a POST request against the /service/emailTemplates endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceEmailTemplate: The parsed response data.
        """
        return self._parse_one(ServiceEmailTemplate, super()._make_request("POST", data=data, params=params).json())
