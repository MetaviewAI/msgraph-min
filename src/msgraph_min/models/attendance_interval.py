from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AttendanceInterval(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Duration of the meeting interval in seconds; that is, the difference between joinDateTime and leaveDateTime.
    duration_in_seconds: Optional[int] = None
    # The time the attendee joined in UTC.
    join_date_time: Optional[datetime.datetime] = None
    # The time the attendee left in UTC.
    leave_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AttendanceInterval:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttendanceInterval
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AttendanceInterval()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "durationInSeconds": lambda n : setattr(self, 'duration_in_seconds', n.get_int_value()),
            "joinDateTime": lambda n : setattr(self, 'join_date_time', n.get_datetime_value()),
            "leaveDateTime": lambda n : setattr(self, 'leave_date_time', n.get_datetime_value()),
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
        writer.write_int_value("durationInSeconds", self.duration_in_seconds)
        writer.write_datetime_value("joinDateTime", self.join_date_time)
        writer.write_datetime_value("leaveDateTime", self.leave_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

