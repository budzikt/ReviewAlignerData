
$( document ).ready(function() {

	var CheckBoxClass = 'RemarkCheckBox';	
	var CheckBoxString ='<td>'
						+'<form action="" method="get">'
  						+'<input type="checkbox" name="vehicle" value="Bike">Remarks<br>'
						+'</form></td>';	
    $('tr').prepend(CheckBoxString);
    $('tr td:first-child').addClass(CheckBoxClass);
    
    
    $(function(){
    $("tr td.RemarkCheckBox input").click(function(event) {
    	if(event.currentTarget.checked == true){
  			alert(event.pageX);
       		alert(event.pageY);  		
    	}

    });
});
    
});