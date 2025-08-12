```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_878.jpeg
document_name: grid
page_number: 878
page_id: grid#page_878
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:36Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
gridGroupingControl1.BaseStyles.AddRange(new GridTableBaseStyle() { style1, 
								style2 });
							 
gridGroupingControl1.Appearance.AlternateRecordFieldCell.BaseStyle = 
'"BaseStyle 1"';
gridGroupingControl1.Appearance.AnyCell.BaseStyle = '"BaseStyle 2"';
```

## 4.3.4.5.7 Get Cell Styles

This topic elaborates the way of retrieving the style information of grid cells. On a mouse hit, when you want to retrieve the content of underlying cells and also its style information, it is good to use the `PointToTableCellStyle` method on the instances of the Grid Table control.

### PointToTableCellStyle Method

For any given point on the grid, this method will return the style information of the underlying cell that is displayed under that point. If the underlying cell belongs to a nested table, then style information is returned for the cell inside the nested table. The details of this method are given below.

| Method Name        | Parameter                                      | Return Value                                      |
|--------------------|------------------------------------------------|--------------------------------------------------|
| PointToTableCellStyle | `ptClient`: A type of `System.Drawing.Point` object that represents the mouse position in client coordinates. | A `GridTableCellStyleInfo` object that stores the style information of the underlying grid cell. |

### Implementation

The implementation of this method is a two-step process.

1. As a first step, it gets the corresponding nested display element that is displayed at the given mouse position. This can be performed easily by employing the `PointToNestedDisplayElement` method. This method is explained later in this chapter.
2.
```