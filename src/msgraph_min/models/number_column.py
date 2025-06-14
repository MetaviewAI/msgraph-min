from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class NumberColumn(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # How many decimal places to display. See below for information about the possible values.
    decimal_places: Optional[str] = None
    # How the value should be presented in the UX. Must be one of number or percentage. If unspecified, treated as number.
    display_as: Optional[str] = None
    # The maximum permitted value.
    maximum: Optional[float] = None
    # The minimum permitted value.
    minimum: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NumberColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NumberColumn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NumberColumn()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "decimalPlaces": lambda n : setattr(self, 'decimal_places', n.get_str_value()),
            "displayAs": lambda n : setattr(self, 'display_as', n.get_str_value()),
            "maximum": lambda n : setattr(self, 'maximum', n.get_float_value()),
            "minimum": lambda n : setattr(self, 'minimum', n.get_float_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("decimalPlaces", self.decimal_places)
        writer.write_str_value("displayAs", self.display_as)
        writer.write_float_value("maximum", self.maximum)
        writer.write_float_value("minimum", self.minimum)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

