from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SecureScoreControlStateUpdate(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Assigns the control to the user who will take the action.
    assigned_to: Optional[str] = None
    # Provides optional comment about the control.
    comment: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # State of the control, which can be modified via a PATCH command (for example, ignored, thirdParty).
    state: Optional[str] = None
    # ID of the user who updated tenant state.
    updated_by: Optional[str] = None
    # Time at which the control state was updated.
    updated_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecureScoreControlStateUpdate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecureScoreControlStateUpdate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecureScoreControlStateUpdate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_str_value()),
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "updatedBy": lambda n : setattr(self, 'updated_by', n.get_str_value()),
            "updatedDateTime": lambda n : setattr(self, 'updated_date_time', n.get_datetime_value()),
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
        writer.write_str_value("assignedTo", self.assigned_to)
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("state", self.state)
        writer.write_str_value("updatedBy", self.updated_by)
        writer.write_datetime_value("updatedDateTime", self.updated_date_time)
        writer.write_additional_data_value(self.additional_data)
    

