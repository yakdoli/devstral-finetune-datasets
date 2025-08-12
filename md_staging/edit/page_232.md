```html
<!--source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_232.jpeg
document_name: edit
page_number: 232
page_id: edit#page_232
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:07:23Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Users can configure headers and footers by handling the PrintHeader and PrintFooter events.
- Handles default text, such as the fully qualified path and page number, for headers and footers.

## Content

Users can also specify their desired text in the header and footer by handling the PrintHeader and PrintFooter events.

The default text in the header and footer is the fully qualified path of the file including the file name and page number respectively.

### Table: Edit Control Properties

| Edit Control Property | Description                            |
|-----------------------|----------------------------------------|
| PrintHeader          | Occurs when page header is printed.   |
| PrintFooter          | Occurs when page footer is printed.   |

### Code Examples

#### C#

```csharp
[C#]

private void editControl_PrintHeader(object sender, Syncfusion.Windows.Forms.Edit.PrintHeadlineEventArgs e)
{
    // Set the desired text in the header. The default text in the header is the full path and the name of the file.
    e.Text = "This is the header";
}

private void editControl_PrintFooter(object sender, Syncfusion.Windows.Forms.Edit.PrintHeadlineEventArgs e)
{
    // Set desired text in the footer. The default text in the footer is the page number.
    e.Text = "This is the footer";
}
```

#### VB.NET

```vb
[VB.NET]

Private Sub editControl_PrintHeader(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.PrintHeadlineEventArgs) Handles EditControl.PrintHeader
    ' Set the desired text in the header. The default text in the header is the full path and the name of the file.
    e.Text = "This is the header"
End Sub 'editControl_PrintHeader

Private Sub editControl_PrintFooter(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.PrintHeadlineEventArgs) Handles EditControl.PrintFooter
    ' Set desired text in the footer. The default text in the footer is the page number.
    e.Text = "This is the footer"
End Sub
```

## Cross References
- See also: PrintHeaderEvent, PrintFooterEvent, PrintHeadlineEventArgs.

<!-- tags: [Syncfusion Winforms, PrintHeader, PrintFooter, PrintHeadlineEventArgs] keywords: [headers, footers, text, file path, page number, default text, event handling, essential edit, windows forms] -->
```