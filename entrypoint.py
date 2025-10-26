#!/usr/bin/env python
import os
from typing import Literal
from mcp_polygon import server

def transport() -> Literal["stdio", "sse", "streamable-http"]:
    mcp_transport_str = os.environ.get("MCP_TRANSPORT", "stdio")
    supported_transports = {
        "stdio": "stdio",
        "sse": "sse",
        "streamable-http": "streamable-http",
    }
    return supported_transports.get(mcp_transport_str, "stdio")

def start_server():
    api_key = os.environ.get("POLYGON_API_KEY", "")
    if not api_key:
        print("Warning: POLYGON_API_KEY environment variable not set.")
    else:
        print("Starting Polygon MCP server with API key configured.")

    port = int(os.getenv("PORT", "10000"))
    os.environ["PORT"] = str(port)
    os.environ["HOST"] = "0.0.0.0"
    print(f"Binding Polygon MCP server to 0.0.0.0:{port}")

    # Запускаем встроенный HTTP сервер MCP
    server.run(transport=transport())

if __name__ == "__main__":
    start_server()



if __name__ == "__main__":
    start_server()


