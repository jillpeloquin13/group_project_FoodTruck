

function createMap(foodStations) {

  var container = L.DomUtil.get('map-id'); if(container != null){ container._leaflet_id = null; }

  // Create the tile layer that will be the background of our map
  var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "light-v10",
    accessToken: API_KEY
  });

  var map = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  maxZoom: 18,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
  }); 

  var defaultmap = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    })

  // Create a baseMaps object to hold the lightmap layer
  var baseMaps = {
    "Light Map": lightmap,
    "Road View": map
  };

  // Create an overlayMaps object to hold the bikeStations layer
  var overlayMaps = {
    "See my favorite Food Truck": foodStations
  };

  // Create the map object with options
  var map = L.map("map-id", {
    center: [39.36, - 98.05],
    zoom: 4,
    layers: [map, lightmap, foodStations]
  });

  // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(map);


};


function createMarkers(citydata) {


  console.log(citydata)

  var foodmarkers = [];

  for (var i = 0; i < citydata.length; i++) {
    var data= citydata[i];

    var foodIcon = L.icon({
      iconUrl: '/static/food-truck-clipart-md.png',
      iconSize:[30,20]
    }); 

    // For each station, create a marker and bind a popup with the station's name
    var foodmarker = L.marker([data.latitude, data.longitude], {icon: foodIcon})
    .bindPopup("<h3>" + "The Food Truck will be at " + data.display + "</h3>");

    // Add the marker to the bikeMarkers array
    foodmarkers.push(foodmarker);
    console.log(foodmarker)
  }

  // Create a layer group made from the bike markers array, pass it into the createMap function
  createMap(L.layerGroup(foodmarkers));

}

// Perform an API call to the Citi Bike API to get station information. Call createMarkers when complete
d3.json("http://127.0.0.1:5000/api/vendor").then(createMarkers);



var button = d3.select("#button");

// Select the form
var form = d3.select("#form");

// Create event handlers for clicking the button or pressing the enter key
button.on("click", runEnter);
form.on("submit",runEnter);

function runEnter() {

  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#example-form-input");

  // Get the value property of the input element
  var name = inputElement.property("value");

  // Print the value to the console
  console.log(name);
  var url = `http://127.0.0.1:5000/api/vendor/${name}`
  console.log(url); 
   
  d3.json(url).then(createMarkers);
  
}
