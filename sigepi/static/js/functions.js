function alert_jqueryalert () {
    $.confirm({
        title: 'Confirm!',
        content: 'Simple confirm!',
        buttons: {
            confirm: function () {
                $.alert('Confirmed!');
            },
            cancel: function () {
                $.alert('Canceled!');
            },
            somethingElse: {
                text: 'Something else',
                btnClass: 'btn-blue',
                keys: ['enter', 'shift'],
                action: function(){
                    $.alert('Something else?');
                }
            }
        }
    });
}