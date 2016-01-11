
$( document ).ready(function() {

	var CheckBoxClass = 'RemarkCheckBox';	
	var CheckBoxString ='<td>'
						+'<form action="" method="get">'
  						+'<input type="checkbox" name="RemarkBox" class="shown remarkCheck">'
  						+'<input type="text" name="remarkText" class="hidden remarkText">'
						+'</form></td>';
						
	var FormCode = '<form method="POST"><input type="submit" value="Submit"></form>';
							
    $('tr').prepend(CheckBoxString);
    $('tr td:first-child').addClass(CheckBoxClass);
    
    //This is just bad... but works.
    // TODO howto obtain ref to newly created element without referencing to parent
    var tableRef = $('table').before('<div></div>');
    tableRef.prev('div').addClass('hoovMenu');
    tableRef.prev('div.hoovMenu').append(FormCode);
    
    
    
    $(function(){
    $("tr td.RemarkCheckBox input.remarkCheck").click(function(event) {
    	
    	var par = $(event.target).closest( "tr" );
    	var commentBox = par.find('.remarkText');
    	commentBox = $(commentBox);
    	
    	if(event.target.checked == true){
       		par.addClass("marked");
       		if(commentBox.hasClass('hidden')) 
       		{commentBox.addClass('shown').removeClass('hidden');}
       		else 
       		{commentBox.addClass('shown');}
    	}
    	else{
    		par.removeClass("marked");
    		if(commentBox.hasClass('shown')) 
    		{commentBox.addClass('hidden').removeClass('shown');}
       		else 
       		{commentBox.addClass('hidden');}
    	}

    });
});
    
});