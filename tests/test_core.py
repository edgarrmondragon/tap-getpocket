"""Tests standard tap features using the built-in SDK tests library."""

import pytest
from singer_sdk.testing import get_standard_tap_tests

from tap_getpocket.tap import TapPocket


@pytest.mark.parametrize("favorite", [True, False, None])
@pytest.mark.parametrize("content_type", ["article", "video", "image", None])
@pytest.mark.parametrize("state", ["archive", "unread", "all"])
@pytest.mark.parametrize("tag", ["python", "_untagged_", None])
def test_standard_tap_tests(favorite, content_type, state, tag):
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        TapPocket,
        config={
            "favorite": favorite,
            "content_type": content_type,
            "state": state,
            "tag": tag,
        },
    )
    for test in tests:
        test()
