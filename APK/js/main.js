function validateForm(filtr) {
    var isValid = true;
    $(filtr).each(function() {
        if ( $(this).val() === '' )
            isValid = true;
    });
    return isValid;
}

jQuery(function() {
    jQuery('#authbtn').click(function () { // catch the form submit event
        if ($('#username').val().length > 0 && $('#password').val().length > 0) {
            // Send data to server through ajax call
            // action is functionality we want to call and outputJSON is our data
            var data={login:$('#username').val(),password:$('#password').val()}
            $.ajax({
                url: 'http://127.0.0.1:8077/enter',
                data:data,
                type: 'post',
                async: true,
                crossDomain: true,
                dataType: 'text',

                success: function (result) {
                    var ans = result;
                    console.log(ans);
                    if (ans == 'true') {
                        alert('Авторизация прошла успешно');
                        $.mobile.changePage("#message_page");
                    }
                    else {
                        alert("Неправельный логин или пароль");
                    }
                },
                error: function (request, error) {
                    // This callback function will trigger on unsuccessful action
                    console.log(error)
                }
            });

        } else {
            alert('Please fill all nececery fields');
        }

        return false; // cancel original event to prevent form submitting
    });

    jQuery('#reg_btn').click(function (event) { // catch the form submit event
            $.mobile.changePage('#message_page');

            if(! validateForm('#reg_form')){
                alert("Заполните все поля!!");
                event.preventDefault();
                return false
            }
            else {
                var data = $('#reg_form').serialize();
                console.log(data);
                $.ajax({
                    url: 'http://127.0.0.1:8077/reg',
                    data:data,
                    type: 'post',
                    async: false,
                    crossDomain: true,
                    dataType: 'text',

                    success: function (result) {
                        var ans = result;
                        console.log(ans);
                        if (ans == 'true') {
                            alert('Регистрация прошла успешно');
                            $.cookie({ 'login': data['login'] });
                            $.mobile.changePage("#message_page");
                            return true;
                        }
                        else {
                            alert("login занят");
                            event.preventDefault();
                            return false;
                        }
                    },
                    error: function (request, error) {
                        // This callback function will trigger on unsuccessful action
                        console.log(error)
                    }
                });
            }
        });
        event.preventDefault();
        return false; // cancel original event to prevent form submitting
});




















// /**
//  * Created by Petr on 17.11.2018.
//  */
// $(document).on('submit', '#start_form', function(e) {
//     e.preventDefault();
//     postForm();
// });
//
// function postForm()
// {
//     var msg   = $('#start_form').serialize();
//     alert (msg)
//
//     $.cookie('login',msg['name']);
//     $.cookie('password',msg['password']);
//
//     var reg = $.ajax({
//         type: 'POST',
//         url: 'http://127.0.0.1:8077/enter',
//         data: msg,
//         crossDomain: true,
//         success: function(data) {
//             alert(data);
//         },
//         error:  function(xhr, str){
//             alert('Возникла ошибка: ' + xhr.responseCode);
//         }
//     }).response;
// }

