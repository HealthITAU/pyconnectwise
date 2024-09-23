from datetime import datetime
from typing import Annotated

from pydantic import Field

from pyconnectwise.models.base.connectwise_model import ConnectWiseModel


class ChangeRequestBundledtickets(ConnectWiseModel):
    company_name: Annotated[str | None, Field(alias="CompanyName")] = None
    ticket_number: Annotated[str | None, Field(alias="ticketNumber")] = None
    summary: Annotated[str | None, Field(alias="summary")] = None


class ChangeRequestAffectedci(ConnectWiseModel):
    id: Annotated[str | None, Field(alias="Id")] = None
    configuration_type: Annotated[str | None, Field(alias="ConfigurationType")] = None
    status: Annotated[str | None, Field(alias="Status")] = None
    configuration_name: Annotated[str | None, Field(alias="ConfigurationName")] = None
    serial_number: Annotated[str | None, Field(alias="SerialNumber")] = None
    contact_name: Annotated[str | None, Field(alias="ContactName")] = None


class ChangeRequestSelectedsitedetails(ConnectWiseModel):
    site_name: Annotated[str | None, Field(alias="SiteName")] = None
    country: Annotated[str | None, Field(alias="Country")] = None


class ChangeRequestOwnerselected(ConnectWiseModel):
    member_rec_id: Annotated[str | None, Field(alias="Member_RecID")] = None
    member_id: Annotated[str | None, Field(alias="Member_ID")] = None
    first_name: Annotated[str | None, Field(alias="First_Name")] = None
    last_name: Annotated[str | None, Field(alias="Last_Name")] = None
    country: Annotated[str | None, Field(alias="Country")] = None
    work_role: Annotated[str | None, Field(alias="Work_Role")] = None


class ChangeRequestContactselected(ConnectWiseModel):
    contact_rec_id: Annotated[str | None, Field(alias="Contact_RecID")] = None
    company_rec_id: Annotated[str | None, Field(alias="Company_RecID")] = None
    company_id: Annotated[str | None, Field(alias="Company_ID")] = None
    first_name: Annotated[str | None, Field(alias="First_Name")] = None
    last_name: Annotated[str | None, Field(alias="Last_Name")] = None
    default_flag: Annotated[str | None, Field(alias="Default_Flag")] = None
    default_phone: Annotated[str | None, Field(alias="Default_Phone")] = None
    default_email: Annotated[str | None, Field(alias="Default_Email")] = None
    country: Annotated[str | None, Field(alias="Country")] = None


class ChangeRequestCompanyselected(ConnectWiseModel):
    city: Annotated[str | None, Field(alias="City")] = None
    fax_number: Annotated[str | None, Field(alias="FaxNumber")] = None
    default_contact_id: Annotated[str | None, Field(alias="DefaultContactId")] = None
    zip: Annotated[str | None, Field(alias="Zip")] = None
    website: Annotated[str | None, Field(alias="Website")] = None
    country: Annotated[str | None, Field(alias="Country")] = None
    site: Annotated[str | None, Field(alias="Site")] = None
    updated_by: Annotated[str | None, Field(alias="UpdatedBy")] = None
    territory: Annotated[str | None, Field(alias="Territory")] = None
    last_updated: Annotated[str | None, Field(alias="LastUpdated")] = None
    company_rec_id: Annotated[str | None, Field(alias="Company_RecID")] = None
    company_name: Annotated[str | None, Field(alias="Company_Name")] = None
    company_id: Annotated[str | None, Field(alias="Company_ID")] = None
    lead_flag: Annotated[str | None, Field(alias="Lead_Flag")] = None
    phone_nbr: Annotated[str | None, Field(alias="PhoneNbr")] = None
    status: Annotated[str | None, Field(alias="status")] = None
    state_id: Annotated[str | None, Field(alias="State_ID")] = None
    address_line1: Annotated[str | None, Field(alias="Address_Line1")] = None
    address_line2: Annotated[str | None, Field(alias="Address_Line2")] = None


class ChangeRequestCustomform(ConnectWiseModel):
    id: Annotated[str | None, Field(alias="id")] = None
    label: Annotated[str | None, Field(alias="label")] = None
    value: Annotated[str | None, Field(alias="value")] = None
    required: Annotated[bool | None, Field(alias="required")] = None
    component: Annotated[str | None, Field(alias="component")] = None


class ChangeRequestApproved(ConnectWiseModel):
    updated: Annotated[int | None, Field(alias="updated")] = None


class ChangeRequestAgingnotifications(ConnectWiseModel):
    approved: Annotated[ChangeRequestApproved | None, Field(alias="Approved")] = None


class ChangeRequestMembers(ConnectWiseModel):
    member_id: Annotated[str | None, Field(alias="memberId")] = None
    mail: Annotated[bool | None, Field(alias="mail")] = None
    mailsentkey: Annotated[int | None, Field(alias="mailsentkey")] = None
    notes: Annotated[str | None, Field(alias="notes")] = None
    approvedcreatedtime: Annotated[int | None, Field(alias="approvedcreatedtime")] = None
    approval: Annotated[str | bool | None, Field(alias="approval")] = None


class ChangeRequestNotifications(ConnectWiseModel):
    status: Annotated[str | None, Field(alias="status")] = None
    members: Annotated[list[ChangeRequestMembers] | None, Field(alias="members")] = None
    template: Annotated[str | None, Field(alias="template")] = None


class ChangeRequestConnectwiseServiceTypes(ConnectWiseModel):
    s_r_type_rec_id: Annotated[str | None, Field(alias="SR_Type_RecID")] = None
    service_type: Annotated[str | None, Field(alias="ServiceType")] = None
    s_r_board_rec_id: Annotated[str | None, Field(alias="SR_Board_RecID")] = None
    board_name: Annotated[str | None, Field(alias="Board_Name")] = None
    inactive_flag: Annotated[str | None, Field(alias="Inactive_Flag")] = None
    updated_by: Annotated[str | None, Field(alias="Updated_By")] = None
    default_flag: Annotated[str | None, Field(alias="Default_Flag")] = None


class ChangeRequestConnectwiseServiceSubtypes(ConnectWiseModel):
    s_r_sub_type_rec_id: Annotated[str | None, Field(alias="SR_SubType_RecID")] = None
    service_sub_type_desc: Annotated[str | None, Field(alias="ServiceSubTypeDesc")] = None
    s_r_board_rec_id: Annotated[str | None, Field(alias="SR_Board_RecID")] = None
    board_name: Annotated[str | None, Field(alias="Board_Name")] = None
    inactive_flag: Annotated[str | None, Field(alias="Inactive_Flag")] = None
    s_r_type_rec_id: Annotated[str | None, Field(alias="SR_Type_RecID")] = None
    service_type_desc: Annotated[str | None, Field(alias="ServiceTypeDesc")] = None
    updated_by: Annotated[str | None, Field(alias="Updated_By")] = None


class ChangeRequestConnectwiseServicePriorities(ConnectWiseModel):
    s_r_urgency_rec_id: Annotated[str | None, Field(alias="SR_Urgency_RecID")] = None
    service_priority_desc: Annotated[str | None, Field(alias="Service_Priority_Desc")] = None
    sort_order: Annotated[str | None, Field(alias="Sort_Order")] = None
    color: Annotated[str | None, Field(alias="Color")] = None
    default_flag: Annotated[str | None, Field(alias="Default_Flag")] = None
    updated_by: Annotated[str | None, Field(alias="Updated_By")] = None


class ChangeRequestMsg(ConnectWiseModel):
    id: Annotated[str | None, Field(alias="_id")] = None
    bundled_tickets: Annotated[list[ChangeRequestBundledtickets] | None, Field(alias="bundledTickets")] = None
    project_tickets_arr: Annotated[list | None, Field(alias="projectTicketsArr")] = None
    affected_c_i: Annotated[list[ChangeRequestAffectedci] | None, Field(alias="affectedCI")] = None
    company_id: Annotated[str | None, Field(alias="companyId")] = None
    change_request_name: Annotated[str | None, Field(alias="changeRequestName")] = None
    selected_site_details: Annotated[ChangeRequestSelectedsitedetails | None, Field(alias="selectedSiteDetails")] = None
    contact_id: Annotated[str | None, Field(alias="contactId")] = None
    short_desc: Annotated[str | None, Field(alias="shortDesc")] = None
    is_converted_service_ticket: Annotated[bool | None, Field(alias="isConvertedServiceTicket")] = None
    from_service_ticket: Annotated[str | None, Field(alias="fromServiceTicket")] = None
    priority: Annotated[str | None, Field(alias="priority")] = None
    category: Annotated[str | None, Field(alias="Category")] = None
    sub_category: Annotated[str | None, Field(alias="subCategory")] = None
    created_by: Annotated[str | None, Field(alias="createdBy")] = None
    notifications: Annotated[list[ChangeRequestNotifications] | None, Field(alias="notifications")] = None
    approval_status: Annotated[str | None, Field(alias="approvalStatus")] = None
    number: Annotated[str | None, Field(alias="number")] = None
    # TODO - Handle unix timestamps to datetime!
    requested_by_date: Annotated[int | datetime | None, Field(alias="requestedByDate")] = None
    planned_start_date: Annotated[int | datetime | None, Field(alias="plannedStartDate")] = None
    planned_end_date: Annotated[int | datetime | None, Field(alias="plannedEndDate")] = None
    work_start: Annotated[int | datetime | None, Field(alias="workStart")] = None
    work_end: Annotated[int | datetime | None, Field(alias="workEnd")] = None
    enable_schedule: Annotated[bool | None, Field(alias="enableSchedule")] = None
    approval_emails: Annotated[list | None, Field(alias="approvalEmails")] = None
    tmp_affected_c_i: Annotated[str | None, Field(alias="tmpAffectedCI")] = None
    creator_firstname: Annotated[str | None, Field(alias="creator_firstname")] = None
    creator_lastname: Annotated[str | None, Field(alias="creator_lastname")] = None
    owner_selected: Annotated[ChangeRequestOwnerselected | None, Field(alias="ownerSelected")] = None
    member_id: Annotated[str | None, Field(alias="memberId")] = None
    contact_selected: Annotated[ChangeRequestContactselected | None, Field(alias="contactSelected")] = None
    contact_name: Annotated[str | None, Field(alias="contactName")] = None
    company_selected: Annotated[ChangeRequestCompanyselected | None, Field(alias="companySelected")] = None
    company_name: Annotated[str | None, Field(alias="companyName")] = None
    site_id: Annotated[str | None, Field(alias="siteId")] = None
    highest_number: Annotated[int | None, Field(alias="highestNumber")] = None
    impact: Annotated[str | None, Field(alias="impact")] = None
    likelihood: Annotated[str | None, Field(alias="likelihood")] = None
    risk: Annotated[str | None, Field(alias="risk")] = None
    change_type_id: Annotated[str | None, Field(alias="changeTypeId")] = None
    change_type_name: Annotated[str | None, Field(alias="changeTypeName")] = None
    approval_group_name: Annotated[str | None, Field(alias="approvalGroupName")] = None
    over_ride_approval_group: Annotated[bool | None, Field(alias="OverRideApprovalGroup")] = None
    steps: Annotated[list | None, Field(alias="steps")] = None
    requested_by_time: Annotated[str | None, Field(alias="requestedByTime")] = None
    planned_star_time: Annotated[str | None, Field(alias="plannedStarTime")] = None
    work_start_time: Annotated[str | None, Field(alias="workStartTime")] = None
    custom_form: Annotated[list[ChangeRequestCustomform] | None, Field(alias="customForm")] = None
    requested_by_time_added: Annotated[bool | None, Field(alias="requestedByTimeAdded")] = None
    planned_start_time_added: Annotated[bool | None, Field(alias="plannedStartTimeAdded")] = None
    work_start_time_added: Annotated[bool | None, Field(alias="workStartTimeAdded")] = None
    planned_end_time_added: Annotated[bool | None, Field(alias="plannedEndTimeAdded")] = None
    work_end_time_added: Annotated[bool | None, Field(alias="workEndTimeAdded")] = None
    is_approved: Annotated[bool | str | None, Field(alias="isApproved")] = None
    risk_token: Annotated[str | None, Field(alias="risk_token")] = None
    aging_notifications: Annotated[ChangeRequestAgingnotifications | None, Field(alias="agingNotifications")] = None
    created: Annotated[int | None, Field(alias="created")] = None
    updated: Annotated[int | None, Field(alias="updated")] = None
    partner_id: Annotated[str | None, Field(alias="partnerId")] = None
    member_rand_strings: Annotated[dict[str, str] | None, Field(alias="memberRandStrings")] = None
    members: Annotated[list[ChangeRequestMembers] | None, Field(alias="members")] = None
    approve_encoded: Annotated[str | None, Field(alias="approveEncoded")] = None
    emergency_status: Annotated[str | None, Field(alias="emergencyStatus")] = None
    planned_starting_date: Annotated[str | None, Field(alias="plannedStartingDate")] = None
    reject_encoded: Annotated[str | None, Field(alias="rejectEncoded")] = None
    requestedby_date: Annotated[str | None, Field(alias="requestedbyDate")] = None
    work_starting_date: Annotated[str | None, Field(alias="workStartingDate")] = None
    connectwise_service_types: Annotated[
        list[ChangeRequestConnectwiseServiceTypes] | None, Field(alias="connectwise_service_types")
    ] = None
    connectwise_service_subtypes: Annotated[
        list[ChangeRequestConnectwiseServiceSubtypes] | None, Field(alias="connectwise_service_subtypes")
    ] = None
    connectwise_service_priorities: Annotated[
        list[ChangeRequestConnectwiseServicePriorities] | None, Field(alias="connectwise_service_priorities")
    ] = None


class ChangeRequestObject(ConnectWiseModel):
    status: Annotated[str | None, Field(alias="status")] = None
    msg: Annotated[ChangeRequestMsg | None, Field(alias="msg")] = None


class ChangeRequestGetMsg(ConnectWiseModel):
    total: Annotated[int | None, Field(alias="total")] = None
    current: Annotated[int | None, Field(alias="current")] = None
    data: Annotated[list[ChangeRequestMsg] | None, Field(alias="data")] = None


class ChangeRequestGetObject(ConnectWiseModel):
    status: Annotated[str | None, Field(alias="status")] = None
    msg: Annotated[ChangeRequestGetMsg | None, Field(alias="msg")] = None


class ChangeTypeForm(ConnectWiseModel):
    component: Annotated[str | None, Field(alias="component")] = None
    editable: Annotated[bool | None, Field(alias="editable")] = None
    index: Annotated[int | None, Field(alias="index")] = None
    label: Annotated[str | None, Field(alias="label")] = None
    description: Annotated[str | None, Field(alias="description")] = None
    placeholder: Annotated[str | None, Field(alias="placeholder")] = None
    options: Annotated[list | None, Field(alias="options")] = None
    required: Annotated[bool | None, Field(alias="required")] = None
    validation: Annotated[str | None, Field(alias="validation")] = None


class ChangeTypeData(ConnectWiseModel):
    _id: Annotated[str | None, Field(alias="_id")] = None
    steps: Annotated[list | None, Field(alias="steps")] = None
    change_type_name: Annotated[str | None, Field(alias="changeTypeName")] = None
    approval_group_id: Annotated[str | None, Field(alias="approvalGroupId")] = None
    template_id: Annotated[str | None, Field(alias="templateId")] = None
    approval_type: Annotated[str | None, Field(alias="approvalType")] = None
    over_ride_approval_group: Annotated[bool | None, Field(alias="overRideApprovalGroup")] = None
    enable_schedule: Annotated[bool | None, Field(alias="enableSchedule")] = None
    approval_group_name: Annotated[str | None, Field(alias="approvalGroupName")] = None
    created: Annotated[int | None, Field(alias="created")] = None
    updated: Annotated[int | None, Field(alias="updated")] = None
    partner_id: Annotated[str | None, Field(alias="partnerId")] = None
    form: Annotated[list[ChangeTypeForm] | None, Field(alias="form")] = None
    selected_change_types: Annotated[bool | None, Field(alias="SelectedChangeTypes")] = None


class ChangeTypeMsg(ConnectWiseModel):
    total: Annotated[int | None, Field(alias="total")] = None
    current: Annotated[int | None, Field(alias="current")] = None
    data: Annotated[list[ChangeTypeData] | None, Field(alias="data")] = None


class ChangeTypeObject(ConnectWiseModel):
    status: Annotated[str | None, Field(alias="status")] = None
    msg: Annotated[ChangeTypeMsg | None, Field(alias="msg")] = None


class UserIdMsg(ConnectWiseModel):
    id: Annotated[str | None, Field(alias="_id")] = None
    user_name: Annotated[str | None, Field(alias="userName")] = None
    company: Annotated[str | None, Field(alias="company")] = None
    domain: Annotated[str | None, Field(alias="domain")] = None
    role: Annotated[str | None, Field(alias="role")] = None
    password: Annotated[str | None, Field(alias="password")] = None
    status: Annotated[str | None, Field(alias="status")] = None
    wizard_complete: Annotated[bool | None, Field(alias="wizardComplete")] = None
    direct_ticket_url: Annotated[bool | None, Field(alias="directTicketUrl")] = None
    partner_id: Annotated[str | None, Field(alias="partnerId")] = None
    api_key: Annotated[str | None, Field(alias="apiKey")] = None
    created: Annotated[int | None, Field(alias="created")] = None
    updated: Annotated[int | None, Field(alias="updated")] = None
    is_agree: Annotated[bool | None, Field(alias="isAgree")] = None


class UserIdObject(ConnectWiseModel):
    status: Annotated[str | None, Field(alias="status")] = None
    msg: Annotated[UserIdMsg | None, Field(alias="msg")] = None


class AclRolesAcl(ConnectWiseModel):
    administration: Annotated[bool | None, Field(alias="administration")] = None
    billingprofile: Annotated[bool | None, Field(alias="billingprofile")] = None
    jobs: Annotated[bool | None, Field(alias="jobs")] = None
    companies: Annotated[bool | None, Field(alias="companies")] = None


class AclRolesData(ConnectWiseModel):
    _id: Annotated[str | None, Field(alias="_id")] = None
    first_name: Annotated[str | None, Field(alias="First_Name")] = None
    last_name: Annotated[str | None, Field(alias="Last_Name")] = None
    member_id: Annotated[str | None, Field(alias="Member_ID")] = None
    member_rec_id: Annotated[str | None, Field(alias="Member_RecID")] = None
    acl_group: Annotated[str | None, Field(alias="aclGroup")] = None
    acl: Annotated[AclRolesAcl | None, Field(alias="acl")] = None
    billing_unit_rec_id: Annotated[str | None, Field(alias="Billing_Unit_RecID")] = None
    created: Annotated[int | None, Field(alias="created")] = None
    updated: Annotated[int | None, Field(alias="updated")] = None
    partner_id: Annotated[str | None, Field(alias="partnerId")] = None


class AclRolesMsg(ConnectWiseModel):
    total: Annotated[int | None, Field(alias="total")] = None
    current: Annotated[int | None, Field(alias="current")] = None
    data: Annotated[list[AclRolesData] | None, Field(alias="data")] = None


class AclRolesObject(ConnectWiseModel):
    status: Annotated[str | None, Field(alias="status")] = None
    msg: Annotated[AclRolesMsg | None, Field(alias="msg")] = None


class LoginMsg(ConnectWiseModel):
    partner_id: Annotated[str | None, Field(alias="partnerId")] = None
    first_name: Annotated[str | None, Field(alias="firstName")] = None
    last_name: Annotated[str | None, Field(alias="lastName")] = None
    company_name: Annotated[str | None, Field(alias="companyName")] = None
    user_name: Annotated[str | None, Field(alias="userName")] = None
    concurrent_count: Annotated[int | None, Field(alias="concurrentCount")] = None
    role: Annotated[str | None, Field(alias="role")] = None
    isloggedin: Annotated[bool | None, Field(alias="isloggedin")] = None
    integrator_id: Annotated[str | None, Field(alias="integratorId")] = None
    domain: Annotated[str | None, Field(alias="domain")] = None
    integrator_company: Annotated[str | None, Field(alias="integratorCompany")] = None
    wizard_complete: Annotated[bool | None, Field(alias="wizardComplete")] = None
    direct_ticket_url: Annotated[bool | None, Field(alias="directTicketUrl")] = None
    rec_id: Annotated[str | None, Field(alias="RecId")] = None
    is_agree: Annotated[bool | None, Field(alias="isAgree")] = None
    version_code: Annotated[str | None, Field(alias="versionCode")] = None
    is_instance_login: Annotated[bool | None, Field(alias="isInstanceLogin")] = None


class SettingsOptions(ConnectWiseModel):
    hide_closed_cr: Annotated[bool | None, Field(alias="hideClosedCr")] = None
    latest_per_format: Annotated[int | None, Field(alias="latestPerFormat")] = None


class LoginObject(ConnectWiseModel):
    status: Annotated[str | None, Field(alias="status")] = None
    msg: Annotated[LoginMsg | None, Field(alias="msg")] = None


class SettingsData(ConnectWiseModel):
    _id: Annotated[str | None, Field(alias="_id")] = None
    options: Annotated[SettingsOptions | None, Field(alias="options")] = None
    name: Annotated[str | None, Field(alias="name")] = None
    partner_id: Annotated[str | None, Field(alias="partnerId")] = None
    created: Annotated[int | None, Field(alias="created")] = None
    updated: Annotated[int | None, Field(alias="updated")] = None


class SettingsMsg(ConnectWiseModel):
    total: Annotated[int | None, Field(alias="total")] = None
    current: Annotated[int | None, Field(alias="current")] = None
    data: Annotated[list[SettingsData] | None, Field(alias="data")] = None


class SettingsObject(ConnectWiseModel):
    status: Annotated[str | None, Field(alias="status")] = None
    msg: Annotated[SettingsMsg | None, Field(alias="msg")] = None


class StatsMsg(ConnectWiseModel):
    count: Annotated[int | None, Field(alias="count")] = None
    approval_status: Annotated[str | None, Field(alias="approvalStatus")] = None


class StatsObject(ConnectWiseModel):
    status: Annotated[str | None, Field(alias="status")] = None
    msg: Annotated[list[StatsMsg] | None, Field(alias="msg")] = None


class TemplateData(ConnectWiseModel):
    _id: Annotated[str | None, Field(alias="_id")] = None
    template_html: Annotated[str | None, Field(alias="template_html")] = None
    img_url: Annotated[str | None, Field(alias="imgUrl")] = None
    name: Annotated[str | None, Field(alias="name")] = None
    subject: Annotated[str | None, Field(alias="subject")] = None
    first_name: Annotated[str | None, Field(alias="firstName")] = None
    last_name: Annotated[str | None, Field(alias="lastName")] = None
    email_address: Annotated[str | None, Field(alias="emailAddress")] = None
    category: Annotated[str | None, Field(alias="category")] = None
    created: Annotated[int | None, Field(alias="created")] = None
    updated: Annotated[int | None, Field(alias="updated")] = None
    partner_id: Annotated[str | None, Field(alias="partnerId")] = None


class TemplateMsg(ConnectWiseModel):
    total: Annotated[int | None, Field(alias="total")] = None
    current: Annotated[int | None, Field(alias="current")] = None
    data: Annotated[list[TemplateData] | None, Field(alias="data")] = None


class TemplateObject(ConnectWiseModel):
    status: Annotated[str | None, Field(alias="status")] = None
    msg: Annotated[TemplateMsg | None, Field(alias="msg")] = None


class SetSettingsOptions(ConnectWiseModel):
    hide_closed_cr: Annotated[bool | None, Field(alias="hideClosedCr")] = None
    latest_per_format: Annotated[int | None, Field(alias="latestPerFormat")] = None


class SetSettingsMsg(ConnectWiseModel):
    id: Annotated[str | None, Field(alias="_id")] = None
    options: Annotated[SetSettingsOptions | None, Field(alias="options")] = None
    name: Annotated[str | None, Field(alias="name")] = None
    partner_id: Annotated[str | None, Field(alias="partnerId")] = None
    created: Annotated[int | None, Field(alias="created")] = None
    updated: Annotated[int | None, Field(alias="updated")] = None


class SetSettingsObject(ConnectWiseModel):
    status: Annotated[str | None, Field(alias="status")] = None
    msg: Annotated[SetSettingsMsg | None, Field(alias="msg")] = None


class ContactsData(ConnectWiseModel):
    contact_rec_id: Annotated[str | None, Field(alias="Contact_RecID")] = None
    company_rec_id: Annotated[str | None, Field(alias="Company_RecID")] = None
    company_id: Annotated[str | None, Field(alias="Company_ID")] = None
    first_name: Annotated[str | None, Field(alias="First_Name")] = None
    last_name: Annotated[str | None, Field(alias="Last_Name")] = None
    default_flag: Annotated[str | None, Field(alias="Default_Flag")] = None
    default_phone: Annotated[str | None, Field(alias="Default_Phone")] = None
    default_email: Annotated[str | None, Field(alias="Default_Email")] = None
    country: Annotated[str | None, Field(alias="Country")] = None


class ContactsMsg(ConnectWiseModel):
    total: Annotated[int | None, Field(alias="total")] = None
    current: Annotated[int | None, Field(alias="current")] = None
    data: Annotated[list[ContactsData] | None, Field(alias="data")] = None


class ContactsObject(ConnectWiseModel):
    status: Annotated[str | None, Field(alias="status")] = None
    msg: Annotated[ContactsMsg | None, Field(alias="msg")] = None
