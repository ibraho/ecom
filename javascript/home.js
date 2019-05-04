  
$('.add1').each(function() {

$(this).click(function(event) {
  
  $(this).closest('span').find('.remove1').addClass('wes')
});
});

$('.remove1').each(function() {

$(this).click(function(event) {
  
  $(this).closest('span').find('.add1').addClass('wesu')
});
});

  $(document).ready(function($) {
   
      
      $('.modo').click(function(event){
   $('.fade').addClass('animated zoomIn')

   
      var modal_id=$(this).attr('id');
      var srv = $('#faso'+modal_id).attr('action')
     var src = $('#im'+modal_id).attr('src')
     var title = $('#sp'+modal_id).text()
     var price = $('#pric'+modal_id).text()
         $('#image').attr('src', src);
      var srcs =  $(this).closest('div').find('.buy').attr('action');
      $('#mform').attr('action', srcs);
      $('#item_price').text( 'Price '+ price+'$').css({'font-weight': 'bold',
        'border-style':'solid','padding':'5px'});
      $('#title_m').text( 'Buying  '+ title );
      $('#mform').attr('action', srv);
     console.log(srv)

               });
     
  
  });

    $('.formos').click(function(e){

$('#carta').addClass('bounceIn')
setTimeout(function(){
$('#carta').removeClass('bounceIn')

}, 500);

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

$(document).ready(function(){

// add items to the cart 


$('.formos').each(function() {

//updates the items number on the cart 
$(this).one('click', function(event) {
 var svg = $(this).parent('form').children('div').children('div').children('select');

     var cart= $('#carta').text()
     var cart_int= parseInt(cart)
     var drop_int= parseInt( svg.val() )

   $('#carta').text( cart_int + drop_int )
});

      $(this).click(function(event){
     
     var formid=$(this).parent('form').attr('id');

     var mydata=$('#'+formid).serialize();
    
    
     var myurl=$('#'+formid).attr('action') || window.location.href;


  $.ajax({
                method:'POST',
                url: myurl,                
                data:mydata,
              
          });
               

        });

       });



 /*
 Selects all the buttons with the class 'formos' and adds an click event 
 on every click of this button hides the button of the other 'form'.We can do that by adding on both forms
 an a empty section with  an id  witch is dynamic and equal with the item number in the forloop 
  as this id='{{forloop.counter}}' .
  after we hide the $('.formos') we append another button with custom class and text 'On cart ' 
*/

  $('.formos').click(function(e){

    e.preventDefault();
    var df = $(this).closest("div").children('a').children('section').attr('id');
    
          $(this).parent('form').attr('action','not');
         
         // $(this).children('i').addClass('fas fa-check-circle').css({'color':'green'});

          $('#formi'+df).find('.formos').children('i').addClass('fas fa-check-circle').css({'color':'green'});

 $('#form'+df).find('.formos').hide()
$('#form'+df).append(' <button onclick=event.preventDefault() class=subis ><i style=padding:0px class=fasio  ></i>On Cart</button>')


         $('#formi'+df).find('.formos').hide()
         $('#formi'+df).append(' <button onclick=event.preventDefault() class=subis ><i style=padding:0px class=fasio  ></i>On Cart</button>')
         $('.subis').addClass('btn btn-warning mb-3'); 
         $('.fasio').addClass('fas fa-check-circle');
         $('.subis').css('padding', '0px'); 
                  $('#formi'+df).find('.formos')
       
      });


 /*
 Selects all the buttons with the class 'formos' from all the forms with the class 'another '
 on every click of this button hides the button of the other 'form'.We can do that by adding on both forms
 an a empty section with  an id  witch is dynamic and equal with the item nr in the forloop 
  as this id='{{forloop.counter}}' So with this on mind  every form has an id of his section equal to another form.
  after we hide the $('.formos') we append another button with custom class and text 'On cart ' 
*/

$('.another').find('.formos').click(function(event) {
  var hb = $(this).parent("form").children('section').attr('id');;
   $('#form'+hb).find('.formos').hide()
    $('#formi'+hb).find('.formos').hide()
         $('#formi'+hb).append(' <button onclick=event.preventDefault() class=subis ><i style=padding:0px class=fasio  ></i>On Cart</button>')
         
         $('#form'+hb).append(' <button onclick=event.preventDefault() class=subis ><i style=padding:0px class=fasio  ></i>On Cart</button>')
         $('.subis').addClass('btn btn-warning mb-3'); 
         $('.fasio').addClass('fas fa-check-circle');
         $('.subis').css('padding', '0px'); 
                  



 });


 });

$(document).ready(function(){
 //open the list of products      
 $('.another').each(function(index, element) {
          var idj= $(this).parent('div').attr('id')
          var sel= $(this).parent('div').children('form').children('div').children('div').children('select');
          var pricon= $(this).parent('div').children('form').children('div').children('span').text();
          var tota = $(this).find('strong');
 var ss= sel.val()
 var thi= $(this);
   sel.on('change', function() {
                var value = $(sel).val();
                var item_price=parseInt(pricon);
                var newp= value * item_price;
                $(this).find('strong').text('new3p');
                tota.text(newp)
             
             });
 
       
       }); 
});

$('.nr').click(function(event) {
});
  $(document).ready(function(){
    $('#div_id_quantity').children('label').css({'display':'none'})
    var r=$(".ui-slider-range:first-child")


 $("#slider-range").children('span:first').append('<div></div>');
 $(".maqos").children(':first').addClass('btn');

  });
$(".but2").click(function(){
        $(".cap").removeClass("col-md-4 "); 
           $(".cap").addClass("col-md-3 ");
           $(".ne").css('display','block');
           $(".whole").css('display','none');
           $(".ssc").css('margin-top','5px');
           $('.first').removeClass('container');
           $('.first').addClass('container-fluid');
           $('.cap').attr('data-aos','flip-up');
         });
       
     $(".but1").click(function(){
        $(".cap").removeClass("col-md-3 "); 
           $(".cap").addClass("col-md-4"); 
           $(".ne").css('display','none');
           $('.first').removeClass('container-fluid');
           $('.first').addClass('container')
           $(".whole").css('display','block');
           $('.cap').attr('data-aos','');
           $(".ssc").css('margin-top','-30px');
         });
function mq() {
$('#max_price').click();
    $('#min_price').click();
};
 $(".maqo").click(function(vv){
    $('#max_price').click();
    $('#min_price').click();
});
  $("#slider-range").click(function(vv){
    $('#max_price').click();
    $('#min_price').click();
});
function subi() {
  document.getElementById("favi").submit();
  document.getElementById("my_form").submit();
}
