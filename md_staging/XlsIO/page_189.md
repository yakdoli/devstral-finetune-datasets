```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_189.jpeg
document_name: XlsIO
page_number: 189
page_id: XlsIO#page_189
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:01:07Z
fidelity: lossless
-->

## Autofit and Cell Visibility in XlsIO

### Overview
- Discusses how the `AutoFit` functionality works in XlsIO, particularly with respect to cell text and row height.
- Highlights specific conditions under which `AutoFit` is not applied, such as cells with text wrapping or merged cells.
- Explains methods to manage cell visibility, including hiding and unhiding rows and columns using commands and properties.

### Content

#### Autofit Usage in XlsIO

Here, though the cell "B2" has long text, `AutoFit` will not be applied to this column as the cell inside the range [5, 2, 19, 2] has text smaller than that. Similarly, the row height for Row 15 will not be affected with `AutoFit` rows, as the range [5, 2, 13, 4] has a row height smaller than Row 15.

**Note:**
1. If a `Range` text is text wrapped, `AutoFitColumn` method will not be applied on it.
2. If a `Range` is merged, `AutoFit` methods will not be applied on it. Note that this is the behavior of MS Word.
3. Implementation of `AutoFit` methods are more time-consuming. Use these methods in minimal for better performance.

#### 4.1.3.3.2 Cell Visibility

- **Controlling Cell Visibility:** One of the most useful features in MS Excel is the ability to show/hide rows and columns according to the user's needs, producing readable content in large data worksheets.
  
  Following section explains the support provided by XlsIO to hide/unhide sheets and rows/columns.

##### 4.1.3.3.2.1 Hide/Unhide Rows and Columns

Excel allows to hide a row/column by using the `Hide` command, but a row or column also becomes hidden when you change its row height or column width to zero. Also, you can show a hidden row/column by using the `Unhide` command.

## RAG Annotations

<!-- tags: [XlsIO, Syncfusion Winforms, Autofit, Cell Visibility, Hide/Unhide, MS Excel] keywords: [AutoFitColumn, AutoFit, text wrapping, merged cells, time-consuming, rows, columns, row height, column width, reading content, large data, readability, user needs, show/hide, Unhide command] -->
```