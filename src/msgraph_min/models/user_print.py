from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .printer_share import PrinterShare

@dataclass
class UserPrint(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The recentPrinterShares property
    recent_printer_shares: Optional[list[PrinterShare]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserPrint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserPrint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserPrint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .printer_share import PrinterShare

        from .printer_share import PrinterShare

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recentPrinterShares": lambda n : setattr(self, 'recent_printer_shares', n.get_collection_of_object_values(PrinterShare)),
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
        writer.write_collection_of_object_values("recentPrinterShares", self.recent_printer_shares)
        writer.write_additional_data_value(self.additional_data)
    

