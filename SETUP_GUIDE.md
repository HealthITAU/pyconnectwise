# ConnectWise Manage API Setup Guide

Based on your ConnectWise instance, here's your setup information:

## Your ConnectWise Instance Details

- **UI Host**: `na.myconnectwise.net`
- **API Host**: `api-na.myconnectwise.net` (typical API endpoint)
- **Codebase**: `v2025_1` (from your URL)

## Step 1: Install the Repository

### Option A: Poetry (Recommended)
```bash
cd /Users/samstacks/.cursor/worktrees/pyconnectwise/yqh
poetry install --with dev
poetry run python -c "import pyconnectwise; print('ok')"
```

### Option B: venv + editable install
```bash
cd /Users/samstacks/.cursor/worktrees/pyconnectwise/yqh
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
python -c "import pyconnectwise; print('ok')"
```

## Step 2: Gather Your Credentials

You need **5 pieces of information**:

1. **CW_COMPANY**: Your ConnectWise login "Company" name
   - This is the value you type in the Company field on the login screen
   - You can try fetching it: `python fetch_company_info.py` (set CW_COMPANY first)

2. **CW_HOST**: `https://api-na.myconnectwise.net`
   - This is your API host (different from UI host)

3. **CW_CODEBASE**: `v2025_1`
   - Already known from your URL
   - Can be auto-detected if omitted

4. **CW_CLIENT_ID**: Your ConnectWise API Client ID
   - Get this from ConnectWise Developer Portal
   - Required even with public/private keys

5. **CW_PUBLIC_KEY** & **CW_PRIVATE_KEY**: Your API keys
   - Generate these in ConnectWise (System → API Members → API Keys)
   - Rotate and re-create them if needed

## Step 3: Test Your Connection

### Quick Test - Fetch Company Info
```bash
export CW_COMPANY="yourCompanyLoginName"
export CW_HOST="https://na.myconnectwise.net"
python fetch_company_info.py
```

### Full Smoke Test
```bash
export CW_COMPANY="yourCompanyLoginName"
export CW_HOST="https://api-na.myconnectwise.net"
export CW_CODEBASE="v2025_1"
export CW_CLIENT_ID="your-client-id"
export CW_PUBLIC_KEY="your-public-key"
export CW_PRIVATE_KEY="your-private-key"

# With Poetry:
poetry run python smoke_test_manage.py

# With venv:
python smoke_test_manage.py
```

## Common Issues

### 401/403 Errors
- **Invalid keys**: Regenerate your public/private keys in ConnectWise
- **Missing Client ID**: Ensure CW_CLIENT_ID is set correctly
- **Permissions**: Check your API member's security role has proper permissions

### 404 Errors
- **Wrong host**: Try `api-na.myconnectwise.net` instead of `na.myconnectwise.net`
- **Wrong codebase**: Verify codebase version matches your instance
- **Wrong path**: Ensure URL format is `https://api-na.myconnectwise.net/v2025_1/apis/3.0`

### Codebase Detection Fails
- Manually set `CW_CODEBASE` environment variable
- Or pass `codebase` parameter directly to `ConnectWiseManageAPIClient`

## Next Steps

Once your smoke test passes, you can:
1. Fetch your assigned tickets
2. Get recent activities
3. Create/update records (with proper permissions)

## Need Help?

If you're stuck, provide:
1. Your ConnectWise "Company" login name
2. Whether you have a Client ID (yes/no)

And I can help you troubleshoot further!
