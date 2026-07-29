import importlib.util
import json
import tempfile
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


class LoadRecordsTests(unittest.TestCase):
    """`load_records` had no coverage at all, which is how the array bug shipped.

    Every case below is a shape the execution log has actually taken or plausibly
    can; the first one is what was failing every review job in the org.
    """

    def setUp(self):
        self.dir = Path(tempfile.mkdtemp())
        self.records = [
            {"type": "system"},
            {"type": "result", "subtype": "success", "is_error": False, "num_turns": 3},
        ]

    def _write(self, text):
        path = self.dir / "claude-execution-output.json"
        path.write_text(text, encoding="utf-8")
        return path

    def test_pretty_printed_array_is_the_real_action_output(self):
        # Regression: json.loads() per line raised on the bare "[" of line 1 with
        # "Expecting value: line 1 column 2 (char 1)" and failed the whole job.
        path = self._write(json.dumps(self.records, indent=2))
        self.assertEqual(self.records, classifier.load_records(path))

    def test_jsonl_is_still_accepted(self):
        path = self._write("\n".join(json.dumps(r) for r in self.records))
        self.assertEqual(self.records, classifier.load_records(path))

    def test_single_object_is_wrapped(self):
        path = self._write(json.dumps(self.records[1], indent=2))
        self.assertEqual([self.records[1]], classifier.load_records(path))

    def test_malformed_log_degrades_instead_of_raising(self):
        # The script's whole purpose is classifying failures, so it must not crash
        # on a truncated or garbled log - that would destroy the diagnostic.
        path = self._write("not json at all")
        self.assertEqual([], classifier.load_records(path))

    def test_partially_garbled_jsonl_keeps_the_parseable_lines(self):
        lines = [json.dumps(self.records[0]), "{truncated", json.dumps(self.records[1])]
        path = self._write("\n".join(lines))
        self.assertEqual(self.records, classifier.load_records(path))

    def test_empty_and_missing_files_are_empty(self):
        self.assertEqual([], classifier.load_records(self._write("")))
        self.assertEqual([], classifier.load_records(self.dir / "does-not-exist.json"))

    def test_non_dict_json_scalars_are_dropped(self):
        path = self._write(json.dumps(["a string", 42, self.records[1]], indent=2))
        self.assertEqual([self.records[1]], classifier.load_records(path))

    def test_array_log_reaches_classify_as_a_completed_review(self):
        # End to end through the real shape: the job should report review-completed,
        # not crash before writing the diagnostic artifact.
        path = self._write(json.dumps(self.records, indent=2))
        result = classifier.classify(classifier.load_records(path), "success")
        self.assertEqual("review-completed", result["classification"])
        self.assertEqual(3, result["num_turns"])


if __name__ == "__main__":
    unittest.main()

