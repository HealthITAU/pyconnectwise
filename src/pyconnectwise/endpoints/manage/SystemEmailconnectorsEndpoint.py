from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemEmailconnectorsCountEndpoint import SystemEmailconnectorsCountEndpoint
from pyconnectwise.endpoints.manage.SystemEmailconnectorsIdEndpoint import SystemEmailconnectorsIdEndpoint
from pyconnectwise.endpoints.manage.SystemEmailconnectorsInfoEndpoint import SystemEmailconnectorsInfoEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import EmailConnector
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemEmailconnectorsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[EmailConnector], ConnectWiseManageRequestParams],
    IPostable[EmailConnector, ConnectWiseManageRequestParams],
    IPaginateable[EmailConnector, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(self, client, "emailConnectors", parent_endpoint=parent_endpoint)
        IGettable.__init__(self, list[EmailConnector])
        IPostable.__init__(self, EmailConnector)
        IPaginateable.__init__(self, EmailConnector)

        self.count = self._register_child_endpoint(SystemEmailconnectorsCountEndpoint(client, parent_endpoint=self))
        self.info = self._register_child_endpoint(SystemEmailconnectorsInfoEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemEmailconnectorsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemEmailconnectorsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemEmailconnectorsIdEndpoint: The initialized SystemEmailconnectorsIdEndpoint object.
        """
        child = SystemEmailconnectorsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[EmailConnector]:
        """
        Performs a GET request against the /system/emailConnectors endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[EmailConnector]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), EmailConnector, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[EmailConnector]:
        """
        Performs a GET request against the /system/emailConnectors endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[EmailConnector]: The parsed response data.
        """
        return self._parse_many(EmailConnector, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> EmailConnector:
        """
        Performs a POST request against the /system/emailConnectors endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            EmailConnector: The parsed response data.
        """
        return self._parse_one(EmailConnector, super()._make_request("POST", data=data, params=params).json())
