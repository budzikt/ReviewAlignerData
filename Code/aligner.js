
$( document ).ready(function() {

	var CheckBoxClass = 'RemarkTd';	
	var CheckBoxString ='<td>'
						+'<form action="" method="get">'
  						+'<input type="checkbox" 	class="remarkCheckBox">'
  						+'<input type="text" 		class="remarkText">'
						+'</form></td>';
						
	var FormCode = '<form method="POST"><input type="submit" value="Submit"></form>';
							
    $('tr').prepend(CheckBoxString);
    $('tr td:first-child').addClass(CheckBoxClass);
    
    // Select table element, embed div before, select those div, add hover class to it and append Sign Form code.
    //One horrible line. <;_;>
    var tableRef = $('table').before('<div></div>').prev('div').addClass('hoovMenu').append(FormCode);
    //Hide all textboxes
    $('tr td.RemarkTd input.remarkText').hide(0);
   
    $(function(){
    $("tr td.RemarkTd input.remarkCheckBox").click(function(event) {
    	
    	var checkedTr = $(event.target).closest( "tr" );
    	var commentBox = checkedTr.find('.remarkText');
    	
    	if(event.target.checked == true){
       		checkedTr.addClass("marked");
       		$(commentBox).show(400);
    	}
    	else{
    		checkedTr.removeClass("marked");
       		$(commentBox).hide(400);
    	}

    });
});
    
});