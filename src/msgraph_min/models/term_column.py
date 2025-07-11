from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .term_store.set import Set
    from .term_store.term import Term

@dataclass
class TermColumn(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Specifies whether the column allows more than one value.
    allow_multiple_values: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The parentTerm property
    parent_term: Optional[Term] = None
    # Specifies whether to display the entire term path or only the term label.
    show_fully_qualified_name: Optional[bool] = None
    # The termSet property
    term_set: Optional[Set] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TermColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TermColumn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TermColumn()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .term_store.set import Set
        from .term_store.term import Term

        from .term_store.set import Set
        from .term_store.term import Term

        fields: dict[str, Callable[[Any], None]] = {
            "allowMultipleValues": lambda n : setattr(self, 'allow_multiple_values', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parentTerm": lambda n : setattr(self, 'parent_term', n.get_object_value(Term)),
            "showFullyQualifiedName": lambda n : setattr(self, 'show_fully_qualified_name', n.get_bool_value()),
            "termSet": lambda n : setattr(self, 'term_set', n.get_object_value(Set)),
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
        writer.write_bool_value("allowMultipleValues", self.allow_multiple_values)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("parentTerm", self.parent_term)
        writer.write_bool_value("showFullyQualifiedName", self.show_fully_qualified_name)
        writer.write_object_value("termSet", self.term_set)
        writer.write_additional_data_value(self.additional_data)
    

