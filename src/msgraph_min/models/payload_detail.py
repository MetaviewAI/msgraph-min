from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_payload_detail import EmailPayloadDetail
    from .payload_coachmark import PayloadCoachmark

@dataclass
class PayloadDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The coachmarks property
    coachmarks: Optional[list[PayloadCoachmark]] = None
    # Payload content details.
    content: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The phishing URL used to target a user.
    phishing_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PayloadDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PayloadDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailPayloadDetail".casefold():
            from .email_payload_detail import EmailPayloadDetail

            return EmailPayloadDetail()
        return PayloadDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_payload_detail import EmailPayloadDetail
        from .payload_coachmark import PayloadCoachmark

        from .email_payload_detail import EmailPayloadDetail
        from .payload_coachmark import PayloadCoachmark

        fields: dict[str, Callable[[Any], None]] = {
            "coachmarks": lambda n : setattr(self, 'coachmarks', n.get_collection_of_object_values(PayloadCoachmark)),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "phishingUrl": lambda n : setattr(self, 'phishing_url', n.get_str_value()),
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
        writer.write_collection_of_object_values("coachmarks", self.coachmarks)
        writer.write_str_value("content", self.content)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("phishingUrl", self.phishing_url)
        writer.write_additional_data_value(self.additional_data)
    

