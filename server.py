from __future__ import annotations

from fastmcp import FastMCP
from modules import register_all

from modules.seq_basics._plumbing import resolve

mcp = FastMCP(
    "BioE234 MCP Starter",
    instructions="Starter MCP server for BioE234."
)

register_all(mcp)

if __name__ == "__main__":
    # print("Registered resources:", resolve.list_resources())
    mcp.run(transport="stdio")
