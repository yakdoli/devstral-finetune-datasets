```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_293.jpeg
document_name: XlsIO
page_number: 293
page_id: XlsIO#page_293
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:08:08Z
fidelity: lossless
-->

## 4.2.8.4 Option Button

### Overview
- Essential XlsIO now provides ability to read/write of Option Button control for XLSX format.
- Implementation involves using the `IOptionButtonShape` interface to add an option button to a worksheet.
- Appearance customization is achieved through the `IFill` interface, while border modification is handled via the `IShapeLineFormat` interface.
- Various other text alignment properties are also supported.

### Content

Essential XlsIO now provides support to read/write of Option Button control for **XLSX** format. This can be achieved by using the `IOptionButtonShape` interface which is used to add an option button inside a worksheet. The `IFill` interface is used to customize its appearance. The `IShapeLineFormat` interface is used to modify the border. Various other text alignment properties are also supported.

The following code example illustrates how to read/write an option button control.

```csharp
[C#]

ExcelEngine excelEngine = new ExcelEngine();
IApplication application = excelEngine.Excel;
application.DefaultVersion = ExcelVersion.Excel2007;
IWorkbook workbook = application.Workbooks.Create(1);
IWorksheet sheet = workbook.Worksheets[0];

// Create an Option Button.
IOptionButtonShape optionButton1 = sheet.OptionButtons.AddOptionButton(27, 5);

// Assign a value to the Option Button.
optionButton1.Text = "American Express";

// Format the control.
optionButton1.Fill.FillType = ExcelFillType.SolidColor;
optionButton1.Fill.ForeColor = Color.Yellow;

// Change the check state.
optionButton1.CheckState = ExcelCheckState.Checked;

// Save and close.
workbook.SaveAs("Sample.xlsx");
workbook.Close();
excelEngine.Dispose();

// Load the existing file.
excelEngine = new ExcelEngine();
application = excelEngine.Excel;
workbook = application.Workbooks.Open("Sample.xlsx", ExcelOpenType.Automatic);
sheet = workbook.Worksheets[0];
```

<!-- tags: [Essential XlsIO, Option Button, XLSX format, IOptionButtonShape, IFill, IShapeLineFormat, text alignment properties, code example, Syncfusion Winforms, C#] keywords: [Essential XlsIO, Option Button, XLSX, IOptionButtonShape, IFill, IShapeLineFormat, text alignment, code example, Syncfusion Winforms, C#] -->
```