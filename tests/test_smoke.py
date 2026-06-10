from pathlib import Path

from agent_ready.main import init_repo, main


def test_init_repo_creates_expected_files(tmp_path: Path) -> None:
    (tmp_path / "pyproject.toml").write_text("[project]\nname='demo'\n", encoding="utf-8")

    written = init_repo(tmp_path)

    assert tmp_path / ".agent" / "skills" / "repo.md" in written
    assert (tmp_path / ".agent" / "checklists" / "delivery.md").exists()
    scorecard = (tmp_path / "AGENT_READY.md").read_text(encoding="utf-8")
    assert "pytest" in scorecard


def test_main_init(tmp_path: Path) -> None:
    assert main(["init", "--repo", str(tmp_path)]) == 0
    assert (tmp_path / "AGENT_READY.md").exists()
