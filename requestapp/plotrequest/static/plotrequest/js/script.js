function activateDateRange() {
    $('#starttime').datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss'
    });

    $('#endtime').datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss'
    });

  }

$(function() {
  $('#starttime').datetimepicker({
    format: 'YYYY-MM-DD HH:mm:ss'
  });

$(function() {
  $('#endtime').datetimepicker({
    format: 'YYYY-MM-DD HH:mm:ss'
  });

});


$(document).ready(function() {
    $('#requestform').submit(function(event) {
        event.preventDefault();
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'),
            url: $(this).attr('action'),
            success: function(data) {
                console.log(data);
            },
            failure: function(data) {
                alert('Request Failed.')
            }
        });
    });
});
});
