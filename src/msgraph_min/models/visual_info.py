from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .image_info import ImageInfo

@dataclass
class VisualInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Optional. JSON object used to represent an icon which represents the application used to generate the activity
    attribution: Optional[ImageInfo] = None
    # Optional. Background color used to render the activity in the UI - brand color for the application source of the activity. Must be a valid hex color
    background_color: Optional[str] = None
    # Optional. Longer text description of the user's unique activity (example: document name, first sentence, and/or metadata)
    description: Optional[str] = None
    # Required. Short text description of the user's unique activity (for example, document name in cases where an activity refers to document creation)
    display_text: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VisualInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VisualInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VisualInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .image_info import ImageInfo

        from .image_info import ImageInfo

        fields: dict[str, Callable[[Any], None]] = {
            "attribution": lambda n : setattr(self, 'attribution', n.get_object_value(ImageInfo)),
            "backgroundColor": lambda n : setattr(self, 'background_color', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayText": lambda n : setattr(self, 'display_text', n.get_str_value()),
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
        writer.write_object_value("attribution", self.attribution)
        writer.write_str_value("backgroundColor", self.background_color)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayText", self.display_text)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

