
// $(document).ready(function(){
//   $(".nav-bar-button").click(function(){
//     $(".title-slide").toggleClass("a-button");
//     $(".nav-bar-button").toggleClass("hover-button");
//     $("rect").toggleClass("icon-button");
//     $("circle").toggleClass("icon-button");
//     $("path").toggleClass("icon-button");
//   });
// });

$(document).ready(function () {

    //this will attach the class to every target 
    $(document).on('click', function (event) {
        $target = $(event.target);   
           $(".title-slide").toggleClass("a-button");
           $target.toggleClass("hover-button");
           $("rect").toggleClass("icon-button");
           $("circle").toggleClass("icon-button");
           $("path").toggleClass("icon-button");
       });

   })