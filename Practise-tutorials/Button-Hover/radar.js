anychart.onDocumentReady(function () {
    // our data from bulbapedia
    var data1 = [
        { x: "O", value: 1 },
        { x: "C", value: 2 },
        { x: "E", value: 3 },
        { x: "A", value: 4 },
        { x: "N", value: 5 }
    ];

    // create radar chart
    var chart = anychart.radar();

    // set chart yScale settings
    chart.yScale()
        .minimum(0)
        .maximum(5)
        .ticks({ 'interval': 5 });

    // color alternating cells
    chart.yGrid().palette(["gray 0.1", "gray 0.2"]);

    // create first series
    chart.area(data1).name('Ocean').markers(true).fill("#E55934", 0.3).stroke("#E55934")

    // set chart title
    chart.title("Radar Ocean Chart")
        // set legend
        .legend(true);

    // set container id for the chart
    chart.rc('rc');
    // initiate chart drawing
    chart.draw();

});