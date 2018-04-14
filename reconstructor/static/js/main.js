/*
 * jQuery File Upload Plugin JS Example
 * https://github.com/blueimp/jQuery-File-Upload
 *
 * Copyright 2010, Sebastian Tschan
 * https://blueimp.net
 *
 * Licensed under the MIT license:
 * https://opensource.org/licenses/MIT
 */

/* global $, window */

$(function () {
    'use strict';

    // Initialize the jQuery File Upload widget:
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();

    $('#fileupload').fileupload({
        // Uncomment the following to send cross-domain cookies:
        //xhrFields: {withCredentials: true},
        url: '/reconstructor/perform',
        formData: [
            { name: 'csrfmiddlewaretoken', value: csrftoken }
        ],
    }).bind('fileuploaddone', function (e, data) {
        // Start the spinner.
        $('#result').show()
        $('#result').spin({color:'#8A89FF', radius: 65, lines: 60})

        // Send POST request to start reconstruction.
        $.ajax({
            url: "/reconstructor/reconstruct",
            type: 'POST',
            data: {'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val()},
            success: function(result){
                alert(result);
            }
        });

        // Stopt the spinner.
        $('#result').spin(false)
    });

    // Load existing files:
    $('#fileupload').addClass('fileupload-processing');
    $.ajax({
        // Uncomment the following to send cross-domain cookies:
        //xhrFields: {withCredentials: true},
        url: $('#fileupload').fileupload('option', 'url'),
        dataType: 'json',
        context: $('#fileupload')[0]
    }).always(function () {
        $(this).removeClass('fileupload-processing');
    }).done(function (result) {
        $(this).fileupload('option', 'done')
            .call(this, $.Event('done'), {result: result});
    });

});