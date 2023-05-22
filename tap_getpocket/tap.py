"""Pocket tap class."""

from __future__ import annotations

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_getpocket.streams import Items

STREAM_TYPES = [
    Items,
]


class TapPocket(Tap):
    """Pocket tap class."""

    name = "tap-getpocket"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "consumer_key",
            th.StringType,
            required=True,
            description="Pocket application key",
        ),
        th.Property(
            "access_token",
            th.StringType,
            required=True,
            description="Pocket user access token",
        ),
        th.Property(
            "start_date",
            th.StringType,
            description="The earliest record datetime to sync as a UNIX timestamp",
        ),
        th.Property(
            "favorite",
            th.BooleanType,
            description=(
                "Set to `true` to sync only favorite items, `false` to sync only "
                "non-favorite items, or omit to sync all items"
            ),
        ),
        th.Property(
            "content_type",
            th.StringType,
            description=(
                "The content type of items to sync. By default, all content types "
                "are synced."
            ),
            allowed_values=["article", "video", "image"],
        ),
        th.Property(
            "state",
            th.StringType,
            description=(
                "Type of item state to sync. By default, all states are synced."
            ),
            allowed_values=["archive", "unread", "all"],
            required=True,  # This is done only to mark the field as non-nullable
            default="all",
        ),
        th.Property(
            "tag",
            th.StringType,
            description=(
                "The tag to sync. By default, all tags are synced. Use `_untagged_` "
                "to sync untagged items."
            ),
        ),
    ).to_dict()

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of all the streams discovered for this tap.
        """
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
