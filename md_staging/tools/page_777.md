```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_777.jpeg
document_name: tools
page_number: 777
page_id: tools#page_777
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:33:10Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Demonstrates configuring the **ScrollBars** property for a textbox control.
- Code examples in C# and VB.NET for enabling multiline text, word wrap, and vertical scrollBars.
- Displays the functionality of **WordWrap** properties with examples.

## Content

### Configuring ScrollBars Property

The **ScrollBars** property can be set to the following options:

None,  
Horizontal,  
Vertical and  
Both.

```csharp
[C#]

this.percentTextBox1.Multiline = true;
this.percentTextBox1.WordWrap = true;
this.percentTextBox1.ScrollBars = 
System.Windows.Forms.ScrollBars.Vertical;
```

```vb
[VB.NET]

Me.percentTextBox1.Multiline = True
Me.percentTextBox1.WordWrap = True
Me.percentTextBox1.ScrollBars = 
System.Windows.Forms.ScrollBars.Vertical
```

#### PercentTextBox Control

The `PercentTextBox` control is a textbox-derived control that can display double data type values in percentage form.

```plaintext
PercentTextBox
control is a
textbox-derived
control that can
display double data
type values in
percentage form.
```

#### Multiline Text

The figure below illustrates the use of multiline text with the **WordWrap** property.

![Figure 492: Multiline Text](image-url-for-figure-492)

#### WordWrap Property Set

The figure below shows the effect of setting the **WordWrap** property to `False` and `True`.

![Figure 493: WordWrap property Set](image-url-for-figure-493)

## API Reference

### Members

- **Multiline**: Determines whether multiple lines of text can be entered and displayed.
- **WordWrap**: Indicates whether the text is wrapped automatically at the edges of the control.
- **ScrollBars**: Defines whether to display vertical or horizontal scrollbars for the textbox.

## Code Examples

### C# Example

```csharp
this.percentTextBox1.Multiline = true;
this.percentTextBox1.WordWrap = true;
this.percentTextBox1.ScrollBars = 
System.Windows.Forms.ScrollBars.Vertical;
```

### VB.NET Example

```vb
Me.percentTextBox1.Multiline = True
Me.percentTextBox1.WordWrap = True
Me.percentTextBox1.ScrollBars = 
System.Windows.Forms.ScrollBars.Vertical
```

### Visual Representation

The following image demonstrates the `PercentTextBox` control with scrollbars.

![PercentTextBox with Scrollbars](image-url-for-scrollbars)

### WordWrap Property Examples

The figure below showsPercentTextBox controls with `WordWrap` set to `False` and `True`.

#### PercentTextBox with WordWrap = "False"

```plaintext
PercentTextBox control
WordWrap = "False"
```

#### PercentTextBox with WordWrap = "True"

```plaintext
PercentTextBox control
WordWrap = "True"
```

## Page-level Navigation/TOC (if applicable)

- [Configuring ScrollBars Property](#scrollbars-property)
- [PercentTextBox Control](#percenttextbox-control)
- [Multiline Text](#multiline-text)
- [WordWrap Property Set](#wordwrap-property)

## Cross References

- See also: [TextBox Control](#textbox-control), [Syncfusion WinForms](#syncfusion-winforms)

<!-- tags: [Syncfusion Winforms, TextBox, PercentTextBox, ScrollBars, WordWrap] keywords: [Multiline, VerticalScrollBars, Textbox control, Wordwrap, Percent textbox] -->
```
