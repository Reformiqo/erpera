import os
import subprocess
import frappe

@frappe.whitelist(allow_guest=True)
def get_site_storage():
    site_path = frappe.get_site_path()
    result = subprocess.check_output(['du', '-sh', site_path])
    return result.decode().split()[0] 



 # returns something like '128M'
@frappe.whitelist(allow_guest=True)
def get_database_size():
    site_db = frappe.get_site_config().get("db_name")

    size = frappe.db.sql(
        """
        SELECT SUM(data_length + index_length) / 1024 / 1024 AS size_mb
        FROM information_schema.tables 
        WHERE table_schema = %s
        """,
        (site_db,)
    )
    
    return round(size[0][0], 2)

@frappe.whitelist(allow_guest=True)
def get_user_count():
    users = frappe.db.sql(
        """
        SELECT COUNT(*) FROM `tabUser`
        """
    )
    return users[0][0]
    
@frappe.whitelist(allow_guest=True)
def activity_log():
    activities = frappe.get_all("Activity Log", 
    fields=["subject", "communication_date", "operation", "full_name", "user", "ip_address", "reference_doctype", "reference_name", "reference_owner"], 
    order_by="creation desc")
    return activities



@frappe.whitelist(allow_guest=True)
def get_site_info():
    storage = get_site_storage()
    user_count = get_user_count()
    database_size = get_database_size()
    activities = activity_log()
    return {
        "storage": storage,
        "user_count": user_count,
        "database_size": database_size,
        "activities": activities
    }
