```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_498.jpeg
document_name: grid
page_number: 498
page_id: grid#page_498
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:20:23Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

The print Page Layout feature helps to view the printing layout for the grid by displaying a segment line and a page number with each segment. This helps users to analyze page breaks within the grid and manage them accordingly. Colors for the line and text of the page layout can be defined with the properties available. Following code example illustrates this.

### 1. Using C#

```csharp
[C#]

LayoutSupportHelper layoutHelper;
layoutHelper = new LayoutSupportHelper(gridControl1);
layoutHelper.LineColor = Color.Blue;
layoutHelper.TextColor = Color.Green;
```

### 2. Using VB.NET

```vb
[VB.NET]

Dim layoutHelper As LayoutSupportHelper
layoutHelper = New LayoutSupportHelper(gridControl1)
layoutHelper.LineColor = Color.Blue
layoutHelper.TextColor = Color.Green
```

### Page Layout Visualization

Following screen shot shows the page layout of the grid, with the segment line and page number.

![Print Page Layout](https://example.com/image.png)

**Figure 192: Print Page**

### API Reference

#### Namespace: Syncfusion.Windows.Forms.Grid
- **Class**: LayoutSupportHelper
  - **Properties**
    - LineColor: Specifies the color of the segment line.
    - TextColor: Specifies the color of the page number text.

#### Methods
- **PrintPreview()**: Displays the print preview of the grid with the specified layout settings.

### Code Examples

#### C#

```csharp
[C#]

LayoutSupportHelper layoutHelper = new LayoutSupportHelper(gridControl1);
layoutHelper.LineColor = Color.Blue;
layoutHelper.TextColor = Color.Green;
layoutHelper.PrintPreview();
```

#### VB.NET

```vb
[VB.NET]

Dim layoutHelper As New LayoutSupportHelper(gridControl1)
layoutHelper.LineColor = Color.Blue
layoutHelper.TextColor = Color.Green
layoutHelper.PrintPreview()
```

### Cross References

See also: 
- GridPrinting
- LayoutSupportHelper
- PrintPreview

### Notes

- Ensure that the gridControl1 is properly initialized before using the LayoutSupportHelper.
- Customize the page layout colors to match your application's theme.
- Use the PrintPreview method to visualize the final printed output.

<!-- tags: [Syncfusion, Windows Forms, Grid, LayoutSupportHelper, PrintPreview, C#, VB.NET] keywords: [print page layout, segment line, page number, colors, grid printing, layout, preview] -->
```