import os

# Load the .env file
from dotenv import load_dotenv

from pyconnectwise.clients.change_request_client import ConnectWiseChangeApprovalClient
import pathlib
current_path = pathlib.Path(__file__).parent.resolve()
# In current directory, load the .env file
assert load_dotenv(os.path.join(current_path,".env"))


def change_approval_client_init():
    client = ConnectWiseChangeApprovalClient(
        company_name=os.environ["CW_COMPANY_NAME"],
        manage_url=os.environ["CW_MANAGE_URL"],
        client_id=os.environ["CW_CLIENT_ID"],
        member_hash=os.environ["CW_MEMBER_HASH"],
        member_id=os.environ["CW_MEMBER_ID"],
        login_username=os.environ["CW_LOGIN_USERNAME"],
        login_password=os.environ["CW_LOGIN_PASSWORD"],
        login_role=os.environ["CW_LOGIN_ROLE"],
        login_partner_id=os.environ["CW_LOGIN_PARTNER_ID"],
    )
    return client


def test_change_approval_client_init():
    client = change_approval_client_init()
    assert client.company_name == os.environ["CW_COMPANY_NAME"]
    assert client.manage_url == os.environ["CW_MANAGE_URL"]
    assert client.client_id == os.environ["CW_CLIENT_ID"]
    assert client.member_hash == os.environ["CW_MEMBER_HASH"]
    assert client.member_id == os.environ["CW_MEMBER_ID"]


def test_get_change_approval():
    # Testing with real data. :D
    change_request_id = "66ed7a101336c1045d07502f"
    client = change_approval_client_init()
    client.login()
    change_approval = client.change_request.id(change_request_id).get()
    assert change_approval.id == change_request_id


def test_get_user():
    # Testing with real data. :D
    test_id = "642bfee39d2d780477bdc662"
    client = change_approval_client_init()
    client.login()
    user_info = client.users.id(test_id).get()
    assert user_info.id == test_id


def test_login():
    client = change_approval_client_init()
    client.login()
    assert True
