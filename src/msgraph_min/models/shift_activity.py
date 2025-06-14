from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .schedule_entity_theme import ScheduleEntityTheme

@dataclass
class ShiftActivity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Customer defined code for the shiftActivity. Required.
    code: Optional[str] = None
    # The name of the shiftActivity. Required.
    display_name: Optional[str] = None
    # The end date and time for the shiftActivity. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Required.
    end_date_time: Optional[datetime.datetime] = None
    # Indicates whether the microsoft.graph.user should be paid for the activity during their shift. Required.
    is_paid: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The start date and time for the shiftActivity. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Required.
    start_date_time: Optional[datetime.datetime] = None
    # The theme property
    theme: Optional[ScheduleEntityTheme] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ShiftActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ShiftActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ShiftActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .schedule_entity_theme import ScheduleEntityTheme

        from .schedule_entity_theme import ScheduleEntityTheme

        fields: dict[str, Callable[[Any], None]] = {
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "isPaid": lambda n : setattr(self, 'is_paid', n.get_bool_value()),
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
        writer.write_str_value("code", self.code)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_bool_value("isPaid", self.is_paid)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("theme", self.theme)
        writer.write_additional_data_value(self.additional_data)
    

