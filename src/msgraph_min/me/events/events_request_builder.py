from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.event_item_request_builder import EventItemRequestBuilder

class EventsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /me/events
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EventsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/me/events", path_parameters)
    
    def by_event_id(self,event_id: str) -> EventItemRequestBuilder:
        """
        Provides operations to manage the events property of the microsoft.graph.user entity.
        param event_id: The unique identifier of event
        Returns: EventItemRequestBuilder
        """
        if event_id is None:
            raise TypeError("event_id cannot be null.")
        from .item.event_item_request_builder import EventItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["event%2Did"] = event_id
        return EventItemRequestBuilder(self.request_adapter, url_tpl_params)
    

