(function($)
{
  $.fn.emptyText = function(txt) {
    emptyClass = arguments[1] ? arguments[1] : "empty";

    if(txt) {
      $(this).addClass(emptyClass);
      $(this).val(txt);

      $(this).bind('focus', function() {
        if ($(this).hasClass(emptyClass)) {
          $(this).removeClass(emptyClass);
          $(this).val("");
        }
      });

      $(this).bind('blur', function() {
         if ($(this).val().trim() == "") {
           $(this).addClass(emptyClass);
           $(this).val(txt);
         }
      });
    }

    /* if no text specified remove emptytext bindings */
    else {
      $(this).unbind('focus');
      $(this).unbind('blur');
      $.each($(this), function(i, elem) {
        if($(elem).hasClass(emptyClass)) {
          $(elem).removeClass(emptyClass);
          $(elem).val("");
        }
      });
    }
  };
})(jQuery);  
