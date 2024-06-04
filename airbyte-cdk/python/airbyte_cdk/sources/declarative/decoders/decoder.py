#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

from abc import abstractmethod
from dataclasses import dataclass
from typing import Any, Generator, Mapping

import requests


@dataclass
class Decoder:
    """
    Decoder strategy to transform a requests.Response into a Mapping[str, Any]
    """

    @abstractmethod
    def decode(self, response: requests.Response) -> Generator[Mapping[str, Any], None, None]:
        """
        Decodes a requests.Response into a Mapping[str, Any] or an array
        :param response: the response to decode
        :return: Mapping or array describing the response
        """
        pass
