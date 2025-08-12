```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_446.jpeg
document_name: chart
page_number: 446
page_id: chart#page_446
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:44:35Z
fidelity: lossless
-->

## Legend Order in Charts

### Overview

- The document introduces the use of legends in charts by specifying their order using the FilterItems Event.
- It discusses customizing the look and feel of legend items.
- Properties such as ChartLegend are utilized to adjust the appearance of the legend.

---

### Legend Item's Look and Feel

The legend item's look and feel can be customized to a good extent using the following properties in ChartLegend.

These settings affect all the items in the legend.

| ChartLegend Property       | Description                                                                                                                                                                                                 |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RowCount                   | Specifies the number of rows to be used in the legend.                                                                                                                                                     |
| ColumnCount                |Specifies the number of columns to be used in the legend.                                                                                                                                                  |
| ItemsAlignment             | Specifies the horizontal alignment of the items within the legend. Possible values:<br>- Near - Default value<br>- Center<br>- Far                                                                 |
| ShowItemsShadow            | Will render a shadow around the item image and text using the ItemsShadowColor. Default is false.                                                                                                         |
| ItemsShadowColor           | Specifies the color of the shadow to use. ShowItemsShadow should be set to true. Default is Gray.                                                                                                         |

---

*Figure 284: Chart with Legends in specified order using FilterItems Event*

![Illustrates Legend Order](#)

---

### Charts with Legends in Specified Order using FilterItems Event

The figure above illustrates a chart displaying three series with legends arranged in a specified order using the FilterItems Event. The chart provides a visual representation of how the legends can be customized for better clarity and user interaction.

---

### Conclusion

By utilizing the ChartLegend properties, developers can effectively control not only the arrangement but also the aesthetics of the legend items, providing a more user-friendly and visually appealing chart interface.

---

<!-- tags: [chart, legend, ChartLegend, FilterItems Event, RowCount, ColumnCount, ItemsAlignment, ShowItemsShadow, ItemsShadowColor] keywords: [Syncfusion Winforms, legend customization, legend properties, chart visual customization, FilterItems Event, legend arrangement] -->
```