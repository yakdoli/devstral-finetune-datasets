```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_343.jpeg
document_name: XlsIO
page_number: 343
page_id: XlsIO#page_343
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:11:18Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Describes the process of inserting defined names using the Insert menu in Excel.
- Explains how to define a name and its reference in a workbook.
- Illustrates creating named ranges programmatically through the XlsIO interface using C#.

## Content

### Inserting Defined Names using Insert Menu

#### Figure: Inserting Defined Names using Insert Menu

![Figure 123: Inserting Defined Names using Insert Menu](https://example.com/figure123.png)

**Figure 123: Inserting Defined Names using Insert Menu**

To insert defined names in an Excel workbook using the Insert menu, follow these steps:

1. Open the Excel worksheet.
2. Go to the **Insert** menu.
3. Select **Name** > **Define**.

This action will open the **Define Name** dialog box.

#### Define Name Dialog Box

![Figure 124: Define Name Dialog Box](https://example.com/figure124.png)

**Figure 124: Define Name Dialog Box**

In the **Define Name** dialog box:

- **Names in workbook**: Lists all defined names in the workbook.
- **Refers to**: Specifies the cell or range of cells that the defined name refers to.

For example, a named range can be created to refer to a specific cell, like `=Sheet1!$A$3`.

### Creating Named Ranges Programmatically

You can create named ranges in spreadsheets through XlsIO with the `IName` interface. The range for the name is specified through the `RefersToRange` property, from which you can access the Range text and other information. This can be specified for workbooks and worksheets.

#### Code Example

The following C# code example illustrates how to create named ranges and use them in formulas.

```csharp
[IName]
```

### Explanation

The `RefersToRange` property allows you to specify the range or cell that the named range refers to. This named range can then be used in formulas or other parts of your Excel workbook programmatically.

#### Example Usage

To assign a named range (`name1`) that points to cell `A3` on `Sheet1`:

```csharp
Workbook workbook = new Workbook();
IWorksheet sheet = workbook.Worksheets[0];
IName name = sheet.Names.Add("name1", sheet.Cells["A3"].ReferenceText);
```

This example creates a named range called `name1` that refers to the range `A3` on the first worksheet.

### API Reference

- **IName** interface: Used for defining named ranges in Excel.
- **RefersToRange** property: Specifies the range or cell reference for the named range.

## Code Examples

### C#

```csharp
Workbook workbook = new Workbook();
IWorksheet sheet = workbook.Worksheets[0];
IName name = sheet.Names.Add("name1", sheet.Cells["A3"].ReferenceText);
```

## Cross References

- See also: Related topics on using named ranges in Excel and other advanced XlsIO functionalities.

<!-- tags: [xlsio, defined names, named ranges, syncfusion winforms, workbook, worksheet, iutility interface, refers to range property, c#, code examples] keywords: [named ranges, define name, workbook, worksheet, insert menu, excelse, workbook utilility, refers to range, programmatic named ranges] -->
```