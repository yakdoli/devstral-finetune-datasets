```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_937.jpeg
document_name: grid
page_number: 937
page_id: grid#page_937
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:58Z
fidelity: lossless
-->

## Overview

- Demonstrates how to configure list box selection mode and color options in the Essential Grid for Windows Forms.
- Provides code examples in both C# and VB.NET for iterating through selected ranges and displaying record values in a list box.
- Includes a sample screenshot to illustrate the feature in practice.

## Content

**WinForms Essential Grid List Box Selection Configuration**

### Setting List Box Selection Mode and Color Options

The following code in VB.NET configures the Essential Grid control (`gridGroupingControl1`) to allow multiple cell selections and specifies the selection color:

```vb
Me.gridGroupingControl1.TableOptions.ListBoxSelectionMode = SelectionMode.MultiExtended
Me.gridGroupingControl1.TableOptions.ListBoxSelectionColorOptions = GridListBoxSelectionColorOptions.DrawAlphablend
Me.gridGroupingControl1.TableModel.Options.AlphaBlendSelectionColor = Color.Red
```

### Iterating Through Selected Ranges

The below code loops through the ranges of all the selections and writes the record values that have been selected to a listbox control.

### C# Example

```csharp
foreach (GridRangeInfo range in
gridGroupingControl1.TableModel.SelectedRanges)
{
    if (range.IsRows)
    {
        for (int i = range.Top; i <= range.Bottom; i++)
        {
            Record rec = gridGroupingControl1.Table.DisplayElements[i].GetRecord();
            listBox1.Items.Add(rec.ToString());
        }
    }
}
```

### VB.NET Example

```vb
For Each range As GridRangeInfo In gridGroupingControl1.TableModel.SelectedRanges
    If range.IsRows Then
        Dim i As Integer = range.Top
        Do While i <= range.Bottom
            Dim rec As Record = gridGroupingControl1.Table.DisplayElements(i).GetRecord()
            listBox1.Items.Add(rec.ToString())
            i += 1
        Loop
    End If
Next range
```

### Sample Screenshot

3. Here is a sample screenshot.

---

## API Reference (if applicable)

This page does not provide explicit API references. It primarily focuses on configuring and iterating through selected ranges in the Essential Grid control.

## Code Examples

- **VB.NET**: Configures the selection mode and color options for the Grid control.
- **C#**: Iterates through selected ranges and displays record values in a list box.
- **VB.NET**: Similar functionality as in C#, iterating through selected ranges.

## Cross References

- Refer to the Essential Grid documentation for more details on list box selection modes and color options.
- Additional samples and tutorials can be found in the Syncfusion WinForms documentation archive.

<!-- tags: [windows-forms, grid, selection, list-box, csharp, vb.net] keywords: [selection mode, selection color options, selected ranges, list box control, record values, iterate through ranges, gridGroupingControl, display elements] -->
```