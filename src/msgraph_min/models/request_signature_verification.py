from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .weak_algorithms import WeakAlgorithms

@dataclass
class RequestSignatureVerification(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies which weak algorithms are allowed.  The possible values are: rsaSha1, unknownFutureValue.
    allowed_weak_algorithms: Optional[WeakAlgorithms] = None
    # Specifies whether signed authentication requests for this application should be required.
    is_signed_request_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RequestSignatureVerification:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RequestSignatureVerification
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RequestSignatureVerification()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .weak_algorithms import WeakAlgorithms

        from .weak_algorithms import WeakAlgorithms

        fields: dict[str, Callable[[Any], None]] = {
            "allowedWeakAlgorithms": lambda n : setattr(self, 'allowed_weak_algorithms', n.get_collection_of_enum_values(WeakAlgorithms)),
            "isSignedRequestRequired": lambda n : setattr(self, 'is_signed_request_required', n.get_bool_value()),
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
        writer.write_enum_value("allowedWeakAlgorithms", self.allowed_weak_algorithms)
        writer.write_bool_value("isSignedRequestRequired", self.is_signed_request_required)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

