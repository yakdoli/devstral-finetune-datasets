```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_478.jpeg
document_name: grid
page_number: 478
page_id: grid#page_478
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:59Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Figure 185: Resize to Fit

Note: The preceding image is the output of a demo that is available in the samples in the following installed location.

### Demo Location
<Install Location>\Syncfusion\EssentialStudio\<Version Number>\Windows\Grid.Windows\Samples\2.0\Grid Layout\Resize To Fit Demo

### Grid Setup
- The two buttons **Set RowHeight** and **Set Column Width** seen in the image above are used to set irregular height and width to the specified rows and columns of the grid respectively.
- The **ColWidths** – **Resize To Fit** and **RowHeights** – **Resize To Fit** are enabled only when the rows or columns are set to irregular height and width by using the **Set RowHeight** and **Set Column Width** buttons respectively.

### Feature Overview: ResizeToFitOptimized

**4.1.4.14.9 ResizeToFitOptimized**

**Description:**
Essential Grid supports a **ResizeToFitOptimized** feature to enable resizing of columns and rows based on the contents of grid cells. The existing **ResizeToFit** method doesn’t resize the columns or rows to make the entire cell value visible in the control. The **ResizeToFitOptimized** method is used for this purpose.

### Use Case Scenarios

- This feature enables you to display the entire cell with resized columns and rows even if the grid cells have special characters such as tab, newline, etc.

### Methods Table

#### Table 7: Method Table

| Method                      | Description                                                                                          | Parameters                                                                                                                                           | Return Type |
|-----------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| ResizeToFitOptimized        | Resizes a range of rows or columns to optimally fit contents of the specified range of cells. | Overloads:<br>1) ResizeToFitOptimized(GridRangeInfo range)<br>2) ResizeToFitOptimized(GridRangeInfo range, GridResizeToFitOptions option)<br>3) ResizeToFitOptimized(GridRangeInfo range, GridTextOptions textOption) | Void         |

## Footer
© 2013 Syncfusion. All rights reserved.
478 | Page
``` 

<!-- tags: [product, EssentialGrid, WindowsForms,ResizeToFit] keywords: [resizeToFitOptimized, GridRangeInfo, GridResizeToFitOptions, GridTextOptions, SetRowHeight, SetColumnWidth, Syncfusion, WindowsForms, grid] -->