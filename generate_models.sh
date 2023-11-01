#!/bin/bash
source venv/scripts/activate

echo Enter JSON path
read jsonPath
echo Enter output filename/directory
read output

datamodel-codegen --input ${jsonPath} --output ${output} --target-python-version 3.10 --collapse-root-models --reuse-model --output-model-type pydantic_v2.BaseModel --base-class pyconnectwise.models.base.connectwise_model.ConnectWiseModel --use-union-operator --use-field-description --use-default --snake-case-field --disable-timestamp --use-standard-collections --use-schema-description --remove-special-field-name-prefix --capitalise-enum-members --set-default-enum-member --enum-field-as-literal all --use-default-kwarg --field-constraints
