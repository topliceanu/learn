$(function () {
    'use strict';

    // Make monochrome.
    Highcharts.getOptions().plotOptions.pie.colors = (function () {
        var colors = [],
            base = Highcharts.getOptions().colors[0],
            i;

        for (i = 0; i < 10; i += 1) {
            // Start out with a darkened base color (negative brighten), and end
            // up with a much brighter color
            colors.push(Highcharts.Color(base).brighten((i - 3) / 7).get());
        }
        return colors;
    }());


    // OVERVIEW > USER STATS
    $('.overview .engagement .users').highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: 'User Stats'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: false
                },
                showInLegend: true
            }
        },
        series: [{
            type: 'pie',
            name: 'User stats',
            data: [
                {
                    name: 'New',
                    y: 12452,
                    sliced: false,
                    selected: false
                },
                ['Returning(non-RF)', 2463],
                ['Returning(RF)', 23567],
            ]
        }]
    });


    // OVERVIEW > SESSION DURATIONS
    $('.overview .engagement .session-duration').highcharts({
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Session Duration'
        },
        subtitle: {
            text: 'Number of session lasting within a threshold'
        },
        xAxis: {
            categories: ['0-10 seconds', '10-30 seconds', '30-60 seconds', '60-180 seconds', '>180 seconds'],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Number of sessions',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'Without RF',
            data: [274449, 33543, 33460, 68646, 88975]
        }, {
            name: 'With RF',
            data: [374449, 43543, 43460, 88636, 98975]
        }]
    });


    // OVERVIEW > SESSION PER USER
    $('.overview .engagement .sessions-user').highcharts({
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Session Per User'
        },
        subtitle: {
            text: 'Number of session lasting within a threshold'
        },
        xAxis: {
            categories: ['1 session', '2 sessions', '3 sessions', '4 sessions', '5 sessions', '>5 sessions'],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Count of sessions',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'Without RF',
            data: [149551, 78901, 30118, 24258, 15648, 49628]
        }, {
            name: 'With RF',
            data: [249551, 88901, 50118, 34258, 25648, 59628]
        }]
    });


    // OVERVIEW > PAGES PER SESSION
    $('.overview .engagement .session-pages').highcharts({
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Session Depth'
        },
        subtitle: {
            text: 'Number of RF events per session'
        },
        xAxis: {
            categories: ['<1 event', '2 events', '3 event', '4 events', '5 events', '>5 events'],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Count of events per session',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'Without RF',
            data: [85895, 164577, 89412, 52456, 30792, 21949, 14072]
        }, {
            name: 'With RF',
            data: [3895, 364577, 99412, 62456, 40792, 31949, 24072]
        }]
    });


    $('#campaign1 .chart').highcharts({
        title: {
            text: '[product-page] recommender widget',
            x: -20 //center
        },
        subtitle: {
            text: 'Conversions: clicks/impressions',
            x: -20
        },
        xAxis: {
            categories: [
                'today',
                'yesterday',
                '-2 days',
                '-3 days',
                '-4 days',
                '-5 days',
                '-6 days',
            ].reverse()
        },
        yAxis: {
            title: {
                text: '%'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: 'impressions',
            data: [40.19, 44.21, 46.32, 55.12, 49.67, 34.93, 43.56]

        }]
    });


    $('#campaign2 .chart').highcharts({
        title: {
            text: '[popup] Subscribe to email',
            x: -20 //center
        },
        subtitle: {
            text: 'Conversions: subscribers/impressions',
            x: -20
        },
        xAxis: {
            categories: [
                'today',
                'yesterday',
                '-2 days',
                '-3 days',
                '-4 days',
                '-5 days',
                '-6 days',
            ].reverse()
        },
        yAxis: {
            title: {
                text: '%'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: 'impressions',
            data: [4.19, 5.21, 4.32, 5.12, 9.67, 4.93, 3.56]

        }]
    });


    $('#campaign3 .chart').highcharts({
        title: {
            text: '[popup] Cart Abandoment',
            x: -20 //center
        },
        subtitle: {
            text: 'Conversions: recovered/abandoned carts',
            x: -20
        },
        xAxis: {
            categories: [
                'today',
                'yesterday',
                '-2 days',
                '-3 days',
                '-4 days',
                '-5 days',
                '-6 days',
            ].reverse()
        },
        yAxis: {
            title: {
                text: '%'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: [{
            name: 'impressions',
            data: [4.19, 5.21, 4.32, 5.12, 3.97, 4.93, 3.56]

        }]
    });

    $('#campaign3 .controls .slider-selection').slider({
        min: 0,
        max: 100,
        step: 1,
        value: 50,
        tooltip: 'show'
    });

    $('.campaign-details-content .slider-selection').slider({
        min: 0,
        max: 100,
        step: 1,
        value: 50,
        tooltip: 'show'
    });


});
