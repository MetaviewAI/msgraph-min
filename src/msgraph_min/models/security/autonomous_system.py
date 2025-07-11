from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AutonomousSystem(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The name of the autonomous system.
    name: Optional[str] = None
    # The autonomous system number, assigned by IANA.
    number: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The name of the autonomous system organization.
    organization: Optional[str] = None
    # A displayable value for these autonomous system details.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutonomousSystem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutonomousSystem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutonomousSystem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "number": lambda n : setattr(self, 'number', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organization": lambda n : setattr(self, 'organization', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("name", self.name)
        writer.write_int_value("number", self.number)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("organization", self.organization)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

