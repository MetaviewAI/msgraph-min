from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RubricQualitySelectedColumnModel(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # ID of the selected level for this quality.
    column_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # ID of the associated quality.
    quality_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RubricQualitySelectedColumnModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RubricQualitySelectedColumnModel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RubricQualitySelectedColumnModel()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "columnId": lambda n : setattr(self, 'column_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "qualityId": lambda n : setattr(self, 'quality_id', n.get_str_value()),
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
        writer.write_str_value("columnId", self.column_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("qualityId", self.quality_id)
        writer.write_additional_data_value(self.additional_data)
    

