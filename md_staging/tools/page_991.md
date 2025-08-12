```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_991.jpeg
document_name: tools
page_number: 991
page_id: tools#page_991
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:47:38Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- This section explains the properties and customization options for the 2D border in Windows Forms.
- Topics include `BorderColor`, `BorderSingle`, `BorderStyle`, and `HotBorderColor`.

### Properties and Descriptions

| Property       | Description                                                                                                                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Default Border | The default value is set to 'Sunken'.                                                                                                                                                                                                                                             |
| BorderColor    | Specifies the color of the 2D border.                                                                                                                                                                                                                                             |
| BorderSingle   | Indicates the 2D border style. The options included are as follows:<br/><br/>- Dotted,<br/>- Dashed,<br/>- Solid,<br/>- Inset,<br/>- Outset, and<br/>- None.<br/><br/>The BorderStyle property should be set to 'FixedSingle'.                               |
| BorderStyle    | Indicates whether the panel should have a border. The options included are given below.<br/><br/>- FixedSingle,<br/>- Fixed3D, and<br/>- None.                                                                                                                                           |
| HotBorderColor | Specifies the color of the FixedSingle border when MouseOver.                                                                                                                                                                                                                      |

### Code Examples

#### C#

```csharp
this.radioButtonAdv1.BorderColor = System.Drawing.Color.Fuchsia;
this.radioButtonAdv1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
this.radioButtonAdv1.BorderSingle = System.Windows.Forms.ButtonBorderStyle.Dotted;
this.radioButtonAdv1.Border3DStyle = System.Windows.Forms.Border3DStyle.RaisedInner;

// BorderStyle must be set to 'FixedSingle'.
this.radioButtonAdv1.HotBorderColor = System.Drawing.Color.DarkOrange;
```

#### VB.NET
```vb
' Code examples for VB.NET will be added here if available.
```

### API Reference

- **Namespace**: `System.Windows.Forms`
- **Class**: `RadioButtonAdv`
- **Properties**:
  - `BorderColor`: Specifies the color of the 2D border.
  - `BorderSingle`: Indicates the 2D border style.
  - `BorderStyle`: Indicates whether the panel should have a border.
  - `HotBorderColor`: Specifies the color of the FixedSingle border on MouseOver.

### Page-level Navigation/TOC (if applicable)
- This section currently does not include a local Table of Contents.

### Cross References
- See also: related pages or features within the WinForms documentation.

<!-- tags: [WinForms, Border Style, Border Color, Border3DStyle, Radio Button] keywords: [Windows Forms, Border properties, Border color, Border style, Dotted, Dashed, Solid, Inset, Outset, FixedSingle, Hot Border Color, RadioButtonAdv] -->
```
