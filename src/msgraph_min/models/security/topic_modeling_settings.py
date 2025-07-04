from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TopicModelingSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Indicates whether the themes model should dynamically optimize the number of generated topics. To learn more, see Adjust maximum number of themes dynamically.
    dynamically_adjust_topic_count: Optional[bool] = None
    # Indicates whether the themes model should exclude numbers while parsing document texts. To learn more, see Include numbers in themes.
    ignore_numbers: Optional[bool] = None
    # Indicates whether themes model is enabled for the case.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The total number of topics that the themes model will generate for a review set. To learn more, see Maximum number of themes.
    topic_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TopicModelingSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TopicModelingSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TopicModelingSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "dynamicallyAdjustTopicCount": lambda n : setattr(self, 'dynamically_adjust_topic_count', n.get_bool_value()),
            "ignoreNumbers": lambda n : setattr(self, 'ignore_numbers', n.get_bool_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "topicCount": lambda n : setattr(self, 'topic_count', n.get_int_value()),
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
        writer.write_bool_value("dynamicallyAdjustTopicCount", self.dynamically_adjust_topic_count)
        writer.write_bool_value("ignoreNumbers", self.ignore_numbers)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("topicCount", self.topic_count)
        writer.write_additional_data_value(self.additional_data)
    

