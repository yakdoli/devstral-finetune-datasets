<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_294.jpeg
document_name: XlsIO
page_number: 294
page_id: XlsIO#page_294
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:07:01Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
// Read an Option Button.
IOptionButtonShape optionButton2 = sheet.OptionButtons[0];
optionButton2.CheckState = ExcelCheckState.Unchecked;

workbook.SaveAs("Unchecked.xlsx");
workbook.Close();
excelEngine.Dispose();
```

## VB.NET

```vb
Dim excelEngine As New ExcelEngine()
Dim application As IApplication = excelEngine.Excel
application.DefaultVersion = ExcelVersion.Excel2007
Dim workbook As IWorkbook = application.Workbooks.Create(1)
Dim sheet As IWorksheet = workbook.Worksheets(0)

' Create an Option Button.
Dim optionButton1 As IOptionButtonShape = sheet.OptionButtons.AddOptionButton(27, 5)

' Assign a value to the Option Button.
optionButton1.Text = "American Express"

' Format the control.
optionButton1.Fill.FillType = ExcelFillType.SolidColor
optionButton1.Fill.ForeColor = Color.Yellow

' Change the check state.
optionButton1.CheckState = ExcelCheckState.Checked

' Save and close.
workbook.SaveAs("Sample.xlsx")
workbook.Close()
excelEngine.Dispose()

' Load the existing file.
excelEngine = New ExcelEngine()
application = excelEngine.Excel
workbook = application.Workbooks.Open("Sample.xlsx", ExcelOpenType.Automatic)
sheet = workbook.Worksheets(0)

' Read an Option Button.
Dim optionButton2 As IOptionButtonShape = sheet.OptionButtons(0)
```

## References

- **See also:** [Syncfusion XlsIO Documentation](https://help.syncfusion.com/xlsio/overview)

<!-- tags: [syncfusion, winforms, xlsio, option button, check state, format control] keywords: [syncfusion winforms, xlsio, option button, check state, format control, vb.net, csharp, excel engine, workbook, worksheet, open, save] -->