import os
import unittest
from unittest.mock import patch

from scripts.fetch_intel_updates import env_flag, feed_error_exit_code


class EnvFlagTests(unittest.TestCase):
    def test_env_flag_defaults_to_false(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(env_flag("INTEL_UPDATE_STRICT_FEEDS"))

    def test_env_flag_accepts_strict_truthy_values(self):
        for value in ("1", "true", "TRUE", "yes", "on", "strict", " strict "):
            with self.subTest(value=value):
                with patch.dict(os.environ, {"INTEL_UPDATE_STRICT_FEEDS": value}, clear=True):
                    self.assertTrue(env_flag("INTEL_UPDATE_STRICT_FEEDS"))

    def test_env_flag_rejects_falsey_values(self):
        for value in ("0", "false", "no", "off", ""):
            with self.subTest(value=value):
                with patch.dict(os.environ, {"INTEL_UPDATE_STRICT_FEEDS": value}, clear=True):
                    self.assertFalse(env_flag("INTEL_UPDATE_STRICT_FEEDS"))

    def test_feed_errors_are_non_fatal_by_default(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(feed_error_exit_code(["FEED-CISA-ADVISORIES: HTTP 403"]), 0)

    def test_feed_errors_fail_in_strict_mode(self):
        with patch.dict(os.environ, {"INTEL_UPDATE_STRICT_FEEDS": "true"}, clear=True):
            self.assertEqual(feed_error_exit_code(["FEED-CISA-ADVISORIES: HTTP 403"]), 2)


if __name__ == "__main__":
    unittest.main()
