```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_470.jpeg
document_name: grid
page_number: 470
page_id: grid#page_470
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:18:30Z
fidelity: lossless
-->

### Grid for Windows Forms

```csharp
// Total of three column header rows.
this.gridControl1.Rows.HeaderCount = 2;
```

```vb.net
' Total of three column header rows.
Me.GridControl1.Cols.Rows.HeaderCount = 2
```

![Grid With Three Column Header Rows](media/image1.png "Figure 180: Grid With Three Column Header Rows")

### 4.1.4.14.3 Frozen Rows and Columns

A frozen row is one that cannot be scrolled. For example, the default column header (row 0) is a frozen row. Frozen rows will always be displayed at the top of the grid. You can set the number of frozen rows using the `GridControl.Rows.FrozenCount` property. In our previous code sample, we used the `Rows.HeaderCount` property to set up two additional column header rows. To cause the new headers to be fixed and not to scroll, you need to set the `Rows.FrozenCount` to two. Note that you can freeze non-header type rows as well, but, in the following code samples, we are freezing headers only.

```csharp
// Have 3 non-scrollable rows at the top.
this.gridControl1.Rows.FrozenCount = 2;
```

### Summary
- Configure the number of frozen rows using the `Rows.FrozenCount` property.
- Ensure that frozen rows remain fixed at the top of the grid.
- Utilize `Rows.HeaderCount` to set multiple column header rows.
- Freezing rows prevents them from scrolling out of view.
- Example code provided for setting both frozen rows and header rows in C#.

### API Reference
- **Property**: `Rows.HeaderCount`
- **Property**: `Rows.FrozenCount`
- **Class**: `GridControl`

### Code Examples
- **C#**:
  ```csharp
  // Configure grid to have two frozen header rows.
  this.gridControl1.Rows.HeaderCount = 2;
  this.gridControl1.Rows.FrozenCount = 2;
  ```
  
- **VB.NET**:
  ```vb.net
  ' Configure grid to have two frozen header rows.
  Me.GridControl1.Cols.Rows.HeaderCount = 2
  Me.GridControl1.Rows.FrozenCount = 2
  ```

```html
<!-- tags: Essential Grid, Grid, Windows Forms, Syncfusion, GridControl, Header Rows, Frozen Rows, API Reference, Code Examples, Version: 11.4.0.26 -->
``` 
```