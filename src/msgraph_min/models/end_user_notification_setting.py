from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .end_user_notification_preference import EndUserNotificationPreference
    from .end_user_notification_setting_type import EndUserNotificationSettingType
    from .no_training_notification_setting import NoTrainingNotificationSetting
    from .positive_reinforcement_notification import PositiveReinforcementNotification
    from .training_notification_setting import TrainingNotificationSetting

@dataclass
class EndUserNotificationSetting(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Notification preference. Possible values are: unknown, microsoft, custom, unknownFutureValue.
    notification_preference: Optional[EndUserNotificationPreference] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Positive reinforcement detail.
    positive_reinforcement: Optional[PositiveReinforcementNotification] = None
    # End user notification type. Possible values are: unknown, noTraining, trainingSelected, noNotification, unknownFutureValue.
    setting_type: Optional[EndUserNotificationSettingType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EndUserNotificationSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EndUserNotificationSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.noTrainingNotificationSetting".casefold():
            from .no_training_notification_setting import NoTrainingNotificationSetting

            return NoTrainingNotificationSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.trainingNotificationSetting".casefold():
            from .training_notification_setting import TrainingNotificationSetting

            return TrainingNotificationSetting()
        return EndUserNotificationSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .end_user_notification_preference import EndUserNotificationPreference
        from .end_user_notification_setting_type import EndUserNotificationSettingType
        from .no_training_notification_setting import NoTrainingNotificationSetting
        from .positive_reinforcement_notification import PositiveReinforcementNotification
        from .training_notification_setting import TrainingNotificationSetting

        from .end_user_notification_preference import EndUserNotificationPreference
        from .end_user_notification_setting_type import EndUserNotificationSettingType
        from .no_training_notification_setting import NoTrainingNotificationSetting
        from .positive_reinforcement_notification import PositiveReinforcementNotification
        from .training_notification_setting import TrainingNotificationSetting

        fields: dict[str, Callable[[Any], None]] = {
            "notificationPreference": lambda n : setattr(self, 'notification_preference', n.get_enum_value(EndUserNotificationPreference)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "positiveReinforcement": lambda n : setattr(self, 'positive_reinforcement', n.get_object_value(PositiveReinforcementNotification)),
            "settingType": lambda n : setattr(self, 'setting_type', n.get_enum_value(EndUserNotificationSettingType)),
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
        writer.write_enum_value("notificationPreference", self.notification_preference)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("positiveReinforcement", self.positive_reinforcement)
        writer.write_enum_value("settingType", self.setting_type)
        writer.write_additional_data_value(self.additional_data)
    

