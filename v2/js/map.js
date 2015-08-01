var map = L.map('map').setView([45.19, 5.76], 14);

var mapboxUrl = 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
mapboxAttribution = '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors';

L.tileLayer(mapboxUrl, {
attribution: mapboxAttribution,
maxZoom:18,
}).addTo(map);


L.easyButton('fa-compass', function(btn, map){
if(navigator.geolocation){
navigator.geolocation.getCurrentPosition(showPosition);

}else{
console.log("error");
}
}).addTo(map);


var marker;

map.on('click', function(e) {
if(marker != null){
map.removeLayer(marker)
}
$("#latitude").val(e.latlng.lat);
$("#longitude").val(e.latlng.lng);
marker = new L.marker([e.latlng.lat, e.latlng.lng]);
map.addLayer(marker);

});


function showPosition(position) {
if(marker != null){
map.removeLayer(marker);
}

marker = new L.marker([position.coords.latitude,position.coords.longitude]);
map.addLayer(marker);
map.panTo(new L.latLng(position.coords.latitude,position.coords.longitude));

}