```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_426.jpeg
document_name: chart
page_number: 426
page_id: chart#page_426
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:42:46Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Illustrates the implementation of ChartStripLine features in both C# and VB.NET for customizing StripLines in Windows Forms.
- Demonstrates how to enable, configure, and apply gradients to StripLines, including text formatting and alignment.

## Content
### ChartStripLine Customization

#### C#

```csharp
//Declaring
ChartStripLine stripLine = new ChartStripLine();

//Customizing the Stripline
stripLine.Enabled = true;
stripLine.Vertical = false;
stripLine.Start = 140;
stripLine.Width = 35;
stripLine.FixedWidth = 30;
stripLine.End = 175;
stripLine.Text = "100% of Quota";
stripLine.TextColor = Color.Cyan;
stripLine.TextAlignment = ContentAlignment.MiddleCenter;
stripLine.Font = new Font("Arial", 10, FontStyle.Bold);
stripLine.Interior = new BrushInfo(230, new BrushInfo(GradientStyle.Vertical, Color.OrangeRed, Color.DarkKhaki));

//Adding stripline to the X-axis
this.chartControl1.PrimaryYAxis.StripLines.Add(stripLine);
```

#### VB.NET

```vb
' Declaring
Private stripLine As ChartStripLine = New ChartStripLine()

' Customizing the Stripline
stripLine.Enabled = True
stripLine.Vertical = True
stripLine.Start = 140
stripLine.Width = 35
stripLine.FixedWidth = 30
stripLine.End = 175
stripLine.Text = "100% of Quota"
stripLine.TextColor = Color.Cyan
stripLine.TextAlignment = ContentAlignment.MiddleCenter
stripLine.Font = New Font("Arial", 10, FontStyle.Bold)
stripLine.Interior = New BrushInfo(230, new BrushInfo(GradientStyle.Vertical, Color.OrangeRed, Color.DarkKhaki))

' Adding stripline to the X-axis
Me.chartControl1.PrimaryXAxis.StripLines.Add(stripLine)
```

### Explanation
- **StripLine Declaration**: `stripLine` is declared as a `ChartStripLine` object.
- **Customization**:
  - **Enabled**: Activates the StripLine.
  - **Vertical**: Specifies the StripLine orientation (horizontal in C#, vertical in VB.NET).
  - **Start and End**: Defines the range of the StripLine on the axis.
  - **Width and FixedWidth**: Adjusts the appearance of the StripLine.
  - **Text and TextFormatting**: Adds descriptive text with specified color and alignment.
  - **Font**: Defines the font style, size, and appearance.
  - **Interior Gradient**: Implements a gradient fill between specified colors.
- **Adding to Axis**: The configured StripLine is added to the primary axis (`X` or `Y`, depending on the example).

## Cross References
- Refer to additional documentation on `ChartStripLine` properties and methods for more comprehensive customization options.
- Consult Syncfusion's official documentation for detailed guidance on UI elements and their configurations.

<!-- tags: [Syncfusion, WinForms, ChartStripLine, GradientFill, TextFormatting, WindowsForms] keywords: [StripLine, Customization, Gradient, FontFormatting, AxisConfiguration, ChartControl] -->
```