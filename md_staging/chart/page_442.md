```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_442.jpeg
document_name: chart
page_number: 442
page_id: chart#page_442
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:44:22Z
fidelity: lossless
-->

## Legend Positioning

The legend positioning can be affected in the following ways.

| ChartLegend Property         | Description                                                                                                                                                                                                                                                                           |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Position**                 | Specifies the position relative to the chart at which to render the legend. <br> - Top - above the chart <br> - Left - left of the chart <br> - Right - right of the chart <br> - Bottom - below the chart <br> - Floating - will not be docked to any specific location (default setting)                                      |
| **LegendAlignment**          | When docked to a side, this property specifies how the legend should be aligned with respect to the chart boundaries.                                                                                                                                                               |
| **LegendPlacement**          | Specifies the placement of a legend in a chart. It can be placed Inside or Outside the chart area using ChartPlacement enum.                                                                                                                                                        |
| **DockingFree**              | If set to **true**, the legend will be floating and cannot be dragged and docked to the sides.                                                                                                                                                                                    |
| **Behavior**                 | Specifies the docking behavior of the Legend. <br> - Docking - It is dockable on all four sides <br> - Movable - It is movable <br> - All - It is movable and dockable <br> - None - It is neither movable nor dockable                                                                                    |
| **FloatingAutoSize**         | Specifies whether to determine the size automatically or not, while floating.                                                                                                                                                                                                      |
| **OnlyColumnsForFloating**   | The legend items will be displayed vertically in columns when floating.                                                                                                                                                                                                            |
| **RowsCount**                | Specifies the number of rows in which the legend items should be rendered.                                                                                                                                                                                                       |
| **ColumnsCount**             | Specifies the number of columns in which the legend items should be rendered.                                                                                                                                                                                                     |

**Note:** Note that the user can drag the legend around during run time. He can dock it to the sides if docking is enabled. Docking behavior is controlled by the **Behavior** property, which is described in the above table.

```