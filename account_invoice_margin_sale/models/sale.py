# Copyright 2017-2018 Sergio Teruel <sergio.teruel@tecnativa.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.multi
    def _prepare_invoice_line(self, qty):
        vals = super()._prepare_invoice_line(qty)
        vals['purchase_price'] = self.purchase_price
        return vals
