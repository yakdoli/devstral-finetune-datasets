```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_095.jpeg
document_name: tools
page_number: 095
page_id: tools#page_095
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:20:06Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes the controls that support Office 2010 themes and how to apply these themes using code examples.
- Lists the controls that support Office 2010 styles.

## Content

### Supported Controls
Controls that support Office 2007 themes will also support the Office 2010 themes. The API used to set the style will also be the same as Office 2007.

The following code samples can be used to apply Office 2010 themes to the DockingManager.

#### [C#]
```csharp
// Set the visual style of the docked controls.
this.dockingManager.VisualStyle =
    Syncfusion.Windows.Forms.VisualStyle.Office2010;
this.dockingManager1.Office2010Theme =
    Syncfusion.Windows.Forms.Office2010Theme.Silver;
```

#### [VB]
```vb
' Set the visual style of the docked controls.
Me.dockingManager.VisualStyle =
    Syncfusion.Windows.Forms.VisualStyle.Office2010
Me.dockingManager1.Office2010Theme =
    Syncfusion.Windows.Forms.Office2010Theme.Silver
```

The list of controls that support Office 2010 styles is displayed in the following table:

| 1 | ButtonAdv |
| --- | --- |
| 2 | ButtonEdit |
| 3 | CalculatorControl |
| 4 | CheckBoxAdv |
| 5 | ColorPickerButton |
| 6 | ColorPickerUIAdv |
| 7 | ColorUIControl |
| 8 | ComboBoxAdv |
| 9 | ComboBoxBase |
| 10 | ComboBoxDropDown |
| 11 | CurrencyEdit |
| 12 | CurrencyTextBox |

<!-- tags: [Syncfusion Winforms, Office themes, DockingManager, VisualStyle, Office2010Theme] keywords: [ButtonAdv, ButtonEdit, CalculatorControl, CheckBoxAdv, ColorPickerButton, ColorPickerUIAdv, ColorUIControl, ComboBoxAdv, ComboBoxBase, ComboBoxDropDown, CurrencyEdit, CurrencyTextBox] -->
```