<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_505.jpeg
document_name: chart
page_number: 505
page_id: chart#page_505
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:45:57Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Code Examples

#### Setting Default Title

**C#**
```csharp
// Default title
chartControl1.Title.Text = "Essential Chart";
this.chartControl1.Title.Font = new System.Drawing.Font("Candara", 9F, System.Drawing.FontStyle.Bold);
```

**VB.NET**
```vb.net
' Default title
chartControl1.Title.Text = "Essential Chart"
chartControl1.Title.Font = New System.Drawing.Font("Candara", 9F, System.Drawing.FontStyle.Bold)
```

### Figure 324: Chart Title Set

![Figure 324: Chart Title Set](https://example.com/image-url)  <!-- Image placeholder -->

The above default chart title is simply the first in the list of titles that can be specified for the Chart.

### Multiple Titles

- Multiple custom Chart Titles can be added to Chart.Titles Collection.
- Supports numerous docking styles (Floating, Left, Right, Bottom or Top) for each title.
- Each of the custom Titles can be aligned to any position as required.

### Titles Positioning

## API Reference

- **Namespace**: `System.Drawing`
- **Class**: `Font`
- **Members**:
  - **Font(string, float, FontStyle)**
    - **Parameters**:
      - `string`: Font name
      - `float`: Font size
      - `FontStyle`: Font style (e.g., Bold)
    - **Returns**: `Font` object
    - **Example**:
      ```csharp
      new System.Drawing.Font("Candara", 9F, System.Drawing.FontStyle.Bold);
      ```

### Cross References

- See also: "Chart Titles and Layout" for more details on docking and alignment options.

<!-- tags: [Essential Chart, Windows Forms, Chart.Titles, Font, Docking Styles, Alignment, Multiple Titles, C#, VB.NET] keywords: [chart, windows forms, titles, font, alignment, docking, multiple titles, default title, essential chart] -->