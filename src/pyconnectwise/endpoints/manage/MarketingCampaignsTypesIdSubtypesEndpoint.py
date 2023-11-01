from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesIdSubtypesCountEndpoint import (
    MarketingCampaignsTypesIdSubtypesCountEndpoint,
)
from pyconnectwise.endpoints.manage.MarketingCampaignsTypesIdSubtypesIdEndpoint import (
    MarketingCampaignsTypesIdSubtypesIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
)
from pyconnectwise.models.manage import TypeSubTypeCampaignSubType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class MarketingCampaignsTypesIdSubtypesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[TypeSubTypeCampaignSubType], ConnectWiseManageRequestParams],
    IPaginateable[TypeSubTypeCampaignSubType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "subTypes", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[TypeSubTypeCampaignSubType])
        IPaginateable.__init__(self, TypeSubTypeCampaignSubType)

        self.count = self._register_child_endpoint(
            MarketingCampaignsTypesIdSubtypesCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> MarketingCampaignsTypesIdSubtypesIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized MarketingCampaignsTypesIdSubtypesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            MarketingCampaignsTypesIdSubtypesIdEndpoint: The initialized MarketingCampaignsTypesIdSubtypesIdEndpoint object.
        """
        child = MarketingCampaignsTypesIdSubtypesIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[TypeSubTypeCampaignSubType]:
        """
        Performs a GET request against the /marketing/campaigns/types/{id}/subTypes endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TypeSubTypeCampaignSubType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            TypeSubTypeCampaignSubType,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[TypeSubTypeCampaignSubType]:
        """
        Performs a GET request against the /marketing/campaigns/types/{id}/subTypes endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TypeSubTypeCampaignSubType]: The parsed response data.
        """
        return self._parse_many(
            TypeSubTypeCampaignSubType,
            super()._make_request("GET", data=data, params=params).json(),
        )
