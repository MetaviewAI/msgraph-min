from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tone import Tone

@dataclass
class ToneInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # An incremental identifier used for ordering DTMF events.
    sequence_id: Optional[int] = None
    # The tone property
    tone: Optional[Tone] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ToneInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ToneInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ToneInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tone import Tone

        from .tone import Tone

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sequenceId": lambda n : setattr(self, 'sequence_id', n.get_int_value()),
            "tone": lambda n : setattr(self, 'tone', n.get_enum_value(Tone)),
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
        writer.write_int_value("sequenceId", self.sequence_id)
        writer.write_enum_value("tone", self.tone)
        writer.write_additional_data_value(self.additional_data)
    

