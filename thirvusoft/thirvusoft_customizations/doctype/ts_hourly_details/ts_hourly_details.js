// Copyright (c) 2021, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt

frappe.ui.form.on('TS Hourly Details', {
	end_time:function(frm, cdt, cdn){
		let row = locals[cdt][cdn];
		var starttimeString = row.start_time;
		var H = +starttimeString.substr(0, 2);
		var h = H % 12 || 12;
		var ampm = (H < 12 || H === 24) ? "AM" : "PM";
		console.log(starttimeString)
		starttimeString = h + starttimeString.substr(2, 3)+starttimeString.substr(5,5) + ampm;

		var endtimeString = row.end_time;
		var H = +endtimeString.substr(0, 2);
		var h = H % 12 || 12;
		var ampm = (H < 12 || H === 24) ? "AM" : "PM";
		console.log(endtimeString)
		endtimeString = h + endtimeString.substr(2, 3)+endtimeString.substr(5,5) + ampm;
		console.log(starttimeString,endtimeString)

		var startTime = moment(starttimeString, "HH:mm:ss a");
		var endTime = moment(endtimeString, "HH:mm:ss a");

		var duration = moment.duration(endTime.diff(startTime));
		var hours = parseInt(duration.asHours());
		var minutes = parseInt(duration.asMinutes())%60;
		frappe.model.set_value(cdt, cdn, "hours",
		hours +' Hours '+ minutes+' Minutes ');
	},
	start_time:function(frm, cdt, cdn){
		let row = locals[cdt][cdn];
		var starttimeString = row.start_time;
		var H = +starttimeString.substr(0, 2);
		var h = H % 12 || 12;
		var ampm = (H < 12 || H === 24) ? "AM" : "PM";
		console.log(starttimeString);
		starttimeString = h + starttimeString.substr(2, 3)+starttimeString.substr(5,5) + ampm;

		var endtimeString = row.end_time;
		var H = +endtimeString.substr(0, 2);
		var h = H % 12 || 12;
		var ampm = (H < 12 || H === 24) ? "AM" : "PM";
		console.log(endtimeString);
		endtimeString = h + endtimeString.substr(2, 3)+endtimeString.substr(5,5) + ampm;
		console.log(starttimeString,endtimeString);

		var startTime = moment(starttimeString, "HH:mm:ss a");
		var endTime = moment(endtimeString, "HH:mm:ss a");

		var duration = moment.duration(endTime.diff(startTime));
		var hours = parseInt(duration.asHours());
		var minutes = parseInt(duration.asMinutes())%60;
		frappe.model.set_value(cdt, cdn, "hours",
		hours +' Hours '+ minutes+' Minutes ');
	}
});
