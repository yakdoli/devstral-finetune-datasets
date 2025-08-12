```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_266.jpeg
document_name: XlsIO
page_number: 266
page_id: XlsIO#page_266
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:05:11Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Explains how to control various settings for Pivot tables using the IPivotTableOptions interface in XlsIO.
- Demonstrates code samples for managing Pivot table options such as field list visibility, header captions, and grand totals.
- Highlights key features like ShowFieldList, RowHeaderCaption, ColumnHeaderCaption, and GrandTotal properties.

## Content

### IPivotTableOptions Interface
XlsIO supports the pivot table options using the IPivotTableOptions interface to control various settings for the existing Pivot table. The following code sample illustrates the same.

```csharp
IPivotTable pivotTable = sheet.PivotTables[0];
IPivotTableOptions options = pivotTable.Options;
options.ShowFieldList = true;
options.ColumnHeaderCaption = "Sales Details";
options.ColumnHeaderCaption = "Customer Names";
options.ErrorString = "#ERROR#";
```

#### Show or Hide the Field List
In MS Excel, click the Field List button in the Design Tab. Show or Hide the pivot table field list pane in XlsIO.

```csharp
options.ShowFieldList = true;
```

#### Header Caption
In MS Excel, the Field Header button is used to show or hide the pivot table caption. In XlsIO, to enable and disable the caption, use the DisplayFieldCaption property. Use the RowHeaderCaption and ColumnHeaderCaption properties to edit the respective pivot table headers.

```csharp
options.RowHeaderCaption = "Payment Dates";
options.ColumnHeaderCaption = "Payments";
```

#### Grand Total
You can display or hide the totals for the current Pivot Table report by selecting an option from Design -> Layout -> Grand Totals. XlsIO provides an equivalent API to perform with simple properties as follows.

```csharp
pivotTable.ColumnGrand = false;
pivotTable.RowGrand = true;
```

## Page-level Navigation/TOC (if applicable)
- IPivotTableOptions Interface
  - Show or Hide the Field List
  - Header Caption
  - Grand Total

## Cross References
See also:
- [MS Excel Pivot Table Field List]
- [Pivot Table Headers in XlsIO]

## RAG Annotations
<!-- tags: [xlsio, pivot table options, ipivottableoptions, pivot table, design tab, field list, header caption, grand total] keywords: [xlsio, ipivottableoptions, pivot table, field list, caption, grand total, design tab, api, csharp] -->
```
