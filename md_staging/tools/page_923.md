```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_923.jpeg
document_name: tools
page_number: 923
page_id: tools#page_923
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:44Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Events

### 3.5.9.1.5 Events

**SelectedIndexChanged event** - This event is raised when the `ListBox.SelectedIndex` property is changed.

The below code snippet lets you set the selected font style for a label on selecting through a FontListBox using the SelectedIndexChanged event.

#### [C#]

```csharp
private void fontListBox1_SelectedIndexChanged(object sender, EventArgs e)
{
    this.label1.Font = new Font(this.fontListBox1.SelectedItem.ToString(), 11, FontStyle.Regular);
}
```

#### [VB.NET]

```vbnet
Private Sub fontListBox1_SelectedIndexChanged(ByVal sender As Object, ByVal e As EventArgs)
    Me.label1.Font = New Font(Me.fontListBox1.SelectedItem.ToString(), 11, FontStyle.Regular)
End Sub
```

## FontComboBox

### 3.5.9.2 FontComboBox

The FontComboBox is a combo box-derived control that is automatically populated with the fonts installed on the user's system. It provides an easy way to fill a combo box with system fonts.

<!-- tags: [
Syncfusion Winforms,
FontComboBox,
SelectedIndexChangedEvent,
FontProperty,
Windows Forms
] keywords: [
selectedindexchanged,
fontlistbox,
fontstyle,
fontsize,
combobox,
systemfonts,
windowsforms,
syncfusionwinforms,
tools,
event handling,
user interface,
controls,
development
] -->
```