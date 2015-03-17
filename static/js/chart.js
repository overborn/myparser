$(function () {
    $('#id_region').change(function(){
        var region = $(this).val();
        $.get('/build_chart/', {region: region}, function(data){
            $('#container').highcharts({
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Показатели по области'
                },

                xAxis: {
                    categories: data['xAxis'],
                    crosshair: true
                },
                yAxis: {
                    min: 0,
                    title: {
                        text: 'Показатель'
                    }
                },
                tooltip: {
                    headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                    pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                        '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
                    footerFormat: '</table>',
                    shared: true,
                    useHTML: true
                },
                plotOptions: {
                    column: {
                        pointPadding: 0.2,
                        borderWidth: 0
                    }
                },
                credits: {
                    enabled: false
                },
                series: [{
                    name: region,
                    data: data['yAxis']
                
                }]
            });
        });
    });
    
    $('#id_region').change()
});