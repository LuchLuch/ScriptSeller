    var c = ["s"]
	new Chartist.Line('.ct-golden-section', {

    labels: c,
        series: [
            [12, 9, 1, 50, 4,12, 9, 1, 5, 4],
            [2, 1, 4.7, 5.5, 8,2, 1, 4.7, 5.5, -8],

        ]
    }, {
        fullWidth: true,
        chartPadding: {
            right: 0,
            top: 50

        }
});

document.span.onmouseover = document.span.onmouseout = handler;
function handler(event) {
      var audio = document.getElementsByTagName("audio")[0];
audio.play();

}