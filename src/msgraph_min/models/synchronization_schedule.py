from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .synchronization_schedule_state import SynchronizationScheduleState

@dataclass
class SynchronizationSchedule(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Date and time when this job expires. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    expiration: Optional[datetime.datetime] = None
    # The interval between synchronization iterations. The value is represented in ISO 8601  format for durations. For example, P1M represents a period of one month and PT1M represents a period of one minute.
    interval: Optional[datetime.timedelta] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state property
    state: Optional[SynchronizationScheduleState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SynchronizationSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationSchedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationSchedule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .synchronization_schedule_state import SynchronizationScheduleState

        from .synchronization_schedule_state import SynchronizationScheduleState

        fields: dict[str, Callable[[Any], None]] = {
            "expiration": lambda n : setattr(self, 'expiration', n.get_datetime_value()),
            "interval": lambda n : setattr(self, 'interval', n.get_timedelta_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(SynchronizationScheduleState)),
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
        writer.write_datetime_value("expiration", self.expiration)
        writer.write_timedelta_value("interval", self.interval)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

