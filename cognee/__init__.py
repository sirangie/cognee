"""
cognee - A knowledge graph and memory layer for LLM applications.

This package provides tools for building, querying, and managing
knowledge graphs powered by large language models.
"""

from cognee.api.v1.cognify import cognify
from cognee.api.v1.add import add
from cognee.api.v1.search import search
from cognee.api.v1.prune import prune
from cognee.config import Config

__version__ = "0.1.0"
__author__ = "cognee contributors"

# Public API surface
__all__ = [
    "cognify",
    "add",
    "search",
    "prune",
    "Config",
    "__version__",
]
