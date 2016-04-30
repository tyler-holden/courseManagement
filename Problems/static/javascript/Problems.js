$('document').ready(function() {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
            return cookieValue;
    }
    var csrftoken = getCookie('csrftoken'); 

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
    
    // Select all li items whose class begins with "diff". These are the problems.
    // Pass them to autorender
    $('[class^="diff"]').each( function () {
        renderMathInElement( $(this)[0] );
    });

    var curFunHandle;

    $('.ajax-form').change( function() {
        use = $('#user').val()
        que = $('#question').val()
        att = $('#attempted').is(':checked');
        sol = $('#solved').is(':checked');
        dif = $('#difficulty').val();
        
        if (curFunHandle) {
            clearTimeout(curFunHandle);
            curFunHandle = null;
        }
        
        curFunHandle = setTimeout( function() {
            $.post('/Problems/update_status/', {attempted: att, solved: sol, difficulty: dif, user: use, question:que}, 
                function(data, status) {
                    $response = $("#response");
                    $response.html(data['response']);
                    setTimeout( function() {$response.html('') }, 2000);
            }, "json")
        },1000);
    });

    // adds a datepicker jquery ui element to dates
    $('#id_expires').datepicker()

    // gets old announcements and inserts them into the page
    $('#get_old').click( function() {
        $.get('/Problems/get_old_announcements/', {}, function(data) {
            $('.old-ann').html(data);
        });
    });
});

