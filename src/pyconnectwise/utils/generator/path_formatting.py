import re
from pyconnectwise.utils.naming import to_title_case_preserve_case


def normalize_path_parameters(path: str) -> str:
    """
    The function takes a path as an input and replaces the path parameter enclosed within {} with {id}

    Args:
        path (str): The path to be normalized.

    Returns:
        str: Normalized path by replacing path parameters with {id}
    """
    pattern = re.compile(r"\{.*?\}")
    return pattern.sub("{id}", path)


def normalize_and_replace_path_parameters(path: str) -> str:
    """
    The function takes a path as an input and replaces the path parameter enclosed within {} with Id

    Args:
        path (str): The path to be normalized.

    Returns:
        str: Normalized path by replacing path parameters with Id
    """
    pattern = re.compile(r"\{.*?\}")
    return pattern.sub("Id", path)


def clean_path(path: str) -> str:
    """
    Strips the trailing slash if present in path.

    Args:
        path (str): The path to be cleaned.

    Returns:
        str: Path after removing trailing slash.
    """
    return path.rstrip("/")


def format_endpoint_path(path: str) -> str:
    """
    Formats a given endpoint path by cleaning and normalizing it.

    Args:
        path (str): The path to format.

    Returns:
        str: Formatted endpoint path.
    """
    return clean_path(normalize_and_replace_path_parameters(path))


def get_endpoint_class_name_from_path(endpoint_path: str) -> str:
    """
    Formats a given endpoint path to form a class name:
    1. Splits the path by "/"
    2. Converts each word to title case (Preserving existing case)
    3. Joins the words together
    4. Appends "Endpoint" to the end

    Args:
        endpoint_path (str): The path of the endpoint.

    Returns:
        str: Formatted class name.
    """
    words = endpoint_path.split("/")
    title_cased_words = map(
        to_title_case_preserve_case, [word.lower() for word in words]
    )
    return "".join(title_cased_words) + "Endpoint"
