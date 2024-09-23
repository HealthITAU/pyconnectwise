import os
import pathlib

# Load the .env file
from dotenv import load_dotenv

from pyconnectwise.clients.change_request_client import ConnectWiseChangeApprovalClient
from pyconnectwise.types import ConnectWiseChangeApprovalRequestParams

current_path = pathlib.Path(__file__).parent.resolve()
# In current directory, load the .env file
assert load_dotenv(os.path.join(current_path, ".env"))


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
    client.auth_login()
    change_approval = client.change_request.id(change_request_id).get()
    assert change_approval.id == change_request_id
    change_approvals = client.change_request.get(params=ConnectWiseChangeApprovalRequestParams(orderBy=[{"updated": -1}]))
    assert len(change_approvals) > 0


def test_get_user():
    # Testing with real data. :D
    test_id = "642bfee39d2d780477bdc662"
    client = change_approval_client_init()
    client.auth_login()
    user_info = client.users.id(test_id).get()
    assert user_info.id == test_id


def test_get_acl_roles():
    client = change_approval_client_init()
    client.auth_login()
    obj_data = client.acl_roles.get()
    assert obj_data is not None
    assert len(obj_data) > 0

    obj_filter_data = client.acl_roles.get(
        params=ConnectWiseChangeApprovalRequestParams(perColConditions={"Member_RecID": client.login_msg.rec_id})
    )
    assert obj_filter_data is not None
    assert len(obj_filter_data) > 0


def test_get_settings():
    client = change_approval_client_init()
    client.auth_login()
    obj_filter_data = client.settings.get()
    assert obj_filter_data is not None
    assert len(obj_filter_data) > 0
    obj_filter_data = client.settings.get(
        params=ConnectWiseChangeApprovalRequestParams(perColConditions={"name": "DefaultSettings"})
    )
    assert obj_filter_data is not None
    assert len(obj_filter_data) > 0


def test_get_templates():
    client = change_approval_client_init()
    client.auth_login()
    obj_filter_data = client.template.get(
        params=ConnectWiseChangeApprovalRequestParams(perColConditions={"category": "My Templates"})
    )
    assert obj_filter_data is not None
    assert len(obj_filter_data) > 0


def test_get_stats():
    client = change_approval_client_init()
    client.auth_login()
    # TODO - Figure out what 120-timeDuration means
    final_stats = client.get_stats.post(data={"timeDuration": 120})
    assert final_stats is not None
    assert len(final_stats) > 0


def test_login():
    client = change_approval_client_init()
    client.auth_login()
    assert True
