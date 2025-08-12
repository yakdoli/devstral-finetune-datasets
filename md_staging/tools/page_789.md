```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_789.jpeg
document_name: tools
page_number: 789
page_id: tools#page_789
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:01Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section explains how to use the PercentTextBox control and its properties.
- Implements functionality to increment and decrement the PercentTextBox value using keyboard arrows.
- Describes the `ThemesEnabled` property and its application to the PercentTextBox control.

## Content

### PercentTextBox Event Handling

The following code snippet demonstrates how to handle the `KeyDown` event for the `PercentTextBox` control, allowing users to increment or decrement its value using the up and down arrow keys.

```vb
Private Sub percentTextBox1_KeyDown(ByVal sender As Object, ByVal e As KeyEventArgs)
    ' Increments the PercentTextBoxValue.
    Dim v As Double = percentTextBox1.PercentValue
    Select e.KeyCode
        Case Keys.Up
            v = v + 1
        Case Keys.Down
            v = v - 1
    End Select
    percentTextBox1.PercentValue = v
End Sub
```

### Applying Themes to PercentTextBox

#### ThemesThemes

ThemesThemes can be applied to the PercentTextBox control using the following property.

| PercentTextBox Property | Description |
|--------------------------|-------------|
| ThemesEnabled           | Specifies whether or not to use XP themes when `BorderStyle` property is set to `'Fixed3D'`. |

**Note:** Refer to the **Border Settings** topic to know about the `BorderStyle` property.

#### Enabling Themes

In C#:
```csharp
this.percentTextBox1.ThemesEnabled = true;
```

In VB.NET:
```vb
Me.percentTextBox1.ThemesEnabled = True
```

#### Example Image

![Themes Applied to PercentTextBox Control](image_path)

**Figure 502: Themes Applied to PercentTextBox Control**

### Sample Availability

A sample demonstrating the `ThemesEnabled` property of the PercentTextBox control is available in the following sample installation path:

```
..My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0\Editors Package\EditorControls
```

## Page-level Navigation/TOC (if applicable)
- [Applying Themes to PercentTextBox]
- [PercentTextBox Event Handling]

## Cross References
- See also: [Border Settings]

<!-- tags: [syncfusion, winforms, percenttextbox, themesenabled, event handling, windows forms] keywords: [themes, up arrow, down arrow, percentvalue, borderstyle, fixed3d, sample path, code examples] -->
```