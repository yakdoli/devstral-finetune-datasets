```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_410.jpeg
document_name: XlsIO
page_number: 410
page_id: XlsIO#page_410
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:13:54Z
fidelity: lossless
-->

# Essential XlsIO

XlsIO provides an option to hide the workbook tabs by using the `IWorkbook.DisplayWorkbookTabs` property. XlsIO also provides an option to get the current tab that is displayed by using the `DisplayedTab` property of `IWorkbook`.

## Code Examples

[C#]
```csharp
workbook.DisplayWorkbookTabs = false;
```

[VB]
```vb
workbook.DisplayWorkbookTabs = False
```

### 4.7.4 Macros

XlsIO supports the usage of Macros in the Template file. A macro is created by using the MS Excel GUI, and then saved. The spreadsheet is then opened by using XlsIO, and saved to retain the macro.

1. Create a macro by using MS Excel and save the file.
2. Open the saved file with XlsIO.
3. XlsIO preserves the macro during the Save process.

<!-- tags: [XlsIO, macros, workbook tabs, IWorkbook.DisplayWorkbookTabs, IWorkbook.DisplayedTab] keywords: [XlsIO, macros, workbook tabs, IWorkbook.DisplayWorkbookTabs, IWorkbook.DisplayedTab, Syncfusion Winforms, Excel, save process] -->
```