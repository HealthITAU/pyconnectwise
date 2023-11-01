from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.automate import LabTechUserFavorite
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class UsersIdFavoritesEndpoint(
    ConnectWiseEndpoint,
    IPostable[LabTechUserFavorite, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Favorites", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, LabTechUserFavorite)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechUserFavorite:
        """
        Performs a POST request against the /Users/{id}/Favorites endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechUserFavorite: The parsed response data.
        """
        return self._parse_one(
            LabTechUserFavorite,
            super()._make_request("POST", data=data, params=params).json(),
        )
