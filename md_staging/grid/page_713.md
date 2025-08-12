```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_713.jpeg
document_name: grid
page_number: 713
page_id: grid#page_713
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:34:30Z
fidelity: lossless
-->

### Essential Grid for Windows Forms

```csharp
groupDropArea.PrepareViewStyleInfo += new GridPrepareViewStyleInfoEventHandler(ParentTable_PrepareViewStyleInfo);
break;

case "ChildTable":
	groupDropArea.Model.ColCount = 80;
	groupDropArea.PrepareViewStyleInfo += new GridPrepareViewStyleInfoEventHandler(ChildTable_PrepareViewStyleInfo);
	break;
}
```

```vb.net
[VB.NET]

Dim ctl As Control
For Each ctl In Me.gridGroupingControl.GridDropPanel.Controls
	Dim groupDropArea As GridGroupDropArea = ctl
	Select Case groupDropArea.Model.Table.TableDescriptor.Name
		Case "ParentTable"
			groupDropArea.Model.ColCount = 80
			AddHandler groupDropArea.PrepareViewStyleInfo, AddressOf ParentTable_PrepareViewStyleInfo

		Case "ChildTable"
			groupDropArea.Model.ColCount = 80
			AddHandler groupDropArea.PrepareViewStyleInfo, AddressOf ChildTable_PrepareViewStyleInfo
	End Select
Next ctl
```

### Setting the style properties in the PrepareViewStyleInfo event.

```csharp
[C#]

private void ParentTable_PrepareViewStyleInfo(object sender, GridPrepareViewStyleInfoEventArgs e)
{
	// Setting color to the text displaying the table name.
	if (e.ColIndex == 2 && e.RowIndex == 2)
	{
		e.Style.Text = "ParentTable";
		e.Style.Font.Bold = true;
		e.Style.BackColor = Color.YellowGreen;
		e.Style.TextColor = Color.Blue;
		e.Style.CellType = "Static";
		e.Style.HorizontalAlignment = GridHorizontalAlignment.Left;
	}
}
```

<!-- tags: [product, module, control, api, version?] keywords: [Essential Grid, Windows Forms, PrepareViewStyleInfo, GridGroupDropArea, GridGroupingControl, event handler, style properties, GridPrepareViewStyleInfoEventHandler,vb.net], ColCount, ParentTable_PrepareViewStyleInfo, ChildTable_PrepareViewStyleInfo, Color, GridHorizontalAlignment, C#, static cell type -->
```