from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .root import Root
    from .site_archival_details import SiteArchivalDetails

@dataclass
class SiteCollection(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Represents whether the site collection is recently archived, fully archived, or reactivating. Possible values are: recentlyArchived, fullyArchived, reactivating, unknownFutureValue.
    archival_details: Optional[SiteArchivalDetails] = None
    # The geographic region code for where this site collection resides. Only present for multi-geo tenants. Read-only.
    data_location_code: Optional[str] = None
    # The hostname for the site collection. Read-only.
    hostname: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If present, indicates that this is a root site collection in SharePoint. Read-only.
    root: Optional[Root] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SiteCollection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SiteCollection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SiteCollection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .root import Root
        from .site_archival_details import SiteArchivalDetails

        from .root import Root
        from .site_archival_details import SiteArchivalDetails

        fields: dict[str, Callable[[Any], None]] = {
            "archivalDetails": lambda n : setattr(self, 'archival_details', n.get_object_value(SiteArchivalDetails)),
            "dataLocationCode": lambda n : setattr(self, 'data_location_code', n.get_str_value()),
            "hostname": lambda n : setattr(self, 'hostname', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "root": lambda n : setattr(self, 'root', n.get_object_value(Root)),
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
        writer.write_object_value("archivalDetails", self.archival_details)
        writer.write_str_value("dataLocationCode", self.data_location_code)
        writer.write_str_value("hostname", self.hostname)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("root", self.root)
        writer.write_additional_data_value(self.additional_data)
    

