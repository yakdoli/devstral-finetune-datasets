```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_466.jpeg
document_name: chart
page_number: 466
page_id: chart#page_466
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:45:50Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This page describes custom commands available in the Chart toolbar for managing chart interactions such as zooming, resetting, autohighlighting, and panning.

## Content

### Chart toolbar Custom Commands

The following table lists the custom commands available in the Chart toolbar and their descriptions:

| Chart toolbar Custom Commands | Description |
|-------------------------------|-------------|
| ZoomIn                        | Using this command, user can zoom the chart. |
| ZoomOut                       | This command zooms out the chart. |
| ResetZooming                  | The zooming is reset using this command. |
| AutoHighlight                 | This command is used to enable the autohighlight feature in the chart series. |
| ToggleXZooming                | This toolbar command enables zooming in the x-axis. |
| ToggleYZooming                | This toolbar command enables zooming in the y-axis. |
| TogglePanning                 | This command enables panning of the zoomed chart. |

#### Example Code for Adding a Custom Command Item

The following code examples demonstrate how to add a custom tool command item to the Chart toolbar.

#### C# Implementation
```csharp
ChartToolBarCommandItem x1 = new ChartToolBarCommandItem();
x1.Command = ChartCommands.AutoHighlight;
x1.IsCheckable = false;
Image v = System.Drawing.Image.FromFile(@"...\Data\Visio.png");
x1.Image = v;
x1.Name = "Custom Tools";
x1.ToolTip = "Highlighting";
x1.Checked = true;
this.chartControl1.ToolBar.Items.Add(x1);
```

#### VB.NET Implementation
```vb
Dim x1 As New ChartToolBarCommandItem()
x1.Command = ChartCommands.AutoHighlight
x1.IsCheckable = False
Dim v As Image = System.Drawing.Image.FromFile("...\Data\Visio.png")
x1.Image = v
x1.Name = "Custom Tools"
x1.ToolTip = "Highlighting"
x1.Checked = True
Me.chartControl1.ToolBar.Items.Add(x1)
```

### Visual Representation of the Custom Command Item

The screenshot below illustrates the added custom command item with its tooltip labeled as "Highlighting."

![Custom Command Item](image.png)

## API Reference

### Namespace: Syncfusion.Windows.Forms.Chart

#### ChartToolBarCommandItem
- **Constructor**  
  ```csharp
  public ChartToolBarCommandItem()
  ```  
  Creates a new instance of the ChartToolBarCommandItem class.

- **Properties**  
  - **Command**: Specifies the command to be executed when the item is clicked.
  - **IsCheckable**: Indicates whether the item can be checked or not.
  - **Image**: Sets the image displayed on the toolbar item.
  - **Name**: Sets the name of the toolbar item.
  - **ToolTip**: Sets the tooltip text for the toolbar item.
  - **Checked**: Indicates whether the item is checked.

#### ChartCommands
- **AutoHighlight**: Enumerates the command for enabling autohighlighting in the chart series.

## Code Examples

The provided code examples show how to add a custom toolbar item to the Chart toolbar in both C# and VB.NET.

<!-- tags: chart, toolbar, zooming, panning, autohighlighting, windows forms, syncfusion winforms, version: 11.4.0.26 -->
```