from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .day_of_week import DayOfWeek
    from .time_zone_base import TimeZoneBase

@dataclass
class WorkingHours(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The days of the week on which the user works.
    days_of_week: Optional[list[DayOfWeek]] = None
    # The time of the day that the user stops working.
    end_time: Optional[datetime.time] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The time of the day that the user starts working.
    start_time: Optional[datetime.time] = None
    # The time zone to which the working hours apply.
    time_zone: Optional[TimeZoneBase] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkingHours:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkingHours
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkingHours()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .day_of_week import DayOfWeek
        from .time_zone_base import TimeZoneBase

        from .day_of_week import DayOfWeek
        from .time_zone_base import TimeZoneBase

        fields: dict[str, Callable[[Any], None]] = {
            "daysOfWeek": lambda n : setattr(self, 'days_of_week', n.get_collection_of_enum_values(DayOfWeek)),
            "endTime": lambda n : setattr(self, 'end_time', n.get_time_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startTime": lambda n : setattr(self, 'start_time', n.get_time_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_object_value(TimeZoneBase)),
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
        writer.write_collection_of_enum_values("daysOfWeek", self.days_of_week)
        writer.write_time_value("endTime", self.end_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_time_value("startTime", self.start_time)
        writer.write_object_value("timeZone", self.time_zone)
        writer.write_additional_data_value(self.additional_data)
    

