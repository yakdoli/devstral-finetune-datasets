```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_628.jpeg
document_name: grid
page_number: 628
page_id: grid#page_628
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:29:12Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Example C# Code

```csharp
System.Drawing.SystemColors.Window;
gridGroupingControl.Dock = System.Windows.Forms.DockStyle.Fill;
gridGroupingControl.Name = "gridGroupingControl";
gridGroupingControl.TabIndex = 0;
gridGroupingControl.VersionInfo = "3.2.0.0";
gridGroupingControl.IntelliMousePanning = true;

this.splitContainer1.Panel1.Controls.Add(this.gridGroupingControl);
gridGroupingControl.Engine = schema;
gridGroupingControl.DataSource = new TestEngineOptimizations.VirtualList(100000);
gridGroupingControl.ShowGroupDropArea = true;
this.Refresh();

Cursor.Current = Cursors.Arrow;
this.LogWindow.Items.Add(string.Format("Elapsed Time: {0}", Environment.TickCount - time));
gridGroupingControl.Appearance.AnyCell.Font.Name = "Verdana";
gridGroupingControl.Appearance.AnyCell.TextColor = Color.MidnightBlue;

gridGroupingControl.TableOptions.GridVisualStyles = Syncfusion.Windows.Forms.GridVisualStyles.Office2007Blue;
gridGroupingControl.TableOptions.GridLineBorder = new GridBorder(GridBorderStyle.Solid, Color.FromArgb(227, 239, 255), GridBorderWeight.Thin);

// Initial Log Display.
LogMemoryUsage();
}
```

### Example VB.NET Code

```vb
Private Sub button1_Click(ByVal sender As Object, ByVal e As EventArgs) Handles button1.Click
    Me.LogWindow.Items.Add("")
    Me.LogWindow.Items.Add("Flat, Virtual List with Sorting and Grouping Enabled.")
    Dim time As Integer = Environment.TickCount
    Windows.Forms.Cursor.Current = Cursors.WaitCursor

    ' Load a Grid Grouping control with a new engine.
    gridGroupingControl = New GridGroupingControl()
    gridGroupingControl.BackColor = System.Drawing.SystemColors.Window
    gridGroupingControl.Dock = System.Windows.Forms.DockStyle.Fill
    gridGroupingControl.Name = "gridGroupingControl"
    gridGroupingControl.TabIndex = 0
    gridGroupingControl.VersionInfo = "3.2.0.0"
End Sub
```

## API Reference

- **Namespace:** Syncfusion.Windows.Forms
- **Class:** GridGroupingControl
- **Properties:**
  - `Dock`: Specifies the docking style of the control.
  - `Name`: Specifies the name of the control.
  - `TabIndex`: Specifies the tab order of the control.
  - `VersionInfo`: Specifies the version information of the control.
  - `IntelliMousePanning`: Enables or disables mouse panning.
  - `DataSource`: Specifies the data source for the grid.
  - `ShowGroupDropArea`: Specifies whether to show the group drop area.
  - `Engine`: Specifies the engine for the grid.
  - `Appearance`: Specifies the appearance settings for the grid.
  - `TableOptions`: Specifies the table options for the grid.
  - `GridVisualStyles`: Specifies the visual styles for the grid.
  - `GridLineBorder`: Specifies the border style for the grid lines.

## Code Examples

The examples above demonstrate how to configure and initialize a `GridGroupingControl` in both C# and VB.NET. They include setting properties such as `Dock`, `Name`, `TabIndex`, `VersionInfo`, and `DataSource`. Additionally, they show how to enable IntelliMouse panning, specify visual styles, and handle event-based updates.

## Cross References

See also: `GridGroupingControl`, `TableOptions`, `GridVisualStyles`, `VirtualList`, `Schema`, `EventArgs`.

<!-- tags: [product, module, control, api, version?] keywords: [GridGroupingControl, TableOptions, GridVisualStyles, VirtualList, Schema, EventArgs] -->
```