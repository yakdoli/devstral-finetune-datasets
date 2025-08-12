```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_212.jpeg
document_name: grid
page_number: 212
page_id: grid#page_212
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:03:13Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## 4.1.4.4.5 Date Time Picker

The Date Time Picker cell type can be embedded into a cell as a drop-down container, where the date and time picker will be added in the drop-down. The cell value of the corresponding cell has to be specified as date value. Various formats of the date and time can be provided in the Format style property.

The following code examples illustrate how to set the cell type to DateTimePicker.

### Using C#

```csharp
RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.DateTimePicker);
this.gridControl1[4, 2].CellType = CustomCellTypes.DateTimePicker.ToString();
this.gridControl1[4, 2].CellValueType = typeof(DateTime);
this.gridControl1[4, 2].CellValue = DateTime.Now;
this.gridControl1[4, 2].Format = "MM/dd/yyyy hh:mm";
```

### Using VB.NET

```vb
RegisterCellModel.GridCellType(Me.gridControl1, CustomCellTypes.DateTimePicker)
Me.gridControl1(4, 2).CellType = CustomCellTypes.DateTimePicker.ToString()
Me.gridControl1(4, 2).CellValueType = GetType(DateTime)
Me.gridControl1(4, 2).CellValue = DateTime.Now
Me.gridControl1(4, 2).Format = "MM/dd/yyyy hh:mm"
```

![Date Picker](attachment:DatePickerImage.png)

*Figure: DateTime Picker Example*

<!-- tags: [Syncfusion Winforms, Grid, DateTimePicker, Control, CellType] keywords: [cell type, date time picker, drop-down, format, cell value, custom cell types, date picker, Grid, code examples, DateTime, C#, VB.NET] -->
```