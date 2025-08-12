```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_844.jpeg
document_name: grid
page_number: 844
page_id: grid#page_844
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:44:19Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Code Examples

#### C#

```csharp
var pager = new Pager { PageSize = 1000 };
pager.Wire(gridGroupingControl); // Data sources assigned to the pager from gridGroupingControl
```

#### VB

```vb
Dim pager = New Pager With {PageSize = 1000}
pager.Wire(gridGroupingControl) 'Data sources assigned to the pager from gridGroupingControl
```

### Appearance

**4.3.4.5 Appearance**

This property allows you to control the appearance of the grouping grid at design time as well as at run time. You can change the overall appearance of the grid and also the appearance of each element in the grid by setting this property.

**Appearance** contains a list of `GridStyleInfo` properties as seen in the following graphic. A `GridStyleInfo` object contains many properties such as `BackColor`, `Font`, and `CellType`, which defines the look and behavior of a grid cell. Each of these properties identifies a particular set of cells that make up a Grid Grouping control.

## API Reference (if applicable)

- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridStyleInfo

### Properties

- **BackColor**: Defines the background color of the grid cell.
- **Font**: Specifies the font used for text rendering in the grid cell.
- **CellType**: Determines the type of content (e.g., text, numeric, etc.) that a grid cell can hold.

## Page-level Navigation/TOC (if applicable)

- 4.3.4.5 Appearance

## Cross References

See also:
- GridStyleInfo
- Grid Grouping Control

<!-- tags: [syncfusion, winforms, grid, gridstyleinfo, appearance, paging, syncfusion-windowsforms, 11.4.0.26] keywords: [gridstyleinfo, appearance, pager, gridgroupingcontrol, backcolor, font, celltype] -->
```