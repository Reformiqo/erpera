import frappe
from frappe import _

#configure the system after the app is installed
def before_install():
    #create theme
    # if not frappe.db.exists("Website Theme", "Erpera"):
    #     create_theme()


    #edit the systemsettings doctype
    frappe.db.set_value("System Settings", "System Settings", "enable_onboarding", 0)
    frappe.db.commit()

    #edit the website settings doctype
    web_settings = frappe.get_doc("Website Settings")
    web_settings.disable_signup = 1
    # web_settings.website_theme = "Erpera"
    web_settings.banner_image = "https://ucarecdn.com/358ec918-a0b2-44ba-9fc0-f674e05f40d9/-/preview/768x133/"
    web_settings.splash_image = "https://ucarecdn.com/358ec918-a0b2-44ba-9fc0-f674e05f40d9/-/preview/768x133/"
    web_settings.favicon = "https://ucarecdn.com/358ec918-a0b2-44ba-9fc0-f674e05f40d9/-/preview/768x133/"
    web_settings.footer_logo = "https://ucarecdn.com/358ec918-a0b2-44ba-9fc0-f674e05f40d9/-/preview/768x133/"
    web_settings.footer_powered = "Erpera"
    web_settings.hide_footer_signup = 1
    web_settings.app_name = "Erpera"
    web_settings.app_logo = "https://ucarecdn.com/358ec918-a0b2-44ba-9fc0-f674e05f40d9/-/preview/768x133/"
    web_settings.save()

    #navbar settings
    navbar = frappe.get_doc("Navbar Settings")
    navbar.app_logo = "https://ucarecdn.com/358ec918-a0b2-44ba-9fc0-f674e05f40d9/-/preview/768x133/"
    navbar.logo_width = 200
    navbar.save()

    #edit the erpnext settings doctype
    edit_erp_info()


#create a theme for the app
def create_theme():
    #create colors
    if not frappe.db.exists("Color", "black"):
        color("black", "#000000")
    if not frappe.db.exists("Color", "white"):
        color("white", "#ffffff")

    theme = frappe.new_doc("Website Theme")
    theme.theme = "Erpera"
    theme.module = 'Erpera'
    theme.custom = 1
    theme.primary_color = frappe.db.get_value("Color", "black", "color")
    
    theme.text_color = frappe.db.get_value("Color", "black", "color")
    theme.background_color = frappe.db.get_value("Color", "white", "color")
    theme.light_color = frappe.db.get_value("Color", "white", "color")
    theme.dark_color = frappe.db.get_value("Color", "black", "color")
    theme.button_shadowhs = 1
    theme.button_gradients = 1
    theme.save()

#create color
def color(color, hex):
    cl = frappe.get_doc({
        'doctype': 'Color',
        '__newname': color,
        'color': hex
    })
    cl.save()

#edit erpnext setting and erpera titles
def edit_erp_info():
    if frappe.db.exists("Workspace", "ERPNext Settings"):
        frappe.db.set_value("Workspace", "ERPNext Settings", "title", "ERPera Settings")
        frappe.db.set_value("Workspace", "ERPNext Settings", "name", "ERPera Settings")
        frappe.db.commit()
    if frappe.db.exists("Workspace", "ERPNext Integrations"):
        frappe.db.set_value("Workspace", "ERPNext Integrations", "title", "ERPera Integrations")
        frappe.db.set_value("Workspace", "ERPNext Integrations", "name", "ERPera Integrations")
        frappe.db.commit()
    
    
    
