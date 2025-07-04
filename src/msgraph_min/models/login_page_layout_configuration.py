from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .layout_template_type import LayoutTemplateType

@dataclass
class LoginPageLayoutConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Option to show the footer on the sign-in page.
    is_footer_shown: Optional[bool] = None
    # Option to show the header on the sign-in page.
    is_header_shown: Optional[bool] = None
    # Represents the layout template to be displayed on the login page for a tenant. The possible values are  default - Represents the default Microsoft layout with a centered lightbox.  verticalSplit - Represents a layout with a background on the left side and a full-height lightbox to the right.  unknownFutureValue - Evolvable enumeration sentinel value. Don't use.
    layout_template_type: Optional[LayoutTemplateType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LoginPageLayoutConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LoginPageLayoutConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LoginPageLayoutConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .layout_template_type import LayoutTemplateType

        from .layout_template_type import LayoutTemplateType

        fields: dict[str, Callable[[Any], None]] = {
            "isFooterShown": lambda n : setattr(self, 'is_footer_shown', n.get_bool_value()),
            "isHeaderShown": lambda n : setattr(self, 'is_header_shown', n.get_bool_value()),
            "layoutTemplateType": lambda n : setattr(self, 'layout_template_type', n.get_enum_value(LayoutTemplateType)),
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
        writer.write_bool_value("isFooterShown", self.is_footer_shown)
        writer.write_bool_value("isHeaderShown", self.is_header_shown)
        writer.write_enum_value("layoutTemplateType", self.layout_template_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

