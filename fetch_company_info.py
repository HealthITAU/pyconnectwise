"""
Helper script to fetch company info from ConnectWise.

This can help you determine your company name and verify the codebase.

Usage:
    export CW_COMPANY="yourCompanyLoginName"  # Try different variations if unsure
    export CW_HOST="https://na.myconnectwise.net"  # Your UI host
    python fetch_company_info.py
"""
import os
import requests
from urllib.parse import urlparse

CW_COMPANY = os.environ.get("CW_COMPANY", "")
CW_HOST = os.environ.get("CW_HOST", "https://na.myconnectwise.net")

# Parse hostname
parsed = urlparse(CW_HOST)
hostname = parsed.netloc or parsed.path.replace("https://", "").replace("http://", "").strip("/")

# Try to fetch company info
# The endpoint is: https://{hostname}/login/companyinfo/{company_name}
if not CW_COMPANY:
    print("Please set CW_COMPANY environment variable")
    print("Example: export CW_COMPANY='yourCompanyName'")
    exit(1)

url = f"https://{hostname}/login/companyinfo/{CW_COMPANY}"
print(f"Fetching company info from: {url}")

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("\n✓ Successfully retrieved company info:")
        print(f"  Company Name: {data.get('CompanyName', 'N/A')}")
        print(f"  Codebase: {data.get('Codebase', 'N/A')}")
        print(f"  Full URL: {data.get('FullUrl', 'N/A')}")
        print("\nUse these values in your smoke test:")
        print(f"  export CW_COMPANY='{data.get('CompanyName', CW_COMPANY)}'")
        print(f"  export CW_CODEBASE='{data.get('Codebase', 'v2025_1')}'")
    else:
        print(f"\n✗ Failed with status {response.status_code}")
        print(f"  Response: {response.text}")
        print("\nPossible issues:")
        print("  - Company name is incorrect (try different variations)")
        print("  - Company name might be case-sensitive")
        print("  - Check if you need to use a different host (e.g., api-na.myconnectwise.net)")
except Exception as e:
    print(f"\n✗ Error: {e}")
    print("\nNote: This endpoint might require authentication or might not be accessible.")
    print("You can also manually check your ConnectWise login page for the company name.")
