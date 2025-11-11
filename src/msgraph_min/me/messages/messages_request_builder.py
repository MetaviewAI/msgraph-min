from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.message_item_request_builder import MessageItemRequestBuilder

class MessagesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /me/messages
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MessagesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/me/messages", path_parameters)
    
    def by_message_id(self,message_id: str) -> MessageItemRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.user entity.
        param message_id: The unique identifier of message
        Returns: MessageItemRequestBuilder
        """
        if message_id is None:
            raise TypeError("message_id cannot be null.")
        from .item.message_item_request_builder import MessageItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["message%2Did"] = message_id
        return MessageItemRequestBuilder(self.request_adapter, url_tpl_params)
    

