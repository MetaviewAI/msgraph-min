from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .insight_identity import InsightIdentity
    from .resource_reference import ResourceReference

@dataclass
class SharingDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The user who shared the document.
    shared_by: Optional[InsightIdentity] = None
    # The date and time the file was last shared. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    shared_date_time: Optional[datetime.datetime] = None
    # Reference properties of the document, such as the URL and type of the document. Read-only
    sharing_reference: Optional[ResourceReference] = None
    # The subject with which the document was shared.
    sharing_subject: Optional[str] = None
    # Determines the way the document was shared. Can be by a 1Link1, 1Attachment1, 1Group1, 1Site1.
    sharing_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharingDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharingDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharingDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .insight_identity import InsightIdentity
        from .resource_reference import ResourceReference

        from .insight_identity import InsightIdentity
        from .resource_reference import ResourceReference

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sharedBy": lambda n : setattr(self, 'shared_by', n.get_object_value(InsightIdentity)),
            "sharedDateTime": lambda n : setattr(self, 'shared_date_time', n.get_datetime_value()),
            "sharingReference": lambda n : setattr(self, 'sharing_reference', n.get_object_value(ResourceReference)),
            "sharingSubject": lambda n : setattr(self, 'sharing_subject', n.get_str_value()),
            "sharingType": lambda n : setattr(self, 'sharing_type', n.get_str_value()),
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
        writer.write_object_value("sharedBy", self.shared_by)
        writer.write_datetime_value("sharedDateTime", self.shared_date_time)
        writer.write_str_value("sharingSubject", self.sharing_subject)
        writer.write_str_value("sharingType", self.sharing_type)
        writer.write_additional_data_value(self.additional_data)
    

