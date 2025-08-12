```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_931.jpeg
document_name: tools
page_number: 931
page_id: tools#page_931
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:44:07Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section discusses the events related to changes in the selected index of a ComboBox and how to add custom events in derived classes.

## Content

### 3.5.9.2.4 Events

This section comprises the below events:

#### 3.5.9.2.4.1 SelectedIndexChanged Event

- SelectedIndexChanged event - This event is raised when the `ComboBox.SelectedIndex` property is changed.

The below code snippet lets you set the selected font style for a label on selecting through a FontComboBox, using the `SelectedIndexChanged` event.

```csharp
[C#]

private void fontComboBox2_SelectedIndexChanged(object sender, 
EventArgs e)
{
    this.label1.Font = new
    Font(this.fontComboBox2.SelectedItem.ToString(), 11, 
    FontStyle.Regular);
}
```

```vb.net
[VB.NET]

Private Sub fontComboBox2_SelectedIndexChanged(ByVal sender As Object, 
ByVal e As EventArgs)
    Me.label1.Font = New Font(Me.fontComboBox2.SelectedItem.ToString(), 
    11, FontStyle.Regular)
End Sub
```

#### 3.5.9.2.4.2 FontSelected Event

To add a `FontSelected` event, derive the classes as shown below.

1. Add an event in the derived class.

```csharp
[C#]

// Adding event.
public event System.EventHandler FontSelected;
```

```vb.net
[VB.NET]

```

## API Reference
- `private void fontComboBox2_SelectedIndexChanged(object sender, EventArgs e)`: This method handles the `SelectedIndexChanged` event of the `fontComboBox2` control.
- `Me.label1.Font = New Font(Me.fontComboBox2.SelectedItem.ToString(), 11, FontStyle.Regular)`: This line sets the font style of the `label1` control based on the selected item in the `fontComboBox2`.

## Code Examples
- The provided C# and VB.NET code snippets demonstrate how to respond to the `SelectedIndexChanged` event and set a label's font style based on the selected item in a FontComboBox.

<!-- tags: [WinForms, ComboBox, SelectedIndexChanged, FontSelected, Events] keywords: [ComboBox, SelectedIndexChanged, FontSelected, Events, Label, FontStyle] -->
```