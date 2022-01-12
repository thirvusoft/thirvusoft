// Copyright (c) 2022, ThirvuSoft Private Limited and contributors
// For license information, please see license.txt
function timediff(frm){
		var starttimeString = frm.doc.start_time;
		var H = +starttimeString.substr(0, 2);
		var h = H % 12 || 12;
		var ampm = (H < 12 || H === 24) ? "AM" : "PM";
		starttimeString = h + starttimeString.substr(2, 3)+starttimeString.substr(5,5) + ampm;

		var endtimeString = frm.doc.end_time;
		var H = +endtimeString.substr(0, 2);
		var h = H % 12 || 12;
		var ampm = (H < 12 || H === 24) ? "AM" : "PM";
		endtimeString = h + endtimeString.substr(2, 3)+endtimeString.substr(5,5) + ampm;

		var startTime = moment(starttimeString, "HH:mm:ss a");
		var endTime = moment(endtimeString, "HH:mm:ss a");

		var duration = moment.duration(endTime.diff(startTime));
		var hours = parseInt(duration.asHours());
		var minutes = parseInt(duration.asMinutes())%60;
		
		cur_frm.set_value("hours",
		hours +' Hours '+ minutes+' Minutes ');
}
frappe.ui.form.on('TS Permission Details', {
	end_time:function(frm){
		timediff(frm)
	},
	start_time:function(frm){
		timediff(frm)
	}
});
