from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdQuestionsIdCopyEndpoint import (
    ServiceSurveysIdQuestionsIdCopyEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceSurveysIdQuestionsIdOptionsEndpoint import (
    ServiceSurveysIdQuestionsIdOptionsEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import ServiceSurveyQuestion
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ServiceSurveysIdQuestionsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[ServiceSurveyQuestion, ConnectWiseManageRequestParams],
    IPuttable[ServiceSurveyQuestion, ConnectWiseManageRequestParams],
    IPatchable[ServiceSurveyQuestion, ConnectWiseManageRequestParams],
    IPaginateable[ServiceSurveyQuestion, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, ServiceSurveyQuestion)
        IPuttable.__init__(self, ServiceSurveyQuestion)
        IPatchable.__init__(self, ServiceSurveyQuestion)
        IPaginateable.__init__(self, ServiceSurveyQuestion)

        self.copy = self._register_child_endpoint(
            ServiceSurveysIdQuestionsIdCopyEndpoint(client, parent_endpoint=self)
        )
        self.options = self._register_child_endpoint(
            ServiceSurveysIdQuestionsIdOptionsEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ServiceSurveyQuestion]:
        """
        Performs a GET request against the /service/surveys/{id}/questions/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ServiceSurveyQuestion]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ServiceSurveyQuestion,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ServiceSurveyQuestion:
        """
        Performs a GET request against the /service/surveys/{id}/questions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurveyQuestion: The parsed response data.
        """
        return self._parse_one(
            ServiceSurveyQuestion,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /service/surveys/{id}/questions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ServiceSurveyQuestion:
        """
        Performs a PUT request against the /service/surveys/{id}/questions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurveyQuestion: The parsed response data.
        """
        return self._parse_one(
            ServiceSurveyQuestion,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ServiceSurveyQuestion:
        """
        Performs a PATCH request against the /service/surveys/{id}/questions/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ServiceSurveyQuestion: The parsed response data.
        """
        return self._parse_one(
            ServiceSurveyQuestion,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
