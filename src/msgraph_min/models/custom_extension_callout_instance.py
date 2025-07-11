from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_extension_callout_instance_status import CustomExtensionCalloutInstanceStatus

@dataclass
class CustomExtensionCalloutInstance(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identification of the custom extension that was triggered at this instance.
    custom_extension_id: Optional[str] = None
    # Details provided by the logic app during the callback of the request instance.
    detail: Optional[str] = None
    # The unique run identifier for the logic app.
    external_correlation_id: Optional[str] = None
    # Unique identifier for the callout instance. Read-only.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of the request to the custom extension. The possible values are: calloutSent, callbackReceived, calloutFailed, callbackTimedOut, waitingForCallback, unknownFutureValue.
    status: Optional[CustomExtensionCalloutInstanceStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomExtensionCalloutInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionCalloutInstance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomExtensionCalloutInstance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_extension_callout_instance_status import CustomExtensionCalloutInstanceStatus

        from .custom_extension_callout_instance_status import CustomExtensionCalloutInstanceStatus

        fields: dict[str, Callable[[Any], None]] = {
            "customExtensionId": lambda n : setattr(self, 'custom_extension_id', n.get_str_value()),
            "detail": lambda n : setattr(self, 'detail', n.get_str_value()),
            "externalCorrelationId": lambda n : setattr(self, 'external_correlation_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CustomExtensionCalloutInstanceStatus)),
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
        writer.write_str_value("customExtensionId", self.custom_extension_id)
        writer.write_str_value("detail", self.detail)
        writer.write_str_value("externalCorrelationId", self.external_correlation_id)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

