from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .broadcast_meeting_audience import BroadcastMeetingAudience
    from .broadcast_meeting_caption_settings import BroadcastMeetingCaptionSettings

@dataclass
class BroadcastMeetingSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Defines who can join the Teams live event. Possible values are listed in the following table.
    allowed_audience: Optional[BroadcastMeetingAudience] = None
    # Caption settings of a Teams live event.
    captions: Optional[BroadcastMeetingCaptionSettings] = None
    # Indicates whether attendee report is enabled for this Teams live event. Default value is false.
    is_attendee_report_enabled: Optional[bool] = None
    # Indicates whether Q&A is enabled for this Teams live event. Default value is false.
    is_question_and_answer_enabled: Optional[bool] = None
    # Indicates whether recording is enabled for this Teams live event. Default value is false.
    is_recording_enabled: Optional[bool] = None
    # Indicates whether video on demand is enabled for this Teams live event. Default value is false.
    is_video_on_demand_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BroadcastMeetingSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BroadcastMeetingSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BroadcastMeetingSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .broadcast_meeting_audience import BroadcastMeetingAudience
        from .broadcast_meeting_caption_settings import BroadcastMeetingCaptionSettings

        from .broadcast_meeting_audience import BroadcastMeetingAudience
        from .broadcast_meeting_caption_settings import BroadcastMeetingCaptionSettings

        fields: dict[str, Callable[[Any], None]] = {
            "allowedAudience": lambda n : setattr(self, 'allowed_audience', n.get_enum_value(BroadcastMeetingAudience)),
            "captions": lambda n : setattr(self, 'captions', n.get_object_value(BroadcastMeetingCaptionSettings)),
            "isAttendeeReportEnabled": lambda n : setattr(self, 'is_attendee_report_enabled', n.get_bool_value()),
            "isQuestionAndAnswerEnabled": lambda n : setattr(self, 'is_question_and_answer_enabled', n.get_bool_value()),
            "isRecordingEnabled": lambda n : setattr(self, 'is_recording_enabled', n.get_bool_value()),
            "isVideoOnDemandEnabled": lambda n : setattr(self, 'is_video_on_demand_enabled', n.get_bool_value()),
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
        writer.write_enum_value("allowedAudience", self.allowed_audience)
        writer.write_object_value("captions", self.captions)
        writer.write_bool_value("isAttendeeReportEnabled", self.is_attendee_report_enabled)
        writer.write_bool_value("isQuestionAndAnswerEnabled", self.is_question_and_answer_enabled)
        writer.write_bool_value("isRecordingEnabled", self.is_recording_enabled)
        writer.write_bool_value("isVideoOnDemandEnabled", self.is_video_on_demand_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

