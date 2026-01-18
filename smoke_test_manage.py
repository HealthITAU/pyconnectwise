"""
Smoke test for ConnectWise Manage API client.

This script performs a simple read-only test to verify API connectivity.

Usage:
    export CW_COMPANY="yourCompanyLoginName"
    export CW_HOST="https://api-na.myconnectwise.net"
    export CW_CODEBASE="v2025_1"  # optional, defaults to v2025_1
    export CW_CLIENT_ID="your-client-id"
    export CW_PUBLIC_KEY="your-public"
    export CW_PRIVATE_KEY="your-private"
    poetry run python smoke_test_manage.py
    # OR
    python smoke_test_manage.py
"""
import os
from pyconnectwise import ConnectWiseManageAPIClient

# Read environment variables
CW_COMPANY = os.environ["CW_COMPANY"]  # login "Company"
CW_HOST = os.environ["CW_HOST"]  # e.g. https://api-na.myconnectwise.net
CW_CODEBASE = os.environ.get("CW_CODEBASE", "v2025_1")  # adjust if needed
CW_CLIENT_ID = os.environ["CW_CLIENT_ID"]
CW_PUBLIC = os.environ["CW_PUBLIC_KEY"]
CW_PRIVATE = os.environ["CW_PRIVATE_KEY"]

# Parse hostname from CW_HOST (remove https:// if present)
# The client expects just the hostname, not the full URL
manage_url = CW_HOST.replace("https://", "").replace("http://", "").strip("/")

print(f"Connecting to ConnectWise Manage API...")
print(f"  Company: {CW_COMPANY}")
print(f"  Host: {manage_url}")
print(f"  Codebase: {CW_CODEBASE}")
print(f"  Client ID: {CW_CLIENT_ID[:10]}..." if len(CW_CLIENT_ID) > 10 else f"  Client ID: {CW_CLIENT_ID}")

# The client will construct the URL as: https://{manage_url}/{codebase}/apis/3.0
# So we pass just the hostname and codebase separately
api = ConnectWiseManageAPIClient(
    CW_COMPANY,
    manage_url,
    CW_CLIENT_ID,
    CW_PUBLIC,
    CW_PRIVATE,
    codebase=CW_CODEBASE,
)

# simplest read: list first 10 companies
print(f"\nFetching companies from {api._get_url()}...")
try:
    companies = api.company.companies.get(params={"page": 1, "pageSize": 10})
    print(f"✓ Successfully connected! Found {len(companies)} companies (showing first 10):\n")
    for c in companies:
        print(f"  ID: {c.id}, Name: {getattr(c, 'name', 'N/A')}")
    print("\n✓ Smoke test passed! API connection is working.")
except Exception as e:
    print(f"\n✗ Smoke test failed with error: {e}")
    print("\nCommon issues:")
    print("  - 401/403: Check your keys, Client ID, or API member permissions")
    print("  - 404: Verify your host and codebase are correct")
    print("  - Network errors: Check your internet connection and firewall settings")
    raise
