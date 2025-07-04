from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AudioConferencing(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The conference id of the online meeting.
    conference_id: Optional[str] = None
    # A URL to the externally-accessible web page that contains dial-in information.
    dialin_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The toll-free number that connects to the Audio Conference Provider.
    toll_free_number: Optional[str] = None
    # List of toll-free numbers that are displayed in the meeting invite.
    toll_free_numbers: Optional[list[str]] = None
    # The toll number that connects to the Audio Conference Provider.
    toll_number: Optional[str] = None
    # List of toll numbers that are displayed in the meeting invite.
    toll_numbers: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AudioConferencing:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AudioConferencing
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AudioConferencing()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "conferenceId": lambda n : setattr(self, 'conference_id', n.get_str_value()),
            "dialinUrl": lambda n : setattr(self, 'dialin_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tollFreeNumber": lambda n : setattr(self, 'toll_free_number', n.get_str_value()),
            "tollFreeNumbers": lambda n : setattr(self, 'toll_free_numbers', n.get_collection_of_primitive_values(str)),
            "tollNumber": lambda n : setattr(self, 'toll_number', n.get_str_value()),
            "tollNumbers": lambda n : setattr(self, 'toll_numbers', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("conferenceId", self.conference_id)
        writer.write_str_value("dialinUrl", self.dialin_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("tollFreeNumber", self.toll_free_number)
        writer.write_collection_of_primitive_values("tollFreeNumbers", self.toll_free_numbers)
        writer.write_str_value("tollNumber", self.toll_number)
        writer.write_collection_of_primitive_values("tollNumbers", self.toll_numbers)
        writer.write_additional_data_value(self.additional_data)
    

