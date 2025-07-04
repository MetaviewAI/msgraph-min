from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .open_shift_item import OpenShiftItem
    from .schedule_entity_theme import ScheduleEntityTheme
    from .shift_item import ShiftItem
    from .time_off_item import TimeOffItem

@dataclass
class ScheduleEntity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The endDateTime property
    end_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The startDateTime property
    start_date_time: Optional[datetime.datetime] = None
    # The theme property
    theme: Optional[ScheduleEntityTheme] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ScheduleEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScheduleEntity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShiftItem".casefold():
            from .open_shift_item import OpenShiftItem

            return OpenShiftItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.shiftItem".casefold():
            from .shift_item import ShiftItem

            return ShiftItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOffItem".casefold():
            from .time_off_item import TimeOffItem

            return TimeOffItem()
        return ScheduleEntity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .open_shift_item import OpenShiftItem
        from .schedule_entity_theme import ScheduleEntityTheme
        from .shift_item import ShiftItem
        from .time_off_item import TimeOffItem

        from .open_shift_item import OpenShiftItem
        from .schedule_entity_theme import ScheduleEntityTheme
        from .shift_item import ShiftItem
        from .time_off_item import TimeOffItem

        fields: dict[str, Callable[[Any], None]] = {
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "theme": lambda n : setattr(self, 'theme', n.get_enum_value(ScheduleEntityTheme)),
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
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("theme", self.theme)
        writer.write_additional_data_value(self.additional_data)
    

