from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .daylight_time_zone_offset import DaylightTimeZoneOffset
    from .day_of_week import DayOfWeek

@dataclass
class StandardTimeZoneOffset(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Represents the nth occurrence of the day of week that the transition from daylight saving time to standard time occurs.
    day_occurrence: Optional[int] = None
    # Represents the day of the week when the transition from daylight saving time to standard time.
    day_of_week: Optional[DayOfWeek] = None
    # Represents the month of the year when the transition from daylight saving time to standard time occurs.
    month: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the time of day when the transition from daylight saving time to standard time occurs.
    time: Optional[datetime.time] = None
    # Represents how frequently in terms of years the change from daylight saving time to standard time occurs. For example, a value of 0 means every year.
    year: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StandardTimeZoneOffset:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StandardTimeZoneOffset
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.daylightTimeZoneOffset".casefold():
            from .daylight_time_zone_offset import DaylightTimeZoneOffset

            return DaylightTimeZoneOffset()
        return StandardTimeZoneOffset()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .daylight_time_zone_offset import DaylightTimeZoneOffset
        from .day_of_week import DayOfWeek

        from .daylight_time_zone_offset import DaylightTimeZoneOffset
        from .day_of_week import DayOfWeek

        fields: dict[str, Callable[[Any], None]] = {
            "dayOccurrence": lambda n : setattr(self, 'day_occurrence', n.get_int_value()),
            "dayOfWeek": lambda n : setattr(self, 'day_of_week', n.get_enum_value(DayOfWeek)),
            "month": lambda n : setattr(self, 'month', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "time": lambda n : setattr(self, 'time', n.get_time_value()),
            "year": lambda n : setattr(self, 'year', n.get_int_value()),
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
        writer.write_int_value("dayOccurrence", self.day_occurrence)
        writer.write_enum_value("dayOfWeek", self.day_of_week)
        writer.write_int_value("month", self.month)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_time_value("time", self.time)
        writer.write_int_value("year", self.year)
        writer.write_additional_data_value(self.additional_data)
    

