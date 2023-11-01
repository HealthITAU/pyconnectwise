from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyCompaniesIdSurveysCountEndpoint import (
    CompanyCompaniesIdSurveysCountEndpoint,
)


class CompanyCompaniesIdSurveysEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None) -> None:  # noqa: ANN001
        ConnectWiseEndpoint.__init__(
            self, client, "surveys", parent_endpoint=parent_endpoint
        )

        self.count = self._register_child_endpoint(
            CompanyCompaniesIdSurveysCountEndpoint(client, parent_endpoint=self)
        )
