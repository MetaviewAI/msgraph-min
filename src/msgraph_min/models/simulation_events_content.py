from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .simulation_event import SimulationEvent

@dataclass
class SimulationEventsContent(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Actual percentage of users who fell for the simulated attack in an attack simulation and training campaign.
    compromised_rate: Optional[float] = None
    # List of simulation events in an attack simulation and training campaign.
    events: Optional[list[SimulationEvent]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SimulationEventsContent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SimulationEventsContent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SimulationEventsContent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .simulation_event import SimulationEvent

        from .simulation_event import SimulationEvent

        fields: dict[str, Callable[[Any], None]] = {
            "compromisedRate": lambda n : setattr(self, 'compromised_rate', n.get_float_value()),
            "events": lambda n : setattr(self, 'events', n.get_collection_of_object_values(SimulationEvent)),
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
        writer.write_float_value("compromisedRate", self.compromised_rate)
        writer.write_collection_of_object_values("events", self.events)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

