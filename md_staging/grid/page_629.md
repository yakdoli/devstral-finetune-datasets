```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_629.jpeg
document_name: grid
page_number: 629
page_id: grid#page_629
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:28:26Z
fidelity: lossless
-->

## Overview
- Demonstrates configurations and event handling for a grid grouping control in a WinForms application.
- Focuses on displaying logs for property changes using the PropertyChanging event.
- Includes detailed code examples to customize the grid's appearance, behavior, and data handling.

## Content

### Configuring Grid Grouping Control

The following code snippet illustrates the setup of a `GridGroupingControl` control within a Windows Forms application. This includes configuring various properties such as data sources, styles, and event handling.

#### Code Example
```csharp
gridGroupingControl1.IntelliMousePanning = True
Me.splitContainer1.Panel1.Controls.Add(Me.gridGroupingControl1)
gridGroupingControl1.Engine = schema
gridGroupingControl1.DataSource = New TestEngineOptimizations.VirtualList(100000)
gridGroupingControl1.ShowGroupDropArea = True
Me.Refresh()

Cursor.Current = Cursors.Arrow
Me.LogWindow.Items.Add(String.Format("Elapsed Time: {0}", Environment.TickCount - time))
gridGroupingControl1.Appearance.AnyCell.Font.Facename = "Verdana"
gridGroupingControl1.Appearance.AnyCell.TextColor = Color.MidnightBlue
gridGroupingControl1.TableOptions.GridVisualStyles = GridVisualStyles.Office2007Blue
gridGroupingControl1.TableOptions.GridLineBorder = New GridBorder(GridBorderStyle.Solid, Color.FromArgb(227, 239, 255), GridBorderWeight.Thin)
```

### Handling Property Changing Events

The `PropertyChanging` event is utilized to log all property changes in the grid. This helps in tracking the results of grid operations such as grouping and sorting.

#### Code Example
```csharp
[C#]

gridGroupingControl1.PropertyChanging += new DescriptorPropertyChangedEventHandler(gridGroupingControl1_PropertyChanging);

Timer t = null;
void gridGroupingControl1_PropertyChanging(object sender, DescriptorPropertyChangedEventArgs e)
{
    LogWindow.Items.Add(e.ToString());
    if (t != null)
    {
        t.Tick -= new EventHandler(t_Tick);
        t.Dispose();
    }
    t = new Timer();
    t.Interval = 100;
    t.Tick += new EventHandler(t_Tick);
}
```

## API Reference

### Event Handling
- **PropertyChanging Event**: Raised when a property of an object is about to be modified. This event is key for logging purposes and monitoring grid operations.
- **DescriptorPropertyChangedEventHandler**: The delegate for handling the `PropertyChanging` event for descriptors. It allows attaching custom event handlers to capture property changes.

### Classes and Properties
- **GridGroupingControl**: The main class representing the grid control.
  - **IntelliMousePanning**: Boolean property to enable intelligent panning behavior.
  - **Engine**: Specifies the engine to be used to operate on the grid control.
  - **DataSource**: Data source property to bind the grid to a dataset.
  - **ShowGroupDropArea**: Boolean to control the visibility of the group drop area.
  - **Appearance.AnyCell.Font.Facename**: Sets the font face for grid cells.
  - **TableOptions.GridLineBorder**: Configures the border style and color for table lines.

### Methods
- **Refresh**: Updates the grid control to reflect any changes made programmatically.

### Additional Features
- **Log Display**: Logs are displayed in the application window to track the `PropertyChanging` events and their timestamps.
- **Memory Usage**: The logs include information about the elapsed time, indicating performance metrics.

## RAG Annotations
<!-- tags: [WinForms, GridGroupingControl, PropertyChanging, EventHandling, Logging] keywords: [grid grouping, property change, descriptor property changed, timer, event handler, data binding, visual styles, memory usage] -->
``` 
