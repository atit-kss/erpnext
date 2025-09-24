# Copyright (c) 2025, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ShippingInvoice(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from erpnext.accounts.doctype.advance_tax.advance_tax import AdvanceTax
		from erpnext.accounts.doctype.payment_schedule.payment_schedule import PaymentSchedule
		from erpnext.accounts.doctype.purchase_invoice_advance.purchase_invoice_advance import PurchaseInvoiceAdvance
		from frappe.model.document import Document
		from frappe.types import DF

		address_display: DF.SmallText | None
		advance_tax: DF.Table[AdvanceTax]
		advances: DF.Table[PurchaseInvoiceAdvance]
		against_expense_account: DF.SmallText | None
		allocate_advances_automatically: DF.Check
		amended_from: DF.Link | None
		auto_repeat: DF.Link | None
		base_paid_amount: DF.Currency
		base_write_off_amount: DF.Currency
		bill_of_lading: DF.Link | None
		billing_address: DF.Link | None
		billing_address_display: DF.SmallText | None
		buying_price_list: DF.Link | None
		carrier: DF.Link | None
		cash_bank_account: DF.Link | None
		clearance_date: DF.Date | None
		contact_display: DF.SmallText | None
		contact_email: DF.SmallText | None
		contact_mobile: DF.SmallText | None
		contact_person: DF.Link | None
		conversion_rate: DF.Float
		cost_center: DF.Link | None
		credit_to: DF.Link | None
		currency: DF.Link | None
		delivery_ticket: DF.Link | None
		discount_amount: DF.Currency
		discount_expiration_date: DF.Date | None
		discount_type: DF.Data | None
		from_date: DF.Date | None
		group_same_items: DF.Check
		hold_comment: DF.SmallText | None
		ignore_default_payment_terms_template: DF.Check
		ignore_pricing_rule: DF.Check
		inter_company_invoice_reference: DF.Link | None
		invoice_currency: DF.Link | None
		invoice_date: DF.Date
		invoice_no: DF.Data
		is_internal_supplier: DF.Check
		is_old_subcontracting_flow: DF.Check
		is_opening: DF.Literal["No", "Yes"]
		is_subcontracted: DF.Check
		items: DF.Table[Document]
		language: DF.Data | None
		letter_head: DF.Link | None
		mode_of_payment: DF.Link | None
		naming_series: DF.Literal["ACC-PINV-.YYYY.-", "ACC-PINV-RET-.YYYY.-"]
		on_hold: DF.Check
		only_include_allocated_payments: DF.Check
		other_charges: DF.TableMultiSelect[Document]
		paid_amount: DF.Currency
		party_account_currency: DF.Link | None
		payer: DF.Link | None
		payment_schedule: DF.Table[PaymentSchedule]
		payment_terms: DF.Link | None
		payment_terms_template: DF.Link | None
		per_received: DF.Percent
		plc_conversion_rate: DF.Float
		price_list_currency: DF.Link | None
		project: DF.Link | None
		purchase_order: DF.Link | None
		rejected_warehouse: DF.Link | None
		release_date: DF.Date | None
		remarks: DF.SmallText | None
		represents_company: DF.Link | None
		scan_barcode: DF.Data | None
		select_print_heading: DF.Link | None
		set_from_warehouse: DF.Link | None
		set_warehouse: DF.Link | None
		ship_date: DF.Date | None
		ship_time: DF.Time | None
		ship_to: DF.Link | None
		shipping_address: DF.Link | None
		shipping_address_display: DF.SmallText | None
		sold_to: DF.Link | None
		status: DF.Literal["", "Draft", "Return", "Debit Note Issued", "Submitted", "Paid", "Partly Paid", "Unpaid", "Overdue", "Cancelled", "Internal Transfer"]
		subscription: DF.Link | None
		supplier: DF.Link | None
		supplier_address: DF.Link | None
		supplier_group: DF.Link | None
		supplier_warehouse: DF.Link | None
		tax_amount: DF.Float
		tax_deferred_invoice_no: DF.Data | None
		taxes_charged: DF.TableMultiSelect[Document]
		taxes_deferred: DF.TableMultiSelect[Document]
		tc_name: DF.Link | None
		terminal: DF.Literal[None]
		terms: DF.TextEditor | None
		to_date: DF.Date | None
		total_w_tax: DF.Float
		total_wo_tax: DF.Float
		unrealized_profit_loss_account: DF.Link | None
		update_stock: DF.Check
		use_transaction_date_exchange_rate: DF.Check
		write_off_account: DF.Link | None
		write_off_amount: DF.Currency
		write_off_cost_center: DF.Link | None
	# end: auto-generated types
	pass
