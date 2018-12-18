$("#id_period").change(function(event) {
    event.preventDefault();
    if ($(this).val() === 'custom') {
        $("#date").show();
        $.ajax({
            data: {
                'period': $(this).val()
            },
            url: $("#requestform").attr('date'),
            success: function(data) {
                $("#date").html(data);
                activateDateRange();
            },
            failure: function(data) {
                alert('Request Failed.')
            }
        });

    } else {
        $("#date").hide();
    }
});
