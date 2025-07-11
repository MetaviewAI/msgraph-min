from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ReferencedObject(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the referenced object. Must match one of the objects in the directory definition.
    referenced_object_name: Optional[str] = None
    # Currently not supported. Name of the property in the referenced object, the value for which is used as the reference.
    referenced_property: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ReferencedObject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReferencedObject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ReferencedObject()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "referencedObjectName": lambda n : setattr(self, 'referenced_object_name', n.get_str_value()),
            "referencedProperty": lambda n : setattr(self, 'referenced_property', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("referencedObjectName", self.referenced_object_name)
        writer.write_str_value("referencedProperty", self.referenced_property)
        writer.write_additional_data_value(self.additional_data)
    

