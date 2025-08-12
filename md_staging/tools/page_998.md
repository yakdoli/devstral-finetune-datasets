```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_998.jpeg
document_name: tools
page_number: 998
page_id: tools#page_998
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:47:33Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

**Figure 647: RadioButton displayed in "Red"**

A sample which demonstrates the Themes and Visual Styles of `RadioButtonAdv` is available in the below sample installation path.

```
..My Documents\Syncfusion\EssentialStudio\Version
Number\Windows\Tools.Windows\Samples\2.0\Editors Package\OptionControls
```

## 3.5.11.2.4 `RadioButtonAdv Events`

The list of events and a detailed explanation about each of them is given in the following sections.

| **`RadioButtonAdv` Events** | **Description** |
|-----------------------------|-----------------|
| `CheckChanged`             | This event is fired when the `Checked` property of the `RadioButtonAdv` changes. |
| `GroupCheckChanged`        | This event is fired when the `Checked` property of the `RadioButtonAdv` in the group changes. |

### 3.5.11.2.4.1 `CheckChanged Event`

This event is fired when the `Checked` property of the `RadioButtonAdv` changes.

The event handler receives an argument of type `EventArgs` containing data related to this event.

#### C#
```csharp
private void radioButtonAdv1_CheckedChanged(object sender, EventArgs e)
{
    Console.WriteLine("CheckChanged event is raised");
}
```

#### VB.NET
```vb
Private Sub radioButtonAdv1_CheckedChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("CheckChanged event is raised")
End Sub
```

## API Reference (if applicable)
- **Namespace:** `Syncfusion.Windows.Forms.Tools`
- **Class:** `RadioButtonAdv`
- **Events:**
  - `CheckChanged`: Triggered when the `Checked` property changes.
  - `GroupCheckChanged`: Triggered when the `Checked` property of the group changes.

## Code Examples (multi-language supported)
- C#
```csharp
private void radioButtonAdv1_CheckedChanged(object sender, EventArgs e)
{
    Console.WriteLine("CheckChanged event is raised");
}
```
- VB.NET
```vb
Private Sub radioButtonAdv1_CheckedChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("CheckChanged event is raised")
End Sub
```

## Page-level Navigation/TOC (if applicable)
- 3.5.11.2.4 `RadioButtonAdv Events`
  - 3.5.11.2.4.1 `CheckChanged Event`

## Cross References
- See also:
  - `RadioButtonAdv` control documentation
  - `Checked` property details
  - Event handling in Windows Forms

<!-- tags: [RadioButtonAdv, Windows Forms, Events, CheckChanged, GroupCheckChanged] keywords: [RadioButtonAdv, CheckChanged, GroupCheckChanged, event, checked property, Windows Forms, C#, VB.NET] -->
```