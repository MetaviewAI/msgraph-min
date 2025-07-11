from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TeamMessagingSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # If set to true, @channel mentions are allowed.
    allow_channel_mentions: Optional[bool] = None
    # If set to true, owners can delete any message.
    allow_owner_delete_messages: Optional[bool] = None
    # If set to true, @team mentions are allowed.
    allow_team_mentions: Optional[bool] = None
    # If set to true, users can delete their messages.
    allow_user_delete_messages: Optional[bool] = None
    # If set to true, users can edit their messages.
    allow_user_edit_messages: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamMessagingSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamMessagingSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamMessagingSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowChannelMentions": lambda n : setattr(self, 'allow_channel_mentions', n.get_bool_value()),
            "allowOwnerDeleteMessages": lambda n : setattr(self, 'allow_owner_delete_messages', n.get_bool_value()),
            "allowTeamMentions": lambda n : setattr(self, 'allow_team_mentions', n.get_bool_value()),
            "allowUserDeleteMessages": lambda n : setattr(self, 'allow_user_delete_messages', n.get_bool_value()),
            "allowUserEditMessages": lambda n : setattr(self, 'allow_user_edit_messages', n.get_bool_value()),
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
        writer.write_bool_value("allowChannelMentions", self.allow_channel_mentions)
        writer.write_bool_value("allowOwnerDeleteMessages", self.allow_owner_delete_messages)
        writer.write_bool_value("allowTeamMentions", self.allow_team_mentions)
        writer.write_bool_value("allowUserDeleteMessages", self.allow_user_delete_messages)
        writer.write_bool_value("allowUserEditMessages", self.allow_user_edit_messages)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

