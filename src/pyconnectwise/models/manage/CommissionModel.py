from __future__ import annotations
from typing import Any
from datetime import datetime
from pyconnectwise.utils.naming import to_camel_case
from pyconnectwise.models.base.connectwise_model import ConnectWiseModel
from pyconnectwise.models.manage.MemberReferenceModel import MemberReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from pyconnectwise.models.manage.SystemDepartmentReferenceModel import SystemDepartmentReferenceModel
from pyconnectwise.models.manage.CompanyReferenceModel import CompanyReferenceModel
from pyconnectwise.models.manage.SiteReferenceModel import SiteReferenceModel
from pyconnectwise.models.manage.AgreementReferenceModel import AgreementReferenceModel
from pyconnectwise.models.manage.ProjectReferenceModel import ProjectReferenceModel
from pyconnectwise.models.manage.BoardReferenceModel import BoardReferenceModel
from pyconnectwise.models.manage.TicketReferenceModel import TicketReferenceModel
from pyconnectwise.models.manage.SystemLocationReferenceModel import SystemLocationReferenceModel
from enum import Enum
from pyconnectwise.models.manage.ServiceTypeReferenceModel import ServiceTypeReferenceModel
from pyconnectwise.models.manage.ProjectBoardReferenceModel import ProjectBoardReferenceModel
from pyconnectwise.models.manage.ProjectTypeReferenceModel import ProjectTypeReferenceModel
from pyconnectwise.models.manage.AgreementTypeReferenceModel import AgreementTypeReferenceModel
from pyconnectwise.models.manage.ProductCategoryReferenceModel import ProductCategoryReferenceModel
from pyconnectwise.models.manage.ProductSubCategoryReferenceModel import ProductSubCategoryReferenceModel
from pyconnectwise.models.manage.IvItemReferenceModel import IvItemReferenceModel
class BillingMethod(str, Enum):
    Agreement = 'Agreement'
    CreditMemo = 'CreditMemo'
    DownPayment = 'DownPayment'
    Miscellaneous = 'Miscellaneous'
    Progress = 'Progress'
    Standard = 'Standard'
class CommissionBasis(str, Enum):
    GrossProfit = 'GrossProfit'
    SalesAmount = 'SalesAmount'
class InvoiceOption(str, Enum):
    AllInvoices = 'AllInvoices'
    PaidInvoices = 'PaidInvoices'

class CommissionModel(ConnectWiseModel):
    id: int
    member: MemberReferenceModel
    commission_percent: float
    date_start: str
    date_end: str
    location: SystemLocationReferenceModel
    department: SystemDepartmentReferenceModel
    company: CompanyReferenceModel
    site: SiteReferenceModel
    agreement: AgreementReferenceModel
    project: ProjectReferenceModel
    service_board: BoardReferenceModel
    ticket: TicketReferenceModel
    territory: SystemLocationReferenceModel
    billing_method: BillingMethod
    service_type: ServiceTypeReferenceModel
    project_board: ProjectBoardReferenceModel
    project_type: ProjectTypeReferenceModel
    agreement_type: AgreementTypeReferenceModel
    number_of_months: int
    product_category: ProductCategoryReferenceModel
    product_sub_category: ProductSubCategoryReferenceModel
    item: IvItemReferenceModel
    commission_basis: CommissionBasis
    invoice_option: InvoiceOption
    services_flag: bool
    agreements_flag: bool
    products_flag: bool
    my_opportunities_flag: bool
    _info: dict[str, str]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
        use_enum_values = True