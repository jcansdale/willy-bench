import contextlib
import io
from pathlib import Path
import re
import unittest
from unittest.mock import patch

import benchmark
import copilot_chat


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_MODELS = [
    "gemini-3.8-flash",
    "gemini-4-argon",
    "gpt-4o-2024-05-13",
    "gpt-5.6-terra",
    "gpt-5.6-sol",
    "gpt-6-astra",
    "gpt-6-luna",
    "gpt-6-sol",
    "gpt-6.1-sol",
    "claude-haiku-4.5",
    "claude-haiku-5.5",
    "claude-sonnet-5",
    "claude-sonnet-5.5",
    "claude-opus-5",
    "claude-opus-5.5",
    "grok-4.6",
    "grok-4.7",
]
RESPONSES_MODELS = {
    "gpt-5.6-terra",
    "gpt-5.6-sol",
    "gpt-6-astra",
    "gpt-6-luna",
    "gpt-6-sol",
    "gpt-6.1-sol",
    "grok-4.6",
    "grok-4.7",
}


class ModelConfigurationTests(unittest.TestCase):
    def test_default_and_quick_models(self) -> None:
        self.assertEqual(benchmark.DEFAULT_MODELS, EXPECTED_MODELS)
        self.assertEqual(
            benchmark.QUICK_MODELS,
            ["gemini-4-argon", "gpt-6.1-sol", "claude-sonnet-5.5"],
        )

    def test_workflow_and_documentation_match_defaults(self) -> None:
        workflow = (ROOT / ".github/workflows/pixel-benchmark.yml").read_text()
        workflow_models = re.findall(r"'(gemini-[^']+)'", workflow)
        self.assertEqual(len(workflow_models), 2)
        for models in workflow_models:
            self.assertEqual(models.split(","), EXPECTED_MODELS)
        readme = (ROOT / "README.md").read_text()
        documented_models = re.findall(
            r"^\| ([a-z0-9.-]+) \| (?:Chat Completions|Responses) \|$",
            readme,
            re.MULTILINE,
        )
        self.assertEqual(documented_models, EXPECTED_MODELS)

    def test_reasoning_effort(self) -> None:
        unsupported = {"gpt-4o-2024-05-13", "claude-haiku-4.5"}
        for model in EXPECTED_MODELS:
            with self.subTest(model=model):
                self.assertEqual(
                    benchmark.reasoning_effort_for_model(model, "low"),
                    None if model in unsupported else "low",
                )
                self.assertIsNone(
                    benchmark.reasoning_effort_for_model(model, "default")
                )
        self.assertIsNone(benchmark.reasoning_effort_for_model("unknown", "low"))

    def test_api_routing(self) -> None:
        for model in EXPECTED_MODELS + ["gpt-5.3-codex", "gpt-5.4", "gpt-5.5"]:
            with self.subTest(model=model):
                uses_responses = model in RESPONSES_MODELS or model in {
                    "gpt-5.3-codex", "gpt-5.4", "gpt-5.5"
                }
                self.check_routing(model, "auto", uses_responses)

    def test_explicit_api_overrides(self) -> None:
        self.check_routing("gpt-6.1-sol", "chat", False)
        self.check_routing("gemini-4-argon", "responses", True)

    def check_routing(self, model: str, api: str, uses_responses: bool) -> None:
        with (
            patch("sys.argv", [
                "cop", "chat", "-m", model, "--api", api,
                "--reasoning-effort", "low", "-i", "image.png", "test",
            ]),
            patch.object(copilot_chat, "load_or_login", return_value={}),
            patch.object(copilot_chat, "copilot_chat", return_value="[]") as chat,
            patch.object(
                copilot_chat, "copilot_responses", return_value="[]"
            ) as responses,
            contextlib.redirect_stdout(io.StringIO()),
            contextlib.redirect_stderr(io.StringIO()),
        ):
            copilot_chat.main()
        selected, other = (responses, chat) if uses_responses else (chat, responses)
        selected.assert_called_once()
        other.assert_not_called()
        self.assertEqual(selected.call_args.kwargs["model"], model)
        self.assertEqual(selected.call_args.kwargs["images"], ["image.png"])
        self.assertEqual(selected.call_args.kwargs["reasoning_effort"], "low")


if __name__ == "__main__":
    unittest.main()
