

function initReviewTd()
{	
	var CheckBoxString ='<td class="commentTd">'
						+'<form action="" method="get">'
  						+'<input type="checkbox" 	class="remarkCheckBox">'
  						+'<textarea rows="4" cols="50"></textarea>'
						+'</form>'
						+'</td>';
	//Attach all review <td> tag						
    $('tr:not(:has(>th))').prepend(CheckBoxString);
    $('tr>th:eq(0)').parent().prepend('<th>Review comment</th>');
    $('tr td:first-child').addClass('RemarkTd');
    //Hide all textboxes
    $('tr td.RemarkTd textarea').hide(0);
}

function initHooverMenu()
{
    var FormCode = 	'<td><button class="saveButton">Save</button></td>';
    var tableRef = $('table').before('<div></div>').prev('div').addClass('hoovMenu').append(FormCode);
}

$( document ).ready(function() {

	//Init compose elements
    initReviewTd();
    initHooverMenu();
    
    //Read table heading
    var TableHeadings = [];
    $('tr th').each(function(index){
    	TableHeadings[index] = $(this).text().toLowerCase();
    });
    var idIndex = TableHeadings.indexOf("id");
    if(idIndex == -1){
    	alert("No ID in match-set");
    }

    
    //Show or Hide comment box
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
	
	
	$('button.saveButton').click(function(event){
		
		//Fild table row with comment content
		var rowWithContent = $('table tr').filter(function(index){
			if($('textarea', this).val() != ""){return true;}
			else{return false;}
		});
		
		var commentId = jQuery.makeArray($('td:eq('+ idIndex +')',rowWithContent).map(function(index){
			return $(this).text();
		}));
		
		var commentText = jQuery.makeArray($('td.RemarkTd textarea', rowWithContent).map(function(){
			return $(this).val();
		}));
		
		fileblob = {"commentId": commentId, "commentText": commentText};
		alert("aaa");



		
		//commentArray = jQuery.makeArray(commentArray);	
    	//commentHeading = jQuery.makeArray(commentHeading);
    	//Crete download dat
    	//var textFileAsBlob = new Blob([commentArray[0]], {type:'text/plain'});
    	
		//create <a> downloadable elemenet
//		var downloadLink = document.createElement("a");
//		downloadLink.href = window.URL.createObjectURL(textFileAsBlob);
//		downloadLink.onclick = destroyClickedElement;
//		downloadLink.style.display = "none";
//		document.body.appendChild(downloadLink);
//		downloadLink.click();
	});

function destroyClickedElement(event)
{
	document.body.removeChild(event.target);
}
    
});


