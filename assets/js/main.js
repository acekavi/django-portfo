$(document).ready(function () {
  $(".IconContainer").click(function () {
    $(".IconContainer").toggleClass("change");
    $(".navLinks").toggle("slow");
  });
});
