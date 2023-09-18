from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ProcurementAdjustmentsEndpoint import ProcurementAdjustmentsEndpoint
from pyconnectwise.endpoints.manage.ProcurementCatalogEndpoint import ProcurementCatalogEndpoint
from pyconnectwise.endpoints.manage.ProcurementCategoriesEndpoint import ProcurementCategoriesEndpoint
from pyconnectwise.endpoints.manage.ProcurementDirectionalsyncsEndpoint import ProcurementDirectionalsyncsEndpoint
from pyconnectwise.endpoints.manage.ProcurementManufacturersEndpoint import ProcurementManufacturersEndpoint
from pyconnectwise.endpoints.manage.ProcurementOnhandserialnumbersEndpoint import ProcurementOnhandserialnumbersEndpoint
from pyconnectwise.endpoints.manage.ProcurementPricingschedulesEndpoint import ProcurementPricingschedulesEndpoint
from pyconnectwise.endpoints.manage.ProcurementProductsEndpoint import ProcurementProductsEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseordersEndpoint import ProcurementPurchaseordersEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseorderstatusesEndpoint import \
    ProcurementPurchaseorderstatusesEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchasingdemandsEndpoint import ProcurementPurchasingdemandsEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmaactionsEndpoint import ProcurementRmaactionsEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmadispositionsEndpoint import ProcurementRmadispositionsEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmastatusesEndpoint import ProcurementRmastatusesEndpoint
from pyconnectwise.endpoints.manage.ProcurementRmatagsEndpoint import ProcurementRmatagsEndpoint
from pyconnectwise.endpoints.manage.ProcurementSettingsEndpoint import ProcurementSettingsEndpoint
from pyconnectwise.endpoints.manage.ProcurementShipmentmethodsEndpoint import ProcurementShipmentmethodsEndpoint
from pyconnectwise.endpoints.manage.ProcurementSubcategoriesEndpoint import ProcurementSubcategoriesEndpoint
from pyconnectwise.endpoints.manage.ProcurementTypesEndpoint import ProcurementTypesEndpoint
from pyconnectwise.endpoints.manage.ProcurementUnitofmeasuresEndpoint import ProcurementUnitofmeasuresEndpoint
from pyconnectwise.endpoints.manage.ProcurementWarehousebinsEndpoint import ProcurementWarehousebinsEndpoint
from pyconnectwise.endpoints.manage.ProcurementWarehousesEndpoint import ProcurementWarehousesEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ProcurementEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "procurement", parent_endpoint=parent_endpoint)

        self.pricingschedules = self._register_child_endpoint(
            ProcurementPricingschedulesEndpoint(client, parent_endpoint=self)
        )
        self.manufacturers = self._register_child_endpoint(
            ProcurementManufacturersEndpoint(client, parent_endpoint=self)
        )
        self.purchasing_demands = self._register_child_endpoint(
            ProcurementPurchasingdemandsEndpoint(client, parent_endpoint=self)
        )
        self.catalog = self._register_child_endpoint(ProcurementCatalogEndpoint(client, parent_endpoint=self))
        self.categories = self._register_child_endpoint(ProcurementCategoriesEndpoint(client, parent_endpoint=self))
        self.warehouse_bins = self._register_child_endpoint(
            ProcurementWarehousebinsEndpoint(client, parent_endpoint=self)
        )
        self.r_m_a_dispositions = self._register_child_endpoint(
            ProcurementRmadispositionsEndpoint(client, parent_endpoint=self)
        )
        self.types = self._register_child_endpoint(ProcurementTypesEndpoint(client, parent_endpoint=self))
        self.unit_of_measures = self._register_child_endpoint(
            ProcurementUnitofmeasuresEndpoint(client, parent_endpoint=self)
        )
        self.settings = self._register_child_endpoint(ProcurementSettingsEndpoint(client, parent_endpoint=self))
        self.shipmentmethods = self._register_child_endpoint(
            ProcurementShipmentmethodsEndpoint(client, parent_endpoint=self)
        )
        self.subcategories = self._register_child_endpoint(
            ProcurementSubcategoriesEndpoint(client, parent_endpoint=self)
        )
        self.rma_actions = self._register_child_endpoint(ProcurementRmaactionsEndpoint(client, parent_endpoint=self))
        self.rma_tags = self._register_child_endpoint(ProcurementRmatagsEndpoint(client, parent_endpoint=self))
        self.rma_statuses = self._register_child_endpoint(ProcurementRmastatusesEndpoint(client, parent_endpoint=self))
        self.purchaseorders = self._register_child_endpoint(
            ProcurementPurchaseordersEndpoint(client, parent_endpoint=self)
        )
        self.onhandserialnumbers = self._register_child_endpoint(
            ProcurementOnhandserialnumbersEndpoint(client, parent_endpoint=self)
        )
        self.adjustments = self._register_child_endpoint(ProcurementAdjustmentsEndpoint(client, parent_endpoint=self))
        self.warehouses = self._register_child_endpoint(ProcurementWarehousesEndpoint(client, parent_endpoint=self))
        self.purchaseorderstatuses = self._register_child_endpoint(
            ProcurementPurchaseorderstatusesEndpoint(client, parent_endpoint=self)
        )
        self.directional_syncs = self._register_child_endpoint(
            ProcurementDirectionalsyncsEndpoint(client, parent_endpoint=self)
        )
        self.products = self._register_child_endpoint(ProcurementProductsEndpoint(client, parent_endpoint=self))
