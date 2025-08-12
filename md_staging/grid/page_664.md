```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_664.jpeg
document_name: grid
page_number: 664
page_id: grid#page_664
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:32:10Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```vb
gridGroupingControl1.TableDescriptor.SortedColumns.Clear()
gridGroupingControl1.TableDescriptor.SortedColumns.Add("1")
gridGroupingControl1.TableDescriptor.SortedColumns.Add("2")
Else
	gridGroupingControl1.TableDescriptor.SortedColumns.Clear()
End If
Me.gridGroupingControl1.Refresh()
End Sub

' Grouping Option.
Private Sub checkBoxGrouping_CheckedChanged(ByVal sender As Object, _
ByVal e As System.EventArgs) Handles checkBoxGrouping.CheckedChanged
If Me.checkBoxGrouping.Checked Then
	gridGroupingControl1.TableDescriptor.GroupedColumns.Clear()
	gridGroupingControl1.TableDescriptor.GroupedColumns.Add("1")
	gridGroupingControl1.Table.ExpandAllGroups()
Else
	gridGroupingControl1.TableDescriptor.GroupedColumns.Clear()
End If
Me.gridGroupingControl1.Refresh()
End Sub

' Filtering Option.
Private Sub checkBoxFilter_CheckedChanged(ByVal sender As Object, ByVal _
e As System.EventArgs) Handles checkBoxFilter.CheckedChanged
If Me.checkBoxFilter.Checked Then
	gridGroupingControl1.TableDescriptor.RecordFilters.Clear()
	gridGroupingControl1.TableDescriptor.RecordFilters.Add(Me.textBoxFilter.Text)
Else
	gridGroupingControl1.TableDescriptor.RecordFilters.Clear()
End If
Me.gridGroupingControl1.Refresh()
End Sub
```

## Overview
- This page demonstrates the functionality of the Essential Grid control for Windows Forms, showcasing how to implement sorting, grouping, and filtering options. The provided code examples illustrate how to dynamically adjust these features based on user interactions, such as checkbox states.
- Additionally, the page explains how TrackBar controls influence the frequency settings for Timer and BlinkTime, integrating these changes within the grid grouping control through TrackBarScroll event handlers.

## Content

### Sorting Option

```vb
gridGroupingControl1.TableDescriptor.SortedColumns.Clear()
gridGroupingControl1.TableDescriptor.SortedColumns.Add("1")
gridGroupingControl1.TableDescriptor.SortedColumns.Add("2")
Else
	gridGroupingControl1.TableDescriptor.SortedColumns.Clear()
End If
Me.gridGroupingControl1.Refresh()
End Sub
```

### Grouping Option

```vb
Private Sub checkBoxGrouping_CheckedChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles checkBoxGrouping.CheckedChanged
If Me.checkBoxGrouping.Checked Then
	gridGroupingControl1.TableDescriptor.GroupedColumns.Clear()
	gridGroupingControl1.TableDescriptor.GroupedColumns.Add("1")
	gridGroupingControl1.Table.ExpandAllGroups()
Else
	gridGroupingControl1.TableDescriptor.GroupedColumns.Clear()
End If
Me.gridGroupingControl1.Refresh()
End Sub
```

### Filtering Option

```vb
Private Sub checkBoxFilter_CheckedChanged(ByVal sender As Object, ByVal e As System.EventArgs) Handles checkBoxFilter.CheckedChanged
If Me.checkBoxFilter.Checked Then
	gridGroupingControl1.TableDescriptor.RecordFilters.Clear()
	gridGroupingControl1.TableDescriptor.RecordFilters.Add(Me.textBoxFilter.Text)
Else
	gridGroupingControl1.TableDescriptor.RecordFilters.Clear()
End If
Me.gridGroupingControl1.Refresh()
End Sub
```

### Integrating TrackBar Controls for Frequency Adjustment

```vb
// To change the Blink Time Frequency.
private void trackBarBlinkFrequency_Scroll(object sender, System.EventArgs e)
{
    this.gridGroupingControl1.BlinkTime = this.trackBarBlinkFrequency.Value * 100;
}
```

### Summary
The page illustrates the essential functionalities of sorting, grouping, and filtering within the Essential Grid control for Windows Forms, along with dynamic adjustments using event handlers. It also demonstrates how user interactions with TrackBar controls can influence the grid's frequency settings.

## Cross References
- [TrackBar Controls](#trackbar-controls)
- [Grid Grouping Control](#grid-grouping-control)
- [Sorting and Filtering](#sorting-and-filtering)

<!-- tags: [Syncfusion Winforms, Grid, Grouping, Filtering, Sorting, TrackBar, Event Handling] keywords: [Essential Grid, Windows Forms, TrackBarControls, frequency adjustment, event handlers, GridGroupingControl] -->
```