google.load("maps", "2");

$(document).unload(function(){
    GUnload();
});

$(document).ready(function(){
    $("input.location").each(function (i) {
        var map = document.createElement('div');
        map.className = "location_map";
        this.parentNode.insertBefore(map, this);
        $(this).css('display','none');

        var lat = 39.952335;
        var lng = -75.163789;
        if (this.value.split(',').length == 2) {
            values = this.value.split(',');
            lat = values[0];
            lng = values[1];
        }
        var center = new GLatLng(lat,lng);

        var map = new google.maps.Map2(map);
        map.addControl(new GSmallMapControl());
        map.setCenter(center, 14);

        this.marker = new GMarker(center);
        map.addOverlay(this.marker);
        
        map.openInfoWindowHtml(center,"<a href='http://maps.google.com/?saddr=&daddr="+center+"&z=13'>Get directions");    
    });
});
