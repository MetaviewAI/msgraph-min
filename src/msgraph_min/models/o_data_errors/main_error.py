from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .error_details import ErrorDetails
    from .inner_error import InnerError

@dataclass
class MainError(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The code property
    code: Optional[str] = None
    # The details property
    details: Optional[list[ErrorDetails]] = None
    # The innerError property
    inner_error: Optional[InnerError] = None
    # The message property
    message: Optional[str] = None
    # The target property
    target: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MainError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MainError
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MainError()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .error_details import ErrorDetails
        from .inner_error import InnerError

        from .error_details import ErrorDetails
        from .inner_error import InnerError

        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_collection_of_object_values(ErrorDetails)),
            "innerError": lambda n : setattr(self, 'inner_error', n.get_object_value(InnerError)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("code", self.code)
        writer.write_collection_of_object_values("details", self.details)
        writer.write_object_value("innerError", self.inner_error)
        writer.write_str_value("message", self.message)
        writer.write_str_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    

