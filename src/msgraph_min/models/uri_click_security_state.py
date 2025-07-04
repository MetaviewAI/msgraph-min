from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UriClickSecurityState(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The clickAction property
    click_action: Optional[str] = None
    # The clickDateTime property
    click_date_time: Optional[datetime.datetime] = None
    # The id property
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The sourceId property
    source_id: Optional[str] = None
    # The uriDomain property
    uri_domain: Optional[str] = None
    # The verdict property
    verdict: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UriClickSecurityState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UriClickSecurityState
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UriClickSecurityState()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "clickAction": lambda n : setattr(self, 'click_action', n.get_str_value()),
            "clickDateTime": lambda n : setattr(self, 'click_date_time', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
            "uriDomain": lambda n : setattr(self, 'uri_domain', n.get_str_value()),
            "verdict": lambda n : setattr(self, 'verdict', n.get_str_value()),
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
        writer.write_str_value("clickAction", self.click_action)
        writer.write_datetime_value("clickDateTime", self.click_date_time)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_str_value("uriDomain", self.uri_domain)
        writer.write_str_value("verdict", self.verdict)
        writer.write_additional_data_value(self.additional_data)
    

