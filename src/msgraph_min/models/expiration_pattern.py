from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .expiration_pattern_type import ExpirationPatternType

@dataclass
class ExpirationPattern(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The requestor's desired duration of access represented in ISO 8601 format for durations. For example, PT3H refers to three hours.  If specified in a request, endDateTime should not be present and the type property should be set to afterDuration.
    duration: Optional[datetime.timedelta] = None
    # Timestamp of date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    end_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The requestor's desired expiration pattern type. The possible values are: notSpecified, noExpiration, afterDateTime, afterDuration.
    type: Optional[ExpirationPatternType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExpirationPattern:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExpirationPattern
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExpirationPattern()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .expiration_pattern_type import ExpirationPatternType

        from .expiration_pattern_type import ExpirationPatternType

        fields: dict[str, Callable[[Any], None]] = {
            "duration": lambda n : setattr(self, 'duration', n.get_timedelta_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(ExpirationPatternType)),
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
        writer.write_timedelta_value("duration", self.duration)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

