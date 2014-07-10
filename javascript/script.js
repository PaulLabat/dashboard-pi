function Poubelle() {
	var poubelle = document.getElementById("poubelle");
	var meteo = document.getElementById("meteo");
	meteo.style.visibility = "hidden";
	poubelle.style.visibility = "visible";
}
function Meteo() {
	var poubelle = document.getElementById("poubelle");
	var meteo = document.getElementById("meteo");
	poubelle.style.visibility = "hidden";
	meteo.style.visibility = "visible";
}

function refresh() {
    "use strict";
	location.reload(true);
}

setTimeout("refresh()", 600000);
