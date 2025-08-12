```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_167.jpeg
document_name: XlsIO
page_number: 167
page_id: XlsIO#page_167
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:00Z
fidelity: lossless
-->

Essential XlsIO

```vbnet
' Clearing a Range and its formatting.
sheet.Range("A4").Clear(True)
```

## Getting Used Range

XlsIO enables to get the range of cells used in a given sheet. This will help the user to apply the same format to all the cells used in the worksheet. You can also get the first row/column, last row/column, and number of rows/columns used in the sheet, by using the various methods of IRange.

---

**Note:** By default, XlsIO considers a cell as used, even if there exists some formatting. You can disable this behavior, and make XlsIO consider a cell as used, only when there exists data, by using the UsedRangeIncludesFormatting property.

---

Following code example is used to format the Used Range.

```csharp
// Modifying only the Used Ranges.
sheet.UsedRange.ColumnWidth = 20;
sheet.UsedRange.RowHeight = 20;
```

```vbnet
' Modifying only the Used Ranges.
sheet.UsedRange.ColumnWidth = 20
sheet.UsedRange.RowHeight = 20
```

### 4.1.2.2 Find and Replace

Find and Replace feature in Excel enables to navigate between large spreadsheets. It carries out a simultaneous search in Microsoft Excel values, formulas, and also comments.

XlsIO also has support for finding and replacing contents in a worksheet. It has various options to find the first matching entry, find all the matching entries, and replace the found content with various data and data sources.

## API Reference (if applicable)
- Namespace: `Syncfusion.XlsIO`
- Class: `IWorkbook`
- Members (Methods/Properties/Events/Enums):
  - `UsedRange`: Gets an `IRange` object representing the used range of cells in the worksheet.
  - `Clear(Boolean clearFormatting)`: Clears the content and optionally the formatting of a range.

## Code Examples (multi-language supported)
- **Clearing a range:**
  ```csharp
  sheet.Range("A4").Clear(true);
  ```
- **Setting Used Range properties:**
  ```csharp
  sheet.UsedRange.ColumnWidth = 20;
  sheet.UsedRange.RowHeight = 20;
  ```
- **Finding and replacing text:**
  ```csharp
  // Find and replace all occurrences of "oldText" with "newText".
  sheet.FindOptions.Find("oldText").Replace("newText", Syncfusion.XlsIO.XlsFindReplaceOptions.ReplaceAll);
  ```

## Cross References
- See also:
  - [XlsIO - Getting Started](#getting-started)
  - [Range Operations](#range-operations)
  - [Data Manipulation](#data-manipulation)

## RAG Annotations
<!-- tags: [xlsio, winforms, find-and-replace, range-operations] keywords: [cell used range, format, row height, column width, usedrange, clear, find, replace] -->
```