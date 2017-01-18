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

        var lat = 39.953333;
        var lng = -75.17;
        if (this.value.split(',').length == 2) {
            values = this.value.split(',');
            lat = values[0];
            lng = values[1];
        }
        var title = "{{ event.title }}"
        var center = new GLatLng(lat,lng);

        var map = new google.maps.Map2(map);
        map.enableScrollWheelZoom();
        map.addControl(new GSmallMapControl());
        map.setCenter(center, 14);

        this.marker = new GMarker(center);
        map.addOverlay(this.marker);
        
        map.openInfoWindowHtml(map.getCenter(),"<a target='_blank' href='http://maps.google.com/maps?saddr=&daddr="+center+"'>Get directions to this event</a>");

        GEvent.bind(map, "click", this, this.onMapClick);
    });
});
