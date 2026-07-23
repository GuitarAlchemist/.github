import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "classify_claude_review.py"
SPEC = importlib.util.spec_from_file_location("classifier", MODULE_PATH)
classifier = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(classifier)


class ClassifierTests(unittest.TestCase):
    def test_completed_review_requires_a_turn(self):
        result = classifier.classify([{"type": "result", "subtype": "success", "is_error": False, "num_turns": 2}], "success")
        self.assertEqual("review-completed", result["classification"])

    def test_zero_turn_quota_is_explicit(self):
        result = classifier.classify([{"type": "result", "subtype": "success", "is_error": True, "num_turns": 0, "result": "rate limit 429"}], "failure")
        self.assertEqual("quota", result["classification"])

    def test_zero_turn_model_entitlement_is_explicit(self):
        result = classifier.classify([{"type": "result", "is_error": True, "num_turns": 0, "error": "model not found"}], "failure")
        self.assertEqual("model-entitlement", result["classification"])

    def test_missing_result_distinguishes_action_failure(self):
        self.assertEqual("action-runtime-failure", classifier.classify([], "failure")["classification"])

    def test_nonzero_error_is_not_misreported_as_outage(self):
        result = classifier.classify([{"type": "result", "is_error": True, "num_turns": 1}], "failure")
        self.assertEqual("claude-execution-error", result["classification"])


if __name__ == "__main__":
    unittest.main()

