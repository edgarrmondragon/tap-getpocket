"""Stream type classes for tap-getpocket."""

from __future__ import annotations

import typing as t

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_getpocket.client import PocketStream

if t.TYPE_CHECKING:
    from singer_sdk.helpers.types import Context, Record

String = th.StringType
Integer = th.IntegerType
Object = th.ObjectType
Array = th.ArrayType


class Items(PocketStream):
    """Items stream."""

    name = "items"
    path = "/v3/get"
    primary_keys = ("item_id",)
    replication_key = "time_updated"
    rest_method = "POST"

    schema = th.PropertiesList(
        th.Property("item_id", String, description="The Pocket item ID"),
        th.Property("resolved_id", String),
        th.Property("given_url", String),
        th.Property("given_title", String),
        th.Property("favorite", String),
        th.Property("status", String),
        th.Property("time_added", Integer),
        th.Property("time_updated", Integer),
        th.Property("time_read", Integer),
        th.Property("time_favorited", Integer),
        th.Property("sort_id", Integer),
        th.Property("resolved_title", String),
        th.Property("resolved_url", String),
        th.Property("excerpt", String),
        th.Property("is_article", String),
        th.Property("is_index", String),
        th.Property("has_video", String),
        th.Property("has_image", String),
        th.Property("word_count", Integer),
        th.Property("lang", String),
        th.Property("time_to_read", Integer),
        th.Property("amp_url", String),
        th.Property("top_image_url", String),
        th.Property(
            "tags",
            Array(
                Object(
                    th.Property("item_id", String),
                    th.Property("tag", String),
                ),
            ),
        ),
        th.Property(
            "authors",
            Array(
                Object(
                    th.Property("item_id", String),
                    th.Property("author_id", String),
                    th.Property("name", String),
                    th.Property("url", String),
                ),
            ),
        ),
        th.Property(
            "image",
            Object(
                th.Property("item_id", String),
                th.Property("src", String),
                th.Property("width", String),
                th.Property("height", String),
            ),
        ),
        th.Property(
            "images",
            Array(
                Object(
                    th.Property("item_id", String),
                    th.Property("image_id", String),
                    th.Property("src", String),
                    th.Property("width", String),
                    th.Property("height", String),
                    th.Property("credit", String),
                    th.Property("caption", String),
                ),
            ),
        ),
        th.Property(
            "videos",
            Array(
                Object(
                    th.Property("item_id", String),
                    th.Property("video_id", String),
                    th.Property("src", String),
                    th.Property("width", String),
                    th.Property("height", String),
                    th.Property("type", String),
                    th.Property("vid", String),
                    th.Property("length", String),
                ),
            ),
        ),
        th.Property(
            "domain_metadata",
            Object(
                th.Property("name", String),
                th.Property("logo", String),
                th.Property("greyscale_logo", String),
            ),
        ),
        th.Property("listen_duration_estimate", Integer),
    ).to_dict()

    def prepare_request_payload(
        self,
        context: Context | None,
        next_page_token: int | None,
    ) -> dict[t.Any, t.Any] | None:
        """Construct and return request body for HTTP request.

        Args:
            context: Stream context.
            next_page_token: Pagination token to retrieve next page.

        Returns:
            Dictionary to pass as JSON body in the HTTP request.
        """
        start_timestamp = self.get_starting_replication_key_value(context)
        self.logger.debug("Initial timestamp: %s", start_timestamp)

        def _get_favorite_state(favorite: bool | None) -> int | None:
            return None if favorite is None else int(favorite)

        payload = {
            "consumer_key": self.config["consumer_key"],
            "access_token": self.config["access_token"],
            "since": start_timestamp,
            "count": self.page_size,
            "offset": next_page_token,
            "sort": "oldest",
            "detailType": "complete",
            "state": self.config.get("state"),
        }

        if tag := self.config.get("tag"):
            payload["tag"] = tag

        if content_type := self.config.get("content_type"):
            payload["contentType"] = content_type

        if favorite := self.config.get("favorite"):
            payload["favorite"] = _get_favorite_state(favorite)

        return payload

    def post_process(
        self,
        row: Record,
        _: Record | None = None,
    ) -> dict[str, t.Any] | None:
        """Clean and massage the record.

        Args:
            row: Stream record.

        Returns:
            Processed record.
        """
        # Deleted items
        if row["status"] == "2":
            return None

        row["tags"] = list(row.get("tags", {}).values())
        row["authors"] = list(row.get("authors", {}).values())
        row["images"] = list(row.get("images", {}).values())
        row["videos"] = list(row.get("videos", {}).values())

        row["word_count"] = int(row["word_count"])

        for key in ("time_added", "time_updated", "time_read", "time_favorited"):
            row[key] = int(row[key])

        return row
