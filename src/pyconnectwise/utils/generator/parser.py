import json
from .endpoint_gen import generate_endpoint, generate_top_level_endpoint
from .client_gen import generate_client
from collections import defaultdict
import re
from typing import List, Dict

def load_schema(filename):
    with open(filename, 'r') as f:
        schema = json.load(f)
    return schema

def generate(schema_path:str, endpoint_output_path:str, model_output_path:str, client_output_path:str):
    schema = load_schema(schema_path)
    __generate_all(endpoint_output_path, model_output_path, client_output_path, schema)
    pass

def __parse_relationships(paths: List[str]):
    relationships = defaultdict(list)
    top_level_endpoints = defaultdict(list)
    
    for path in paths:
        raw_path = path
        #path = path.replace("{id}", "Id").replace("{parentId}", "ParentId").replace('{grandparentId}', 'GrandparentId').replace('{reportName}', 'ReportName').replace('{externalId}', 'ExternalId')
        path = path.replace("{id}", "Id").replace("{parentId}", "Id").replace('{grandparentId}', 'Id').replace('{reportName}', 'Id').replace('{externalId}', 'Id')
        segments = path.split('/')
        raw_segments = raw_path.split('/')
        if len(raw_segments) >= 3:  # Check if the path depth is 2 or more
            top_level_endpoints[raw_segments[1]].append('/'.join(raw_segments[2:]))
        parent_path = '/'.join(segments[:-1])
        relationships[parent_path].append(segments[-1])

    return relationships, top_level_endpoints

def __generate_all(endpoint_output_path:str, model_output_path:str, client_output_path:str, schema:dict):
    relationships, top_level_endpoints = __parse_relationships(schema['paths'])
    models = schema['components']['schemas']
    client_top_level_endpoints = []
    for path, path_info in schema['paths'].items():
        _, endpoint_class = generate_endpoint(endpoint_output_path, model_output_path, path, path_info, relationships, models)
    
    for endpoint, children in top_level_endpoints.items():
        path = f'/{endpoint}'
        path_info = {child: schema['paths'][f'/{endpoint}/{child}'] for child in children}
        endpoint_class = generate_top_level_endpoint(endpoint_output_path, path, path_info, relationships)
        client_top_level_endpoints.append(endpoint_class)
    
    generate_client(client_output_path, client_top_level_endpoints)