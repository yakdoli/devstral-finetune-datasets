```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_381.jpeg
document_name: tools
page_number: 381
page_id: tools#page_381
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:08:42Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Associating PercentTextBox to the ButtonEdit control.
- Setting percent properties for the ButtonEdit control.
- Setting tooltip for ButtonEdit Child buttons.

## Content

### Figure 185: Associating PercentTextBox to the ButtonEdit Control

The provided image illustrates the properties window for a `ButtonEdit` control, where the `TextBox` property is set to `percentTextBox1`. This association links the `PercentTextBox` to the `ButtonEdit` control.

#### Procedure:
1. In the properties window, select the `TextBox` property under the `ButtonEdit` control.
2. Choose the `percentTextBox1` from the dropdown list to associate the `PercentTextBox` with the `ButtonEdit` control.

![Figure 186: ButtonEditControl with PercentTextBox Control](https://i.imgur.com/example_image.png)

### Figure 186: ButtonEditControl with PercentTextBox Control

The resulting `ButtonEdit` control, as shown in the image, indicates that the `PercentTextBox` control is successfully associated and configured to display percentages.

#### Setting Percent Properties:
From the same properties window, you can configure the percent properties for the `ButtonEdit` control, ensuring it displays and handles percentage values appropriately.

### 3.5.2.2.5.3 How to set tooltip for ButtonEdit Child buttons?

To set a tooltip for a child button in a `ButtonEdit` control, follow these steps:

#### Procedure:
1. Drag and drop a `ToolTip` control from the toolbox onto your form.
2. Assign the tooltip text using the `extender` property associated with the specific child button within the `ButtonEdit` control.

### Summary
This section details how to associate a `PercentTextBox` with a `ButtonEdit` control, set its percent properties, and configure tooltips for child buttons of the `ButtonEdit` control.

## API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Tools`
- **Class**: `ButtonEdit`
- **Properties**:
  - `TextBox`: Associated `PercentTextBox` control.
  - `tooltip`: Configures tooltips for child buttons.

### Code Examples

#### Example 1: Associating PercentTextBox with ButtonEdit
```csharp
SyncfusionButtonEdit buttonEdit = new SyncfusionButtonEdit();
SyncfusionTextBox percentTextBox = new SyncfusionTextBox();

// Assign PercentTextBox to ButtonEdit
buttonEdit.TextBox = percentTextBox;
```

#### Example 2: Setting Tooltip for Child Button
```csharp
SyncfusionButtonEdit buttonEdit = new SyncfusionButtonEdit();
SyncfusionToolTip tooltip = new SyncfusionToolTip();

// Set tooltip for a child button
buttonEdit_extender.ToolTip.SetToolTip(childButton, "This is a tooltip for the child button");
```

## Page-level Navigation/TOC (if applicable)
- Associating PercentTextBox to the ButtonEdit Control
- Setting Percent Properties for ButtonEdit
- Setting Tooltip for ButtonEdit Child Buttons

## Cross References
- See also: Other controls in `Syncfusion.Windows.Forms.Tools` for additional properties and configurations.

<!-- Tags: ["Windows Forms", "ButtonEdit", "PercentTextBox", "Tooltip", "Syncfusion", "version: 11.4.0.26"] -->
```