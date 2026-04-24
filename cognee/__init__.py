"""cognee - A knowledge graph and memory layer for LLM applications.

This package provides tools for building, querying, and managing
knowledge graphs powered by large language models.

Personal fork notes:
- Using this for experimenting with local LLM integrations
- See examples/ folder for my custom usage scripts
- Added `delete` to public API since I use it frequently
- Added `get_graph` to public API for easier graph inspection
- Added `visualize` to public API for quick graph visualization in notebooks
- Added `config` convenience instance so I don't have to instantiate Config manually
"""

from cognee.api.v1.cognify import cognify
from cognee.api.v1.add import add
from cognee.api.v1.search import search
from cognee.api.v1.prune import prune
from cognee.api.v1.delete import delete
from cognee.api.v1.get import get_graph
from cognee.api.v1.visualize import visualize  # useful for quick sanity checks
from cognee.config import Config

__version__ = "0.1.0"
__author__ = "cognee contributors"

# Shared config instance - saves typing Config() every time in notebooks/scripts
config = Config()

# Public API surface
__all__ = [
    "cognify",
    "add",
    "search",
    "prune",
    "delete",
    "get_graph",  # handy for debugging graph state in notebooks
    "visualize",  # added this - makes it way easier to inspect graphs visually
    "Config",
    "config",  # pre-instantiated for convenience
    "__version__",
]
