from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .rating_new_zealand_movies_type import RatingNewZealandMoviesType
    from .rating_new_zealand_television_type import RatingNewZealandTelevisionType

@dataclass
class MediaContentRatingNewZealand(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Movies rating labels in New Zealand
    movie_rating: Optional[RatingNewZealandMoviesType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # TV content rating labels in New Zealand
    tv_rating: Optional[RatingNewZealandTelevisionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MediaContentRatingNewZealand:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MediaContentRatingNewZealand
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MediaContentRatingNewZealand()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .rating_new_zealand_movies_type import RatingNewZealandMoviesType
        from .rating_new_zealand_television_type import RatingNewZealandTelevisionType

        from .rating_new_zealand_movies_type import RatingNewZealandMoviesType
        from .rating_new_zealand_television_type import RatingNewZealandTelevisionType

        fields: dict[str, Callable[[Any], None]] = {
            "movieRating": lambda n : setattr(self, 'movie_rating', n.get_enum_value(RatingNewZealandMoviesType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tvRating": lambda n : setattr(self, 'tv_rating', n.get_enum_value(RatingNewZealandTelevisionType)),
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
        writer.write_enum_value("movieRating", self.movie_rating)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("tvRating", self.tv_rating)
        writer.write_additional_data_value(self.additional_data)
    

