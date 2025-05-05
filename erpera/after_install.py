import requests

import frappe

# generate api keys for the user admin 
@frappe.whitelist(allow_guest=True)
def after_install():

    user_details = frappe.get_doc('User', "Administrator")
    
    api_secret = frappe.generate_hash(length=15)

    api_key = frappe.generate_hash(length=15)
    user_details.api_key = api_key

    user_details.api_secret = api_secret
    
    user_details.save(ignore_permissions=True)
    frappe.db.commit()
    get_site_details(api_key, api_secret)




@frappe.whitelist(allow_guest=True)
def get_site_details(api_key, api_secret):
    domain = frappe.utils.get_url()
    site_name = domain.split(".")[0]
    site_name = site_name.replace("https://", "")
    site_name = site_name.replace("http://", "")
    response = requests.get(f"{domain}/api/method/reformiqo.utils.set_site_admin_details?site_name={site_name}&api_key={api_key}&api_secret={api_secret}")
    return response.json()
