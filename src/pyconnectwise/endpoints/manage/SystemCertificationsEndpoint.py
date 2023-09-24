from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SystemCertificationsCountEndpoint import SystemCertificationsCountEndpoint
from pyconnectwise.endpoints.manage.SystemCertificationsIdEndpoint import SystemCertificationsIdEndpoint
from pyconnectwise.interfaces import IDeleteable, IGettable, IPaginateable, IPatchable, IPostable, IPuttable
from pyconnectwise.models.manage import Certification
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import JSON, ConnectWiseAutomateRequestParams, ConnectWiseManageRequestParams, PatchRequestData


class SystemCertificationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[Certification], ConnectWiseManageRequestParams],
    IPostable[Certification, ConnectWiseManageRequestParams],
    IPaginateable[Certification, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "certifications", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SystemCertificationsCountEndpoint(client, parent_endpoint=self))

    def id(self, id: int) -> SystemCertificationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemCertificationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemCertificationsIdEndpoint: The initialized SystemCertificationsIdEndpoint object.
        """
        child = SystemCertificationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child

    def paginated(
        self, page: int, page_size: int, params: ConnectWiseManageRequestParams | None = None
    ) -> PaginatedResponse[Certification]:
        """
        Performs a GET request against the /system/certifications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[Certification]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params), Certification, self, page, page_size, params
        )

    def get(
        self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None
    ) -> list[Certification]:
        """
        Performs a GET request against the /system/certifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[Certification]: The parsed response data.
        """
        return self._parse_many(Certification, super()._make_request("GET", data=data, params=params).json())

    def post(self, data: JSON | None = None, params: ConnectWiseManageRequestParams | None = None) -> Certification:
        """
        Performs a POST request against the /system/certifications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            Certification: The parsed response data.
        """
        return self._parse_one(Certification, super()._make_request("POST", data=data, params=params).json())
