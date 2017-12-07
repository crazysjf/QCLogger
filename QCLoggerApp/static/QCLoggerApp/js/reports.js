$(document).ready(function() {
    $("#search-button").click(function(event){
        event.preventDefault();
        var employee = $("#employee-select  option:selected").text();
        var ucode = $('#ucode-input').val();

        var requestData = { ucode: ucode,
                            employee: employee }

  		$.get('/QCLogger/recordCount/', requestData, function(data) {

			setRecordTableContent($("div.ucode-table"), data)
        })
    });
})

