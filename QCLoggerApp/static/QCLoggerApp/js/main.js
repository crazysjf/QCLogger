
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
            if (data['error']) {
                // 数据重复
                alert("唯一码重复:\n" + data['e-employee'] + "\n" + data['e-datetime'])
            } else {
                $('#ucode-table').prepend(makeRows([data]))
            }
            $('#ucode-input').val("")
        });

       //$("#ucode-table").prepend('<tr><td>'+ $('#ucode-input').val() + '</td><td>'+'日期' + '</td></tr>');

      }
    });

    // 员工选择变化处理
    $("#employee-select").change(function(){
            var employee = $("#employee-select  option:selected").text();

            // 如果选择空，则清空列表
            if (employee == "") {
                replaceTableBody([])
            }


            var requestData = {employee: employee}
            $.get('QCLogger/records/', requestData, function(data) {
                replaceTableBody(data)
            })
    })

    function replaceTableBody(rList) {
    	var tb = '<tbody>' + makeRows(rList) + '</tbody>'
    	$("#ucode-table tbody").replaceWith(tb)
    }

    // 生成列表里面的行
    // rList格式：[{ucode:u1, datetime:d1}, {ucode:u2, datetime:d2} ]
    function makeRows(rList) {
        var tr = ""
        for (var r in rList) {
            tr += '<tr><td>';
            tr += rList[r]['ucode']
            tr += '</td><td>';
            tr += rList[r]['datetime'];
            tr += '</td></tr>'
        }
        return tr
    }
});
