```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_231.jpeg
document_name: grid
page_number: 231
page_id: grid#page_231
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:04:17Z
fidelity: lossless
-->

## Current Cell

Essential Grid supports MS-Excel like **Current Cell** feature. This feature can be enabled by setting **ExcelLikeCurrentCell** property to `true`. When the user moves the current cell out of a selected range, the range will be cleared. If the user moves the current cell inside a selected range, the range will stay.

Current Cell feature can be enabled for Essential Grid by using the following code:

### Using C#

```csharp
this.gridControl1.ExcelLikeCurrentCell = true;
```

### Using VB.NET

```vb
Me.gridControl1.ExcelLikeCurrentCell = True
```

![Current Cell](./figure125.png)

**Figure 125: Current Cell**

### Summary

- The current cell feature mimics Excel-like functionality.
- It can be enabled by setting the `ExcelLikeCurrentCell` property to `true`.
- The range behavior is affected based on whether the current cell is within or outside the selected range.
- Code examples in C# and VB.NET are provided to enable this feature.

## Notes

## See also

<!-- tags: [current cell, Essential Grid, Windows Forms, Excel-like features, grid, Syncfusion, Winforms] keywords: [current cell, ExcelLikeCurrentCell, range behavior, C#, VB.NET, user interaction, Windows Forms, grid controls] -->
```