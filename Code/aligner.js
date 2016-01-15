

function initReviewTd()
{	
	var CheckBoxString ='<td>'
						+'<form action="" method="get">'
  						+'<input type="checkbox" 	class="remarkCheckBox">'
  						+'<textarea rows="4" cols="50"></textarea>'
						+'</form></td>';
	//Attach all review <td> tag						
    $('tr').prepend(CheckBoxString);
    $('tr td:first-child').addClass('RemarkTd');

    //Hide all textboxes
    $('tr td.RemarkTd textarea').hide(0);
}

function initHooverMenu()
{
    var FormCode = 	'<td><button class="saveButton">Save</button></td>';
    // Select table element, embed div before, select those div, add hover class to it and append Sign Form code.
    //One horrible line. <;_;>
    var tableRef = $('table').before('<div></div>').prev('div').addClass('hoovMenu').append(FormCode);
}

$( document ).ready(function() {

    initReviewTd();
    initHooverMenu();
    
    $(function(){
	    $("tr td.RemarkTd input.remarkCheckBox").click(function(event) {
	    	
	    	var checkedTr = $(event.target).closest( "tr" );
	    	var commentBox = checkedTr.find('textarea');
	    	
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
	
	$('button.saveButton').click(function(event){
		//Gather comments with non-empty value
		var commentArray = $('tr td.RemarkTd textarea').filter(function(){
			if (this.value == "") {return false;}
			else {return true;}
		});
		var commentHeading = [];
		$(commentArray).closest('td').next('td').each(function(index, commentHeading) {
    		commentHeading[index] = $(this).html();
    		});
		
	});
    
});


