from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teams_app_resource_specific_permission_type import TeamsAppResourceSpecificPermissionType

@dataclass
class TeamsAppResourceSpecificPermission(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The type of resource-specific permission.
    permission_type: Optional[TeamsAppResourceSpecificPermissionType] = None
    # The name of the resource-specific permission.
    permission_value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamsAppResourceSpecificPermission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamsAppResourceSpecificPermission
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamsAppResourceSpecificPermission()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .teams_app_resource_specific_permission_type import TeamsAppResourceSpecificPermissionType

        from .teams_app_resource_specific_permission_type import TeamsAppResourceSpecificPermissionType

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permissionType": lambda n : setattr(self, 'permission_type', n.get_enum_value(TeamsAppResourceSpecificPermissionType)),
            "permissionValue": lambda n : setattr(self, 'permission_value', n.get_str_value()),
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
        writer.write_enum_value("permissionType", self.permission_type)
        writer.write_str_value("permissionValue", self.permission_value)
        writer.write_additional_data_value(self.additional_data)
    

