"""Stream type classes for tap-lotr."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_lotr.client import lotrStream


class BooksStream(lotrStream):
    """Define custom stream."""
    name = "books"
    path = "/book"
    primary_keys = ["_id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property("name", th.StringType),
        th.Property("_id",th.StringType,description="The Books's system ID"),
        th.Property("name",th.StringType,description="The Books name"),
    ).to_dict()

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "_id": record["_id"],
        }

class ChaptersStream(lotrStream):
    """Define custom stream."""
    name = "chapters"
    parent_stream_type = BooksStream

    path = "/book/{_id}/chapter"
    primary_keys = ["_id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("_id",th.StringType,description="The Chapter ID"),
        th.Property("chapterName",th.StringType,description="The chapterName name"),
    ).to_dict()

class MoviesStream(lotrStream):
    """Define custom stream."""
    name = "movies"
    path = "/movie"
    primary_keys = ["_id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("_id",th.StringType,description="The Movies's system ID"),
        th.Property("name",th.StringType,description="The Movies name"),
        th.Property("budgetInMillions",th.StringType),
        th.Property("boxOfficeRevenueInMillions",th.StringType),
        th.Property("academyAwardNominations",th.StringType),
        th.Property("academyAwardWins",th.StringType),
        th.Property("rottenTomatoesScore",th.StringType),
        th.Property("runtimeInMinutes", th.StringType),
    ).to_dict()

class CharactersStream(lotrStream):
    """Define Characters stream."""
    name = "character"
    path = "/character"
    primary_keys = ["_id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("_id",th.StringType,description="The Character's system ID"),
        th.Property("wikiUrl",th.StringType,description="The wikiUrl for character"),
    ).to_dict()
