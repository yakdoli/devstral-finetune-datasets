```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_531.jpeg
document_name: grid
page_number: 531
page_id: grid#page_531
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:22:39Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## 4.1.4.31 Zooming options

This section discusses the following zooming options:

### 4.1.4.31.1 Cell-level and grid-level

We can implement zooming functionality in Essential Grid to show a magnified image of the Grid for better visualization. A method named ZoomGrid is used for this purpose. It accepts the percentage of zoom as the parameter and then uses this value to set the font size and cell size for the grid. Zooming can be implemented at cell-level and at grid-level.

The preceding screen shot shows a grid that is zoomed to the grid-level.

![Figure: Zoom Grid Demo](https://example.com/ZoomGridDemo.png)

*Zoom Option*
* 100%
* Zoom Cell (Checkbox)

|  | A    | B      | C       | D       | E    |
|---|------|--------|---------|---------|------|
| 1 | 0    | name0  | desc0   | addr0   | city |
| 2 | 1    | name1  | desc1   | addr1   | city |
| 3 | 2    | name2  | desc2   | addr2   | city |
| 4 | 3    | name3  | desc3   | addr3   | city |
| 5 | 4    | name4  | desc4   | addr4   | city |
| 6 | 5    | name5  | desc5   | addr5   | city |
| 7 | 6    | name6  | desc6   | addr6   | city |
| 8 | 7    | name7  | desc7   | addr7   | city |
| 9 | 8    | name8  | desc8   | addr8   | city |

*188%*

<!-- tags: [grid, zooming, EssentialGrid, Windows Forms, cell-level, grid-level, font size, cell size] keywords: [zooming, magnified image, better visualization, ZoomGrid, percentage of zoom, cell size, grid-level] -->
```