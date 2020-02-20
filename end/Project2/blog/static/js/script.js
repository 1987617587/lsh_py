var searchvisible = 0;

$("#search-menu").click(function(e){ 
    //This stops the page scrolling to the top on a # link.
    e.preventDefault();

    var val = $('#search-icon');
    if(val.hasClass('ion-ios-search-strong')){
        val.addClass('ion-ios-close-empty');
        val.removeClass('ion-ios-search-strong');
    }
    else{
         val.removeClass('ion-ios-close-empty');
        val.addClass('ion-ios-search-strong');
    }
    
    
    if (searchvisible ===0) {
        //Search is currently hidden. Slide down and show it.
        $("#search-form").slideDown(200);
        $("#s").focus(); //Set focus on the search input field.
        searchvisible = 1; //Set search visible flag to visible.
    } 

    else {
        //Search is currently showing. Slide it back up and hide it.
        $("#search-form").slideUp(200);
        searchvisible = 0;
    }
});

/*!
 * classie - class helper functions
 * from bonzo https://github.com/ded/bonzo
 * 
 * classie.has( elem, 'my-class' ) -> true/false
 * classie.add( elem, 'my-new-class' )
 * classie.remove( elem, 'my-unwanted-class' )
 * classie.toggle( elem, 'my-class' )
 */

/*jshint browser: true, strict: true, undef: true */
/*global define: false */

( function( window ) {

'use strict';

// class helper functions from bonzo https://github.com/ded/bonzo

function classReg( className ) {
  return new RegExp("(^|\\s+)" + className + "(\\s+|$)");
}

// classList support for class management
// altho to be fair, the api sucks because it won't accept multiple classes at once
var hasClass, addClass, removeClass;

if ( 'classList' in document.documentElement ) {
  hasClass = function( elem, c ) {
    return elem.classList.contains( c );
  };
  addClass = function( elem, c ) {
    elem.classList.add( c );
  };
  removeClass = function( elem, c ) {
    elem.classList.remove( c );
  };
}
else {
  hasClass = function( elem, c ) {
    return classReg( c ).test( elem.className );
  };
  addClass = function( elem, c ) {
    if ( !hasClass( elem, c ) ) {
      elem.className = elem.className + ' ' + c;
    }
  };
  removeClass = function( elem, c ) {
    elem.className = elem.className.replace( classReg( c ), ' ' );
  };
}

function toggleClass( elem, c ) {
  var fn = hasClass( elem, c ) ? removeClass : addClass;
  fn( elem, c );
}

var classie = {
  // full names
  hasClass: hasClass,
  addClass: addClass,
  removeClass: removeClass,
  toggleClass: toggleClass,
  // short names
  has: hasClass,
  add: addClass,
  remove: removeClass,
  toggle: toggleClass
};

// transport
if ( typeof define === 'function' && define.amd ) {
  // AMD
  define( classie );
} else {
  // browser global
  window.classie = classie;
}

})( window );
