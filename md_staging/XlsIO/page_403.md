```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_403.jpeg
document_name: XlsIO
page_number: 403
page_id: XlsIO#page_403
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:15:02Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Excel features Freeze Panes to keep certain areas or headings visible while scrolling.
- Freeze Panes can be enabled via the Window menu, making data easier to read.
- XlsIO provides freeze panes support through the `FreezePanes` method of `IRange`.

## Content

### Freeze Panes Feature in Excel

Excel features Freeze Panes to avoid losing visibility of important areas or headers when scrolling. This feature can be enabled by selecting the Freeze option from the Window menu. Once enabled, it allows you to "freeze" certain areas or panes of the spreadsheet, ensuring they remain visible at all times while scrolling to the right or bottom. Headings make it easier to read the data in the spreadsheet.

### XlsIO Support for Freeze Panes

XlsIO provides support for the freeze panes functionality through the `FreezePanes` method of `IRange`. This method allows developers to programmatically set freeze panes in Excel spreadsheets, enhancing the usability and readability of large datasets.

#### Code Examples

##### C#

```csharp
// Applying Freeze Pane to the sheet by specifying a cell.
sheet.Range["B2"].FreezePanes();
```

##### VB.NET

```vb
' Applying Freeze Pane to the sheet by specifying a cell.
sheet.Range("B2").FreezePanes()
```

### Example Screenshot

The following screenshot illustrates the effect of applying freeze panes to a sheet. In this example, the cell `B2` is used to specify the freeze pane, ensuring that the rows above and to the left of this cell remain fixed while scrolling.

![Microsoft Excel - Book1](https://user-images.githubusercontent.com/10437331/20552601.jpg)

### Key Points
- The `FreezePanes` method is triggered by specifying a cell (e.g., `B2`).
- When freeze panes are applied, the rows above and columns to the left of the specified cell remain fixed.
- This feature improves the readability and usability of spreadsheets with large datasets.

<!-- tags: [xlsio, freeze panes, excel, spreadshseets, syncfusion, winforms] keywords: [freeze panes, xlsio, spreadsheet, excel, readability, fixed rows, fixed columns,.freeze option, window menu, programmatic freeze panes, C#, VB.NET] -->
```