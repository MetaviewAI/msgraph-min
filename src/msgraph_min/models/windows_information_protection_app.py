from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_information_protection_desktop_app import WindowsInformationProtectionDesktopApp
    from .windows_information_protection_store_app import WindowsInformationProtectionStoreApp

@dataclass
class WindowsInformationProtectionApp(AdditionalDataHolder, Parsable):
    """
    App for Windows information protection
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # If true, app is denied protection or exemption.
    denied: Optional[bool] = None
    # The app's description.
    description: Optional[str] = None
    # App display name.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The product name.
    product_name: Optional[str] = None
    # The publisher name
    publisher_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsInformationProtectionApp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionApp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionDesktopApp".casefold():
            from .windows_information_protection_desktop_app import WindowsInformationProtectionDesktopApp

            return WindowsInformationProtectionDesktopApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionStoreApp".casefold():
            from .windows_information_protection_store_app import WindowsInformationProtectionStoreApp

            return WindowsInformationProtectionStoreApp()
        return WindowsInformationProtectionApp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_information_protection_desktop_app import WindowsInformationProtectionDesktopApp
        from .windows_information_protection_store_app import WindowsInformationProtectionStoreApp

        from .windows_information_protection_desktop_app import WindowsInformationProtectionDesktopApp
        from .windows_information_protection_store_app import WindowsInformationProtectionStoreApp

        fields: dict[str, Callable[[Any], None]] = {
            "denied": lambda n : setattr(self, 'denied', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "productName": lambda n : setattr(self, 'product_name', n.get_str_value()),
            "publisherName": lambda n : setattr(self, 'publisher_name', n.get_str_value()),
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
        writer.write_bool_value("denied", self.denied)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("productName", self.product_name)
        writer.write_str_value("publisherName", self.publisher_name)
        writer.write_additional_data_value(self.additional_data)
    

