import black
from black import NothingChanged
import isort


def save_py_file(filepath: str, content: str):
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
    with open(filepath, "w") as f:
        try:
            formatted_content = black.format_file_contents(
                content, fast=False, mode=black.FileMode(line_length=120)
            )
        except NothingChanged:
            formatted_content = content
        formatted_content = isort.code(formatted_content, line_length=120)
        f.write(formatted_content)
