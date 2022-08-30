$(document).ready(function () {
  $(".IconContainer").click(function () {
    $(".IconContainer").toggleClass("change");
    $(".navLinks").toggle("slow");
  });

  $(".alternate").hide();

  $(".clickable").click(() =>{
    if($(".alternate").is(":visible")){
      $(".alternate").hide();
      $(".normal").show();
    }else{
      $(".alternate").show();
      $(".normal").hide();
    }
  });
  
  $(".clickable").mousedown(()=>{
    $(".clickable").css("cursor", 'grabbing');
  })
  $(".clickable").mouseenter(()=>{
    $(".clickable").css("cursor", 'grab');
  })
  $(".clickable").mouseup(()=>{
    $(".clickable").css("cursor", 'grab');
  })
  
});
