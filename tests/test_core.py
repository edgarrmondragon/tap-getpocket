"""Tests standard tap features using the built-in SDK tests library."""

import datetime

from singer_sdk.testing import get_standard_tap_tests

from tap_pocket.tap import TapPocket

SAMPLE_CONFIG = {
    "consumer_key": "100055-b43370578682acfb76b20b5",
    "access_token": "dcdd762a-a84e-d90c-bcfc-5380e0",
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(TapPocket, config=SAMPLE_CONFIG)
    for test in tests:
        test()
