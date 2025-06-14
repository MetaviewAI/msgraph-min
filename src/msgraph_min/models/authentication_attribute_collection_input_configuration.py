from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_attribute_collection_input_type import AuthenticationAttributeCollectionInputType
    from .authentication_attribute_collection_option_configuration import AuthenticationAttributeCollectionOptionConfiguration

@dataclass
class AuthenticationAttributeCollectionInputConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The built-in or custom attribute for which a value is being collected.
    attribute: Optional[str] = None
    # The default value of the attribute displayed to the end user. The capability to set the default value isn't available through the Microsoft Entra admin center.
    default_value: Optional[str] = None
    # Defines whether the attribute is editable by the end user.
    editable: Optional[bool] = None
    # Defines whether the attribute is displayed to the end user. The capability to hide isn't available through the Microsoft Entra admin center.
    hidden: Optional[bool] = None
    # The inputType property
    input_type: Optional[AuthenticationAttributeCollectionInputType] = None
    # The label of the attribute field that's displayed to end user, unless overridden.
    label: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The option values for certain multiple-option input types.
    options: Optional[list[AuthenticationAttributeCollectionOptionConfiguration]] = None
    # Defines whether the field is required.
    required: Optional[bool] = None
    # The regex for the value of the field. For more information about the supported regexes, see validationRegEx values for inputType objects. To understand how to specify regexes, see the Regular expressions cheat sheet.
    validation_reg_ex: Optional[str] = None
    # Defines whether Microsoft Entra ID stores the value that it collects.
    write_to_directory: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationAttributeCollectionInputConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationAttributeCollectionInputConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationAttributeCollectionInputConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_attribute_collection_input_type import AuthenticationAttributeCollectionInputType
        from .authentication_attribute_collection_option_configuration import AuthenticationAttributeCollectionOptionConfiguration

        from .authentication_attribute_collection_input_type import AuthenticationAttributeCollectionInputType
        from .authentication_attribute_collection_option_configuration import AuthenticationAttributeCollectionOptionConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "attribute": lambda n : setattr(self, 'attribute', n.get_str_value()),
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_str_value()),
            "editable": lambda n : setattr(self, 'editable', n.get_bool_value()),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "inputType": lambda n : setattr(self, 'input_type', n.get_enum_value(AuthenticationAttributeCollectionInputType)),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "options": lambda n : setattr(self, 'options', n.get_collection_of_object_values(AuthenticationAttributeCollectionOptionConfiguration)),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
            "validationRegEx": lambda n : setattr(self, 'validation_reg_ex', n.get_str_value()),
            "writeToDirectory": lambda n : setattr(self, 'write_to_directory', n.get_bool_value()),
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
        writer.write_str_value("attribute", self.attribute)
        writer.write_str_value("defaultValue", self.default_value)
        writer.write_bool_value("editable", self.editable)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_enum_value("inputType", self.input_type)
        writer.write_str_value("label", self.label)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("options", self.options)
        writer.write_bool_value("required", self.required)
        writer.write_str_value("validationRegEx", self.validation_reg_ex)
        writer.write_bool_value("writeToDirectory", self.write_to_directory)
        writer.write_additional_data_value(self.additional_data)
    

