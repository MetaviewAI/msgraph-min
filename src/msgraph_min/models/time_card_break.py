from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_body import ItemBody
    from .time_card_event import TimeCardEvent

@dataclass
class TimeCardBreak(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # ID of the timeCardBreak.
    break_id: Optional[str] = None
    # The start event of the timeCardBreak.
    end: Optional[TimeCardEvent] = None
    # Notes about the timeCardBreak.
    notes: Optional[ItemBody] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The start property
    start: Optional[TimeCardEvent] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimeCardBreak:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimeCardBreak
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimeCardBreak()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .item_body import ItemBody
        from .time_card_event import TimeCardEvent

        from .item_body import ItemBody
        from .time_card_event import TimeCardEvent

        fields: dict[str, Callable[[Any], None]] = {
            "breakId": lambda n : setattr(self, 'break_id', n.get_str_value()),
            "end": lambda n : setattr(self, 'end', n.get_object_value(TimeCardEvent)),
            "notes": lambda n : setattr(self, 'notes', n.get_object_value(ItemBody)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "start": lambda n : setattr(self, 'start', n.get_object_value(TimeCardEvent)),
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
        writer.write_str_value("breakId", self.break_id)
        writer.write_object_value("end", self.end)
        writer.write_object_value("notes", self.notes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("start", self.start)
        writer.write_additional_data_value(self.additional_data)
    

