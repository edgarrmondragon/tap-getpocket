"""REST client handling, including PocketStream base class."""

from __future__ import annotations

from singer_sdk.pagination import BaseOffsetPaginator
from singer_sdk.streams import RESTStream


class PocketStream(RESTStream[int]):
    """Pocket stream class."""

    url_base = "https://getpocket.com"
    records_jsonpath = "$.list.*"
    page_size = 100

    def get_new_paginator(self) -> BaseOffsetPaginator:
        """Return a new instance of the paginator for this stream.

        Returns:
            A new instance of the paginator for this stream.
        """
        return BaseOffsetPaginator(0, self.page_size)

    @property
    def http_headers(self) -> dict[str, str]:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "X-Accept": "application/json",
        }
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config["user_agent"]

        return headers
