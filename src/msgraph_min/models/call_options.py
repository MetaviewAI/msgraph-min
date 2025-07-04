from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .incoming_call_options import IncomingCallOptions
    from .outgoing_call_options import OutgoingCallOptions

@dataclass
class CallOptions(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether to hide the app after the call is escalated.
    hide_bot_after_escalation: Optional[bool] = None
    # Indicates whether content sharing notifications should be enabled for the call.
    is_content_sharing_notification_enabled: Optional[bool] = None
    # Indicates whether delta roster is enabled for the call.
    is_delta_roster_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CallOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.incomingCallOptions".casefold():
            from .incoming_call_options import IncomingCallOptions

            return IncomingCallOptions()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outgoingCallOptions".casefold():
            from .outgoing_call_options import OutgoingCallOptions

            return OutgoingCallOptions()
        return CallOptions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .incoming_call_options import IncomingCallOptions
        from .outgoing_call_options import OutgoingCallOptions

        from .incoming_call_options import IncomingCallOptions
        from .outgoing_call_options import OutgoingCallOptions

        fields: dict[str, Callable[[Any], None]] = {
            "hideBotAfterEscalation": lambda n : setattr(self, 'hide_bot_after_escalation', n.get_bool_value()),
            "isContentSharingNotificationEnabled": lambda n : setattr(self, 'is_content_sharing_notification_enabled', n.get_bool_value()),
            "isDeltaRosterEnabled": lambda n : setattr(self, 'is_delta_roster_enabled', n.get_bool_value()),
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
        writer.write_bool_value("hideBotAfterEscalation", self.hide_bot_after_escalation)
        writer.write_bool_value("isContentSharingNotificationEnabled", self.is_content_sharing_notification_enabled)
        writer.write_bool_value("isDeltaRosterEnabled", self.is_delta_roster_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

