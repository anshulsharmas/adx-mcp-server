#!/usr/bin/env python
import sys
import dotenv
from adx_mcp_server.server import mcp, config

def setup_environment():
    if dotenv.load_dotenv():
        print("Loaded environment variables from .env file")
    else:
        print("No .env file found or could not load it - using environment variables")

    if not config.cluster_url:
        print("ERROR: ADX_CLUSTER_URL environment variable is not set")
        print("Please set it to your Azure Data Explorer cluster URL")
        print("Example: https://youradxcluster.region.kusto.windows.net")
        return False
    
    if not config.database:
        print("ERROR: ADX_DATABASE environment variable is not set")
        print("Please set it to your Azure Data Explorer database name")
        return False

    print(f"Azure Data Explorer configuration:")
    print(f"  Cluster: {config.cluster_url}")
    print(f"  Database: {config.database}")
    print(f"  Authentication: Using DefaultAzureCredential")
    
    return True

def run_server():
    """Main entry point for the Azure Data Explorer MCP Server"""
    # Setup environment
    if not setup_environment():
        sys.exit(1)
    
    print("\nStarting Azure Data Explorer MCP Server...")
    print("Running server in standard mode...")
    
    # Run the server with the stdio transport
    mcp.run(transport="stdio")

if __name__ == "__main__":
    run_server()
