```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_306.jpeg
document_name: XlsIO
page_number: 306
page_id: XlsIO#page_306
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:07:34Z
fidelity: lossless
-->

## 4.3.1 Page Setup

In MS Excel, the way the spreadsheet fits onto paper can be controlled through the **Page Setup** dialog box. You can select the size and orientation of the paper, the width of the margins, what goes into the header and footer of each page, and the order of printing cells for sheets that will take several pieces of paper.

**Note:** Though the sample code uses sheet object, it is possible to read/write page setup options for chart worksheet and embedded chart using `IChartPageSetup` interface.

There may also be a need to change the first page number, which starts with '1', by default. This can be done through the page number customization options provided by the Page Setup dialog box.

### Example Code: Changing the First Page Number

#### C#

```csharp
sheet.PageSetup.AutoFirstPageNumber = false;
sheet.PageSetup.FirstPageNumber = 2;
```

#### VB.NET

```vb
sheet.PageSetup.AutoFirstPageNumber = false
sheet.PageSetup.FirstPageNumber = 2;
```

Following topics explain how various other page setup options can be set by using XlsIO.

### 4.3.1.1 Margins

Page margins are the blank spaces between the worksheet data and the edges of the printed page, and hence provide better readability. Page margins can be used for items such as headers, footers and page numbers.

Excel allows to set the page margin through the Page Setup dialog box. Note that the page margins that you define in a given worksheet, are stored with that particular worksheet, when you save the workbook. You cannot change the default page margins for new workbooks.
```


<!-- tags: [product, module, control, api, version?] keywords: [page setup, page margins, header, footer, first page number, chart worksheet, embedded chart, XlsIO, Syncfusion Winforms, Excel, paper orientation, margin customization] -->
```