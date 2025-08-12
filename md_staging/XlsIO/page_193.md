```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_193.jpeg
document_name: XlsIO
page_number: 193
page_id: XlsIO#page_193
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:01:21Z
fidelity: lossless
-->

## Overview

- Demonstrates how to hide a worksheet using the `Visibility` property.
- Explains hiding all tabs in a workbook using the `DisplayWorkbookTabs` option.
- Highlights the ability to activate a specific worksheet on opening using the `Activate` method.

## Content

### Hiding Worksheets

To hide a specific worksheet, you can use the `Visibility` property as shown below:

```csharp
sheet.Visibility = WorksheetVisibility.Hidden;
```

This code snippet hides the specified worksheet. The effect is illustrated in **Figure 68: Hidden Worksheet**.

![Figure 68: Hidden Worksheet](Sheet2Hidden.png)

### Hiding All Tabs

You can also hide all tabs in the worksheet by using the `DisplayWorkbookTabs` option in the `IWorkbook` interface. This feature is particularly useful for managing large workbooks where you want to minimize visual clutter and improve navigation.

### Activating a Worksheet

XlsIO provides an option to activate a worksheet while opening it in the workbook, equivalent to clicking on a worksheet in MS Excel. This is achieved using the `Activate` method:

#### C#

```csharp
sheet.Activate();
```

#### VB.NET

```vb
sheet.Activate()
```

When the workbook is opened, the specified worksheet will be the active one, simplifying user interaction.

## API Reference

### Methods and Properties

- **Visibility Property**
  - Type: `WorksheetVisibility`
  - Possible values: `Hidden`, `Visible`
  - Use to set the visibility state of a worksheet.

- **Activate Method**
  - Activates the specified worksheet upon opening the workbook.

## Code Examples

### Hiding a Worksheet

#### C#

```csharp
IWorksheet sheet = workbook.Worksheets["Sheet2"];
sheet.Visibility = WorksheetVisibility.Hidden;
```

### Activating a Worksheet

#### C#

```csharp
IWorksheet sheet = workbook.Worksheets["Sheet1"];
sheet.Activate();
```

## See also

- [Workbook Tabs Visibility](#workbook-tabs-visibility)
- [Opening and Activating Worksheets](#opening-and-activating-worksheets)

<!-- tags: [XlsIO, worksheet visibility, hiding tabs, worksheet activation] keywords: [SheetVisibility.Hidden, DisplayWorkbookTabs, Activate, C#, VB.NET, workbooks, tabs, navigation] -->
```