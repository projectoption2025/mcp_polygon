##!/usr/bin/env python
import os
import subprocess
from typing import Literal
from mcp_polygon import server


def transport() -> Literal["stdio", "sse", "streamable-http"]:
    return os.environ.get("MCP_TRANSPORT", "stdio")


def start_server():
    polygon_api_key = os.environ.get("POLYGON_API_KEY", "")
    if not polygon_api_key:
        print("Warning: POLYGON_API_KEY environment variable not set.")
    else:
        print("Starting Polygon MCP server with API key configured.")

    # Ensure correct binding
    port = os.getenv("PORT", "10000")
    host = "0.0.0.0"
    print(f"Binding MCP server to {host}:{port}")

    # Start uvicorn manually to ensure binding
    subprocess.run(
        [
            "uvicorn",
            "mcp_polygon.server:app",
            "--host",
            host,
            "--port",
            port
        ],
        check=True
    )


if __name__ == "__main__":
    start_server()


