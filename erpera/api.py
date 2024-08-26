#delete company using sql
import frappe
@frappe.whitelist()
def delete_company():
    company = "Reformiqo"
    frappe.db.sql("DELETE FROM `tabCompany` WHERE name = %s", company)
    frappe.db.commit()
   