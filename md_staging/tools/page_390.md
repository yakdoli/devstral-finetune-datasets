```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_390.jpeg
document_name: tools
page_number: 390
page_id: tools#page_390
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:10:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to set the background image and layout for a Calculator control using C# and VB.NET.
- Explains the concept of border styles for the Calculator control and their available options.

## Content

### Setting Background Image and Layout
#### Code Examples

**C#**
```csharp
this.calculatorControl1.BackgroundImage =
    (System.Drawing.Image)(resources.GetObject("calculatorControl1.BackgroundImage"));
this.calculatorControl1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center;
```

**VB.NET**
```vb.net
Me.calculatorControl1.BackgroundImage =
    DirectCast((resources.GetObject("calculatorControl1.BackgroundImage")), System.Drawing.Image)
Me.calculatorControl1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Center
```

#### Background Image for Calculator
![Figure 195: Background Image for Calculator](https://placehold.it/600x300)

### Border Styles
The below property lets you specify the border style for the Calculator control.

#### Calculatorcontrol Properties Description
| **Calculatorcontrol Properties** | **Description** |
| --- | --- |
| **BorderStyle** | Specifies the 3D border style for the control. The options are,<br><ul><li>RaisedOuter</li><li>RaisedInner</li><li>SunkenOuter</li></ul> |

## API Reference
- **Properties**
  - **BorderStyle**: Specifies the 3D border style for the Calculator control.

## Code Examples (Reiteration)
Refer to the code examples provided above for setting the background image and border styles for the Calculator control.

## Tags and Keywords
<!-- tags: [Syncfusion Winforms, Calculator control, Background Image, Border Style] keywords: [calculatorControl, BackgroundImage, BorderStyle, ImageLayout] -->
```