from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_registration_membership import DeviceRegistrationMembership

@dataclass
class AzureADRegistrationPolicy(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The allowedToRegister property
    allowed_to_register: Optional[DeviceRegistrationMembership] = None
    # The isAdminConfigurable property
    is_admin_configurable: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AzureADRegistrationPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureADRegistrationPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AzureADRegistrationPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_registration_membership import DeviceRegistrationMembership

        from .device_registration_membership import DeviceRegistrationMembership

        fields: dict[str, Callable[[Any], None]] = {
            "allowedToRegister": lambda n : setattr(self, 'allowed_to_register', n.get_object_value(DeviceRegistrationMembership)),
            "isAdminConfigurable": lambda n : setattr(self, 'is_admin_configurable', n.get_bool_value()),
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
        writer.write_object_value("allowedToRegister", self.allowed_to_register)
        writer.write_bool_value("isAdminConfigurable", self.is_admin_configurable)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

