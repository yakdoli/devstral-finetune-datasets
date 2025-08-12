```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_382.jpeg
document_name: tools
page_number: 382
page_id: tools#page_382
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:10:23Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

![](Properties配置界面.png)

## Overview
- Describes setting the ToolTip text for a ButtonEdit control using properties.
- Explains how to programmatically set ToolTip using the `SetToolTip()` method.
- Demonstrates the CalculatorControl and its features.

## Content
### Setting ToolTip
The ToolTip can be set for a ButtonEdit control in the properties window. As shown in the figure, the ToolTip text can be configured in the properties panel.

#### Figure 187: Setting ToolTip Text
![](Properties配置图.png)

We can also set the ToolTip for ButtonEdit control programmatically using its `SetToolTip()` method.

#### Example Code

**[C#]**
```csharp
this.toolTip1.SetToolTip(this.buttonEdit1, "Click here to search");
```

**[VB.NET]**
```vb
Me.toolTip1.SetToolTip(Me.buttonEdit1, "Click here to search")
```

#### Resulting ToolTip Display
When the ToolTip is set using the `SetToolTip()` method, it appears as shown below.

#### Figure 188: ToolTip set by using the SetToolTip Method
![](SetToolTip方法显示图.png)

### 3.5.2.3 CalculatorControl
This section introduces the CalculatorControl and delves into its features and usage within Windows Forms.

#### Overview of CalculatorControl
The CalculatorControl is a specialized control designed to include calculator functionalities within Windows Forms applications.

#### Installation and Setup
To integrate the CalculatorControl into your application, follow these steps:
1. Add the required Syncfusion libraries.
2. Drag and drop the CalculatorControl from the toolbox onto your form.
3. Configure the properties as needed to customize the look and functionality.

#### Properties and Methods
- **Properties**: Customize aspects such as the display type, button styles, and calculation modes.
- **Methods**: Implement methods to handle complex mathematical operations or customize the behavior based on user input.

#### Example Use Case
The CalculatorControl can be utilized in applications requiring financial calculations, scientific computations, or general arithmetic operations. It provides a user-friendly interface for these tasks.

#### Conclusion
The CalculatorControl offers a versatile solution for incorporating calculator functionalities into your Windows Forms applications, enabling a seamless user experience with customizable features.

---

## Page-level Navigation/TOC
- [3.5.2.3 CalculatorControl](#3.5.2.3-CalculatorControl)

## Cross References
See also:
- [Properties window in Windows Forms](#Properties配置界面)
- [Programmatic ToolTip setting](#SetToolTip方法显示图)

<!-- tags: [Syncfusion, WinForms, ToolTip, CalculatorControl, ButtonEdit, Windows Forms, Control] keywords: [CalculatorControl, ToolTip, SetToolTip, Windows Forms, ButtonEdit, properties, programming] -->
```