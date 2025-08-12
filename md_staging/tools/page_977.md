```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_977.jpeg
document_name: tools
page_number: 977
page_id: tools#page_977
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:45:53Z
fidelity: lossless
-->

Essential Tools for Windows Forms

## Databinding a CheckBoxAdv to an SQL Database

### Overview
- Demonstrates how to bind a CheckBoxAdv control to an SQL database when the corresponding Datatable Field is Boolean.
- Includes implementation using VB.NET code.
- Highlights the use of the `BoolValue` property for databinding.

### Content

#### CheckBoxAdv Databinding Example

```vb
Private Sub Form1_Load(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.oleDbDataAdapter1.Fill(Me.dataSet1.Table1)
End Sub

' Using CheckBoxAdv's BoolValue property for Databinding.
Me.checkBoxAdv1.DataBindings.Add("BoolValue", Me.dataSet1.Table1, "CheckValue")
```

**Figure 630: Databinding a CheckBoxAdv to an SQL Database if the corresponding Datatable Field is Boolean**

![Figure 630](image.png)

#### RadioButtonAdv

**Subsection: RadioButtonAdv**
- **RadioButtonAdv** functions similar to the Windows standard RadioButton but includes additional enhancements.
- Provides an improved look and feel to the RadioButtons.
- Supports themes, gradient colors, images, and shadow text.

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Class**: RadioButtonAdv
- **Properties**: 
  - Themes
  - Gradient colors
  - Support for images
  - Shadow text

### Code Examples

#### Example: Visual Basic .NET
```vb
' Example code to demonstrate the usage of RadioButtonAdv with enhanced features.
' Implementation details for themes, images, and shadow text.
```

#### Example: C#
```csharp
// Example code to demonstrate the usage of RadioButtonAdv with enhanced features.
// Implementation details for themes, images, and shadow text.
```

## Cross References
- See also: Documentation on advanced theming and customization for WinForms controls.

<!-- tags: Syncfusion WinForms, CheckBoxAdv, DataBinding, RadioButtonAdv, Databinding, Themes, Images, ShadowText, version 11.4.0.26 -->
```