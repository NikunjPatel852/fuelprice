
// Function created to load in charts from tableau. 
function initViz() {

        url = "https://public.tableau.com/views/yearly_avg_fuel_price/yearly_avg_by_fuel_type";
        viz = new tableau.Viz(yearlyAvgprice, url);
      
        url = "https://public.tableau.com/views/northvssouth/north_south_price_comp";
        viz = new tableau.Viz(northvsSouth, url);

        url = "https://public.tableau.com/views/monhtly_average_by_year/monthly_avg_year";
        viz = new tableau.Viz(monthlyByyear, url);

        url = "https://public.tableau.com/views/weekly_changes/weekly_cycle";
        viz = new tableau.Viz(weekly_cycle, url);

}; 

initViz(); 

