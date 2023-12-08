"""REST client handling, including PocketStream base class."""

from __future__ import annotations

from typing import TYPE_CHECKING

from singer_sdk.pagination import BaseOffsetPaginator
from singer_sdk.streams import RESTStream

if TYPE_CHECKING:
    from requests import Response


class PocketPaginator(BaseOffsetPaginator):
    """Pocket API pagination handler."""

    def has_more(self, response: Response) -> bool:
        """Return True if there are more pages to fetch.

        Args:
            response: The most recent response object.

        Returns:
            Whether there are more pages to fetch.
        """
        if response.json()["list"]:
            return True
        return False


class PocketStream(RESTStream[int]):
    """Pocket stream class."""

    url_base = "https://getpocket.com"
    records_jsonpath = "$.list.*"
    page_size = 100

    def get_new_paginator(self) -> PocketPaginator:
        """Return a new instance of the paginator for this stream.

        Returns:
            A new instance of the paginator for this stream.
        """
        return PocketPaginator(0, self.page_size)

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
