```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_599.jpeg
document_name: chart
page_number: 599
page_id: chart#page_599
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:50:06Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This page demonstrates the **Essential Chart** in interaction with the **Essential Grid**, showcasing how data from the grid can be visualized in charts.
- The chart displays three series of data (Series0, Series1, Series2) extracted from the grid. Each series corresponds to a column in the grid.
- The example highlights how to bind chart data dynamically from a grid, providing an interactive and integrated user interface.

## Content

### Data Grid Interaction Example

#### Grid Data

The following table shows the data populated in the grid, which serves as the source for the chart:

| A           | B           | C           | D           | E           | F           | G           | H           |
|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| 1           | 2.7313777   | 20.629898   | 20.445380   | 18.166092   | 24.023313   | 10.370515   | 26.067572   |
| 2           | 41.772156   | 41.134484   | 45.801838   | 26.099261   | 40.781914   | 16.589995   | 44.140266   |
| 3           | 14.088424   | 7.8898641   | 36.765727   | 0.0899115   | 9.8047393   | 2.6983694   | 29.746208   |
| 4           | 29.444343   | 20.592892   | 25.541384   | 35.901997   | 23.322617   | 12.333244   | 39.308891   |
| 5           | 48.206503   | 5.7733126   | 17.950836   | 48.824408   | 37.302331   | 14.027290   | 21.710497   |
| 6           | 13.790842   | 7.3291798   | 44.190727   | 9.3181971   | 36.961111   | 44.841513   | 33.864171   |
| 7           | 30.624307   | 16.511343   | 41.139703   | 43.719993   | 8.6172848   | 21.179264   | 15.593100   |
| 8           | 27.281103   | 31.086227   | 29.277655   | 4.2731413   | 49.155150   | 8.3151123   | 39.939027   |
| 9           | 30.987872   | 34.850845   | 7.3802273   | 12.458917   | 15.512699   | 22.115163   | 26.402165   |
| 10          | 28.469073   | 18.953423   | 4.6926861   | 36.524482   | 31.761952   | 31.695160   | 14.633608   |

### Chart Visualization

#### Chart Legend
- **Series0**: Orange bars
- **Series1**: Blue bars
- **Series2**: Red bars

#### Chart Description
The chart visualizes the data for each row across the three selected series:

```markdown
| Row | Series0 | Series1 | Series2 |
|-----|---------|---------|---------|
| 1   | 20.629898 | 20.445380 | 18.166092 |
| 2   | 41.134484 | 45.801838 | 26.099261 |
| 3   | 7.8898641 | 36.765727 | 0.0899115 |
| 4   | 20.592892 | 25.541384 | 35.901997 |
| 5   | 5.7733126 | 17.950836 | 48.824408 |
| 6   | 7.3291798 | 44.190727 | 9.3181971 |
| 7   | 16.511343 | 41.139703 | 43.719993 |
| 8   | 31.086227 | 29.277655 | 4.2731413 |
| 9   | 34.850845 | 7.3802273 | 12.458917 |
| 10  | 18.953423 | 4.6926861 | 36.524482 |
```

The chart's y-axis ranges from -10 to 60, and the x-axis corresponds to the row numbers (1 to 10) of the grid.

#### Example Chart
![Bar Chart](http://placeholder-link-for-visualization.png)

This bar chart shows the visualization of grid data, with Series0, Series1, and Series2 distinguished by their respective colors.

## Page-level Navigation/TOC (if applicable)
- [Essential Chart Overview]
- [Data Grid Integration]
- [Chart Customization]

## Cross References
See also:
- [Essential Grid Documentation]
- [Chart Types and Features]

<!-- tags: [Essential Chart, Windows Forms, Grid Interaction, Data Visualization, Syncfusion Winforms] keywords: [Essential Grid, Chart, Data Binding, Series, Visual Data Representation, Interactive UI] -->
```