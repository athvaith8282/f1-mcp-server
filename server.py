from mcp.server.fastmcp import FastMCP
from tools.f1_tools import resgister_tools
from mcp.server.auth.settings import AuthSettings 
import os

from pydantic import AnyHttpUrl

from utils.auth import create_auth0_verifier

from dotenv import load_dotenv

load_dotenv()

# Get Auth0 configuration from environment
auth0_domain = os.getenv("AUTH0_DOMAIN")
resource_server_url = os.getenv("RESOURCE_SERVER_URL")

if not auth0_domain:
    raise ValueError("AUTH0_DOMAIN environment variable is required")
if not resource_server_url:
    raise ValueError("RESOURCE_SERVER_URL environment variable is required")

# Initialize Auth0 token verifier
token_verifier = create_auth0_verifier()

def create_mcp_server():
    mcp = FastMCP(
        name="F1_MCP",
        host="0.0.0.0",
         token_verifier=token_verifier,
        auth=AuthSettings(
            issuer_url=AnyHttpUrl(f"https://{auth0_domain}/"),
            resource_server_url=AnyHttpUrl(resource_server_url),
            required_scopes=["openid", "profile", "email", "address", "phone"],
            ),
        )
    resgister_tools(mcp)
    return mcp