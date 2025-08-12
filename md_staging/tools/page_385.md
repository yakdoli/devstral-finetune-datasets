```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_385.jpeg
document_name: tools
page_number: 385
page_id: tools#page_385
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:09:00Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section demonstrates how to create and add a Calculator control to a Windows Forms application using Syncfusion's tools library.
- Covers the instantiation and addition of the CalculatorControl to the form with code examples in both C# and VB.NET.

## Content

### Creating and Adding the Calculator Control

#### 1. Instantiating the Calculator Control
To create an instance of the Calculator control, use the following code:

```vb
[VB.NET]
Private calculatorControl1 As Syncfusion.Windows.Forms.Tools.CalculatorControl
' Create an instance of the Calculator control
Me.calculatorControl1 = New CalculatorControl()
```

```csharp
[C#]
// Create an instance of the Calculator control
this.calculatorControl1 = new CalculatorControl();
```

#### 2. Adding the Calculator Control to the Form
As the final step, add the Calculator control to the form using the following code:

```csharp
[C#]
// Add the CalculatorControl control to the form.
this.Controls.Add(this.calculatorControl1);
this.calculatorControl1.Visible = true;
```

```vb
[VB.NET]
' Add the CalculatorControl control to the form.
Me.Controls.Add(Me.calculatorControl1)
Me.calculatorControl1.Visible = True
```

### Visual Representation of the Calculator Control

#### Figure 191: Calculator Control at Run Time
![](attachment:calculator-control.png)
*Figure 191: Calculator Control at Run Time*

## See Also
- [Concepts and Features](Concepts and Features)

## Page-level Navigation/TOC (if applicable)
- This page provides detailed steps and example code for incorporating the Calculator Control into a Windows Forms application.

### API Reference (if applicable)
- The examples in this section are direct uses of the `Syncfusion.Windows.Forms.Tools.CalculatorControl` API.

### Code Examples
```csharp
[C#]
this.Controls.Add(this.calculatorControl1);
this.calculatorControl1.Visible = true;
```

```vb
[VB.NET]
Me.Controls.Add(Me.calculatorControl1)
Me.calculatorControl1.Visible = True
```

## RAG Annotations
<!-- tags: [Syncfusion, Windows Forms, Calculator Control, Tools Library, C#, VB.NET] keywords: [CalculatorControl, Windows Forms, instantiation, adding controls, visible property] -->
```