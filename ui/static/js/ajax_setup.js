(function($) {
    $("body").ajaxError(
        function(event, request, settings, error) {
            var data;
            TCM.removeLoading();
            if(error === "UNAUTHORIZED" || error === "FORBIDDEN") {
                data = $.parseJSON(request.responseText);
                window.location = data.login_url + "?next=" + window.location.pathname;
            } else {
                // @@@ do something nicer than an alert()?
                alert("Help! Something broke, and we're not sure just what. Try reloading the page.");
            }
        });

    $.ajaxSetup(
        {
            dataType: "json",
            dataFilter: function(data, type) {
                if (type == "json") {
                    var messagelist = $("#messages ul"),
                    parsed = $.parseJSON(data),
                    messages = $(parsed.messages);
                    messages.each(function() {
                        $(ich.message(this)).appendTo(messagelist);
                    });
                    TCM.messages();
                }
                return data;
            }
        }
    );
})(jQuery);