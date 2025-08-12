```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_865.jpeg
document_name: grid
page_number: 865
page_id: grid#page_865
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:45:03Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

A demo of this feature is available in the following location:

```
..\\AppData\\Local\\Syncfusion\\EssentialStudio\\{Version}\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Appearance\\FormatCells Dialog Demo
```

## Adding GridFormatCellDialog To The GridGroupingControl

You can add the cell formatting dialog using the `GridFormatCellDialog` class. To add the `GridFormatCellDialog`, pass the `GridGroupingControl` as a parameter of the `GroupingGridFormatCellDialog()` method.

The following code illustrates this:

```csharp
[C#]

GroupingGridFormatCellDialog Dialog = new GroupingGridFormatCellDialog(this.gridGroupingControl1);
Dialog.ShowDialog();
```

```vb
[VB]

Dim Dialog As GroupingGridFormatCellDialog = New GroupingGridFormatCellDialog(Me.gridGroupingControl1)
Dialog.ShowDialog()
```

<!-- tags: [product, windows assemblies, grid, gridgroupingcontrol, gridformatcelldialog, appearance, cellformat] keywords: [gridgroupingcontrol, gridformatcelldialog, cell formatting, appearance, feature demo] -->
```