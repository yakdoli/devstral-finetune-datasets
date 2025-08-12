```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_079.jpeg
document_name: QTP
page_number: 079
page_id: QTP#page_079
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:23Z
fidelity: lossless
-->

# Essential QuickTest Professional

```csharp
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCellData 1,2,"435.00"
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCurrentCell 2,1
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCellCheckBox 2,1,"ON"
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCurrentCell 3,1
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCellCheckBox 3,1,"OFF"
```

If the mapping points to the wrong version, then no scripts will be generated. The right version would be the same version as the AUT developed. For an example, if the AUT is developed in 7.3.0.20, the custom libraries (DLLs) should also be developed in 7.3.0.20. This means that Essential QuickTest Professional version 7.3.0.20 is required. With proper versions and proper mapping, the record will appear as shown in the script below:

```csharp
[QTP]
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCurrentCell 1,2
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCellData 1,2,"435.00"
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCurrentCell 2,1
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCellCheckBox 2,1,"ON"
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCurrentCell 3,1
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCellCheckBox 3,1,"OFF"
```

In the above scripts, `SetCurrentCell`, `SetCellData`, and `SetCellCheckBox` are the methods of Grid control.

> For the list of methods that will be recorded for all the supported controls, refer to the Supported Controls topic. You can also visit our Knowledge Base for Essential QuickTest Professional at the following link for more details: [http://www.syncfusion.com/support/kb/tag/QTP](http://www.syncfusion.com/support/kb/tag/QTP)

## 7.2 Essential Grid

<!-- tags: [winforms, essential quicktest professional, grid, dll, aut, testing] keywords: [Essential QuickTest, GridDataBoundGrid, SetCellData, SetCurrentCell, SetCellCheckBox, AUT, version, Syncfusion, WinForms] -->
```