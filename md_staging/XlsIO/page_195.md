```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_195.jpeg
document_name: XlsIO
page_number: 195
page_id: XlsIO#page_195
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:01:03Z
fidelity: lossless
-->

## Content

### Hiding and Unhiding Columns and Rows in a Worksheet

This section demonstrates how to hide and unhide specific columns and rows in a worksheet using VB.NET. The code snippets provided illustrate various methods to manipulate visibility settings.

#### Example Code

```vb
' Hiding the First Column and Second Row.
sheet.ShowColumn(1, False)
sheet.ShowRow(2, False)

' Hiding the Fifth Column and Fifth Row.
sheet.ShowColumn(5, False)
sheet.ShowRow(5, False)

' Unhiding the Fifth Column and Second Row.
sheet.ShowColumn(5, True)
sheet.ShowRow(2, True)

IRange range = sheet[1, 4];
// Hiding the first to third row and first to third column
sheet.ShowRange(range, false);

IRange firstRange = ws[1, 1, 3, 3];
IRange secondRange = ws[5, 5, 7, 7];
RangesCollection rangeCollection = new RangesCollection(app, ws);
rangeCollection.Add(firstRange);
rangeCollection.Add(secondRange);
// Hiding the collection of ranges
ws.ShowRange(rangeCollection, false);
```

### Methods for Manipulating Range Visibility

The following table describes the methods available for showing or hiding specific ranges in a worksheet.

| Prototype                                      | Description                       |
|-----------------------------------------------|-----------------------------------|
| ShowRange (IRange, bool)                     | Shows or hides a particular range. |
| ShowRange(IRange[], bool)                    | Shows or hides a particular array of ranges. |
| ShowRange(RangesCollection, bool)            | Shows or hides a particular collection of ranges. |

### Summary

This page explains how to programmatically hide and unhide specific columns and rows in a worksheet using the `ShowColumn` and `ShowRow` methods. Additionally, it demonstrates how to manage the visibility of specific ranges using the `ShowRange` method with various parameters.

### See also
- [Range Visibility Management Documentation](#)
- [IRange Type Documentation](#)
- [RangesCollection Documentation](#)

<!-- tags: [XlsIO, worksheet, range visibility,VB.NET,hide row,hide column] keywords: [hide,unhide,sheet,range visibility,IRange,RangesCollection,worksheet,VB.NET] -->
```