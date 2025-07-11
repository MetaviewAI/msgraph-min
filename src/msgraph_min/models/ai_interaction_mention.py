from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet

@dataclass
class AiInteractionMention(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The mentionId property
    mention_id: Optional[int] = None
    # The mentionText property
    mention_text: Optional[str] = None
    # The mentioned property
    mentioned: Optional[AiInteractionMentionedIdentitySet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AiInteractionMention:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AiInteractionMention
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AiInteractionMention()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet

        from .ai_interaction_mentioned_identity_set import AiInteractionMentionedIdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "mentionId": lambda n : setattr(self, 'mention_id', n.get_int_value()),
            "mentionText": lambda n : setattr(self, 'mention_text', n.get_str_value()),
            "mentioned": lambda n : setattr(self, 'mentioned', n.get_object_value(AiInteractionMentionedIdentitySet)),
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
        writer.write_int_value("mentionId", self.mention_id)
        writer.write_str_value("mentionText", self.mention_text)
        writer.write_object_value("mentioned", self.mentioned)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

