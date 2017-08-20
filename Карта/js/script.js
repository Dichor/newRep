//Определяем карту, координаты центра и начальный масштаб
var map = L.map('map').setView([47.240933, 39.710653], 17);
//Добавляем на нашу карту слой OpenStreetMap
L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
L.control.mousePosition().addTo(map);
// L.Control.measureControl().addTo(map);

var LeafIcon = L.Icon.extend({
    options: {
        iconSize:     [32, 37],
        shadowSize:   [51, 37],
        iconAnchor:   [16,37],
        shadowAnchor: [16, 37],
        popupAnchor:  [0, -30]
    }
});
var churchIcon = new LeafIcon({iconUrl: 'images/cross1.png'}),
    monumentIcon = new LeafIcon({iconUrl: 'images/monument.png'}),
    sportIcon = new LeafIcon({iconUrl: 'images/sp.png'});
L.marker([47.239220, 39.711080], {icon: churchIcon}).addTo(map).bindPopup("<div id = 'image'><img src='images/church.jpg'/></div><strong>Храм святой мученицы Татианы при ДГТУ</strong>");
L.marker([47.239210, 39.710500], {icon: monumentIcon}).addTo(map).bindPopup("<div id = 'image'><img src='images/monument.jpg'/></div><strong>Памятник студентам и сотрудникам РИСХМ</strong>");
L.marker([47.240856, 39.709850], {icon: sportIcon}).addTo(map).bindPopup("<div id = 'image'><img src='images/sport.jpg'/></div><strong>Спортивный манеж ДГТУ</strong>");