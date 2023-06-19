from enum import Enum
from typing import Any
import json


class Patch:
    class PatchOp(Enum):
        """
        PatchOperation is an enumeration of the different patch operations supported
        by the ConnectWise API. These operations are ADD, REPLACE, and REMOVE.
        """

        ADD = 1
        REPLACE = 2
        REMOVE = 3

    def __init__(self, op: PatchOp, path: str, value: Any):
        self.op = op.name.lower()
        self.path = path
        self.value = value

    def __repr__(self) -> str:
        """
        Return a string representation of the model as a formatted JSON string.

        Returns:
            str: A formatted JSON string representation of the model.
        """
        return json.dumps(self.__dict__, default=str, indent=2)


class PatchGroup:
    def __init__(self, *patches: Patch) -> None:
        self.patches = list(patches)

    def __repr__(self) -> str:
        return str(self.patches)
