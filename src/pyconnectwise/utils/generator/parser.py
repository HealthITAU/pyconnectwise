import glob
import json
from collections import defaultdict
from pathlib import Path

from .client_gen import generate_automate_client, generate_manage_client
from .endpoint_gen import generate_endpoint, normalize_path_parameters


def capitalize_path(path):  # noqa: ANN001, ANN201
    segments = path.split("/")
    segments = [
        "{" + segment[1:] if segment.startswith("{") else segment.title()
        for segment in segments
    ]
    return "/".join(segments)


def merge_automate_specs(folder_path):  # noqa: ANN001, ANN201
    merged_spec = {
        "openapi": "3.0.0",
        "info": {"version": "v1", "title": "Merged API"},
        "paths": {},
        "components": {"requestBodies": {}, "schemas": {}},
    }
    for filename in glob.glob(f"{folder_path}/*.json"):  # noqa: PTH207
        with open(filename) as f:  # noqa: PTH123
            spec = json.load(f)

            # Merge paths
            if "paths" in spec:
                for path, path_content in spec["paths"].items():
                    tidied_path_name = capitalize_path(
                        f'/{path.replace("api", "").replace("v1", "").replace("v2", "").lstrip("/")}'
                    )
                    merged_spec["paths"][tidied_path_name] = path_content

            # Merge components
            if "components" in spec:
                if "requestBodies" in spec["components"]:
                    for req_body, req_body_content in spec["components"][
                        "requestBodies"
                    ].items():
                        merged_spec["components"]["requestBodies"][
                            req_body
                        ] = req_body_content

                if "schemas" in spec["components"]:
                    for schema, schema_content in spec["components"]["schemas"].items():
                        merged_spec["components"]["schemas"][schema] = schema_content
    with open("merged_spec.json", "w") as f:  # noqa: PTH123
        json.dump(merged_spec, f, indent=4)
    return merged_spec


def load_schema(filename: str):  # noqa: ANN201
    return json.loads(Path(filename).read_bytes())


def _pre_process_schema(schema: dict) -> list[str]:
    processed_schema = schema.copy()
    normalized_paths = {}

    for path, path_info in schema["paths"].items():
        normalized_paths[normalize_path_parameters(path)] = path_info

    processed_schema["paths"] = normalized_paths
    return processed_schema


def _parse_relationships(
    paths: list[str],
) -> [dict[str, set[str]], dict[str, set[str]]]:
    relationships = defaultdict(set)
    top_level_endpoints = defaultdict(set)

    for path in paths:
        path = normalize_path_parameters(path)
        endpoint = path.strip("/").split("/")

        # Add parent nodes to the relationships dictionary even if they have no children
        for i in range(len(endpoint)):
            parent = "/" + "/".join(endpoint[: i + 1])
            relationships[parent]  # this will initialize the set if it doesn't exist

            if i < len(endpoint) - 1:
                child = endpoint[i + 1]
                relationships[parent].add(child)

        if len(endpoint) > 1:
            top_level_endpoints[endpoint[0]].add(endpoint[1])

    return dict(relationships), dict(top_level_endpoints)


def generate_manage(
    endpoint_output_path: str,
    model_output_path: str,
    client_output_path: str,
    schema: dict,
) -> None:
    schema = _pre_process_schema(schema)
    relationships, top_level_endpoints = _parse_relationships(schema["paths"])
    client_top_level_endpoints = []
    for endpoint in relationships:
        path = f"{endpoint}"
        path_info = {}
        if schema["paths"].get(path) is not None:
            path_info = dict(schema["paths"][path].items())
        generate_endpoint(
            endpoint_output_path,
            model_output_path,
            path,
            path_info,
            relationships,
            is_manage=True,
        )

    for endpoint in top_level_endpoints:
        path = f"/{endpoint}"
        path_info = {}
        if schema["paths"].get(path) is not None:
            path_info = dict(schema["paths"][path].items())
        endpoint_class = generate_endpoint(
            endpoint_output_path,
            model_output_path,
            path,
            path_info,
            relationships,
            is_manage=True,
        )
        client_top_level_endpoints.append(endpoint_class)

    generate_manage_client(client_output_path, client_top_level_endpoints)


def generate_automate(
    endpoint_output_path: str,
    model_output_path: str,
    client_output_path: str,
    schema: dict,
) -> None:
    schema = _pre_process_schema(schema)
    relationships, top_level_endpoints = _parse_relationships(schema["paths"])
    client_top_level_endpoints = []
    for endpoint in relationships:
        path = f"{endpoint}"
        path_info = {}
        if schema["paths"].get(path) is not None:
            path_info = dict(schema["paths"][path].items())
        generate_endpoint(
            endpoint_output_path,
            model_output_path,
            path,
            path_info,
            relationships,
            is_manage=False,
        )

    for endpoint in top_level_endpoints:
        path = f"/{endpoint}"
        path_info = {}
        if schema["paths"].get(path) is not None:
            path_info = dict(schema["paths"][path].items())

        endpoint_class = generate_endpoint(
            endpoint_output_path,
            model_output_path,
            path,
            path_info,
            relationships,
            is_manage=False,
        )
        client_top_level_endpoints.append(endpoint_class)

    generate_automate_client(client_output_path, client_top_level_endpoints)
