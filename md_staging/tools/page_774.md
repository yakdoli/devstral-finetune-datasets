```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_774.jpeg
document_name: tools
page_number: 774
page_id: tools#page_774
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:33:58Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains the text settings of the PercentTextBox control.
- Discusses how to set and customize the text associated with the PercentTextBox control using specific properties.

## Text Settings

### Overview
This section discusses the text settings of the PercentTextBox control. The text associated with the PercentTextBox control can be set and customized using the following settings:

| PercentTextBox Properties | Description |
|---------------------------|-------------|
| **Text**                  | Specifies the text associated with the control. |
| **CharacterCasing**       | Gets / sets the case of character as they are typed.<br><br>It includes the below given options:<br><br>Normal, Upper and Lower. |
| **TextAlign**             | Indicates how the text should be aligned for edit controls. |
| **SelectedText**          | Gets / sets the selected text in the PercentTextBox. |
| **SelectAllOnFocus**      | Specifies if the text should be selected when the control gets the focus. |
| **SwitchModeOnFocus**     | Indicates whether the PercentTextBox should allow editing in numeric mode, when it receives focus. |
| **HideSelection**         | Indicates that the selection should be hidden when the edit control loses focus. |
| **ClipText**              | Returns the clipped text without the formatting. |
| **DrawActiveWhenDisabled**| Specifies if the text should be drawn active, |

## API Reference

### Usage
- Utilize the properties listed in the table above to customize the text settings of the PercentTextBox control as per application requirements.

### Code Example
```csharp
// Example usage of PercentTextBox properties
PercentTextBox percentTextBox = new PercentTextBox();
percentTextBox.CharacterCasing = CharacterCasing.Upper;
percentTextBox.TextAlign = HorizontalAlignment.Center;
percentTextBox.SelectAllOnFocus = true;
percentTextBox.SwitchModeOnFocus = true;
```

## Cross References
- For more information on customizing controls in Syncfusion WinForms, see the [Syncfusion Windows Forms Documentation](https://www.syncfusion.com/kb/197/).
- Related controls and their customization options can be found in the [Editor Controls section](#).

<!-- tags: [winforms, percenttextbox, text settings, customization, syncfusion] keywords: [text alignment, character casing, selected text, selection visibility, input mode, draw active, percenttextbox properties] -->
```