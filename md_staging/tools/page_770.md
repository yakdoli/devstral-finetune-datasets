```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_770.jpeg
document_name: tools
page_number: 770
page_id: tools#page_770
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:33:45Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses the various values and settings of the PercentTextBox control.
- Explains the properties and their functionalities with examples in C# and VB.NET.

## Value Settings
The various values of the PercentTextBox control and their settings are given below.

| **PercentTextBox Properties**      | **Description**                                                                 |
|------------------------------------|---------------------------------------------------------------------------------|
| PercentValue                       | Specifies the double value of the PercentTextBox control.                    |
| DefaultValue                       | Specifies the default value. The default value is set to 'Null'.               |
| BindableValue                      | Wrapper property that indicates the value. This property can be used to set the value of the control to 'Null'. |
| BindablePercentValue              | Wrapper property that indicates the percent value. This property can be used to set the value of the control to 'Null'. |
| DoubleValue                        | Gets / sets the double value of the control. This will be formatted and displayed. |

### Code Examples

#### C#
```csharp
this.percentTextBox1.PercentValue = 5;
this.percentTextBox1.DefaultValue = 0;
this.percentTextBox1.BindableValue = 0.05;
this.percentTextBox1.BindablePercentValue = 5;
this.percentTextBox1.DoubleValue = 0.05;
```

#### VB.NET
```vb
Me.percentTextBox1.PercentValue = 5
Me.percentTextBox1.DefaultValue = 0
Me.percentTextBox1.BindableValue = 0.05
Me.percentTextBox1.BindablePercentValue = 5
Me.percentTextBox1.DoubleValue = 0.05
```

### Figure: Percent Value Set
![Percent Value Set](https://example.com/image770)  
*Figure 486: Percent Value Set*

## Page-level Navigation/TOC (if applicable)
- None

## Cross References
- None

<!-- tags: [Windows Forms, PercentTextBox, Properties, Syncfusion Winforms, C# code, VB.NET code] keywords: [PercentTextBox, DefaultValue, BindableValue, BindablePercentValue, DoubleValue] -->
```