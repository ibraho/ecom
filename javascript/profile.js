 $(document).ready(function(){


document.getElementById("id_photo").required = true;
$( "#id_birth_date" ).attr("type", "date");
$("#id_zipcode").attr("pattern","[0-9]{4}");
$("#id_zipcode").attr("title","Enter 4 digits ZipCode");
$("#id_phone").attr("type","text");
$("#id_phone").attr("placeholder","00355");
$("#id_phone").attr("type","text");

$("#id_birth_date").addClass("mr");
$('.one,.two,.thre,.four').addClass('animated zoomIn');

//$("#id_photo").addClass(" btn btn-secondary ");
$(".control-group").addClass("row ");
$(".control-label").addClass("col ");
$(".controls").addClass("col ");
$("#div_id_photo").removeClass('row');
if (screen.width > 860) {
   $("#div_id_name").append('<i  class=name  ></i>');
$(".name").addClass("fas fa-user-edit");

$("#div_id_last_name").append('<i class= last ></i>');
$(".last").addClass("fas fa-file-signature ");

$("#div_id_email").append('<i class=mail ></i>');
$(".mail").addClass("fas fa-envelope-square ");

$("#div_id_birth_date").append('<i class=birth ></i>');
$(".birth").addClass("far fa-calendar-alt ");

$("#div_id_location").append('<i class=loca ></i>');
$(".loca").addClass("fas fa-map-marked-alt ");
$("#div_id_zipcode").append('<i class=zip ></i>');
$(".zip").addClass("fas fa-city ");
$("#div_id_phone").append('<i class= pho ></i>');
$(".pho").addClass("fas fa-phone ");
}

});
  $(document).ready(function(){

$("button").addClass(" ");
});

$("").click (function(){

});

$(".show1").click (function(){

$(".form1").addClass(" ");
$(".form1").toggle('slow');

$(".info").toggle('slow');

$("#ciro").toggle('slow');
$("#edo").toggle('slow');
if ($(window).width() < 500) {
//$('.form1')[0].scrollIntoView(true);
 $('html,body').animate({                                                          
        scrollTop: $(".form2").offset().top},
        'slow');
   
}

});
$(".show2").click (function(){
$(".form2").addClass(" animated slideInRight");
$(".form2").toggle('slow');
$("#cir").toggle('slow');
$("#ed").toggle('slow');
if ($(window).width() < 500) {
 $('html,body').animate({                                                         
        scrollTop: $(".offset1").offset().top},
        'slow');
   
}
});
$('input').focus(
    function(){

        $(this).parent('div').parent('div').children().addClass('').show('slow');
         $(this).parent('div').parent('div').css({'border-left-style':'solid'});
        //$(this).parent('div').parent('div').css('transition','2s');

    }).blur(
    function(){
      $(this).parent('div').parent('div').children('i').removeClass('animated bounceIn').hide('slow');
      $(this).parent('div').parent('div').children().removeClass('animated bounceIn');
      $(this).parent('div').parent('div').css({'border-left-style':''});
       //$(this).parent('div').parent('div').css('border-style','');
    });

//removes the wished item
$('.wish2').each(function() {

      $(this).click(function(event){

    event.preventDefault();

    var formid=$(this).attr('id');

    var mydata=$('#'+formid).serialize();
    
    var myurl=$('#'+formid).attr('action') || window.location.href;
    
  $.ajax({
                method:'POST',
                url: myurl,                
                data:mydata,
              
          });
               

        });
      

       });

$(document).ready(function(){

//adds product to the cart 

$('.formos').each(function() {

      $(this).click(function(event){

    event.preventDefault();

    var formid=$(this).parent('form').attr('id');

    var mydata=$('#'+formid).serialize();
    
    //var location= window.location.href+'/cart/add/'+id;
    var myurl=$('#'+formid).attr('action') || window.location.href;
   
    //console.log(mydata)
  $.ajax({
                method:'POST',
                url: myurl,                
                data:mydata,
                //success: handleSuccess,
                //error:handleError,
          });
               
        });

       });
    $('.formos').click(function(e){
        e.preventDefault();
       $(this).parent('form').attr('action','not');
      
       $(this).children('i').addClass('fas fa-check-circle').css({'color':'green'});

          });
 });

$(document).ready(function(){
$('.orderdd').click(function() {
   $('.orders').show();
   $('.an').addClass('slideInLeft')
   $('.anu').addClass('slideInRight')
   $('.wished').hide();

});
$('.wishedd').click(function() {
   $('.orders').hide();
   $('.wished').show();
   $('.ani').addClass('slideInLeft')
   $('.down').addClass('slideInDown')
   $('.anud').addClass('slideInRight')
});

// change the button color
$('.ico').each(function() {
  $(this).click(function(){
    if($(window).width() > 768 ){



   $(this).css('margin-left', '15px');
   $(this).css('background-color','black')

   //  on each element that is not clicked
   $('.ico').not(this).each(function(){ 
         $(this).css('margin-left', '0px');
         $(this).css('background-color','#17a2b8')
     });
   } // end if statment
 else{
   $(this).css('background-color','black')
     $('.ico').not(this).each(function(){ 
         
         $(this).css('background-color','#17a2b8')
     });
}

  });
  
});
 
 //calculate the price of pruduct     
 $('.another').each(function(index, element) {

      var idj= $(this).parent('div').attr('id')
          var sel= $(this).parent('div').children('form').children('div').children('div').children('select');
          var pricon= $(this).parent('div').children('form').children('div').children('span').text();
          var tota = $(this).find('strong');
 //alert(sel)
var th= $(this).closest('div').attr('id');
 var ss= sel.val();
   sel.on('change', function() {
        var sss= sel.val()
                var value = $(sel).val();
                var item_price=parseInt(pricon);
                var newp= value * item_price;
                $(this).find('strong').text('new3p');
                 tota.text(newp)
//.val(value); )
                     $('#faso'+th).find('.te').val(value)
                console.log(th)
           });

       
       }); 


});


