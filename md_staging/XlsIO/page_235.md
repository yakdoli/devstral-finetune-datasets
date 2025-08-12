```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_235.jpeg
document_name: XlsIO
page_number: 235
page_id: XlsIO#page_235
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:03:53Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Explains how to save a workbook using the SaveAs method.
- Demonstrates creating and applying 3-D charts with wall settings.
- Describes filtering chart series and categories in Excel 2013 using Essential XlsIO.

## Content

### Saving the Workbook

The following code snippet shows how to save a workbook using the `SaveAs` method in Essential XlsIO:

```csharp
// Save the workbook
workbook.SaveAs("Sample.xlsx")
```

#### Creating and Applying 3-D Charts with Wall Settings

The image below illustrates a 3-D chart applied with wall settings for Crescent City, CA, displaying monthly precipitation in inches and temperature in degrees Fahrenheit.

![3-D Chart with Wall Settings](https://user-images.githubusercontent.com/123456789/98765432-bc94cf80-9cea-11eb-9191-1234567890ce.png)

*Figure 78: 3-D Chart Applied with Wall Settings*

### Filtering Chart Series and Categories

#### Overview

Essential XlsIO supports filtering chart series and categories for Excel 2013 files. The following code samples explain how to perform filtering for series and categories in a chart.

#### Code Example

```csharp
//Step 1: Instantiate the spreadsheet creation engine.
ExcelEngine excelEngine = new ExcelEngine();
```

## API Reference

### Methods
- `SaveAs`:
  - **Description**: Saves the workbook to a specified file name.
  - **Parameters**:
    - `fileName`: The name of the file to save as.
  - **Returns**: None.
  - **Exceptions**:
    - FileNotFoundException if the file cannot be found.
    - IOException if an I/O error occurs.

## Code Examples

#### Saving a Workbook

```csharp
// Example code to save a workbook
workbook.SaveAs("Sample.xlsx");
```

#### Creating a 3-D Chart

The example above demonstrates how to create and apply a 3-D chart with wall settings for Crescent City, CA.

#### Filtering Chart Series and Categories

The code snippet below initializes the Excel engine for chart filtering:

```csharp
ExcelEngine excelEngine = new ExcelEngine();
```

## Page-level Navigation/TOC

- [Save the workbook](#saving-the-workbook)
- [Creating and Applying 3-D Charts with Wall Settings](#creating-and-applying-3-d-charts-with-wall-settings)
- [Filtering Chart Series and Categories](#filtering-chart-series-and-categories)

<!-- tags: [Essential XlsIO, Excel, Chart, Filtering] keywords: [workbook.SaveAs, 3D chart, wall settings, filtering chart series, filtering categories, Excel 2013, chart filtering] -->
```