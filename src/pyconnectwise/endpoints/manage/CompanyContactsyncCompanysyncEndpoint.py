from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsyncCompanysyncIdEndpoint import (
    CompanyContactsyncCompanysyncIdEndpoint,
)


class CompanyContactsyncCompanysyncEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(self, client, "companysync", parent_endpoint=parent_endpoint)

    def id(self, id: int) -> CompanyContactsyncCompanysyncIdEndpoint:  # noqa: A002
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsyncCompanysyncIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsyncCompanysyncIdEndpoint: The initialized CompanyContactsyncCompanysyncIdEndpoint object.
        """
        child = CompanyContactsyncCompanysyncIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
