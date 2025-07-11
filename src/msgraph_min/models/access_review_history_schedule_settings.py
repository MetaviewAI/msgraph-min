from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .patterned_recurrence import PatternedRecurrence

@dataclass
class AccessReviewHistoryScheduleSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The recurrence property
    recurrence: Optional[PatternedRecurrence] = None
    # A duration string in ISO 8601 duration format specifying the lookback period of the generated review history data. For example, if a history definition is scheduled to run on the first of every month, the reportRange is P1M. In this case, on the first of every month, access review history data is collected containing only the previous month's review data. Note: Only years, months, and days ISO 8601 properties are supported. Required.
    report_range: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewHistoryScheduleSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewHistoryScheduleSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewHistoryScheduleSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .patterned_recurrence import PatternedRecurrence

        from .patterned_recurrence import PatternedRecurrence

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(PatternedRecurrence)),
            "reportRange": lambda n : setattr(self, 'report_range', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_str_value("reportRange", self.report_range)
        writer.write_additional_data_value(self.additional_data)
    

