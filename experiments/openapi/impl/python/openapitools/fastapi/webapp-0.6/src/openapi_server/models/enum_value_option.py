# coding: utf-8

"""
    IVOA ExecutionBroker

    Prototype implementation of the IVOA ExecutionBroker interface 

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from openapi_server.models.option_base import OptionBase
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EnumValueOption(OptionBase):
    """
    A simple enum value option. This option tells the client that they can set the enum value pointed to by the path. 
    """ # noqa: E501
    type: StrictStr
    path: StrictStr = Field(description="The target path that the option applies to. ")
    values: List[StrictStr] = Field(description="The list of allowed values to use. ")
    __properties: ClassVar[List[str]] = ["type", "path", "values"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EnumValueOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EnumValueOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "path": obj.get("path"),
            "values": obj.get("values")
        })
        return _obj


