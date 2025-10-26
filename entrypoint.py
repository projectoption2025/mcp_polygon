#!/usr/bin/env python
import os
from typing import Literal
from mcp_polygon import server


def transport() -> Literal["stdio", "sse", "streamable-http"]:
    """
    Determine the transport type for the MCP server.
    Defaults to 'stdio' if not set in environment variables.
    """
    mcp_transport_str = os.environ.get("MCP_TRANSPORT", "stdio")
    supported_transports: dict[str, Literal["stdio", "sse", "streamable-http"]] = {
        "stdio": "stdio",
        "sse": "sse",
        "streamable-http": "streamable-http",
    }
    return supported_transports.get(mcp_transport_str, "stdio")


def start_server():
    polygon_api_key = os.environ.get("POLYGON_API_KEY", "")
    if not polygon_api_key:
        print("Warning: POLYGON_API_KEY environment variable not set.")
    else:
        print("Starting Polygon MCP server with API key configured.")

    # Ensure Render sees the correct binding
    port = int(os.getenv("PORT", "10000"))
    os.environ["PORT"] = str(port)
    os.environ["HOST"] = "0.0.0.0"
    print(f"Binding MCP server to 0.0.0.0:{port}")

    server.run(transport=transport())


if __name__ == "__main__":
    start_server()

