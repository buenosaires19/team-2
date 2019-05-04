$(document).ready(function(){
console.log(123123123);

//CONTENIDO MOCKEADO

var modals=[{}]

var modal1 = {}
modal1.title= "modal 1";  
modal1.mainText = ["Pregunta de prueba1","Pregunta de prueba2","Pregunta de prueba3","Pregunta de prueba4"];

var modal2 = {}
modal2.title= "modal 2";  
modal2.mainText = ["Pregunta de prueba5","Pregunta de prueba6","Pregunta de prueba7","Pregunta de prueba8"];

modals["modal1"] = modal1;
modals["modal2"] = modal2;

function goToRegistration() {
	location.href='registration.html';
	//window.open("https://www.w3schools.com"); 
	//window.alert("sometext");
	//window.open('/registration.html',windowName,'height=200,width=150');
}

function goToQuestions() {
	//location.href=
}




function createCheckboxes(mdl)
{


	var cbx = '';
	

		for(j in modals[mdl].mainText)
		{
			cbx +='<div class="input-group mb-3">';
		cbx+='<div class="input-group-prepend">';
		cbx+='<div class="input-group-text">';
		cbx+=' <input type="checkbox" aria-label="Checkbox for following text input">';
		cbx+='<label>';
		cbx += modals[mdl].mainText[j];
		cbx+='</label>';
		cbx+='</div></div></div>';	
		}
		
		if (mdl == 'modal1'){
			$('#cbxRespuesta1').append(cbx);
		} else if (mdl == 'modal2') {
			$('#cbxRespuesta2').append(cbx);
		}
		

	

}


 

createCheckboxes("modal1");
createCheckboxes("modal2");


});

