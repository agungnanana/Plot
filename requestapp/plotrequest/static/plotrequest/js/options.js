$("#id_kind").change(function(event) {
    event.preventDefault();
    $.ajax({
        data: {
            'kind': $(this).val()
        },
        url: $("#requestform").attr('options'),
        success: function(data) {
            $("#options").html(data);
        },
        failure: function(data) {
            alert('Request Failed.')
        }
    });
});
