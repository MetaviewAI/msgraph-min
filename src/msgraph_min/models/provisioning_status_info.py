from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .provisioning_error_info import ProvisioningErrorInfo
    from .provisioning_result import ProvisioningResult

@dataclass
class ProvisioningStatusInfo(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # If status isn't success/ skipped details for the error are contained in this.
    error_information: Optional[ProvisioningErrorInfo] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Possible values are: success, warning, failure, skipped, unknownFutureValue.
    status: Optional[ProvisioningResult] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProvisioningStatusInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProvisioningStatusInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProvisioningStatusInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .provisioning_error_info import ProvisioningErrorInfo
        from .provisioning_result import ProvisioningResult

        from .provisioning_error_info import ProvisioningErrorInfo
        from .provisioning_result import ProvisioningResult

        fields: dict[str, Callable[[Any], None]] = {
            "errorInformation": lambda n : setattr(self, 'error_information', n.get_object_value(ProvisioningErrorInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ProvisioningResult)),
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
        writer.write_object_value("errorInformation", self.error_information)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

