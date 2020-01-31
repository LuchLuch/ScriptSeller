			 var
					canv = document.getElementById("canvas"),
					ctx  = canv.getContext("2d");
			 canv.width = window.innerWidth;
			 canv.height = window.innerHeight;

			 // Code
			 var x = 900;
			 var y = 900;
			 ctx.fillStyle = "magenta";
			 ctx.fillRect(x,y,300,200);

			 var timerId = setInterval(function() {

			 	ctx.fillRect(x-=10,y-=10,300,200);

//              document.body.scrollTop = document.documentElement.scrollTop = 0;
			 },100);

			 setTimeout(function() {
  clearInterval(timerId);
//  alert( 'Go to the top' );
//  document.body.scrollTop = document.documentElement.scrollTop = 0;


}, 2000);


