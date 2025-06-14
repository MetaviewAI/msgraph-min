from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .simulation_report_overview import SimulationReportOverview
    from .user_simulation_details import UserSimulationDetails

@dataclass
class SimulationReport(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Overview of an attack simulation and training campaign.
    overview: Optional[SimulationReportOverview] = None
    # The tenant users and their online actions in an attack simulation and training campaign.
    simulation_users: Optional[list[UserSimulationDetails]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SimulationReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SimulationReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SimulationReport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .simulation_report_overview import SimulationReportOverview
        from .user_simulation_details import UserSimulationDetails

        from .simulation_report_overview import SimulationReportOverview
        from .user_simulation_details import UserSimulationDetails

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "overview": lambda n : setattr(self, 'overview', n.get_object_value(SimulationReportOverview)),
            "simulationUsers": lambda n : setattr(self, 'simulation_users', n.get_collection_of_object_values(UserSimulationDetails)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("overview", self.overview)
        writer.write_collection_of_object_values("simulationUsers", self.simulation_users)
        writer.write_additional_data_value(self.additional_data)
    

