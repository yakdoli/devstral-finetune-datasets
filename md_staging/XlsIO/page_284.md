```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_284.jpeg
document_name: XlsIO
page_number: 284
page_id: XlsIO#page_284
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:08:31Z
fidelity: lossless
-->

# Essential XlslO

## Overview
- Once you select a field, the PivotTable and the PivotChart appear.
- PivotTable and PivotChart should be populated with data fields, which appear on the field list on the right.
- Fields can be dragged to the PivotTable grid, to one of the defined areas and also there is an option to move the created PivotChart to a separate sheet.

## Content

### Figure: Adding Fields to the PivotChart

![Figure 95: Adding fields to the PivotChart](https://i.imgur.com/4UoSd7A.png)

---

### PivotChart Creation Using XlslO

XlslO provides support for the creation of PivotTables and PivotCharts by using simple code samples. IPivotCache interface caches the data that need to be summarized when filtering. IPivotTable represents a PivotTable in object, and has properties that allow customizing it. IPivotTable interface returns the collection of PivotTables that are present in a worksheet. IPivotField represents the field in the PivotTable. This includes row, column and data field axes. IPivotDataFields get a collection of the data field and once the PivotTable is created, it is required to create a PivotChart by setting the PivotSource property of the IChart interface, which references the created PivotTable.

#### Note: PivotTable and PivotChart are currently not supported for .xls format.
The following code example illustrates the creation of a PivotTable and PivotChart by using XlslO.

## Code Examples

```csharp
// Example code for creating a PivotTable and PivotChart using XlslO.
// Code is yet to be provided. Please check the official documentation for usage.
```

## API Reference

### **Namespace**: Syncfusion.XlsIO
#### Classes
- **IPivotCache**: Interface to cache the data required for summarizing.
- **IPivotTable**: Interface representing a PivotTable object.
  - **Properties**: Customization settings for the PivotTable.
  - **Methods**: To retrieve and modify PivotTable elements.
- **IPivotField**: Represents the field in the PivotTable.
  - **Properties**: Includes row, column, and data field axes.
- **IPivotDataFields**: Gets a collection of the data field.
  - **Methods**: To manage data field collection.

### **Namespace**: Syncfusion.XlsIO.Chart
#### Interfaces
- **IChart**: Interface for creating and managing charts.
  - **Properties**:
    - **PivotSource**: References the created PivotTable.

## Cross References
- **See also**: [Syncfusion XlsIO Documentation](https://www.syncfusion.com/documentation/xlsio) for detailed information on PivotTables and PivotCharts.

## RAG Annotations
<!-- tags: [Syncfusion, XlslO, PivotTable, PivotChart, Winforms] keywords: [charts, PivotCache, IPivotTable, IPivotField, IPivotDataFields, IChart, PivotSource, PivotTable] -->
```