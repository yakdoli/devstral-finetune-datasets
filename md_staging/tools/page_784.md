```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_784.jpeg
document_name: tools
page_number: 784
page_id: tools#page_784
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:23Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview

- Directory path for samples: `..My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0\Editors Package\EditorControls`
- Description of the `PercentTextBox` control's behavior settings, focusing on the `NegativeInputPendingOnSelectAll` property.

### Behavior Settings: The Behavior settings of the PercentTextBox control are discussed below.

#### NegativeInputPendingOnSelectAll

The percent value of the `PercentTextBox` can be changed to a negative value using the properties given below.

| PercentTextBox Property                | Description                                                                 |
|----------------------------------------|---------------------------------------------------------------------------|
| NegativeInputPendingOnSelectAll        | This property defines the behavior when the contents of the `IntegerTextBox` is fully selected and the negative key is pressed by the user. <br> <br> When set to 'True', the current value is not changed at all. The next key stroke is taken to be a new value and the entire contents of the `PercentTextBox` is replaced by the negative value of the key stroke character entered. <br> <br> When set to 'False', the current value is changed to the negative value immediately. |

### Code Examples

- **C#**
  ```csharp
  this.percentTextBox1.NegativeInputPendingOnSelectAll = true;
  ```

- **VB.NET**
  ```vb
  Me.percentTextBox1.NegativeInputPendingOnSelectAll = True
  ```

### Border Settings

Color and Styles can be applied to the Border of the `PercentTextBox` control as discussed below.

### API Reference

- `NegativeInputPendingOnSelectAll`: Property that controls behavior when a negative key is pressed with all content selected in the `PercentTextBox`.

## Page-level Navigation/TOC (if applicable)

### Content
- `NegativeInputPendingOnSelectAll` property description
- Code examples in C# and VB.NET
- Border settings discussion

### Related Sections
- Behavior settings of the `PercentTextBox` control

### Cross References
- Related controls or properties in the toolbox
- Documentation on other editor controls in the package

<!-- tags: [ Phần mềm, Syncfusion, WinForms, PercentTextBox, NegativeInputPendingOnSelectAll, Border Settings, C#, VB.NET, API Reference, Code Examples] keywords: [Behavior settings, NegativeInputPendingOnSelectAll, PercentTextBox, Border Styles, Control properties, Change negative value, Code examples, C#, VB.NET] -->
```