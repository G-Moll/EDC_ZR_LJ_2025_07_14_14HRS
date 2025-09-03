var listDevices = [ "android", "iphone", "bb10", "ipad", "tablet" ];
var ua = navigator.userAgent.toLowerCase();

for( var i = 0; i < listDevices.length; i ++ ) {
    if( ua.indexOf( listDevices[ i ] ) >= 0 ) {
        var matchDevice = checkDevice( listDevices[ i ] );
        if( matchDevice == "phone" ) {
            window.location = "http://localhost:3000/index-smartphone.html";
        }
        else {
            window.location = "http://localhost:3000/index-tablet.html";
        }
        break;
    }
}

function checkDevice( device ) {
    var currentDevice = "";

    switch( device ) {
        case "ipad":
            currentDevice = "tablet";
            break;
        case "iphone":
        case "bb10":
            currentDevice = "phone";
            break;
    }
    return currentDevice;
}
// checkDevice( "ipad" );
// checkDevice( "iphone" );
// checkDevice( "android" );
// checkDevice( "bb10" );
