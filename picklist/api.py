import frappe


@frappe.whitelist()
def get_sales_order_detailes(so_name):
    if not frappe.db.exists("Sales Order", so_name):
        frappe.throw("This Sales Order Barcode Not Found")
    
    so_doc = frappe.get_doc("Sales Order", so_name)
    customer = so_doc.customer
    items = so_doc.items
    
    return {"customer":customer, "items":items}

@frappe.whitelist()
def get_item_by_barcode(barcode):
    item_code = ""
    is_exists = frappe.db.exists("Item Barcode", {"barcode":barcode})
    if is_exists:
        item_code = frappe.db.get_value("Item Barcode", is_exists, "parent")
    else: 
        frappe.throw("This Barcode not Found, Please check your barcode")
        
    return {"item_code":item_code}


@frappe.whitelist()
def update_so_status(doc, method):
    if doc.total_actual_qty != doc.total_pick_qty:
        frappe.throw("Can't Submit this doc before Scanning all Ordered Qty")
    
    frappe.db.set_value("Sales Order", doc.sales_order, "status", "Processed")
    frappe.db.commit()
    

@frappe.whitelist()
def check_barcodes(doc, method):
    # Create Doc Barcode
    doc.doc_barcode = doc.name
    
    # Create Items Barcode
    for item in doc.items:
        if item.barcode:
        	item.item_barcode = item.barcode