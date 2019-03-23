$(document).ready(function(){

	function clock(){

		const now = new Date();
		const secs = ('0' + now.getSeconds()).slice(-2);
		const mins = ('0' + now.getMinutes()).slice(-2);
		const hr = now.getHours();
		const Time = hr + ":" + mins + ":" + secs;
		document.getElementById('jam').innerHTML = Time;
		requestAnimationFrame(clock);

		if (Time >= '18:37:00'){


			document.getElementsByTagName('body')[0].style.backgroundImage = "linear-gradient(rgba(0,0,0,0.6),rgba(0,0,0,0.6)),url('/static/Main/img/anime.jpg')";
			document.getElementById('timer').setAttribute('class','hilang');
			document.getElementById('surat').removeAttribute('id');

		}

	}

	requestAnimationFrame(clock);

});