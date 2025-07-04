from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_strength_policy import AuthenticationStrengthPolicy
    from .conditional_access_grant_control import ConditionalAccessGrantControl

@dataclass
class ConditionalAccessGrantControls(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The authenticationStrength property
    authentication_strength: Optional[AuthenticationStrengthPolicy] = None
    # List of values of built-in controls required by the policy. Possible values: block, mfa, compliantDevice, domainJoinedDevice, approvedApplication, compliantApplication, passwordChange, unknownFutureValue.
    built_in_controls: Optional[list[ConditionalAccessGrantControl]] = None
    # List of custom controls IDs required by the policy. For more information, see Custom controls.
    custom_authentication_factors: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Defines the relationship of the grant controls. Possible values: AND, OR.
    operator: Optional[str] = None
    # List of terms of use IDs required by the policy.
    terms_of_use: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConditionalAccessGrantControls:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessGrantControls
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConditionalAccessGrantControls()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .conditional_access_grant_control import ConditionalAccessGrantControl

        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .conditional_access_grant_control import ConditionalAccessGrantControl

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationStrength": lambda n : setattr(self, 'authentication_strength', n.get_object_value(AuthenticationStrengthPolicy)),
            "builtInControls": lambda n : setattr(self, 'built_in_controls', n.get_collection_of_enum_values(ConditionalAccessGrantControl)),
            "customAuthenticationFactors": lambda n : setattr(self, 'custom_authentication_factors', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_str_value()),
            "termsOfUse": lambda n : setattr(self, 'terms_of_use', n.get_collection_of_primitive_values(str)),
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
        writer.write_object_value("authenticationStrength", self.authentication_strength)
        writer.write_collection_of_enum_values("builtInControls", self.built_in_controls)
        writer.write_collection_of_primitive_values("customAuthenticationFactors", self.custom_authentication_factors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operator", self.operator)
        writer.write_collection_of_primitive_values("termsOfUse", self.terms_of_use)
        writer.write_additional_data_value(self.additional_data)
    

