

$(document).ready(function(){
  $(".nav-bar-button").click(function(){
    $(".title-slide").toggleClass("a-button");
    $(".nav-bar-button").toggleClass("hover-button");
    $(".logo").toggleClass("i-button");
  });
});
