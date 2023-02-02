let map, heatmap;

// function intToFloat(num, decPlaces) { return num.toFixed(2); }

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 7,
    center: { lat: 38.5, lng: -8.2},
    mapTypeId: "satellite",
  });
  heatmap = new google.maps.visualization.HeatmapLayer({
    data: getPoints(),
    map: map,
  });

  heatmap.set("maxIntensity", 100);
  heatmap.set("radius", 5);
  heatmap.set("opacity", 1);

  document
    .getElementById("intensity")
    .addEventListener('click', changeIntensity)
  document
    .getElementById("radius")
    .addEventListener('click', changeRadius)
  document
    .getElementById("opacity")
    .addEventListener('click', changeOpacity)
}

var disp_intencity = document.getElementById("disp_intensity");
  disp_intensity.innerHTML= 100;
var disp_radius = document.getElementById("disp_radius");
  disp_radius.innerHTML = 5;
var slider_opacity = document.getElementById("disp_opacity");
  disp_opacity.innerHTML = 1;
      
function changeIntensity() {
  disp_intensity.innerHTML = this.value;
  heatmap.set("maxIntensity", this.value);
}
function changeRadius() {
  disp_radius.innerHTML = this.value;
  heatmap.set("radius", this.value);
}

function changeOpacity() {
  disp_opacity.innerHTML = this.value;
  heatmap.set("opacity", this.value/100);
}


window.initMap = initMap;