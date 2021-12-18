"""REST client handling, including PocketStream base class."""

from singer_sdk.streams import RESTStream


class PocketStream(RESTStream):
    """Pocket stream class."""

    url_base = "https://getpocket.com"
    records_jsonpath = "$.list.*"

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {
            "Content-Type": "application/json; charset=UTF-8",
            "X-Accept": "application/json",
        }
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")

        return headers
