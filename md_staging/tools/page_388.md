```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_388.jpeg
document_name: tools
page_number: 388
page_id: tools#page_388
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:09:52Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Layout Modes - Layout of the components in a Calculator.
- Background Settings - Background settings for the control.
- Border Styles - Border for the control.
- Button Spacing - Spacing between the Calculator buttons.
- Button Foreground - Foreground settings for the buttons.

### 3.5.2.3.3.2.1 Layout Modes

The Calculator control can be laid out in the following modes.

- WindowsStandard Mode - Modeled with windows standard layout (Default).
- Financial Mode - Modeled with windows financial layout.

```csharp
this.calculatorControl1.LayoutType =
Syncfusion.Windows.Forms.Tools.CalculatorLayoutTypes.Financial;
```

```vbnet
Me.calculatorControl1.LayoutType =
Syncfusion.Windows.Forms.Tools.CalculatorLayoutTypes.Financial
```

![Financial Standard Layout Mode](image1.png)
**Figure 193: Financial Standard Layout Mode**

**Note:** We can set different button styles for the Calculator control, using `CalculatorControl.ButtonStyle` property. Refer to the **Themes and Button Styles** topic to know more. ButtonStyles can be applied to both the layout modes.

### 3.5.2.3.3.2.2 Background Settings

Background settings for a Calculator control is discussed in this section.

## Code Examples

```csharp
this.calculatorControl1.LayoutType =
Syncfusion.Windows.Forms.Tools.CalculatorLayoutTypes.Financial;
```

```vbnet
Me.calculatorControl1.LayoutType =
Syncfusion.Windows.Forms.Tools.CalculatorLayoutTypes.Financial
```

## See also:
- Themes and Button Styles
- Layout Modes
- Background Settings
- Border Styles
- Button Spacing
- Button Foreground
- Calculator Control

<!-- tags: [winforms, calculator control, layout modes, background settings, button styles] keywords: [C#, VB.NET, financial layout, windows standard layout, Syncfusion Windows Forms, CalculatorLayoutTypes, button styles] -->
```