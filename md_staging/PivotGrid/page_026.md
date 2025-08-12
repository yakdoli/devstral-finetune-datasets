```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_026.jpeg
document_name: PivotGrid
page_number: 026
page_id: PivotGrid#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:10Z
fidelity: lossless
-->

## Freezing Headers

The PivotGrid for Windows Forms provides built-in support for freezing column and row headers. This is achieved by setting the `FreezeHeaders` property of `PivotGrid` to `True`. This feature also enables scrolling through the value cells.

### Code Examples

#### C# Code

```csharp
// To Freeze Grid Headers
this.PivotGridControl1.FreezeHeaders = true;
```

#### VB Code

```vb
' To Freeze Grid Headers
Me.PivotGridControl1.FreezeHeaders = True
```

### Figure: PivotGrid with Frozen Headers
![PivotGrid with Frozen Headers](https://via.placeholder.com/800x400)

## Grouping Bar

The PivotGrid Grouping Bar enables the drag-and-drop feature of fields between different areas such as column, row, value, and filter. By using the Grouping Bar, you can add, rearrange, or remove fields to show data in the PivotGrid exactly the way you want.

### Description of Grouping Bar

The Grouping Bar has field headers that identify fields in the pivot grid. One field header contains:

- **Caption string** - Identifies the field's content
- **Sort indicator** - Identifies the sort order applied to the field's values

---

### Summary

- The PivotGrid provides built-in support for freezing headers, which helps when scrolling through the value cells.
- The Grouping Bar enables flexible manipulation of fields in the PivotGrid for precise data display.

### Copyright

© 2013 Syncfusion. All rights reserved.
```