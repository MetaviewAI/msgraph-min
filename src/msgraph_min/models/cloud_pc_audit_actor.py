from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_user_role_scope_tag_info import CloudPcUserRoleScopeTagInfo

@dataclass
class CloudPcAuditActor(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Name of the application.
    application_display_name: Optional[str] = None
    # Microsoft Entra application ID.
    application_id: Optional[str] = None
    # IP address.
    ip_address: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The delegated partner tenant ID.
    remote_tenant_id: Optional[str] = None
    # The delegated partner user ID.
    remote_user_id: Optional[str] = None
    # Service Principal Name (SPN).
    service_principal_name: Optional[str] = None
    # Microsoft Entra user ID.
    user_id: Optional[str] = None
    # List of user permissions and application permissions when the audit event was performed.
    user_permissions: Optional[list[str]] = None
    # User Principal Name (UPN).
    user_principal_name: Optional[str] = None
    # List of role scope tags.
    user_role_scope_tags: Optional[list[CloudPcUserRoleScopeTagInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcAuditActor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcAuditActor
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcAuditActor()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_user_role_scope_tag_info import CloudPcUserRoleScopeTagInfo

        from .cloud_pc_user_role_scope_tag_info import CloudPcUserRoleScopeTagInfo

        fields: dict[str, Callable[[Any], None]] = {
            "applicationDisplayName": lambda n : setattr(self, 'application_display_name', n.get_str_value()),
            "applicationId": lambda n : setattr(self, 'application_id', n.get_str_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remoteTenantId": lambda n : setattr(self, 'remote_tenant_id', n.get_str_value()),
            "remoteUserId": lambda n : setattr(self, 'remote_user_id', n.get_str_value()),
            "servicePrincipalName": lambda n : setattr(self, 'service_principal_name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPermissions": lambda n : setattr(self, 'user_permissions', n.get_collection_of_primitive_values(str)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "userRoleScopeTags": lambda n : setattr(self, 'user_role_scope_tags', n.get_collection_of_object_values(CloudPcUserRoleScopeTagInfo)),
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
        writer.write_str_value("applicationDisplayName", self.application_display_name)
        writer.write_str_value("applicationId", self.application_id)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("remoteTenantId", self.remote_tenant_id)
        writer.write_str_value("remoteUserId", self.remote_user_id)
        writer.write_str_value("servicePrincipalName", self.service_principal_name)
        writer.write_str_value("userId", self.user_id)
        writer.write_collection_of_primitive_values("userPermissions", self.user_permissions)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_collection_of_object_values("userRoleScopeTags", self.user_role_scope_tags)
        writer.write_additional_data_value(self.additional_data)
    

