# Chart.js and Canvas

## Chart.js
A JavaScript plugin that uses HTML5's canvas element

### Setting up a chart
1. Download Chart.js.
1. Copy Chart.min.js into working directory.
1. Import script into desired HTML page.
1. Create an element in the HTML with `<canvas></canvas>` tags.

**Within the script:**
1. Retrieve context of the canvas using  
`let <variableName> = document.getElementById('<variableName>').getContext('2d');`  
1. Add context to HTML page.  
`new Chart(<variableName>).<type of chart>(<variableName>Data);`
1. Create the data for the chart.  
```
let <variableName>Data = {    
    labels: [], // The is typically the x-axis labels and values are separated by a comma
    datasets: [
        {
            fillColor: <value>,
            strokeColor: <value>,
            pointColor: <value>,
            pointStrokeColor: <value>,
            data: [<values>]
        }
    ]
}
```

### Types of Charts and data constructs for above datasets
1. Line chart  
`new Chart(<variableName>).Pie(pieData, pieOptions);`
```
let pieData = [
    {
        value: <% of pie chart>,  // Do this and the next line for each wedge of the pie.  Separate with a comma between {}'s.
        color: <value>
    }
]
```
1. Bar chart
`new Chart(variableName).Bar(barData);`  
```
let barData = {
    labels : [],
    datasets: [
        {
            fillColor: <value>,  // Do this and the next line for each bar value.  Separate with a comma between {}'s.
            data: [values]
        }
    ]
}
```
## Canvas
1. If no width and height specified, default is 300px x 150px.  
1. id typically supplied to make it easier to idenfity in script.
1. Can be styled like any normal image, but rules do not affect actual drawing on the canvas.
1. Fallback content for things like screen readers goes between the `<canvas></canvas>` tags.
1. Provides one ore more rendering contexts.
1. To render, use
```
let canvas = document.getElemnetByID('variableName');  
let ctx = canvas.getContext('2d');
```
