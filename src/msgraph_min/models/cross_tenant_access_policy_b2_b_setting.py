from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_access_policy_target_configuration import CrossTenantAccessPolicyTargetConfiguration
    from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions

@dataclass
class CrossTenantAccessPolicyB2BSetting(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The list of applications targeted with your cross-tenant access policy.
    applications: Optional[CrossTenantAccessPolicyTargetConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of users and groups targeted with your cross-tenant access policy.
    users_and_groups: Optional[CrossTenantAccessPolicyTargetConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CrossTenantAccessPolicyB2BSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyB2BSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantAccessPolicyTenantRestrictions".casefold():
            from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions

            return CrossTenantAccessPolicyTenantRestrictions()
        return CrossTenantAccessPolicyB2BSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_access_policy_target_configuration import CrossTenantAccessPolicyTargetConfiguration
        from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions

        from .cross_tenant_access_policy_target_configuration import CrossTenantAccessPolicyTargetConfiguration
        from .cross_tenant_access_policy_tenant_restrictions import CrossTenantAccessPolicyTenantRestrictions

        fields: dict[str, Callable[[Any], None]] = {
            "applications": lambda n : setattr(self, 'applications', n.get_object_value(CrossTenantAccessPolicyTargetConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "usersAndGroups": lambda n : setattr(self, 'users_and_groups', n.get_object_value(CrossTenantAccessPolicyTargetConfiguration)),
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
        writer.write_object_value("applications", self.applications)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("usersAndGroups", self.users_and_groups)
        writer.write_additional_data_value(self.additional_data)
    

