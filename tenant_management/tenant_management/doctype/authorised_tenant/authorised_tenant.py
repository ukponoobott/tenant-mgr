# -*- coding: utf-8 -*-
# Copyright (c) 2019, Ukpono Obott and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class AuthorisedTenant(Document):
	def validate(self):
		if property_name != confirm_property:
			frappe.throw(_("Property does not match"))
