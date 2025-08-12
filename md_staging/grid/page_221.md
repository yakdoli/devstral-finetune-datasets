```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_221.jpeg
document_name: grid
page_number: 221
page_id: grid#page_221
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:03:44Z
fidelity: lossless
-->


# Essential Grid for Windows Forms

```csharp
xhtml1 += "<p/>";
xhtml1 += "<p>XhtmlCells use the RichTextBoxSupportsXHTML control from GotDotNet user samples to display XHTML formatted text inside a cell.</p>";
xhtml1 += "</body>";
gridControl[rowIndex, 1].CellType = "XhtmlCell";
gridControl[rowIndex, 1].Text = xhtml1;
```

## Using VB.NET

```vb
Dim xhtml1 As String = "<body style=""font-family:Arial; line-height:1em""> "
xhtml1 += "<h1 style=""text-align:center; color:#EE7A03 "">XhtmlCells</h1>"
xhtml1 += "<p/>"
xhtml1 += "<p>XhtmlCells use the RichTextBoxSupportsXHTML control from GotDotNet user samples to display XHTML formatted text inside a cell.</p>"
xhtml1 += "</body>"
gridControl(rowIndex, 1).CellType = "XhtmlCell"
gridControl(rowIndex, 1).Text = xhtml1
```

![Grid Displaying XHTML Content](./image.png)

### Grid Displaying XHTML Content

The screenshot above demonstrates the Essential Grid control in a Windows Forms application displaying XHTML-formatted text in a cell. The `XhtmlCell` type allows the rendering of rich, styled text using XHTML.

## API Reference

### Methods
- `CellType`: Sets the type of a cell in the grid.
- `Text`: Sets the text content of a cell.

### Properties
- `RowIndex`: Specifies the row index of the cell.
- `CellType`: Defines the type of the cell (e.g., `XhtmlCell`).

## Code Examples

### C#
```csharp
string xhtmlContent = "<body style=\"font-family:Arial; line-height:1em\">" +
                      "<h1 style=\"text-align:center; color:#EE7A03\">XhtmlCells</h1>" +
                      "<p/>" +
                      "<p>XhtmlCells use the RichTextBoxSupportsXHTML control from GotDotNet user samples to display XHTML formatted text inside a cell.</p>" +
                      "</body>";

gridControl[rowIndex, 1].CellType = "XhtmlCell";
gridControl[rowIndex, 1].Text = xhtmlContent;
```

### VB.NET
```vb
Dim xhtmlContent As String = "<body style=""font-family:Arial; line-height:1em"">" &
                             "<h1 style=""text-align:center; color:#EE7A03"">XhtmlCells</h1>" &
                             "<p/>" &
                             "<p>XhtmlCells use the RichTextBoxSupportsXHTML control from GotDotNet user samples to display XHTML formatted text inside a cell.</p>" &
                             "</body>"

gridControl(rowIndex, 1).CellType = "XhtmlCell"
gridControl(rowIndex, 1).Text = xhtmlContent
```

## Cross References

- **RichTextBoxSupportsXHTML Control**: For more information on the RichTextBox control that supports XHTML formatting.
- **Essential Grid Documentation**: For comprehensive details on the Grid control and its various features.

<!-- tags: [WinForms, Essential Grid, XHTML, Cells, Formatting, RichTextBoxSupportsXHTML, Control] keywords: [xhtmlcells, gridcontrol, celltype, text, rowindex, rich text box, windows forms, gotdotnet, sample, text formatting, html, styled text, visual basic.net, csharp, code example] -->
```