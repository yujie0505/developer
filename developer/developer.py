import json
import uuid

import requests


class Developer:
    def __init__(self, api_endpoint: str, api_key: str, model: str) -> None:
        self.__api_endpoint = api_endpoint
        self.__api_key = api_key
        self.__model = model
        self.__uuid = uuid.uuid4()

    @property
    def api_endpoint(self) -> str:
        """Get the URL of the API used for AI chat completion."""
        return self.__api_endpoint

    @property
    def model(self) -> str:
        """Get the name of the model used for this instance."""
        return self.__model

    @property
    def uuid(self) -> uuid.UUID:
        """Get the unique id for this instance."""
        return self.__uuid

    def code(self) -> None:
        messages = []

        data = {"messages": messages, "model": self.model, "user": self.uuid}
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.__api_key}",
        }

        requests.post(self.api_endpoint, data=json.dumps(data), headers=headers)
