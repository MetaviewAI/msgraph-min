from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attribute_rule_members import AttributeRuleMembers
    from .connected_organization_members import ConnectedOrganizationMembers
    from .external_sponsors import ExternalSponsors
    from .group_members import GroupMembers
    from .identity_governance.group_based_subject_set import GroupBasedSubjectSet
    from .identity_governance.rule_based_subject_set import RuleBasedSubjectSet
    from .internal_sponsors import InternalSponsors
    from .requestor_manager import RequestorManager
    from .single_service_principal import SingleServicePrincipal
    from .single_user import SingleUser
    from .target_application_owners import TargetApplicationOwners
    from .target_manager import TargetManager
    from .target_user_sponsors import TargetUserSponsors

@dataclass
class SubjectSet(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SubjectSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SubjectSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attributeRuleMembers".casefold():
            from .attribute_rule_members import AttributeRuleMembers

            return AttributeRuleMembers()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.connectedOrganizationMembers".casefold():
            from .connected_organization_members import ConnectedOrganizationMembers

            return ConnectedOrganizationMembers()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalSponsors".casefold():
            from .external_sponsors import ExternalSponsors

            return ExternalSponsors()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupMembers".casefold():
            from .group_members import GroupMembers

            return GroupMembers()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.groupBasedSubjectSet".casefold():
            from .identity_governance.group_based_subject_set import GroupBasedSubjectSet

            return GroupBasedSubjectSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.ruleBasedSubjectSet".casefold():
            from .identity_governance.rule_based_subject_set import RuleBasedSubjectSet

            return RuleBasedSubjectSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.internalSponsors".casefold():
            from .internal_sponsors import InternalSponsors

            return InternalSponsors()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.requestorManager".casefold():
            from .requestor_manager import RequestorManager

            return RequestorManager()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.singleServicePrincipal".casefold():
            from .single_service_principal import SingleServicePrincipal

            return SingleServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.singleUser".casefold():
            from .single_user import SingleUser

            return SingleUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetApplicationOwners".casefold():
            from .target_application_owners import TargetApplicationOwners

            return TargetApplicationOwners()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetManager".casefold():
            from .target_manager import TargetManager

            return TargetManager()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetUserSponsors".casefold():
            from .target_user_sponsors import TargetUserSponsors

            return TargetUserSponsors()
        return SubjectSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attribute_rule_members import AttributeRuleMembers
        from .connected_organization_members import ConnectedOrganizationMembers
        from .external_sponsors import ExternalSponsors
        from .group_members import GroupMembers
        from .identity_governance.group_based_subject_set import GroupBasedSubjectSet
        from .identity_governance.rule_based_subject_set import RuleBasedSubjectSet
        from .internal_sponsors import InternalSponsors
        from .requestor_manager import RequestorManager
        from .single_service_principal import SingleServicePrincipal
        from .single_user import SingleUser
        from .target_application_owners import TargetApplicationOwners
        from .target_manager import TargetManager
        from .target_user_sponsors import TargetUserSponsors

        from .attribute_rule_members import AttributeRuleMembers
        from .connected_organization_members import ConnectedOrganizationMembers
        from .external_sponsors import ExternalSponsors
        from .group_members import GroupMembers
        from .identity_governance.group_based_subject_set import GroupBasedSubjectSet
        from .identity_governance.rule_based_subject_set import RuleBasedSubjectSet
        from .internal_sponsors import InternalSponsors
        from .requestor_manager import RequestorManager
        from .single_service_principal import SingleServicePrincipal
        from .single_user import SingleUser
        from .target_application_owners import TargetApplicationOwners
        from .target_manager import TargetManager
        from .target_user_sponsors import TargetUserSponsors

        fields: dict[str, Callable[[Any], None]] = {
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

