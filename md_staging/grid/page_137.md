```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_137.jpeg
document_name: grid
page_number: 137
page_id: grid#page_137
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:47:59Z
fidelity: lossless
-->


## Essential Grid for Windows Forms

### Creating and Configuring the Essential Grid

#### C#

```csharp
// Create the Essential Grid.
private Syncfusion.Windows.Forms.Grid.GridControl gridControl;
....
this.gridControl1 = new Syncfusion.Windows.Forms.Grid.GridControl();

// Set the number of rows and columns.
this.gridControl1.ColCount = 10;
this.gridControl1.RowCount = 100;

// Position it on the form.
this.gridControl1.Location = new System.Drawing.Point(20, 20);
this.gridControl1.Size = new System.Drawing.Size(344, 200);

// Add it to the form's controls.
this.Controls.Add(this.gridControl1);
```

#### VB.NET

```vbnet
' Create the Essential Grid.
Private WithEvents gridControl1 As GridControl
....
Me.gridControl1 = New Syncfusion.Windows.Forms.Grid.GridControl()

' Set the number of rows and columns.
Me.gridControl1.ColCount = 10
Me.gridControl1.RowCount = 100

' Position it on the form.
Me.gridControl1.Location = New System.Drawing.Point(20, 15)
Me.gridControl1.Size = New System.Drawing.Size(344, 150)

' Add it to the form's controls.
Me.Controls.Add(Me.gridControl1)
```

---

## See Also

- [Through Designer](#)

<!-- tags: [windows-forms, grid, essential-grid] keywords: [syncfusion, c#, vb.net, grid control, rows, columns, location, size, designer] -->
``` 
