import frappe

@frappe.whitelist(allow_guest=True)
def get_emoji():
    return "hohoho!🎅"

def throw_emoji(doc, event):
    frappe.msgprint("why are you creating a new task😢")

def send_payment_reminders():
    print("Sending payment reminders...")
    pass

def insert_10000_invoices():
    pass

def get_query_conditions_for_vehicle(user):
    return 'name = "VHCL-0031"'