function refresh() {
	location.reload(true);
}


function Meteo() {
	var meteo = document.getElementById("meteo");
	var poubelle = document.getElementById("poubelle");
	var menuMeteo = document.getElementById("menuMeteo");
	var menuPoubelle = document.getElementById("menuPoubelle");

	poubelle.style.visibility = "hidden";
	meteo.style.visibility ="visible";
	menuMeteo.style.backgroundImage = "linear-gradient(#dedede, #6e6e6e)";
	menuPoubelle.style.backgroundImage = "linear-gradient(#6e6e6e, #dedede)";	
}

function Poubelle() {
	var poubelle = document.getElementById("poubelle");
	var meteo = document.getElementById("meteo");
	var menuPoubelle = document.getElementById("menuPoubelle");
	var menuMeteo = document.getElementById("menuMeteo");


	meteo.style.visibility = "hidden";
	poubelle.style.visibility = "visible";
	menuPoubelle.style.backgroundImage = "linear-gradient(#dedede, #6e6e6e";
	menuMeteo.style.backgroundImage = "linear-gradient(#6e6e6e, #dedede)";	
}



window.setTimeout("refresh()", 60000);