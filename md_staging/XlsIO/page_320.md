```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_320.jpeg
document_name: XlsIO
page_number: 320
page_id: XlsIO#page_320
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:10:42Z
fidelity: lossless
-->

# Essential XlsIO

## Navigation and Headers

Row and column headings are the row numbers and the column letters. Checking the box enables them to print in MS Excel. XlsIO has the option to enable/disable headings through the **PrintHeadings** property of IPageSetup. Remember, headings are not the same as the labels created.

## Color

Excel allows setting the colors for printing. You can print a sheet without colors by using the **BlackAndWhite** property of the **IPageSetup** interface in XlsIO.

## Quality

Excel provides options to toggle the quality by using the "DraftQuality" option. Draft quality is a fast, but not a crisp print quality. XlsIO allows to enable this option through the **Draft** property of the IPageSetup interface. You can also set the print quality that controls the dpi by using the **PrintQuality** property.

## Comments

Comments are little notes that you can attach to cells. They can be printed all together at the end of the sheet, or within the sheet, or not at all. This can be set through XlsIO by using the **PrintNotes** property.

## Page Order

Excel allows to set the page order in which the sections of a worksheet should be printed, when it does not fit on one paper page. The default option is **DownThenOver**. The other option, **OverThenDown**, prints the cells across the top of the sheet, first, and then moves down to print the next set of rows.

XlsIO allows to set the print direction as illustrated in the following code example.

### Code Example

```csharp
[C#]
// Set direction of printing.
workbook.Worksheets[0].PageSetup.Order = ExcelOrder.DownThenOver;
```

```vb.net
[VB.NET]
```

## API Reference

### Properties
- **PrintHeadings**: Enables or disables row and column headings in print output.
- **BlackAndWhite**: Allows printing a sheet without colors.
- **Draft**: Enables draft-quality printing.
- **PrintQuality**: Controls the dpi of the print quality.
- **PrintNotes**: Controls the printing of comments.

### Methods
No specific methods are documented in this excerpt.

## Code Examples

See the provided C# example to set the print order direction.

## Cross References

See also:
- [Working with Print Settings](#working-with-print-settings)

<!-- tags: XlsIO, Excel, Print Settings, Page Setup, PrintHeadings, PrintQuality, PrintNotes, Page Order -->
```