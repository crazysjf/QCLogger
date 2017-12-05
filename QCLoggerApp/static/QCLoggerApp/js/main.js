
$(document).ready(function() {
    $('#letter-e a').click(function(event) {
        event.preventDefault();
        var requestData = {term: $(this).text()};
        $.post('e.php', requestData, function(data) {
            $('#dictionary').html(data);
        });
    });
    $('#ucode-input').bind('keypress',function(event){

      if(event.keyCode == "13") {
        event.preventDefault();
        var employee = $("#employee-select  option:selected").text();
        var requestData = {ucode: $('#ucode-input').val(),
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