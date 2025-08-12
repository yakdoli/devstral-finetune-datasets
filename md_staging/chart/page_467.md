```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_467.jpeg
document_name: chart
page_number: 467
page_id: chart#page_467
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:42:31Z
fidelity: lossless
-->

## Chart for Windows Forms

### Overview

- This section explains how to use the `CustomCommand` and `Command ToolTip` properties to enable the `AutoHighlight` feature in a chart.
- Demonstrates configuring toolbar properties and accessing the toolbar using `ToolBar` properties.

## Content

### Figure 297: CustomCommand = "ChartCommands.AutoHighlight" ; Command ToolTip = "Highlighting"

![Figure 297: CustomCommand = "ChartCommands.AutoHighlight" ; Command ToolTip = "Highlighting"](https://i.imgur.com/example_chart_image.png)

### Figure 298: AutoHighlight feature enabled in Chart using Custom Toolbar Command

![Figure 298: AutoHighlight feature enabled in Chart using Custom Toolbar Command](https://i.imgur.com/example_chart_image2.png)

### 4.9.2.1 Toolbar Properties

The chart control provides complete support for customizing the toolbar appearance. Use the **ChartControl.ToolBar** property to access the toolbar. At runtime, double-click the toolbar to show the **ToolBar Properties** dialog box as in the below image, which lists all the properties. For this, you need to set the `ToolBar.ShowDialog` property to `True`. If you do not want to display this dialog box, set this property to `False`.

## API Reference

### Properties

- **ChartControl.ToolBar**
  - **Description**: Accesses the toolbar for customizing appearance and functionality.
  - **Type**: `ToolBar` (or equivalent)

### Methods

- **ToolBar.ShowDialog(Boolean showDialog)**
  - **Parameters**:
    - **showDialog**: Boolean value to determine whether the toolbar properties dialog is displayed.
  - **Returns**: None.
  - **Default**: False.
  - **Required**: No.

## Code Examples

### Enabling the ToolBar Properties Dialog Box

```csharp
// Enable the ToolBar Properties dialog box
ChartControl chart = new ChartControl();
chart.ToolBar.ShowDialog = true;
```

### Disabling the ToolBar Properties Dialog Box

```csharp
// Disable the ToolBar Properties dialog box
ChartControl chart = new ChartControl();
chart.ToolBar.ShowDialog = false;
```

### Cross References

- See also: CustomCommand, Command ToolTip, AutoHighlight feature, and ChartControl properties related to toolbar configuration.

<!-- tags: [syncfusion, winforms, chart, toolbar, control, api, version: 11.4.0.26] keywords: [chartcommands, autohighlight, customcommand, toolbar properties, dialog box, properties, winforms, syncfusion] -->
```