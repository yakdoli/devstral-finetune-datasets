```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_443.jpeg
document_name: XlsIO
page_number: 443
page_id: XlsIO#page_443
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:17:25Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- You can set a discontinuous range by adding different ranges to the Range collection.
- The example demonstrates how to format text within a cell using the RichText functionality of XlsIO.

## Content

### Setting a Discontinuous Range

You can set a discontinuous range by adding different ranges to the Range collection. The following code example illustrates this.

#### C#

```csharp
// Create Range collection.
IRanges rangesOne = sheet.CreateRangesCollection();

// Add different ranges to the Range collection.
rangesOne.Add(sheet.Range["D2:D3"]);
rangesOne.Add(sheet.Range["D10:D11"]);
```

#### VB.NET

```vb.net
' Create Range collection.
Dim rangesOne As Syncfusion.XlsIO.IRanges = sheet.CreateRangesCollection()

' Add different ranges to the Range collection.
rangesOne.Add(sheet.Range("D2:D3"));
rangesOne.Add(sheet.Range("D10:D11"));
```

### 5.2.3 How to format text within a cell?

The text within a cell can be formatted by using the RichText functionality of XlsIO. The following code example illustrates this.

#### C#

```csharp
// Insert Rich Text.
IRange range = sheet.Range["A1"];
range.Text = "RichText";
IRichTextString rtf = range.RichText;

// Formatting first 4 characters.
IFont redFont = workbook.CreateFont();
redFont.Bold = true;
redFont.Italic = true;
redFont.RGBColor = Color.Red;
rtf.SetFont(0, 3, redFont);

// Formatting last 4 characters.
IFont blueFont = workbook.CreateFont();
```

## API Reference
- **Sheet.CreateRangesCollection()**: Creates a collection of ranges.
- **IRanges.Add(IRange range)**: Adds a range to the collection.
- **IRange.Text**: Sets or gets the text of a cell.
- **IRange.RichText**: Accesses the RichText functionality for formatting text.
- **IRichTextString.SetFont(int start, int length, IFont font)**: Applies a font to a specified range of text.

## Code Examples

- **Discontinuous Range Example**:
  - **C#**: Demonstrates how to create and add ranges to a collection.
  - **VB.NET**: Demonstrates the same functionality in VB.NET.

- **RichText Formatting Example**:
  - **C#**: Demonstrates formatting specific portions of text within a cell using different fonts.

<!-- tags: [Essential XlsIO, Range collection, RichText, Cell formatting] keywords: [discontinuous range, text formatting, IRanges, IRange, RichTextString] -->
```