from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .online_meeting_content_sharing_disabled_reason import OnlineMeetingContentSharingDisabledReason
    from .online_meeting_video_disabled_reason import OnlineMeetingVideoDisabledReason

@dataclass
class OnlineMeetingRestricted(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies the reason shared content from this participant is disabled. Possible values are: watermarkProtection, unknownFutureValue.
    content_sharing_disabled: Optional[OnlineMeetingContentSharingDisabledReason] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the reason video from this participant is disabled. Possible values are: watermarkProtection, unknownFutureValue.
    video_disabled: Optional[OnlineMeetingVideoDisabledReason] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnlineMeetingRestricted:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnlineMeetingRestricted
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnlineMeetingRestricted()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .online_meeting_content_sharing_disabled_reason import OnlineMeetingContentSharingDisabledReason
        from .online_meeting_video_disabled_reason import OnlineMeetingVideoDisabledReason

        from .online_meeting_content_sharing_disabled_reason import OnlineMeetingContentSharingDisabledReason
        from .online_meeting_video_disabled_reason import OnlineMeetingVideoDisabledReason

        fields: dict[str, Callable[[Any], None]] = {
            "contentSharingDisabled": lambda n : setattr(self, 'content_sharing_disabled', n.get_collection_of_enum_values(OnlineMeetingContentSharingDisabledReason)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "videoDisabled": lambda n : setattr(self, 'video_disabled', n.get_collection_of_enum_values(OnlineMeetingVideoDisabledReason)),
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
        writer.write_enum_value("contentSharingDisabled", self.content_sharing_disabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("videoDisabled", self.video_disabled)
        writer.write_additional_data_value(self.additional_data)
    

