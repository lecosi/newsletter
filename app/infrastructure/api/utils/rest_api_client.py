
from typing import Dict, Any, Tuple

from requests import get, post, Response


class RestAPIClient:

    @staticmethod
    def request_get(
        *,
        url: str,
        headers: Dict[str, Any]
    ) -> Response:
        try:
            response = get(
                url=url,
                headers=headers
            )
        except Exception as e:
            raise ValueError(e)

        return response

    @staticmethod
    def request_post(
        *,
        url: str,
        headers: Dict[str, Any],
        data: Dict[str, Any],
        auth: Tuple[str, Any] = None,
    ) -> Response:
        response = post(
            url=url,
            headers=headers,
            auth=auth,
            json=data
        )
        return response
