```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_626.jpeg
document_name: chart
page_number: 626
page_id: chart#page_626
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:56:48Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
group.TableDescriptor.RecordFilters.Add(rfd);
System.Diagnostics.Trace.WriteLine("Filtered Record Count:" & 
                                   group.Table.FilteredRecords.Count);
System.Diagnostics.Trace.WriteLine("Values greater than 30:");
```

## Content

### Filtering Data
```csharp
Me.chartControl1.Series(0).Points.Clear()
Dim j As Integer = 0
For Each rec As Record In group.Table.FilteredRecords
    Dim b As String = rec.GetData().ToString()
    System.Diagnostics.Trace.WriteLine(b)
    Me.chartControl1.Series(0).Points.Add(j, Convert.ToDouble(b))
    j += 1
Next rec
Me.label2.Text = "Number of Filtered points: " & 
                group.Table.FilteredRecords.Count.ToString()
```

## 5.8 How to hide the Chart ZoomButton

### Overview
- Explains how to hide the ZoomButton in the Syncfusion Chart.
- Discusses issues with setting the `Visible` property and provides an alternative solution.

### Content
**Syncfusion Chart** provides a way to access the **ZoomOutButton** through the **ScrollBar** instance. In order to hide this Zoom button, if the **Visible** property is set to **false**, the ZoomButton will be disabled, but there will be an empty space. So instead of setting the **Visible** property, we can set the **ZoomButton** size to be **0**.

### Implementation

#### C#
```csharp
this.chartControl1.GetVScrollBar(this.chartControl1.PrimaryYAxis).ZoomButton.Size = new Size(0, 0);
this.chartControl1.GetHScrollBar(this.chartControl1.PrimaryXAxis).ZoomButton.Size = new Size(0, 0);
```

#### VB.NET
```vb
Me.chartControl1.GetVScrollBar(Me.chartControl1.PrimaryYAxis).ZoomButton.Size = New Size(0, 0)
Me.chartControl1.GetHScrollBar(Me.chartControl1.PrimaryXAxis).ZoomButton.Size = New Size(0, 0)
```

#### Related Topics
- [Managing Zoom Levels in Charts](#)
- [Customizing Chart Appearance](#)
- [Chart Interactivity Features](#)

### References
- API Documentation: [SyncfusionChart API Reference](#)
- User Guide: [Syncfusion WinForms User Guide](#)

<!-- tags: [syncfusion, winforms, chart, zoombutton, vscrollbar, hscrollbar, userguide, sdk] keywords: [chart, zoombutton, hide, scrollbar, size, visible, winforms, syncfusionchart, api] -->
```
