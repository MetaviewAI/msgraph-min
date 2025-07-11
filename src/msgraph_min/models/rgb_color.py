from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RgbColor(AdditionalDataHolder, Parsable):
    """
    Color in RGB.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Blue value
    b: Optional[int] = None
    # Green value
    g: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Red value
    r: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RgbColor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RgbColor
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RgbColor()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "b": lambda n : setattr(self, 'b', n.get_int_value()),
            "g": lambda n : setattr(self, 'g', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "r": lambda n : setattr(self, 'r', n.get_int_value()),
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
        writer.write_int_value("b", self.b)
        writer.write_int_value("g", self.g)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("r", self.r)
        writer.write_additional_data_value(self.additional_data)
    

