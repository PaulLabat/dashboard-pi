function Poubelle() {
	var poubelle = document.getElementById("poubelle");
	var meteo = document.getElementById("meteo");
	var menuPoubelle = document.getElementById("menuPoubelle");
	var menuMeteo = document.getElementById("menuMeteo");

	meteo.style.visibility = "hidden";
	poubelle.style.visibility = "visible";
	menuPoubelle.style.backgroundImage = "linear-gradient(#6e6e6e, #dedede)";
	menuMeteo.style.backgroundImage = "linear-gradient(#dedede, #6e6e6e)";	
}
function Meteo() {
	var poubelle = document.getElementById("poubelle");
	var meteo = document.getElementById("meteo");
	var menuPoubelle = document.getElementById("menuPoubelle");
	var menuMeteo = document.getElementById("menuMeteo");
	poubelle.style.visibility = "hidden";
	meteo.style.visibility = "visible";
	menuMeteo.style.backgroundImage = "linear-gradient(#6e6e6e, #dedede)";	
}

function refresh() {
    "use strict";
	location.reload(true);
}

setTimeout("refresh()", 600000);
