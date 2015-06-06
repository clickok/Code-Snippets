

function () { 
    var overlay = document.createElement('overlay');
    overlay.css.({
        position: absolute,
        background-color: rgba(0, 0, 0, 0.5),
        z-index: 1000000,
    });

    if (document.body.addEventListener) {
        document.body.addEventListener('mouseover', handler, false);
    }
    else if (document.body.attachEvent) {
        document.body.attachEvent('mouseover', function(e) {
            return handler(e || window.event);
    });
    }
    else {
        document.body.onmouseover = handler;
    }

    function handler(event) {
        if (event.target)
        {
            prev = event.target;

        }
    }
};


function fillScreen(elem) {};