```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_122.jpeg
document_name: grid
page_number: 122
page_id: grid#page_122
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:39:41Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Essential Grid is a powerful data grid control for Windows Forms applications.
- Demonstrates how to export data from grid controls to Excel files.
- Covers accessibility information for Grid Windows Forms.

## Content

```csharp
proc.Start();
}
}
```

### [VB.NET]
```vbnet
Dim engine As New ExcelEngine()
Dim app As IApplication = engine.Excel.Application
app.DefaultVersion = ExcelVersion.Excel2010
Dim book As IWorkbook = app.Workbooks.Create()
Dim gecc As New GroupingGridExcelConverterControl()
Dim saveFileDialog As New SaveFileDialog()
saveFileDialog.Filter = "Files(*.xlsx)|*.xlsx"
saveFileDialog.DefaultExt = ".xlsx"
If saveFileDialog.ShowDialog() = System.Windows.Forms.DialogResult.OK Then
    gecc.GroupingGridToExcel(Me.gridGroupingControl1, book.Worksheets(0), ConverterOptions.Visible)
    book.SaveAs(saveFileDialog.FileName)
    If MessageBox.Show("Do you wish to open the xls file now?", "Export to Excel", MessageBoxButtons.YesNo, MessageBoxIcon.Question) = System.Windows.Forms.DialogResult.Yes Then
        Dim proc As New Process()
        proc.StartInfo.FileName = saveFileDialog.FileName
        proc.Start()
    End If
End If
```

### Note: This is applicable to all Grid controls in Essential Grid.

### 3.1.7 Lesson 6: Accessibility Information for Grid Windows Forms

#### Technical Standards
- Software Applications and Operating Systems – Detail Voluntary Product Accessibility Template

## API Reference (if applicable)
- This section references the packaged APIs used for accessibility in Grid Windows Forms.

## Code Examples (multi-language supported)
- The above code examples demonstrate exporting data from grid controls to Excel files in both C# and VB.NET.

## Cross References
- For more information on technical standards related to accessibility, refer to "Software Applications and Operating Systems – Detail Voluntary Product Accessibility Template."

## RAG Annotations
<!-- tags: [grid, windows forms, accessibility, excel export, technical standards] keywords: [grid export, Windows Forms, accessibility standards, Excel conversion] -->
```