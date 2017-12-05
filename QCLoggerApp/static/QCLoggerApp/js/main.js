
$(document).ready(function() {
    $('#ucode-input').bind('keypress',function(event){
      if(event.keyCode == "13") {
        event.preventDefault();
        var employee = $("#employee-select  option:selected").text();
        var ucode = $('#ucode-input').val();
        // 无输入则无动作
        if (ucode == "")
            return
        var requestData = {ucode: ucode,
                            employee: employee }


        $.post('QCLogger/log/', requestData, function(data) {
            var tr = '<tr><td>';
            tr += data['ucode'];
            tr += '</td><td>';
            tr += data['datetime'];
            tr += '</td></tr>'
            $('#ucode-table').prepend(tr)
            $('#ucode-input').val("")
        });

       //$("#ucode-table").prepend('<tr><td>'+ $('#ucode-input').val() + '</td><td>'+'日期' + '</td></tr>');

      }
    });//
});