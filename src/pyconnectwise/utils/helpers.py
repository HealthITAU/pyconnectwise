from datetime import datetime
import re
from typing import Any


def cw_format_datetime(datetime: datetime) -> str:
    return datetime.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_link_headers(headers: dict[str, str]) -> dict[str, Any]:
    links = headers["Link"].split(",")
    has_next_page: bool = False
    has_prev_page: bool = False
    first_page: int | None = None
    prev_page: int | None = None
    next_page: int | None = None
    last_page: int | None = None

    for link in links:
        match = re.search(r'page=(\d+)>; rel="(.*?)"', link)
        if match:
            page_number = int(match.group(1))
            rel_value = match.group(2)
            if rel_value == "first":
                first_page = page_number
            elif rel_value == "prev":
                prev_page = page_number
                has_prev_page = True
            elif rel_value == "next":
                next_page = page_number
                has_next_page = True
            elif rel_value == "last":
                last_page = page_number

    result = {}

    if first_page is not None:
        result["first_page"] = first_page

    if prev_page is not None:
        result["prev_page"] = prev_page

    if next_page is not None:
        result["next_page"] = next_page

    if last_page is not None:
        result["last_page"] = last_page

    if has_next_page:
        result["has_next_page"] = has_next_page

    if has_prev_page:
        result["has_prev_page"] = has_prev_page

    return result
