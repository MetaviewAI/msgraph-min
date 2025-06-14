from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_all_external_tenants import ConditionalAccessAllExternalTenants
    from .conditional_access_enumerated_external_tenants import ConditionalAccessEnumeratedExternalTenants
    from .conditional_access_external_tenants_membership_kind import ConditionalAccessExternalTenantsMembershipKind

@dataclass
class ConditionalAccessExternalTenants(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The membership kind. Possible values are: all, enumerated, unknownFutureValue. The enumerated member references an conditionalAccessEnumeratedExternalTenants object.
    membership_kind: Optional[ConditionalAccessExternalTenantsMembershipKind] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessExternalTenants:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessExternalTenants
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conditionalAccessAllExternalTenants".casefold():
            from .conditional_access_all_external_tenants import ConditionalAccessAllExternalTenants

            return ConditionalAccessAllExternalTenants()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conditionalAccessEnumeratedExternalTenants".casefold():
            from .conditional_access_enumerated_external_tenants import ConditionalAccessEnumeratedExternalTenants

            return ConditionalAccessEnumeratedExternalTenants()
        return ConditionalAccessExternalTenants()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_all_external_tenants import ConditionalAccessAllExternalTenants
        from .conditional_access_enumerated_external_tenants import ConditionalAccessEnumeratedExternalTenants
        from .conditional_access_external_tenants_membership_kind import ConditionalAccessExternalTenantsMembershipKind

        from .conditional_access_all_external_tenants import ConditionalAccessAllExternalTenants
        from .conditional_access_enumerated_external_tenants import ConditionalAccessEnumeratedExternalTenants
        from .conditional_access_external_tenants_membership_kind import ConditionalAccessExternalTenantsMembershipKind

        fields: dict[str, Callable[[Any], None]] = {
            "membershipKind": lambda n : setattr(self, 'membership_kind', n.get_enum_value(ConditionalAccessExternalTenantsMembershipKind)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("membershipKind", self.membership_kind)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

