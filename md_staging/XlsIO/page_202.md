```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_202.jpeg
document_name: XlsIO
page_number: 202
page_id: XlsIO#page_202
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:00:44Z
fidelity: lossless
-->

# Essential XlsIO

Essential XlsIO can convert a worksheet based on the input range of the rows and columns which does not support the following elements:

- Subscript/Superscript
- RTF
- Shrink to fit
- Shapes (except TextBox shape and Image)
- Charts and Chart Worksheet
- Complex conditional formatting
- Gradient fill is partially supported

## Sheet Format

Excel provides various options to format a sheet. This includes setting the tab color, naming sheets, and clearing the data in the sheet. This section demonstrates how these formats can be applied to the worksheets in XlsIO.

![](https://i.imgur.com/74w.png)

Figure 70: Menu for formatting a Sheet

### Worksheet Formatting in XlsIO

#### Sheet Naming

Sheets can be named/renamed to find out the sheet or provide a hint on the data in the sheet, in a large workbook that has a number of worksheets. You can name a worksheet by using the IWorksheet.Name property.

```csharp
[C#]

sheet.Name = "Result";
```

### API References

- **Namespace:** Syncfusion.XlsIO
- **Class:** Workbook
  - **Property:** IWorksheet.Name

### Code Examples

```csharp
// C# Example
IWorksheet sheet = workbook.Worksheets["Sheet1"];
sheet.Name = "Result";
```

<!-- tags: [syncfusion, essentialxlsio, sheetformatting, worksheetname, winforms, xlsio, 11.4.0.26] keywords: [Essential XlsIO, worksheet formatting, sheet naming, workbook, IWorksheet.Name, C# code example, Excel sheet formatting, tab color, sheet properties, data clearing, chart worksheet, complex conditional formatting, gradient fill, sheet menu, figure 70, Windows Forms, Syncfusion] -->
``` 
