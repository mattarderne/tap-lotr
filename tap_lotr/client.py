"""REST client handling, including lotrStream base class."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from memoization import cached

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import BearerTokenAuthenticator


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class lotrStream(RESTStream):
    """lotr stream class."""

    limit: int = 10

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return self.config["api_url"]

    records_jsonpath = "$.docs[*]"  # Or override `parse_response`.
    page_number_jsonpath = "$.page"  # Or override `get_next_page_token`.
    pages_count_json_path = "$.pages"

    @property
    def authenticator(self) -> BearerTokenAuthenticator:
        """Return a new authenticator object."""
        return BearerTokenAuthenticator.create_for_stream(
            self,
            token=self.config.get("api_key")
        )

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        pages_count = extract_jsonpath(
            self.pages_count_json_path, response.json()
        )
        pages_count = next(iter(pages_count), None)

        page_number = extract_jsonpath(
            self.page_number_jsonpath, response.json()
        )
        page_number = next(iter(page_number), None)

        if pages_count == page_number:
            next_page_token = None
        else:
            next_page_token = page_number + 1

        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        return {
            "limit": self.limit,
            "page": next_page_token,
        }

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        # TODO: Parse response body and return a set of records.
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """As needed, append or transform raw data to match expected structure."""
        # TODO: Delete this method if not needed.
        return row
