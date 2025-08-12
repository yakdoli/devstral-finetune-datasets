```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_472.jpeg
document_name: chart
page_number: 472
page_id: chart#page_472
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:44:22Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to set the toolbar behavior for a Chart in Windows Forms.
- Explains the use of context menus on the chart, including Chart Area and Series menus.
- Provides examples in C# and VB.NET for configuring toolbar behavior.

## Content

### Toolbar Behavior

The following examples show how to configure the toolbar behavior for a Chart:

- **C# Example:**
  ```csharp
  this.chartControl1.ToolBar.Behavior = ChartDockingFlags.All;
  ```

- **VB.NET Example:**
  ```vb.net
  Me.chartControl1.ToolBar.Behavior = ChartDockingFlags.All
  ```

#### Note: Toolbar Display or Hiding During Printing
You can display or hide a toolbar while printing a Chart. Refer to the **Printing And Print Preview** topic for more details.

### 4.9.3 Context Menu

#### Chart Area and Series Context menu

##### Chart Area and Series Context menu

The chart has a built-in context menu, which can be enabled by setting the `ShowContextMenu` property to `true`. This context menu will let the user change the chart type on a series, enable zooming, switch between 2D and 3D modes, and more.

There are two types of context menus, both of which get shown by default when the above property is set to `true`.

1. **Chart Area context menu** - This will be displayed when the mouse is over the chart area.

## API Reference

### Properties
- `ShowContextMenu`: Enables or disables the display of the context menu.

## Code Examples

The examples above demonstrate how to configure the toolbar behavior and enable the context menu for a Chart in Windows Forms.

## Cross References

See also:
- **Printing And Print Preview** for details on displaying or hiding the toolbar during printing.

<!-- tags: [syncfusion, winforms, chart, toolbar, context menu, printing] keywords: [chartdockflags, showcontextmenu] -->
```