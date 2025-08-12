```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_961.jpeg
document_name: grid
page_number: 961
page_id: grid#page_961
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:51:28Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

DrawHeader and DrawFooter are the events offered by the Grouping Grid Word Converter that aids in adding as well as customizing the header and footer in the destination word document.

## Sample Output

Below images depicts the conversion of grid content to a word file.

![Grid to be Exported](Figure 354.png)

*Figure 354: Grid to be Exported*

## API Reference

Namespace: Syncfusion.Windows.Forms.Grid

### Events
- **DrawHeader**: Event for customizing the header in the destination word document.
- **DrawFooter**: Event for customizing the footer in the destination word document.

## Code Examples

### C#

```csharp
// Example of handling DrawHeader event
void grid_DrawHeader(object sender, GridDrawHeaderEventArgs e)
{
    using (SolidBrush brush = new SolidBrush(Color.Red))
    {
        e.Graphics.FillRectangle(brush, e.HeaderCell.DisplayRect);
    }
}
```

### VB.NET

```vb
' Example of handling DrawHeader event
Private Sub grid_DrawHeader(ByVal sender As Object, ByVal e As GridDrawHeaderEventArgs)
    Using brush As New SolidBrush(Color.Red)
        e.Graphics.FillRectangle(brush, e.HeaderCell.DisplayRect)
    End Using
End Sub
```

## RAG Annotations

<!-- tags: grid, windows forms, drawheader, drawfooter, word converter, essential grid, syncfusion winforms, version: 11.4.0.26 -->
<!-- keywords: header customization, footer customization, grid content, word document, events, griddrawheader, griddrawfooter -->
```