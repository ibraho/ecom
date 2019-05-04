$('.add1').each(function() {

$(this).click(function(event) {
  $(this).addClass('wes')
  $(this).closest('span').find('.remove1').addClass('wes')
});
});

$('.remove1').each(function() {

$(this).click(function(event) {
  
  $(this).closest('span').find('.add1').addClass('wesu')
});
});
  
// add items to wish list

$('.wish').each(function() {

      $(this).click(function(event){

    event.preventDefault();

    var formid=$(this).attr('id');

    var mydata=$('#'+formid).serialize();
    
    //var location= window.location.href+'/cart/add/'+id;
    var myurl=$('#'+formid).attr('action') || window.location.href;

  

  $.ajax({  
                method:'POST',
                url: myurl,                
                data:mydata,
         
           });
        });
    });
// add items to the wish list 

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





//updates the items number on the cart 
$('.cart_on').one('click', function(event) {

 
    var svg = $('.select');

     var cart= $('#carta').text()
     var cart_int= parseInt(cart)
     var drop_int= parseInt( svg.val() )
     console.log(cart)

    $('#carta').text(cart_int + drop_int )
});




     $('.cart_on').click(function(event){

    event.preventDefault();

    var formid=$('#fdd').attr('id');

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
                              //success: function(data){
               //alert(data.message);  
               //},
               //error: function(data){
               //alert(data.error);
               //}
          });
$(this).text('')          
$(this).append(' <i style=padding:0px class=fasio  ></i>'+' On Cart');


$('#fdd').attr('action','Not');

        });

    $('.cart_on').click(function(e){
        e.preventDefault();
       $(this).parent('form').attr('action','not');
      
       $(this).children('i').addClass('fas fa-check-circle').css({'color':'green'});

          });


// on slider updates the items number on the cart 
$('.cart_ons').one('click', function(event) {



     var cart= $('#carta').text()
     var cart_int= parseInt(cart)
     
     console.log(cart)

    $('#carta').text(cart_int + 1 )
});



/// on slider add to cart 



     $('.cart_ons').click(function(event){

    event.preventDefault();

   var formid=$(this).closest('span').children('form').attr('id');
$('#'+formid).find('.cart_ons').not($(this)).hide();
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
  $('#'+formid).attr('action','Not');
$(this).text('')          
$(this).append(' <i style=padding:0px;color:green; class=fas  ></i>'+' On Cart');

$('.fas').addClass('fa-check-circle')



        });

    $('.cart_on').click(function(e){
        e.preventDefault();
       $(this).parent('form').attr('action','not');
      
       $(this).children('i').addClass('fas fa-check-circle').css({'color':'green'});

          });






  $(document).ready(function() {


$('.desc').click(function(event) {
  $('.ratings').hide(); 
  $('.cae').show();
  $(this).addClass('border');
  $('.rev').removeClass('border');
});

$('.rev').click(function(event) {
  $('.cae').hide(); 
  $('.ratings').show();
  $(this).addClass('border');
  $('.fano').addClass('zoomIn');

  $('.desc').removeClass('border');

});






    $('.similar').owlCarousel({
 
  //loop: true,
  dots: true,
  nav: true,
  navText: [
    "<i class='fa fa-caret-left'></i>",
    "<i class='fa fa-caret-right'></i>"
  ],
 
  margin:0,
  responsive: {
    0: {
      items: 1
    },
    600: {
      items: 3
    },
    1000: {
      items: 5
    }
  }
})


    $('.brand').owlCarousel({
 
  loop: true,
  dots: true,
  nav: true,
  navText: [
    "<i class='fa fa-caret-left'></i>",
    "<i class='fa fa-caret-right'></i>"
  ],
 
  margin:0,
  responsive: {
    0: {
      items: 1
    },
    600: {
      items: 3
    },
    1000: {
      items: 5
    }
  }
})



      $('.owl-dot').append('<i class="fas fa-circle"></i>')

});
var owl = $('.brand');
owl.on('changed.owl.carousel',function(property){
    var current = property.item.index;
    var src = $(property.target).find(".owl-item").eq(current).find("img").attr('src');
    $('#zog').attr('src', src);
        $('#zog').addClass('fadeIn')
        setTimeout(function() { 
       $('#zog').removeClass(' fadeIn')
    }, 700);
    
});
$(".item").each(function(index, el) {
  $(this).click(function(event) {
   var the_src= $(this).find('img').attr('src');
    $('#zog').attr('src',the_src);
    $('#zog').addClass('fadeIn')
        setTimeout(function() { 
       $('#zog').removeClass(' fadeIn')
    }, 700);
  });
  
});
