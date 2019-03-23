setTimeout(function(){

	const loginpage = document.getElementById('login-page');
	const bola = document.getElementById('bola');
	const form = document.querySelectorAll('form');

	bola.removeAttribute('class');
	loginpage.removeAttribute('id');



},5000);


function Login(){

	if(document.getElementById('user').value != "" && document.getElementById('pas').value != ""){

		document.getElementById('login-form').setAttribute('action','/Main/');

	}

	



}
