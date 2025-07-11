from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .education_channel_resource import EducationChannelResource
    from .education_excel_resource import EducationExcelResource
    from .education_external_resource import EducationExternalResource
    from .education_file_resource import EducationFileResource
    from .education_linked_assignment_resource import EducationLinkedAssignmentResource
    from .education_link_resource import EducationLinkResource
    from .education_media_resource import EducationMediaResource
    from .education_power_point_resource import EducationPowerPointResource
    from .education_teams_app_resource import EducationTeamsAppResource
    from .education_word_resource import EducationWordResource
    from .identity_set import IdentitySet

@dataclass
class EducationResource(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The individual who created the resource.
    created_by: Optional[IdentitySet] = None
    # Moment in time when the resource was created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime.datetime] = None
    # Display name of resource.
    display_name: Optional[str] = None
    # The last user to modify the resource.
    last_modified_by: Optional[IdentitySet] = None
    # Moment in time when the resource was last modified.  The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EducationResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EducationResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationChannelResource".casefold():
            from .education_channel_resource import EducationChannelResource

            return EducationChannelResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationExcelResource".casefold():
            from .education_excel_resource import EducationExcelResource

            return EducationExcelResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationExternalResource".casefold():
            from .education_external_resource import EducationExternalResource

            return EducationExternalResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationFileResource".casefold():
            from .education_file_resource import EducationFileResource

            return EducationFileResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationLinkedAssignmentResource".casefold():
            from .education_linked_assignment_resource import EducationLinkedAssignmentResource

            return EducationLinkedAssignmentResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationLinkResource".casefold():
            from .education_link_resource import EducationLinkResource

            return EducationLinkResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationMediaResource".casefold():
            from .education_media_resource import EducationMediaResource

            return EducationMediaResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationPowerPointResource".casefold():
            from .education_power_point_resource import EducationPowerPointResource

            return EducationPowerPointResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationTeamsAppResource".casefold():
            from .education_teams_app_resource import EducationTeamsAppResource

            return EducationTeamsAppResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationWordResource".casefold():
            from .education_word_resource import EducationWordResource

            return EducationWordResource()
        return EducationResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .education_channel_resource import EducationChannelResource
        from .education_excel_resource import EducationExcelResource
        from .education_external_resource import EducationExternalResource
        from .education_file_resource import EducationFileResource
        from .education_linked_assignment_resource import EducationLinkedAssignmentResource
        from .education_link_resource import EducationLinkResource
        from .education_media_resource import EducationMediaResource
        from .education_power_point_resource import EducationPowerPointResource
        from .education_teams_app_resource import EducationTeamsAppResource
        from .education_word_resource import EducationWordResource
        from .identity_set import IdentitySet

        from .education_channel_resource import EducationChannelResource
        from .education_excel_resource import EducationExcelResource
        from .education_external_resource import EducationExternalResource
        from .education_file_resource import EducationFileResource
        from .education_linked_assignment_resource import EducationLinkedAssignmentResource
        from .education_link_resource import EducationLinkResource
        from .education_media_resource import EducationMediaResource
        from .education_power_point_resource import EducationPowerPointResource
        from .education_teams_app_resource import EducationTeamsAppResource
        from .education_word_resource import EducationWordResource
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

