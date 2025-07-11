from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class OutlookGeoCoordinates(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The accuracy of the latitude and longitude. As an example, the accuracy can be measured in meters, such as the latitude and longitude are accurate to within 50 meters.
    accuracy: Optional[float] = None
    # The altitude of the location.
    altitude: Optional[float] = None
    # The accuracy of the altitude.
    altitude_accuracy: Optional[float] = None
    # The latitude of the location.
    latitude: Optional[float] = None
    # The longitude of the location.
    longitude: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OutlookGeoCoordinates:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OutlookGeoCoordinates
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OutlookGeoCoordinates()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "accuracy": lambda n : setattr(self, 'accuracy', n.get_float_value()),
            "altitude": lambda n : setattr(self, 'altitude', n.get_float_value()),
            "altitudeAccuracy": lambda n : setattr(self, 'altitude_accuracy', n.get_float_value()),
            "latitude": lambda n : setattr(self, 'latitude', n.get_float_value()),
            "longitude": lambda n : setattr(self, 'longitude', n.get_float_value()),
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
        writer.write_float_value("accuracy", self.accuracy)
        writer.write_float_value("altitude", self.altitude)
        writer.write_float_value("altitudeAccuracy", self.altitude_accuracy)
        writer.write_float_value("latitude", self.latitude)
        writer.write_float_value("longitude", self.longitude)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

