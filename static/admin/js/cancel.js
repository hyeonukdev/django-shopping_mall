(function($) {
    'use strict';
    $(function() {
<<<<<<< HEAD
        $('.cancel-link').click(function(e) {
            e.preventDefault();
            window.history.back();
=======
        $('.cancel-link').on('click', function(e) {
            e.preventDefault();
            if (window.location.search.indexOf('&_popup=1') === -1) {
                window.history.back(); // Go back if not a popup.
            } else {
                window.close(); // Otherwise, close the popup.
            }
>>>>>>> e84629bf0de49523aeb8814977d16613497d0c14
        });
    });
})(django.jQuery);
