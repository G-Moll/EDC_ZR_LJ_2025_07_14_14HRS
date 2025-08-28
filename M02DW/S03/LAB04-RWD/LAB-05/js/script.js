
var ua = navigator.userAgent;
console.log( ua  );

console.log(ua.indexOf( "Windows" ));
console.log(ua.indexOf( "Android" ));
console.log(ua.indexOf( "iPhone" ));

if( ua.indexOf( "Android" ) >= 0 || ua.indexOf( "iPhone" ) >= 0 ) {
    window.location = "http://localhost:3000/index-smartphone.html";
}

console.log( window.location );

// http://localhost:3000/index.html
// http://localhost:3000/index-smartphone.html

// -1, 0 > =
/*
Smartphones
    - Android
    - iPhone

Tablet
    - iPad
    - Androind *

Computer
    - Windows
    - MacOS
    - Linux
*/
