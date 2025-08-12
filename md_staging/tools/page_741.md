```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_741.jpeg
document_name: tools
page_number: 741
page_id: tools#page_741
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:30:53Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
this.integerTextBox1.NegativeSign = "-";
```

```vb.net
[VB.NET]

Me.integerTextBox1.NumberGroupSeparator = "/"
Me.integerTextBox1.NumberGroupSizes = New Integer() {5}
Me.integerTextBox1.NumberNegativePattern = 2
Me.integerTextBox1.NegativeSign = "-"
```

![Display Settings of IntegerTextBox](https://via.placeholder.com/200x100?text=Figure%20467:%20Display%20Settings%20of%20IntegerTextBox)

## Overview

A Sample which demonstrates the Display Settings of IntegerTextBox control is available in the below sample installation path.

## Content

### Value Settings

- **.My Documents\Syncfusion\EssentialStudio\Version NumberWindows\Tools.Windows\Samples\2.0\Editors Package\EditorControls**

The various values of the IntegerTextBox control and their settings are given below.

| **IntegerTextBox Properties**  | **Description**                                                                 |
|--------------------------------|--------------------------------------------------------------------------------|
| IntegerValue                   | Specifies the integer value of the text.                                    |
| DefaultValue                   | Specifies the default value. The default value is set to 'Null'.              |
| BindableValue                  | Wrapper property that indicates the value. This property can be used to set the value of the control to 'Null'. |

### WinForms-specific conventions

```csharp
[C#]

this.integerTextBox1.IntegerValue = ((long)(777));
this.integerTextBox1.DefaultValue = 0;
this.integerTextBox1.BindableValue = 777;
```

```vb.net
[VB.NET]

[VB.NET]
```

## Page-level Navigation/TOC (if applicable)

None specified in the provided content.

### Cross References

See also: Essential Tools for Windows Forms, IntegerTextBox controls.

## RAG Annotations

<!-- tags: [Syncfusion Winforms, IntegerTextBox, control settings, VALUE, Version NumberWindows] keywords: [IntegerTextBox, Display Settings, DefaultValue, BindableValue, NegativeSign, NumberGroupSeparator, NumberGroupSizes, NumberNegativePattern] -->
```