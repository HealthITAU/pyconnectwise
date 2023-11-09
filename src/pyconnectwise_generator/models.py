import json
import tempfile
from pathlib import Path
from typing import Any

# Use main instead of generate() so that it loads pyproject.toml
from datamodel_code_generator.__main__ import Exit, main


def generate_models(schema: dict[str, Any], model_output_dir: Path) -> None:
    # datamodel-gen needs a file...
    with tempfile.NamedTemporaryFile("w") as schema_file:
        schema_file.write(json.dumps(schema))

        e = main(
            [
                "--input",
                str(schema_file.name),
                "--output",
                str(model_output_dir),
            ]
        )
        if e != Exit.OK:
            raise Exception("Model generation failed")  # noqa: TRY002, TRY003
