from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .external_link import ExternalLink

@dataclass
class PageLinks(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Opens the page in the OneNote native client if it's installed.
    one_note_client_url: Optional[ExternalLink] = None
    # Opens the page in OneNote on the web.
    one_note_web_url: Optional[ExternalLink] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PageLinks:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PageLinks
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PageLinks()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .external_link import ExternalLink

        from .external_link import ExternalLink

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "oneNoteClientUrl": lambda n : setattr(self, 'one_note_client_url', n.get_object_value(ExternalLink)),
            "oneNoteWebUrl": lambda n : setattr(self, 'one_note_web_url', n.get_object_value(ExternalLink)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("oneNoteClientUrl", self.one_note_client_url)
        writer.write_object_value("oneNoteWebUrl", self.one_note_web_url)
        writer.write_additional_data_value(self.additional_data)
    

