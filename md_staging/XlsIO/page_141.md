```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_141.jpeg
document_name: XlsIO
page_number: 141
page_id: XlsIO#page_141
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:57:56Z
fidelity: lossless
-->

## XlsIO: Applying Global Styles

### Overview
- Demonstrates how to apply global styles to an Excel worksheet using XlsIO.
- Highlights the use of body and header styles with thin borders and a defined color palette.

### Content

#### Setting Global Styles

Below is the code snippet demonstrating how to apply global styles to an Excel worksheet:

```csharp
workbook.SetPaletteColor(9, Color.FromArgb(239, 243, 247));
bodyStyle.Color = Color.FromArgb(239, 243, 247);
bodyStyle.Borders(ExcelBordersIndex.EdgeLeft).LineStyle = ExcelLineStyle.Thin;
bodyStyle.Borders(ExcelBordersIndex.EdgeRight).LineStyle = ExcelLineStyle.Thin;
bodyStyle.EndUpdate();

' Apply the defined styles.
' Apply Body Style.
sheet.UsedRange.CellStyleName = "BodyStyle"

' Apply Header style.
sheet.Rows[0].CellStyleName = "HeaderStyle"
```

#### Explanation of Code
- `workbook.SetPaletteColor(9, Color.FromArgb(239, 243, 247))`: Sets the color palette for the workbook.
- `bodyStyle.Color = Color.FromArgb(239, 243, 247)`: Applies a specific color to the body style.
- `bodyStyle.Borders(ExcelBordersIndex.EdgeLeft).LineStyle = ExcelLineStyle.Thin`: Configures thin borders for the left edge of the body style.
- `bodyStyle.Borders(ExcelBordersIndex.EdgeRight).LineStyle = ExcelLineStyle.Thin`: Configures thin borders for the right edge of the body style.
- `bodyStyle.EndUpdate()`: Completes the update of the body style.
- `sheet.UsedRange.CellStyleName = "BodyStyle"`: Applies the defined body style to the entire used range of the sheet.
- `sheet.Rows[0].CellStyleName = "HeaderStyle"`: Applies a header style to the first row of the sheet.

#### Output

The following image shows the result of applying global styles to an Excel worksheet:

![XlsIO with Global Styles](https://i.imgur.com/example_image.png)

**Figure 45: XlsIO with Global Styles**

### For More Information Refer:
- For additional details, refer to the Syncfusion documentation.

### API Reference
- `ExcelWorkbook.SetPaletteColor(int index, Color color)`: Sets a color in the workbook's palette.
- `ExcelRangeCellStyle.Color`: Sets the background color for a cell or range.
- `ExcelRangeCellStyle.Borders(ExcelBordersIndex borderIndex).LineStyle = ExcelLineStyle`: Configures the line style for specified borders.
- `ExcelRange.EndUpdate()`: Ends updates to an Excel range.
- `ExcelRange.UsedRange`: Represents the used range of a worksheet.
- `ExcelRange.CellStyleName`: Sets or gets the cell style name for a range.
- `ExcelSheet.Rows[int rowNumber].CellStyleName`: Sets or gets the cell style name for a specific row.

### Code Examples

The following code example demonstrates applying styles to an Excel worksheet:

```csharp
using (ExcelEngine excelEngine = new ExcelEngine())
{
    IWorkbook workbook = excelEngine.Excel.Workbooks.Create(1);
    IWorksheet sheet = workbook.Worksheets[0];

    // Set palette color
    workbook.SetPaletteColor(9, Color.FromArgb(239, 243, 247));

    // Define body style
    IStyle bodyStyle = workbook.Styles.Add("BodyStyle");
    bodyStyle.Color = Color.FromArgb(239, 243, 247);
    bodyStyle.Borders(ExcelBordersIndex.EdgeLeft).LineStyle = ExcelLineStyle.Thin;
    bodyStyle.Borders(ExcelBordersIndex.EdgeRight).LineStyle = ExcelLineStyle.Thin;
    bodyStyle.EndUpdate();

    // Define header style
    IStyle headerStyle = workbook.Styles.Add("HeaderStyle");
    headerStyle.Font.Bold = true;
    headerStyle.Borders(ExcelBordersIndex.EdgeTop).LineStyle = ExcelLineStyle.Thin;

    // Apply styles
   (sheet.UsedRange.CellStyleName = "BodyStyle");
    sheet.Rows[0].CellStyleName = "HeaderStyle";

    // Save and close
    workbook.SaveAs("Sample.xls");
    workbook.Close();
}
```

### Cross References
- See also:
  - Excel Styles
  - Workbook Palette
  - Range and Cell Styling

<!-- tags: XlsIO, Excel, Styles, Workbook, Range, CellStyle, Palette colors, Thin borders, Header styles, Body styles, Global styles keywords: Excel, Styles, CellStyle, Palette, Thin borders, Header style, Body style, Global styles -->
```