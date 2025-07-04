from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SignInActivity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The last non-interactive sign-in date for a specific user. You can use this field to calculate the last time a client attempted (either successfully or unsuccessfully) to sign in to the directory on behalf of a user. Because some users may use clients to access tenant resources rather than signing into your tenant directly, you can use the non-interactive sign-in date to along with lastSignInDateTime to identify inactive users. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Microsoft Entra ID maintains non-interactive sign-ins going back to May 2020. For more information about using the value of this property, see Manage inactive user accounts in Microsoft Entra ID.
    last_non_interactive_sign_in_date_time: Optional[datetime.datetime] = None
    # Request identifier of the last non-interactive sign-in performed by this user.
    last_non_interactive_sign_in_request_id: Optional[str] = None
    # The last interactive sign-in date and time for a specific user. This property records the last time a user attempted an interactive sign-in to the directory—whether the attempt was successful or not. Note: Since unsuccessful attempts are also logged, this value might not accurately reflect actual system usage. For tracking actual account access, please use the lastSuccessfulSignInDateTime property. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    last_sign_in_date_time: Optional[datetime.datetime] = None
    # Request identifier of the last interactive sign-in performed by this user.
    last_sign_in_request_id: Optional[str] = None
    # The date and time of the user's most recent successful interactive or non-interactive sign-in. Use this property if you need to determine when the account was truly accessed. This field can be used to build reports, such as inactive users. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Microsoft Entra ID maintains interactive sign-ins going back to April 2020. For more information about using the value of this property, see Manage inactive user accounts in Microsoft Entra ID.
    last_successful_sign_in_date_time: Optional[datetime.datetime] = None
    # The request ID of the last successful sign-in.
    last_successful_sign_in_request_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SignInActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SignInActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SignInActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "lastNonInteractiveSignInDateTime": lambda n : setattr(self, 'last_non_interactive_sign_in_date_time', n.get_datetime_value()),
            "lastNonInteractiveSignInRequestId": lambda n : setattr(self, 'last_non_interactive_sign_in_request_id', n.get_str_value()),
            "lastSignInDateTime": lambda n : setattr(self, 'last_sign_in_date_time', n.get_datetime_value()),
            "lastSignInRequestId": lambda n : setattr(self, 'last_sign_in_request_id', n.get_str_value()),
            "lastSuccessfulSignInDateTime": lambda n : setattr(self, 'last_successful_sign_in_date_time', n.get_datetime_value()),
            "lastSuccessfulSignInRequestId": lambda n : setattr(self, 'last_successful_sign_in_request_id', n.get_str_value()),
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
        writer.write_datetime_value("lastNonInteractiveSignInDateTime", self.last_non_interactive_sign_in_date_time)
        writer.write_str_value("lastNonInteractiveSignInRequestId", self.last_non_interactive_sign_in_request_id)
        writer.write_datetime_value("lastSignInDateTime", self.last_sign_in_date_time)
        writer.write_str_value("lastSignInRequestId", self.last_sign_in_request_id)
        writer.write_datetime_value("lastSuccessfulSignInDateTime", self.last_successful_sign_in_date_time)
        writer.write_str_value("lastSuccessfulSignInRequestId", self.last_successful_sign_in_request_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

