$('.dropdown-toggle').dropdown()


$(document).ready(function() {
    $('.dropright div').on("click", function(e) {
      e.stopPropagation();
      e.preventDefault();
  
      if (!$(this).next('div').hasClass('show')) {
        $(this).next('div').addClass('show');
      } else {
        $(this).next('div').removeClass('show');
      }
  
    });
  });


$(document).ready(function(){
  $('.dropdown-submenu a.test').on("click", function(e){
    $(this).next('ul').toggle();
    e.stopPropagation();
    e.preventDefault();
  });
});
