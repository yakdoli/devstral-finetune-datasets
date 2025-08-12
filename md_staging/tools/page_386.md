```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_386.jpeg
document_name: tools
page_number: 386
page_id: tools#page_386
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:10:40Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Provides a detailed look into the Calculator control and its features.
- Focuses on the Display TextBox section of the Calculator control.
- Explains how to customize the behavior of the display area with properties like `DisplayTextAlign`, `Font`, and `DoubleValue`.

## Content

### 3.5.2.3.3 Concepts and Features
The following topics will help you become more familiar in using the Calculator control.

#### 3.5.2.3.3.1 Display TextBox
The Calculator control has a display text area on its top corner, which displays all the digits and the calculations performed on the calculator. This display area is displayed by default. To hide this display area, set the `ShowDisplayArea` property to false.

The below properties control the behavior of the display area.

| Calculatorcontrol Properties | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| `DisplayTextAlign`          | Specifies the text alignment in the display text area. The values are Right, Left, and Center. By default, it is set to Right. |
| `Font`                      | Sets font style for display text in the textbox control.                  |
| `DoubleValue`               | Sets the value of the Calculator control as double value. The default value is zero. |

[C#]

```csharp
this.calculatorControl1.DisplayTextAlign =
    System.Windows.Forms.HorizontalAlignment.Left;
this.calculatorControl1.DoubleValue = 5;
this.calculatorControl1.Font = new System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Bold);
```

[VB.NET]

```vb
Me.calculatorControl1.DisplayTextAlign = System.Windows.Forms.HorizontalAlignment.Left
Me.calculatorControl1.DoubleValue = 5
Me.calculatorControl1.Font = New System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Bold)
```

![Figure 192](https://example.com/fig192.png)  
*Figure 192: DisplayTextAlign = "Left"; DoubleValue = "5"; Font = "Verdana, 8, Bold"*

```html
<!-- tags: [Calculator control, Display TextBox, DisplayTextAlign, Font, DoubleValue, ShowDisplayArea] keywords: [Calculator control, display text area, alignment, font style, double value, text box, properties, customization] -->
```