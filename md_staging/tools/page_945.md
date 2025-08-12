```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_945.jpeg
document_name: tools
page_number: 945
page_id: tools#page_945
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Implements a GradientLabel control.
- Demonstrates adding the GradientLabel to a Form.
- Discusses border settings for the GradientLabel.

## Content

### Adding the GradientLabel Control

```csharp
// Add the GradientLabel control to the Form.
this.Controls.Add(this.gradientLabel);
```

```vb.net
[VB.NET]

Me.gradientLabel.BorderStyle = 
System.Windows.Forms.Border3DStyle.Sunken
Me.gradientLabel.ForeColor = System.Drawing.SystemColors.Info
Me.gradientLabel.Text = "Syncfusion Control"

' Add the GradientLabel control to the Form.
Me.Controls.Add(Me.gradientLabel)
```

- **Run the application.**

![GradientLabel created Through Code](image.png)

**Figure 607: GradientLabel created Through Code**

#### 3.5.10.2.3 Concepts and Features

The following topics will help you become more familiar in using the GradientLabel control.

##### 3.5.10.2.3.1 Border Settings

This section discusses the border settings of the GradientLabel control.

**The border style and sides of the GradientLabel can be customized using the properties given below.**

| GradientLabel Properties | Description |
|--------------------------|-------------|
| BorderSides             | Specifies the sides of the GradientLabel that will have a border. |

---

## API Reference

No API references are specified in this section.

## Code Examples

No additional code examples are provided in this section.

### Cross References

- Refer to the official Syncfusion documentation for more details on the GradientLabel control.
- See also: Border styles, Customization, Windows Forms.

<!-- tags: [Syncfusion, WinForms, GradientLabel, Border Settings] keywords: [GradientLabel, BorderSides, Windows Forms, Customization, Border Styles] -->
```