```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_639.jpeg
document_name: chart
page_number: 639
page_id: chart#page_639
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:52:59Z
fidelity: lossless
-->

## Chart Control Print Document Event Handling

### Overview
- Demonstrates the management of chart control printing, including handling toolbar functionality, maximum page range, and reseting chart axis properties.
- Includes C# and VB.NET code examples for setting up print document event handlers and managing chart rendering during the print process.

### Content

#### C# Example: Handling Print Document Events

```csharp
mf.Dispose();
}
}
EndTransform(e.Graphics, container);

for (int i = 0; i < this.chartControl1.Series.Count; i++)
{
    this.chartControl1.Series[i].StylesImpl.Style.ResetInterior();
    this.chartControl1.Series[i].StylesImpl.Style.ResetBorder();
    this.chartControl1.Series[i].StylesImpl.Style.CopyFrom(tempStyles[i]);
}

// Checking Toolbar functionality of print
if (!this.chartControl1.PrintDocument.PrintToolBar)
{
    this.chartControl1.ShowToolbar = toolBatVisibility;
}

// Redraws the chart
this.chartControl1.Redraw(true);

// Maximum exceeds the default range means reset the HasMorePages property.
if (mx > end)
    e.HasMorePages = false;

// Finally resets the maximum and minimum value for default chartcontrol
this.chartControl1.ChartArea.PrimaryXAxis.Range.Min = start;
this.chartControl1.ChartArea.PrimaryXAxis.Range.Max = end;
this.chartControl1.ChartArea.PrimaryXAxis.Range.Interval = Interval;
}
```

#### VB.NET Example: Printing Event Handler Setup

```vb
Me.chartControl1.PrintDocument.PrintPage += New System.Drawing.Printing.PrintPageEventHandler(PrintDocument_PrintPage)

''' PrintPage Event
```

### API Reference

#### Methods
- `Dispose()`: Disposes of the managed resources owned by the object.
- `EndTransform(Graphics, Container)`: Ends the transformation for the specified Graphics object.
- `Redraw(Boolean)`: Forces a redraw of the chart control.

### Code Examples

The examples above demonstrate how to:
- Reset the style properties of a chart's series.
- Manage print toolbar visibility based on whether the print document has a toolbar.
- Redraw the chart control to reflect changes.
- Handle the logic for multiple pages by resetting the `HasMorePages` property.
- Reset axis range and interval properties of the chart after printing.

### Cross References
- For more detailed information on chart control properties and methods, refer to the [chart control documentation](#chart-control-documentation).
- See also: [printing in Windows Forms](#printing-in-windows-forms).

<!-- tags: [chart, control, print document, event handling, windows forms, syncfusion, 11.4.0.26] keywords: [print document, chart control, event handler, PrintPageEventHandler, PrintToolBar, HasMorePages, Redraw, Axis Range] -->
```