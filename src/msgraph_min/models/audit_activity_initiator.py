from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_identity import AppIdentity
    from .user_identity import UserIdentity

@dataclass
class AuditActivityInitiator(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # If the resource initiating the activity is an app, this property indicates all the app related information like appId, Name, servicePrincipalId, Name.
    app: Optional[AppIdentity] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If the resource initiating the activity is a user, this property Indicates all the user related information like userId, Name, UserPrinicpalName.
    user: Optional[UserIdentity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuditActivityInitiator:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuditActivityInitiator
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuditActivityInitiator()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_identity import AppIdentity
        from .user_identity import UserIdentity

        from .app_identity import AppIdentity
        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "app": lambda n : setattr(self, 'app', n.get_object_value(AppIdentity)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(UserIdentity)),
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
        writer.write_object_value("app", self.app)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    

