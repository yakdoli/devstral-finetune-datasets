```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_909.jpeg
document_name: grid
page_number: 909
page_id: grid#page_909
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:48:00Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### Handling the `FieldChooserClosing` Event

#### C#

```csharp
FieldChooserClosingEventArgs e)
{
    e.Caption = "Syncfusion Inc";
    e.Cancel = true;
}
```

#### VB.NET

```vbnet
Private Sub GroupingControl_FieldChooserClosing(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Grid.FieldChooserClosingEventArgs)
    e.Caption = "Syncfusion Inc"
    e.Cancel = True
End Sub
```

#### Description
The following code example illustrates handling the `FieldChooserClosed` event. Here it is used to get the caption name of the `FieldChooser` dialog after closing it.

### Handling the `FieldChooserClosed` Event

#### C#

```csharp
// FieldChooserClosed Event
void gridGroupingControl_FieldChooserClosed(object sender, FieldChooserClosedEventArgs e)
{
    string caption = e.Caption;
    Console.WriteLine(caption);
}
```

#### VB.NET

```vbnet
' FieldChooserClosed Event
Private Sub GroupingControl_FieldChooserClosed(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Grid.FieldChooserClosedEventArgs)
    Dim captionName As String = e.Caption.ToString()
    Console.WriteLine(captionName)
End Sub
```

### 4.3.4.6.4 Field Chooser for Stacked Header

## API Reference (if applicable)
- None explicitly mentioned in this section.

## Code Examples (multi-language supported)
- See the above examples in C# and VB.NET demonstrating event handling for `FieldChooserClosing` and `FieldChooserClosed`.

## Cross References
- Related sections or topics may involve working with dialog boxes or event handling in `Syncfusion.Windows.Forms.Grid`.

<!-- tags: [syncfusion, winforms, grid, fieldchooser, event, dialog] keywords: [fieldchooser, event, caption, closing, closed, syncfusion inc, dialog box, stackeheader] -->
```