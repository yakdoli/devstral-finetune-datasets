```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_399.jpeg
document_name: tools
page_number: 399
page_id: tools#page_399
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:11:01Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates configuring button style for a calculator control in Windows Forms.
- Shows how to apply the Office 2007 button style to a Syncfusion calculator control.
- Includes C# and VB.NET code examples for setting the button style.

## Content

### Configuring Button Style for the Calculator Control

To apply the Office 2007 button style to a Syncfusion calculator control, you can use the following code examples:

#### C#
```csharp
this.calculatorControl1.UseVisualStyle = true;
// Setting Office2007 button style for the calculator control
this.calculatorControl1.ButtonStyle = Syncfusion.Windows.Forms.ButtonAppearance.Office2007;
```

#### VB.NET
```vb.net
Me.calculatorControl1.UseVisualStyle = True
' Setting Office2007 button style for the calculator control
this.calculatorControl1.ButtonStyle = Syncfusion.Windows.Forms.ButtonAppearance.Office2007;
```

This code snippet sets the `UseVisualStyle` property to `true` for visual style support and then configures the `ButtonStyle` property to emulate the Office 2007 button appearance.

## Pagination Information
© 2013 Syncfusion. All rights reserved. Page 399

<!-- tags: [syncfusion winforms, windows forms, button style, calculator control, office 2007] keywords: [calculator control, ButtonAppearance, Office2007, Windows Forms, C#, VB.NET] -->
```