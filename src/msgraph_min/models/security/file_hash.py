from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_hash_algorithm import FileHashAlgorithm

@dataclass
class FileHash(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The algorithm property
    algorithm: Optional[FileHashAlgorithm] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The hash value.
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileHash:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileHash
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileHash()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .file_hash_algorithm import FileHashAlgorithm

        from .file_hash_algorithm import FileHashAlgorithm

        fields: dict[str, Callable[[Any], None]] = {
            "algorithm": lambda n : setattr(self, 'algorithm', n.get_enum_value(FileHashAlgorithm)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_enum_value("algorithm", self.algorithm)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

