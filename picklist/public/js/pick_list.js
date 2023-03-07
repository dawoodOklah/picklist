frappe.ui.form.on('Pick List', {
	refresh: function(frm){
		frm.trigger("create_progress_bar")
		frm.trigger("calc_total_pick_qty")
		frm.trigger("calc_total_actual_qty")
	},
	sales_order: function (frm) {
		frm.set_value("sales_order_barcode", frm.doc.sales_order)
		frm.set_value("customer", "")
		frm.set_value("locations", [])
		frm.refresh_field("sales_order_barcode")
		if (frm.doc.sales_order) {
			frappe.call({
				method: "picklist.api.get_sales_order_detailes",
				args: {
					"so_name": frm.doc.sales_order
				},
				callback: function(r) {
					if (r.message.customer) {
						frm.set_value("customer", r.message.customer)
					}
					if ( r.message.items ) {
						frm.doc.locations = [];
						r.message.items.forEach(row => {
							frm.add_child('locations', row);
						});
					}
					frm.trigger("calc_total_pick_qty")
					frm.trigger("calc_total_actual_qty")
					frm.save()
					frm.refresh_fields()
					frm.trigger("calc_total_pick_qty")
					frm.trigger("create_progress_bar")
				}
			})
		}
	},
	item: function(frm){
		frm.set_value("item_barcode", frm.doc.item)
		frm.refresh_field("item_barcode")
		if (frm.doc.item){
			frappe.call({
				method: "picklist.api.get_item_by_barcode",
				args: {
					"barcode": frm.doc.item
				},
				callback: function(r){
					console.log(r.message);
					let item_code = r.message.item_code
					let qty = frm.doc.qty
					// Ckeck if scanned item in location table
					let item_list = []
					frm.doc.locations.forEach(row => {
						item_list.push(row.item_code)
					});
					let is_exist = item_list.includes(item_code)
					// Update Picked Qty If item is in location table
					if (is_exist) {
						frm.events.update_item_picked_qty(frm, item_code, qty)
					}else {
						frappe.msgprint(__("Scanned Item <b>{0}</b>, with barcode <b> {1} </b> Not Exists in Item Locations Table", [item_code, frm.doc.item]));
						frm.doc.item = ""
						frm.doc.item_barcode = ""
						frm.doc.qty = 1
						frm.refresh_fields()
					}
					
				}
			})
		}
	},
	qty: function(frm){
		if (frm.doc.item){
			frm.trigger("item")
		}
	},
	// helper Function
	create_progress_bar: function(frm) {
		let width = frm.doc.total_pick_qty/frm.doc.total_actual_qty*100
		let progress = `<div class="progress-area"><div class="progress-chart" style="padding-top: 0;">`;
		let message =  __('{0} out of {1}', [frm.doc.total_pick_qty, frm.doc.total_actual_qty])
		progress += `
			<label class="control-label" style="padding-right: 0px;">Picked Items Progress</label>
			<div class="progress picked-progress">
				<div class="progress-bar progress-bar-success" style="width: ${width}%" title="Picked Items Progress Bar"></div>
				<span class="progress-percent">${parseInt(width)}%</span>
			</div>
			<p class="progress-message text-muted small">${message}</p>
			</div></div>
		`
		$(frm.fields_dict['progress'].wrapper).html(progress);
	},
	calc_total_pick_qty: function(frm){
		let total_pick_qty = 0
		frm.doc.locations.forEach(item => {
			total_pick_qty += item.picked_qty
		});
		frm.set_value("total_pick_qty", total_pick_qty)
		frm.refresh_field("total_pick_qty")
	},
	calc_total_actual_qty: function(frm){
		let total_actual_qty = 0
		frm.doc.locations.forEach(item => {
			total_actual_qty += item.qty
		});
		frm.set_value("total_actual_qty", total_actual_qty)
		frm.refresh_field("total_actual_qty")
	},
	update_item_picked_qty: function(frm, item_code, qty) {
		frm.doc.locations.forEach(row => {
			if (row.item_code == item_code){
				let allowed_qty = row.qty - row.picked_qty
				if (qty > allowed_qty) {
					frappe.throw(__("The Enterd Qty <b>{0}</b> is Greater Than the Remainig Qty that equal <b>{1}</b>",[qty, allowed_qty]))
				} else {
					row.picked_qty += qty
				}
			}
		});
		frm.doc.item = ""
		frm.doc.item_barcode = ""
		frm.doc.qty = 1
		frm.trigger("calc_total_pick_qty")
		frm.trigger("create_progress_bar")
		frm.refresh_fields()
		frm.save()
	}
});