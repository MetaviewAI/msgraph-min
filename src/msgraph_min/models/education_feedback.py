from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_item_body import EducationItemBody
    from .identity_set import IdentitySet

@dataclass
class EducationFeedback(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # User who created the feedback.
    feedback_by: Optional[IdentitySet] = None
    # Moment in time when the feedback was given. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    feedback_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Feedback.
    text: Optional[EducationItemBody] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationFeedback:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationFeedback
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EducationFeedback()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_item_body import EducationItemBody
        from .identity_set import IdentitySet

        from .education_item_body import EducationItemBody
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "feedbackBy": lambda n : setattr(self, 'feedback_by', n.get_object_value(IdentitySet)),
            "feedbackDateTime": lambda n : setattr(self, 'feedback_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_object_value(EducationItemBody)),
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
        writer.write_object_value("feedbackBy", self.feedback_by)
        writer.write_datetime_value("feedbackDateTime", self.feedback_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    

