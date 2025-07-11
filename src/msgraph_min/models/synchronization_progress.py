from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SynchronizationProgress(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The numerator of a progress ratio; the number of units of changes already processed.
    completed_units: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The time of a progress observation as an offset in minutes from UTC.
    progress_observation_date_time: Optional[datetime.datetime] = None
    # The denominator of a progress ratio; a number of units of changes to be processed to accomplish synchronization.
    total_units: Optional[int] = None
    # An optional description of the units.
    units: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SynchronizationProgress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationProgress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationProgress()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "completedUnits": lambda n : setattr(self, 'completed_units', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "progressObservationDateTime": lambda n : setattr(self, 'progress_observation_date_time', n.get_datetime_value()),
            "totalUnits": lambda n : setattr(self, 'total_units', n.get_int_value()),
            "units": lambda n : setattr(self, 'units', n.get_str_value()),
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
        writer.write_int_value("completedUnits", self.completed_units)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("progressObservationDateTime", self.progress_observation_date_time)
        writer.write_int_value("totalUnits", self.total_units)
        writer.write_str_value("units", self.units)
        writer.write_additional_data_value(self.additional_data)
    

