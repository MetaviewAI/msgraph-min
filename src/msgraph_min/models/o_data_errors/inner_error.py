from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class InnerError(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Client request Id as sent by the client application.
    client_request_id: Optional[str] = None
    # Date when the error occured.
    date: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Request Id as tracked internally by the service
    request_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InnerError:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InnerError
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InnerError()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "client-request-id": lambda n : setattr(self, 'client_request_id', n.get_str_value()),
            "date": lambda n : setattr(self, 'date', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "request-id": lambda n : setattr(self, 'request_id', n.get_str_value()),
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
        writer.write_str_value("client-request-id", self.client_request_id)
        writer.write_datetime_value("date", self.date)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("request-id", self.request_id)
        writer.write_additional_data_value(self.additional_data)
    

