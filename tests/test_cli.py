import json

from fabric_physics_engine.cli import main


def test_prompt_cli_outputs_json(capsys):
    assert main(["prompt", "--intensity", "high", "--json"]) == 0
    output = json.loads(capsys.readouterr().out)
    assert output["config"]["intensity"] == "high"
    assert "Gravity" in output["prompt"]


def test_simulation_cli_outputs_bounds(capsys):
    assert main(["simulate", "--garment", "dress", "--fabric", "silk", "--steps", "1"]) == 0
    output = json.loads(capsys.readouterr().out)
    assert output["vertex_count"] == 1000
    assert output["face_count"] == 1950
