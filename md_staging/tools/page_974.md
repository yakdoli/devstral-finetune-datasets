```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_974.jpeg
document_name: tools
page_number: 974
page_id: tools#page_974
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:46:17Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

A sample which demonstrates the Themes and Visual Styles of CheckBoxAdv is available in the below sample installation path.

## Overview
- Demonstrates the Themes and Visual Styles of CheckBoxAdv.
- Provides a detailed explanation about the CheckBoxAdv CheckStateChanged event.
- Explains the CheckedChanged event in relation to property changes.

## Content

### Installation Path
The sample demonstrating the Themes and Visual Styles of CheckBoxAdv is available at the following installation path:
- My Documents\\Syncfusion\\EssentialStudio\\Version\\
\\Number\\Windows\\Tools.Windows\\Samples\\2.0\\Editors Package\\OptionControls

### 3.5.11.1.4 CheckBoxAdv Events

A detailed explanation about the **CheckStateChanged** event is given in the following section.

| CheckBoxAdv Events       | Description                                                                      |
|--------------------------|----------------------------------------------------------------------------------|
| CheckStateChanged        | This event occurs when the CheckState property is changed.                    |
| CheckStateChanged        | This event is raised when the Checked property is changed.                   |

### 3.5.11.1.4.1 CheckStateChanged Event

This event occurs when the CheckState property is changed.

The event handler receives an argument of type **EventArgs** containing data related to this event.

#### Example: C# Code

```csharp
private void checkBoxAdv1_CheckStateChanged(object sender, EventArgs e)
{
    Console.WriteLine(" CheckStateChanged event is raised");
}
```

#### Example: VB.NET Code

```vb
Private Sub checkBoxAdv1_CheckStateChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" CheckStateChanged event is raised")
End Sub
```

### 3.5.11.1.4.2 CheckedChanged Event

This event is raised when the Checked property is changed. The Checked property changes automatically when the CheckState property is changed.

## API Reference

### Events
- **CheckStateChanged**: Triggered when the CheckState property changes.
- **CheckedChanged**: Triggered when the Checked property is changed.

## Code Examples

#### Sample Code (C#)
```csharp
private void checkBoxAdv1_CheckStateChanged(object sender, EventArgs e)
{
    Console.WriteLine(" CheckStateChanged event is raised");
}
```

#### Sample Code (VB.NET)
```vb
Private Sub checkBoxAdv1_CheckStateChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" CheckStateChanged event is raised")
End Sub
```

<!-- tags: [syncfusion-sdk, checkboxes, checkstatechanged, checkedchanged, winforms] -->
```