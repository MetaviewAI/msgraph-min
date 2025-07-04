from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attribute_definition import AttributeDefinition
    from .object_definition_metadata_entry import ObjectDefinitionMetadataEntry

@dataclass
class ObjectDefinition(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Defines attributes of the object.
    attributes: Optional[list[AttributeDefinition]] = None
    # Metadata for the given object.
    metadata: Optional[list[ObjectDefinitionMetadataEntry]] = None
    # Name of the object. Must be unique within a directory definition. Not nullable.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The API that the provisioning service queries to retrieve data for synchronization.
    supported_apis: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ObjectDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ObjectDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ObjectDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attribute_definition import AttributeDefinition
        from .object_definition_metadata_entry import ObjectDefinitionMetadataEntry

        from .attribute_definition import AttributeDefinition
        from .object_definition_metadata_entry import ObjectDefinitionMetadataEntry

        fields: dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_collection_of_object_values(AttributeDefinition)),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(ObjectDefinitionMetadataEntry)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "supportedApis": lambda n : setattr(self, 'supported_apis', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("attributes", self.attributes)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("supportedApis", self.supported_apis)
        writer.write_additional_data_value(self.additional_data)
    

