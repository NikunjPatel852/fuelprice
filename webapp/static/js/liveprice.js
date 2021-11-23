
// Read in flask end point
d3.json(`/ULPavgmetro`).then((data) => {
        console.log(data);
        d3.select("#final_score1")
            .append("h4")
            // .attr("class", "text-muted")
            .text(String(data[0]));
});

// Read in flask end point
d3.json(`/bestulpmetro`).then((data) => {
        console.log(data);
        d3.select("#final_score3")
            .append("h4")
            // .attr("class", "text-muted")
            .text(String(data[0]));
});

// Read in flask end point
d3.json(`/Diesavgmetro`).then((data) => {
        console.log(data);
        d3.select("#final_score2")
            .append("h4")
            // .attr("class", "title")
            .text(data[0]);
});
// Read in flask end point
d3.json(`/bestDLpmetro`).then((data) => {
        console.log(data);
        d3.select("#final_score4")
            .append("h4")
            // .attr("class", "text-muted")
            .text(data[0]);
});


function map() {

    url = "https://public.tableau.com/views/map_16375814493070/Sheet1";
        viz = new tableau.Viz(mapupl, url);
};

map();