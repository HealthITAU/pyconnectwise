import json
import argparse

def normalize_schema_name(schema_name):
    """Extracts the part of the schema name after the last dot."""
    split = schema_name.split('.')
    if len(split) >= 2:
        return split[0]+split[-1]
    return ''.join(schema_name.split('.'))

def update_schema_references(data, name_mapping):
    """Updates all $ref entries with the new names from the name_mapping."""
    if isinstance(data, dict):
        for key, value in data.items():
            if key == '$ref':
                # Extract schema name from the reference
                ref_schema_name = value.split('/')[-1]
                # Update the reference if the schema name is in name_mapping
                if ref_schema_name in name_mapping:
                    data[key] = value.replace(ref_schema_name, name_mapping[ref_schema_name])
            else:
                update_schema_references(value, name_mapping)
    elif isinstance(data, list):
        for item in data:
            update_schema_references(item, name_mapping)

def main():
    # Parsing command-line arguments
    parser = argparse.ArgumentParser(description='Normalize OpenAPI JSON schema names.')
    parser.add_argument('--input', type=str, required=True, help='Path to the OpenAPI JSON file.')
    args = parser.parse_args()

    # Loading the JSON file
    with open(args.input, 'r') as file:
        data = json.load(file)

    # Normalizing schema names and storing the old-new name mapping
    name_mapping = {}
    schemas = data.get('components', {}).get('schemas', {})
    for schema_name in list(schemas.keys()):
        new_name = normalize_schema_name(schema_name)
        name_mapping[schema_name] = new_name
        schemas[new_name] = schemas.pop(schema_name)

    # Updating all path references
    update_schema_references(data, name_mapping)

    # Writing the updated JSON back to the file
    with open(args.input, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    main()
