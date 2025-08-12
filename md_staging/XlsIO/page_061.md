```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: XlsIO
page_number: 061
page_id: XlsIO#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:52:23Z
fidelity: lossless
-->

## Overview
- Demonstrates various formatting options in Excel, focusing on font, border, alignment, fill, and number formatting.
- Explains range manipulations, including copying and moving ranges, as part of the editing functionality in *Essential XlsIO*.
- Mentions the availability of Find and Replace options for text searches.

## Content

### Formatting Options in Excel

#### Figure 25: Various Formatting options

This figure illustrates different formatting options available in Microsoft Excel. The image is divided into sections highlighting various formatting aspects:

1. **Font Settings**:
   - Displays examples of text formatting with varying font styles, sizes, and colors.
   - Highlights the application of bold, italic, and underlined styles to "Hello World."

2. **Border Settings**:
   - Shows different border styles applied to cells, including solid, dashed, and double lines.
   - Demonstrates the customization of border thickness and styles for enhanced visual presentation.

3. **Alignment Settings**:
   - Demonstrates text alignment options such as horizontal and vertical alignment.
   - Includes examples of rotated text and text alignment in different sections of a cell.

4. **Fill Settings**:
   - Illustrates the capability to apply background colors and patterns to cells for enhanced visual effects.

5. **Number Format**:
   - Displays formatted numbers in columns, showcasing how numbers can be displayed in currency, percentage, and scientific notation formats.

#### Editing Features

- **Essential XlsIO** supports range manipulations such as copying, moving, and various editing actions like Find and Replace.
- The richness of editing functionalities is emphasized, indicating comprehensive document manipulation capabilities.

#### Find and Replace Dialog Box

- The text mentions that the following screenshot will show the Find and Replace dialog box.
- This suggests a practical demonstration of finding and replacing text within the Excel document.

## API Reference

While no specific API details are shown in the image, the content implies the use of Syncfusion's XlsIO library for managing and formatting Excel documents. Users leveraging this functionality should refer to the library's API documentation for detailed implementation guidance.

## Code Examples

The image does not include actual code examples, but given the context of formatting and range manipulation:

```csharp
// Example of copying a range
using (var workbook = new Workbook())
{
    IWorksheet sheet = workbook.Worksheets[0];
    sheet.Range["A1:B5"].Copy();
}
```

See also: [Further code examples and API details in the XlsIO library documentation](#)

## RAG Annotations
<!-- tags: [XlsIO, Excel, formatting, range manipulation, Syncfusion, Winforms] keywords: [Essential XlsIO, font settings, border settings, alignment, fill settings, number format, find and replace, range manipulations] -->
```