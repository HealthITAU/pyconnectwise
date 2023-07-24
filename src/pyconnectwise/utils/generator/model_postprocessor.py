import os
import ast
from ast import parse
from astunparse import unparse
import re


def move_imports_to_bottom(filename):
    exceptions = [
        "pydantic",
        "typing",
        "enum",
        "datetime",
        "__future__",
        "pyconnectwise.models.base.connectwise_model",
    ]
    with open(filename, "r") as file:
        source_code = file.read()

    module = parse(source_code)
    body = module.body

    # Check each statement in the body of the module
    for i, statement in reversed(list(enumerate(body))):
        # If the statement is an import
        if isinstance(statement, ast.Import) or isinstance(statement, ast.ImportFrom):
            # If the imported module is not in the list of exceptions
            if not any(ex in unparse(statement) for ex in exceptions):
                # Remove the import statement from its current position and append it to the end of the body
                import_statement = body.pop(i)
                body.append(import_statement)

    # Using astunparse to convert the ast back to source code
    updated_source_code = unparse(module)
    updated_source_code = re.sub(r"\n\s*\n", "\n\n", updated_source_code)

    # Writing back the updated source code to the file
    with open(filename, "w") as file:
        file.write(updated_source_code)


def post_process_directory(dir_path):
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                move_imports_to_bottom(file_path)


if __name__ == "__main__":
    post_process_directory("./src/pyconnectwise/models/automate")
