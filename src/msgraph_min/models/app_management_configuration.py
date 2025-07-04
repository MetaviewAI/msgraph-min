from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_management_application_configuration import AppManagementApplicationConfiguration
    from .app_management_service_principal_configuration import AppManagementServicePrincipalConfiguration
    from .custom_app_management_configuration import CustomAppManagementConfiguration
    from .key_credential_configuration import KeyCredentialConfiguration
    from .password_credential_configuration import PasswordCredentialConfiguration

@dataclass
class AppManagementConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Collection of keyCredential restrictions settings to be applied to an application or service principal.
    key_credentials: Optional[list[KeyCredentialConfiguration]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of password restrictions settings to be applied to an application or service principal.
    password_credentials: Optional[list[PasswordCredentialConfiguration]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppManagementConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppManagementConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appManagementApplicationConfiguration".casefold():
            from .app_management_application_configuration import AppManagementApplicationConfiguration

            return AppManagementApplicationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appManagementServicePrincipalConfiguration".casefold():
            from .app_management_service_principal_configuration import AppManagementServicePrincipalConfiguration

            return AppManagementServicePrincipalConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customAppManagementConfiguration".casefold():
            from .custom_app_management_configuration import CustomAppManagementConfiguration

            return CustomAppManagementConfiguration()
        return AppManagementConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_management_application_configuration import AppManagementApplicationConfiguration
        from .app_management_service_principal_configuration import AppManagementServicePrincipalConfiguration
        from .custom_app_management_configuration import CustomAppManagementConfiguration
        from .key_credential_configuration import KeyCredentialConfiguration
        from .password_credential_configuration import PasswordCredentialConfiguration

        from .app_management_application_configuration import AppManagementApplicationConfiguration
        from .app_management_service_principal_configuration import AppManagementServicePrincipalConfiguration
        from .custom_app_management_configuration import CustomAppManagementConfiguration
        from .key_credential_configuration import KeyCredentialConfiguration
        from .password_credential_configuration import PasswordCredentialConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "keyCredentials": lambda n : setattr(self, 'key_credentials', n.get_collection_of_object_values(KeyCredentialConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "passwordCredentials": lambda n : setattr(self, 'password_credentials', n.get_collection_of_object_values(PasswordCredentialConfiguration)),
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
        writer.write_collection_of_object_values("keyCredentials", self.key_credentials)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("passwordCredentials", self.password_credentials)
        writer.write_additional_data_value(self.additional_data)
    

