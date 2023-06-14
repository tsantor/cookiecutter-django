import json
from collections.abc import Sequence
from pathlib import Path

from dotenv import dotenv_values

BASE_DIR = Path(__file__).parent.resolve()
PRODUCTION_DOTENVS_DIR = BASE_DIR / ".envs" / ".production"
PRODUCTION_DOTENV_FILES = [
    PRODUCTION_DOTENVS_DIR / ".django",
    PRODUCTION_DOTENVS_DIR / ".postgres",
]
DOTENV_FILE = BASE_DIR / ".env"

OUTPUT_FILE = PRODUCTION_DOTENVS_DIR / "aws-secrets.json"


def envs_to_dict(env_files) -> dict:
    """Read env files, merge them and return a dict"""
    config = {}
    for env_file in env_files:
        config = config | dotenv_values(env_file)
    return dict(config)


def merge(
    output_file: Path,
    files_to_merge: Sequence[Path],
) -> None:
    config = envs_to_dict(files_to_merge)
    with open(output_file, "w", encoding="utf-8") as fh:
        fh.write(json.dumps(config, indent=2))


if __name__ == "__main__":
    merge(OUTPUT_FILE, PRODUCTION_DOTENV_FILES)
