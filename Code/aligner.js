
$( document ).ready(function() {

	var CheckBoxClass = 'RemarkCheckBox';	
	var CheckBoxString ='<td>'
						+'<form action="" method="get">'
  						+'<input type="checkbox" name="RemarkBox" value="Remark">Remarks<br>'
						+'</form></td>';	
    $('tr').prepend(CheckBoxString);
    $('tr td:first-child').addClass(CheckBoxClass);
    
    //This is just bad... but works.
    // TODO howto obtain ref to newly created element without referencing to parent
    var tableRef = $('table').before('<div></div>');
    tableRef.prev('div').addClass('hoovMenu');
    tableRef.prev('div.hoovMenu').append('<ul><li>Opt1</li><li>Opt2</li></ul>');
    //tableRef.prev('div.hoovMenu div').addClass('hidden');
    
    
    $(function(){
    $("tr td.RemarkCheckBox input").click(function(event) {
    	
    	var par = $(event.target).closest( "tr" );
    	
    	if(event.target.checked == true){
       		par.addClass("marked"); 			
    	}
    	else{
    		par.removeClass("marked"); 
    	}

    });
});
    
});