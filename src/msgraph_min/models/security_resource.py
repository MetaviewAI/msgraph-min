from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .security_resource_type import SecurityResourceType

@dataclass
class SecurityResource(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Name of the resource that is related to current alert. Required.
    resource: Optional[str] = None
    # Represents type of security resources related to an alert. Possible values are: attacked, related.
    resource_type: Optional[SecurityResourceType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .security_resource_type import SecurityResourceType

        from .security_resource_type import SecurityResourceType

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_str_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_enum_value(SecurityResourceType)),
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
        writer.write_str_value("resource", self.resource)
        writer.write_enum_value("resourceType", self.resource_type)
        writer.write_additional_data_value(self.additional_data)
    

