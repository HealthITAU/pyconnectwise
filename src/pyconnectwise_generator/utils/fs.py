import black
import isort
from black import NothingChanged


def save_py_file(filepath: str, content: str) -> None:
    """
    Save Python file

    This method takes a file path and content as input, and saves the content as a Python file with the specified file path. If the file path does not have a '.py' extension, it is automatically appended.

    Parameters:
    - filepath (str): The file path where the Python file should be saved. If the file path does not have a '.py' extension, it is automatically appended.
    - content (str): The content that should be saved in the Python file.

    Returns:
    None

    Example usage:
    save_py_file("example/file", "print('Hello, World!')")
    save_py_file("example/file.py", "print('Hello, World!')")
    """
    if ".py" not in filepath:
        filepath += ".py"
    with open(filepath, "w") as f:  # noqa: PTH123
        # First write the unformatted content so we have something to debug
        # against if formatters fail
        f.write(content)
        try:
            formatted_content = black.format_file_contents(content, fast=False, mode=black.FileMode(line_length=120))
        except NothingChanged:
            formatted_content = content
        formatted_content = isort.code(formatted_content, line_length=120)

        # Reset the file handle, and write the formatted content
        f.seek(0)
        f.truncate()
        f.write(formatted_content)
