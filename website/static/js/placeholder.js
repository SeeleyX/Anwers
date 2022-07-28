
$(document).ready(function(){
  $().click(function(event) {
    let $target = $(event.target);
    if (!$target.closest('.nav-bar-button')) {
      $('.nav-bar-button').children("i").removeClass("i-button");
    }
  })

  $(".nav-bar-button").click(function(){
    let iChild = $(this).children("i");
    let aChild = $(this).children("a");
    iChild.addClass("i-button");
    aChild.addClass("a-button");
    $(this).addClass("hover-button");

  });
  $(".nav-bar-button").mouseleave(function() {
    let iChild = $(this).children("i");
    let aChild = $(this).children("a");
    aChild.removeClass("a-button");
    iChild.removeClass("i-button");
    $(this).removeClass("hover-button")
  })
});
