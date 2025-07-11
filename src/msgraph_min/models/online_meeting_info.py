from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .phone import Phone

@dataclass
class OnlineMeetingInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The ID of the conference.
    conference_id: Optional[str] = None
    # The external link that launches the online meeting. This is a URL that clients launch into a browser and will redirect the user to join the meeting.
    join_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # All of the phone numbers associated with this conference.
    phones: Optional[list[Phone]] = None
    # The preformatted quick dial for this call.
    quick_dial: Optional[str] = None
    # The toll free numbers that can be used to join the conference.
    toll_free_numbers: Optional[list[str]] = None
    # The toll number that can be used to join the conference.
    toll_number: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnlineMeetingInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnlineMeetingInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnlineMeetingInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .phone import Phone

        from .phone import Phone

        fields: dict[str, Callable[[Any], None]] = {
            "conferenceId": lambda n : setattr(self, 'conference_id', n.get_str_value()),
            "joinUrl": lambda n : setattr(self, 'join_url', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "phones": lambda n : setattr(self, 'phones', n.get_collection_of_object_values(Phone)),
            "quickDial": lambda n : setattr(self, 'quick_dial', n.get_str_value()),
            "tollFreeNumbers": lambda n : setattr(self, 'toll_free_numbers', n.get_collection_of_primitive_values(str)),
            "tollNumber": lambda n : setattr(self, 'toll_number', n.get_str_value()),
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
        writer.write_str_value("joinUrl", self.join_url)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("phones", self.phones)
        writer.write_str_value("quickDial", self.quick_dial)
        writer.write_collection_of_primitive_values("tollFreeNumbers", self.toll_free_numbers)
        writer.write_str_value("tollNumber", self.toll_number)
        writer.write_additional_data_value(self.additional_data)
    

