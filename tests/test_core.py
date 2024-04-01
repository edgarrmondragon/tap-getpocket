"""Tests standard tap features using the built-in SDK tests library."""

from __future__ import annotations

from singer_sdk.testing import get_tap_test_class

from tap_getpocket.tap import TapPocket

TestTapPocket = get_tap_test_class(TapPocket)
