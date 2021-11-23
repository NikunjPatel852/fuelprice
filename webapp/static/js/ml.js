d3.selectAll("body").on(updatePlotly);

function updatePlotly() {
    
    // d3.json('/mlpredict').then(function(data) {
    //     console.log(data)
    // })

    d3.json("/mlpredict").then(function (data){
        console.log(data);

            var table = new Tabulator("#machinlearn-table", {
                data:data,
                height:"311px",
                layout:"fitColumns",
                columns:[
                    {title:"Actual", field:"Actual", width:150},
                    {title:"LineearReg", field:"LineearReg"},   
                    {title:"LGBMRegressor", field:"LGBMRegressor"},
                    {title:"LinearSVR", field:"LinearSVR"},
                    {title:"RandomForestRegressor", field:"RandomForestRegressor"}
                ]
        });
        
    });

    url = "https://public.tableau.com/views/map_16375814493070/Sheet1";
    viz = new tableau.Viz(machine_learning_chart, url);

};

updatePlotly();

