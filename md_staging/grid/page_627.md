```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_627.jpeg
document_name: grid
page_number: 627
page_id: grid#page_627
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:29:27Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Logging Memory Usage

```vb
Private Sub LogMemoryUsage()

    ' Force garbage collection and get used memory size.
    GC.Collect()
    System.Threading.Thread.Sleep(10)
    GC.Collect()
    System.Threading.Thread.Sleep(100)
    GC.Collect()
    LogWindow.Items.Add(String.Format("Optimizations for {0}: ", _
        Me.gridGroupingControl.TableDescriptor.Name))
    LogWindow.Items.Add(String.Format("VirtualMode: {0}, ", _
        Me.gridGroupingControl.Table.VirtualMode))
    LogWindow.Items.Add(String.Format("WithoutCounter: {0}, ", _
        Me.gridGroupingControl.Table.WithoutCounter))
    LogWindow.Items.Add(String.Format("RecordsAsDisplayElements: {0}, ", _
        gridGroupingControl1.Table.RecordsAsDisplayElements))

    Dim myProcess As Process = Process.GetCurrentProcess()
    Dim workingSetSizeinKiloBytes As Double = myProcess.WorkingSet64 / 1000
    Dim s As String = "Process's physical memory usage: " & _
        workingSetSizeinKiloBytes.ToString() & " kb"
    LogWindow.Items.Add(s)
    LogWindow.Items.Add("")
End Sub
```

### Handling Button Click Event

6. Handle the ButtonClick event in order to populate the grid when the button is clicked. It also calls `LogMemoryUsage` method to display the initial optimization settings for the grid - the optimizations for an ungrouped and unsorted grid.

```csharp
[C#]

this.button1.Click += new System.EventHandler(this.button1_Click);

private void button1_Click(object sender, EventArgs e)
{
    this.LogWindow.Items.Add("");
    this.LogWindow.Items.Add("Flat, Virtual List with Sorting and Grouping Enabled.");
    int time = Environment.TickCount;
    Cursor.Current = Cursors.WaitCursor;

    // Load a Grid Grouping control with a new engine.
    gridGroupingControl1 = new GridGroupingControl();
    gridGroupingControl1.BackColor =
```

## Page-level Navigation/TOC (if applicable)
- If this page contains a local Table of Contents or cross-references, include them here as described in the schema.

## Cross References
- See also: Any explicit links or references present on the page.

<!-- tags: [grid, windowsforms, optimization, memoryusage, log, eventhandler, grouping, list, sort] keywords: [gridgroupingcontrol, virtualmode, withoutcounter, recordsasdisplayelements, workingsetsize, environtickcount, cursors] -->
```