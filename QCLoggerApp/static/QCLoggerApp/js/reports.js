$(document).ready(function() {
    $("#search-button").click(function(event){
        event.preventDefault();
        var employee = $("#employee-select  option:selected").text();
        var ucode = $('#ucode-input').val();
        var requestData = { ucode: ucode,
                            employee: employee }
  		$.get('/QCLogger/records/', requestData, function(data) {
			setRecordTableContent($("div.ucode-table"), data)

			var counts = {}
			for (var i in data['ucodeList']) {
				var e = data['employeeList'][i] 
				var c = counts[e]
				counts[e] = typeof(c)=="undefined" ? 1 : c+1  
			}

			updateSumaryTable(counts)
        })
    });

    function updateSumaryTable(counts) {
    	var tr = ""
	  	for (var i  in counts) {
	        tr += '<tr><td>';
	        tr += i
	        tr += '</td><td>';
	        tr += counts[i]
	        tr += '</td></tr>'
	    }


	    $("table#summary-table tbody").html(tr)
    }
})

