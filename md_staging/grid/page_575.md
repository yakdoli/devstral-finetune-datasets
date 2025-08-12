```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_575.jpeg
document_name: grid
page_number: 575
page_id: grid#page_575
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:25:30Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Expand Grid Demonstration

![Figure 225: Expand Grid](https://images描绘Expand Grid的界面截图)

**Description:**  
A sample demonstrating the "Expand Grid" feature is available under the following sample installation path:

`\Install Location\Syncfusion\EssentialStudio\Version Number\Windows\Grid.Windows\Samples\2.0\Data Bound\Hierarchy\Expand Grid Demo`

### Hierarchical Grid with Tree Lines

#### Overview
- Demonstrates the functionality of displaying hierarchical grid data with tree lines.
- Highlighted the use of the `ShowTreeLines` property to enable tree lines in a Grid Data Bound Grid.

#### Hierarchical Grid with Tree Lines

**Content:**

Grid Data Bound Grid supports the display of hierarchical grid data with tree lines. This can be achieved by setting the `ShowTreeLines` property to `true`.

**Code Examples:**

- **C#**
  ```csharp
  this.gridDataBoundGrid1.ShowTreeLines = true;
  ```

- **VB.NET**
  ```vb
  Me.gridDataBoundGrid1.ShowTreeLines = True
  ```

#### Notes:
- The `ShowTreeLines` property is a boolean value that, when set to `true`, enables the display of tree lines in a hierarchical grid structure.

### API Reference

- **Namespace:** Syncfusion.Windows.Forms.Grid
- **Class:** GridDataBoundGrid
- **Property:** `ShowTreeLines`
  - **Type:** `bool`
  - **Description:** Enables or disables the display of tree lines in a hierarchical grid.
  - **Default:** `false`
  - **Required:** No

### Code Examples Recap

```csharp
// C#
this.gridDataBoundGrid1.ShowTreeLines = true;
```

```vb
' VB.NET
Me.gridDataBoundGrid1.ShowTreeLines = True
```

### Cross References
- See also: Hierarchical Grid Data Binding, Tree Line Display Properties.

<!-- tags: [product, module, control, api, version?] keywords: [hierarchical grid, tree lines, grid databound grid, showtreelines, expand grid, windows forms, syncfusion, version 11.4.0.26] -->
```