```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_227.jpeg
document_name: XlsIO
page_number: 227
page_id: XlsIO#page_227
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:03:27Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
[C#]
'Step 1: Instantiate the spreadsheet creation engine
ExcelEngine excelEngine = new ExcelEngine();
'Step 2: Instantiate the excel application object
IApplication application = excelEngine.Excel;
IWorkbook workbook = application.Workbooks.Open(@".../.../Data/Sample.xlsx", ExcelOpenType.Automatic);
IWorksheet sheet = workbook.Worksheets[0];
IChart chart = sheet.Charts[0];
chart.ChartTitle = "Title with a variable font style";
//Rich-text in chart title
//Create a new font with the following properties
IFont redFont = workbook.CreateFont();
redFont.Bold = true;
redFont.Italic = false;
redFont.Size = 18;
redFont.FontName = "Georgia";
redFont.Color = ExcelKnownColors.Red;
//SetFont(int startIndex, int endIndex, IFont font)
IChartRichTextString chartRTS = chart.ChartTitleArea.RichText;
chartRTS.SetFont(0, 12, redFont);
//Rich-Text in data label
//Create another font with the following properties
IFont greenFont = workbook.CreateFont();
greenFont.Bold = true;
greenFont.Italic = false;
greenFont.Size = 17;
greenFont.FontName = "Times New Roman";
greenFont.Color = ExcelKnownColors.Green;
//SetFont(int startIndex, int endIndex, IFont font)
chart.Series[0].DataPoints[0].DataLabels.RichText.SetFont(0, 0, greenFont);
//Create a third font with the following properties
IFont blueFont = workbook.CreateFont();
blueFont.Bold = true;
```
```html
<!-- tags: [syncfusion-sdk, XlsIO, C#, Excel, fonts, fonts styling, rich-text, chart title, data labels] keywords: [fonts, styling, rich-text, chart title, data labels, Excel, C#, fonts properties, text formatting, rich-text, text styling, Excel chart, chart title area, chart data labels, Excel formatting] -->
```