```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_351.jpeg
document_name: XlsIO
page_number: 351
page_id: XlsIO#page_351
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:11:51Z
fidelity: lossless
-->

## AutoFilters in Essential XlsIO

**Essential XlsIO also comes with APIs for reading and writing AutoFilters in a worksheet.** You can specify the range of data that needs to be viewed through the `FilterRange` property. Following code example illustrates writing AutoFilters.

### Code Examples

```csharp
[C#]

// Creating an AutoFilter in the first worksheet. Specifying the AutoFilter range.
sheet.AutoFilters.FilterRange = sheet.Range["A1:B7"];
```

```vbnet
[VB.NET]

' Creating an AutoFilter in the first worksheet. Specifying the AutoFilter range.
sheet.AutoFilters.FilterRange = sheet.Range("A1:B7")
```

**XlsIO also provides options to set the built-in conditions for filters by using various properties of IAutoFilter.** Following code example illustrates various conditions based on which data can be filtered.

```csharp
[C#]

IAutoFilter filter = sheet1.AutoFilters[0];
filter.IsTop = true;
filter.IsTop10 = true;
filter.Top10Number = 5;
```

```vbnet
[VB.NET]

Dim filter As IAutoFilter = sheet1.AutoFilters(0)
```

## API Reference

- **Namespace:** Essential XlsIO
- **Class:** AutoFilters
- **Properties:**
  - `FilterRange`: Specifies the range for AutoFilter.
  - `IAutoFilter.IsTop`: Indicates whether the filter should display top-filtered data.
  - `IAutoFilter.IsTop10`: Indicates whether the filter should display top 10 filtered data.
  - `IAutoFilter.Top10Number`: Specifies the number for top 10 filtering.

<!-- tags: [product, module, control, api, version?] keywords: [Essential XlsIO, AutoFilters, FilterRange, IAutoFilter, IsTop, IsTop10, Top10Number, data filtering, worksheet, built-in conditions, API example, see also: Conditional Formatting, Data Validation] -->
```