```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_182.jpeg
document_name: XlsIO
page_number: 182
page_id: XlsIO#page_182
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:59:27Z
fidelity: lossless
-->

## Customizing Cell Dimensions in XlsIO

This section discusses ways to customize the cell width and height according to user needs. There are two methods to adjust cell size:

### Methods to Change Cell Size

- **Manual Adjustment:** Changing the row height and column width manually, with the values specified.
- **Automatic Adjustment:** Changing the row height and column width automatically, to fit the text into the cell.

This is discussed in the following topics.

### 4.1.3.3.1.1 Row Height and Column Width

**MS Excel:**
MS Excel allows setting the row height and column width using the **Format** menu option. Go to the **Format** menu, click **Row/Column**, and then click **Height/Width** option.

![Row Height and Column Width dialog boxes in Excel](https://i.imgur.com/4i8Bqkr.png)
*Figure 61: Row Height and Column Width dialog boxes in Excel*

#### Specifying Row Height and Column Width in XlsIO

**Column Width:**
XlsIO allows specifying a column width of 0 to 255 in a spreadsheet. This value represents the number of characters that can be displayed in a cell formatted with the standard font. The default column width is 8.43 characters, which is the default value of MS Excel. If a column has a width of 0, it is hidden.

**Row Height:**
Similarly, you can specify a row height of 0 to 409. Note that this is the restriction of MS Excel. This value represents the height measurement in points (1 point equals approximately 1/72 inch or \(0.035 \, \text{cm}\)). The default row height is 12.75 points. If a row has a height of 0, the row is hidden.

XlsIO provides support for setting the **RowHeight** and **ColumnWidth** properties in a worksheet. You can also set the column width and row height in pixels using the **IWorksheet.SetColumnWidthInPixel** and **IWorksheet.SetRowHeightInPixel** methods respectively.

### Code Example

```csharp
// Changing the Column Width.
sheet.Range["A1"].ColumnWidth = 20;
```
```html

<!-- tags: [XlsIO, cell dimensions, row height, column width, manual adjustment, automatic adjustment, MS Excel, Syncfusion Winforms] keywords: [customizing cell size, row height, column width, manual adjustment, automatic adjustment, worksheet properties, C# example, IWorksheet interface] -->
```