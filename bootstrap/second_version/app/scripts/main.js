$(function () {
    'use strict';

    // Enable all tooltips.
    $('[data-toggle="tooltip"]').tooltip();

    // Global Highcharts Options.
    Highcharts.setOptions({
        chart: {
        },
        exporting: {
            enabled: false
        },
        credits: {
            enabled: false
        }
    });

    $('.plain-chart').each(function (index, elem) {
        $(elem).highcharts({
            chart: {
                backgroundColor:'rgba(255, 255, 255, 0.1)',
                spacingBottom: 0,
                spacingTop: 0,
                spacingLeft: 0,
                spacingRight: 0,
                marginBottom: 0,
                marginTop: 0,
                marginLeft: 0,
                marginRight: 0,

                type: 'area',
                height: 60
            },
            title: {
                text: ''
            },
            xAxis: {
                tickWidth: 0,
                gridLineWidth: 0
            },
            yAxis: {
                tickWidth: 0,
                gridLineWidth: 0
            },
            tooltip: {
                pointFormat: '{point.value}'
            },
            plotOptions: {
                area: {
                    marker: {
                        enabled: false
                    }
                }
            },
            series: [{
                name: 'USA',
                showInLegend: false,
                lineWidth: 2,
                data: (function () {
                    var numPoints = 30 + Math.floor(Math.random() * 20),
                        data = [], i, point;
                    for (i = 0; i < numPoints; i ++) {
                        point = 50 + Math.floor(Math.random() * 50);
                        data.push(point);
                    }
                    return data;
                })()
            }]
        });
    });

     $('.pie-chart').highcharts({
        chart: {
            type: 'pie',
            backgroundColor:'rgba(255, 255, 255, 0.1)',
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            height: 200,

            //spacingBottom: 0,
            spacingTop: 0,
            spacingLeft: 0,
            spacingRight: 0,
            //marginBottom: 0,
            marginTop: 0,
            marginLeft: 0,
            marginRight: 0,

        },
        title: {
            text: ''
        },
        tooltip: {
            enabled: false
        },

        plotOptions: {
            series: {
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    formatter: function() {
                        return Math.round(this.percentage*100)/100 + ' %';
                    },
                    distance: -30,
                    color:'white'
                },
                showInLegend: true
            }
        },
        series: [{
            type: 'pie',
            name: 'Browser share',
            data: [
                ['New Users',   57.2],
                ['Returning',   42.8]
            ]
        }]
    });


    // Create the chart
    $('.column-chart').highcharts({
        chart: {
            type: 'column',
            backgroundColor:'rgba(255, 255, 255, 0.1)',
            height: 150,
            marginTop: 0
        },
        title: {
            text: ''
        },
        xAxis: {
            gridLineWidth: 0,
            labels: {
               enabled: false
           },
            tickLength: 0
        },
        yAxis: {
            title: {
                text: ''
            },
            gridLineWidth: 0,
            labels: {
               enabled: false
           },
            tickLength: 0
        },
        legend: {
            enabled: false
        },
        plotOptions: {
            series: {
                marker: {
                    enabled: false
                },
                borderWidth: 0,
                dataLabels: {
                    enabled: true,
                    format: '{point.name}'
                }
            }
        },
        tooltip: {
            pointFormat: '<b>{point.y:.1f}%</b> of total'
        },

        series: [{
            name: 'Sources',
            data: [
                {name: 'facebook', y: 20},
                {name: 'twitter', y: 10},
                {name: 'google', y: 50},
                {name: 'rightfunnel', y: 20}
            ]
        }]
    });



    $('.vertical-column-chart').highcharts({
        chart: {
            type: 'bar',
            backgroundColor:'rgba(255, 255, 255, 0.1)',
            height: 200
        },
        title: {
            text: ''
        },
        xAxis: {
            categories: ['0-10 sec', '10-30 sec', '30-60 sec', '60-180 sec', '180+ sec'],
            title: {
                text: ''
            },
            gridLineWidth: 0,
            tickLength: 0
        },
        yAxis: {
            min: 0,
            title: {
                text: ''
            },
            labels: {
                enabled: false
            },
            gridLineWidth: 0
        },
        tooltip: {
            pointFormat: '{point.y} sessions'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: false
                }
            }
        },
        legend: {
            enabled: false
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'Number of Sessions',
            data: [807, 431, 135, 203, 512]
        }]
    });


    $('.vertical-column-chart-2').highcharts({
        chart: {
            type: 'bar',
            backgroundColor:'rgba(255, 255, 255, 0.1)',
            height: 150
        },
        title: {
            text: ''
        },

        xAxis: {
            categories: ['1 session', '2 sessions', '3 sessions', '4 sessions', '> 4 sessions'],
            title: {
                text: ''
            },
            gridLineWidth: 0,
            tickLength: 0
        },
        yAxis: {
            min: 0,
            title: {
                text: ''
            },
            labels: {
                enabled: false
            },
            gridLineWidth: 0
        },
        tooltip: {
            pointFormat: '{point.y} users'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: false
                }
            }
        },
        legend: {
            enabled: false
        },
        credits: {
            enabled: false
        },
        series: [{
            name: 'Number of Sessions',
            data: [1807, 531, 235, 103, 1012]
        }]
    });

    $('.double-line-chart').highcharts({
        chart: {
            type: 'column',
            backgroundColor:'rgba(255, 255, 255, 0.1)',
            height: 200,
            marginTop: 0
        },
        title: {
            text: ''
        },
        xAxis: {
            gridLinesWidth: 0,
            labels: {
                enabled: false
            },
            tickLength: 0
        },
        yAxis: {
            title: {
                text: ''
            },
            gridLineWidth: 0,
            labels: {
               enabled: false
           },
            tickLength: 0

        },
        tooltip: {
            headerFormat: '<span style="font-size:10px"></span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} carts</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            },
            series: {
                marker: {
                    enabled: false
                },
                borderWidth: 0,
                dataLabels: {
                    enabled: true,
                    format: '{point.name}'
                }
            }

        },
        series: [{
            name: 'Abandoned',
            data: [249, 271, 206, 329, 344, 276, 235]

        }, {
            name: 'Recovered',
            data: [83, 78, 98, 93, 106, 84, 105]

        }]
    });


    // CAMPAIGNS PAGE
    $('.campaign-evolution').each(function (index, elem) {
        $(elem).highcharts({
            chart: {
                type: 'area',
                backgroundColor:'rgba(255, 255, 255, 0.1)',
                height: 25,

                spacingBottom: 0,
                spacingTop: 0,
                spacingLeft: 0,
                spacingRight: 0,
                marginBottom: 0,
                marginTop: 0,
                marginLeft: 0,
                marginRight: 0
            },
            title: {
                text: ''
            },
            xAxis: {
                tickWidth: 0,
                gridLineWidth: 0
            },
            yAxis: {
                tickWidth: 0,
                gridLineWidth: 0
            },
            tooltip: {
                pointFormat: '{point.value}'
            },
            plotOptions: {
                area: {
                    marker: {
                        enabled: false
                    }
                }
            },
            series: [{
                name: 'USA',
                showInLegend: false,
                lineWidth: 2,
                data: (function () {
                    var numPoints = 50 + Math.floor(Math.random() * 20),
                        data = [], i, point;
                    for (i = 0; i < numPoints; i ++) {
                        point = 50 + Math.floor(Math.random() * 50);
                        data.push(point);
                    }
                    return data;
                })()
            }]
        });
    });


    // CAMPAIGN EDIT PAGE
    $('.detailed-events-report').highcharts({
        chart: {
            type: 'area'
        },
        title: {
            text: 'Events Relevant to the Current Campaign'
        },
        xAxis: {
            categories: ['Mar 1', 'Mar 2', 'Mar 3', 'Mar 4', 'Mar 5', 'Mar 6', 'Mar 7']
        },
        yAxis: {
            title: {
                text: 'Number of Events'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        plotOptions: {
            area: {
                stacking: 'normal',
                lineColor: '#666666',
                lineWidth: 1,
                marker: {
                    lineWidth: 1,
                    lineColor: '#666666'
                }
            }
        },
        series: [{
            name: 'sent emails',
            data: [678, 634, 689, 598, 578, 599, 611]
        }, {
            name: 'opened emails',
            data: [243, 254, 287, 203, 291, 215, 343]
        }, {
            name: 'clicks',
            data: [215, 223, 237, 189, 255, 202, 323]
        }, {
            name: 'purchases',
            data: [23, 29, 24, 23, 37, 24, 35]
        }]
    });

});
