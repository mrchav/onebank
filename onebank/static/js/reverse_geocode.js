ymaps.ready(init);

function init() {
var adres = document.getElementById('map_adres');

var myGeocoder = ymaps.geocode(adres.innerHTML);
myGeocoder.then(
    function (res) {

        var coord = res.geoObjects.get(0).geometry.getCoordinates();

        var myMap = new ymaps.Map('map', {
            center: coord,
            zoom: 13
        }, {
            searchControlProvider: 'yandex#search',
        });

      var BankPlacemark = new ymaps.Placemark(coord, null, {
          preset: 'islands#blueDotIcon'
        });
      myMap.geoObjects.add(BankPlacemark);

    }
);


}