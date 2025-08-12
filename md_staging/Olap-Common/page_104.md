```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_104.jpeg
document_name: Olap Common
page_number: 104
page_id: Olap Common#page_104
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:45Z
fidelity: lossless
-->

## Overview

- Displays the Expander button in Controls.
- Explains internal processing of OlapReport within OlapDataManager.
- Describes methods for handling Drill Down/Up operations.

## Content

### 5.19 Process OlapReport Internally

Once the `OlapReport` is created and bound to the `OlapDataManager`, the data processing begins. By binding the report, the given report will be set as the current report of the `OlapDataManager` and it will invoke the two important methods that let the way to generate the **MDX query** and `CellSet`.

- **NotifyReportChanged**
  - After initialization, the data processing begins. When the `NotifyReportChanged` is invoked, it triggers the `ReportChaned` event, which will be handled by the control level.

- **NotifyElementModified**
  - The `NotifyElementModified` method begins the processing by invoking the `ExecuteCellSet()` method, which creates the `CellSet` and `PivotEngine` based on the `OlapReport`.

#### Explanation of `ExecuteCellSet()`
- The `ExecuteCellSet()` method checks whether the user has given the MDX query. If the query exists, it will invoke an overloaded method of the `ExecuteCellSet(string query)` which in turn calls the `ExecuteCellSet(string query, bool b1, bool b2)` of `DataProvider` class. The given query will be executed in the `DataProvider` class and the `CellSet` will be produced.
- If the query does not exist, the overloaded method of `ExecuteCellSet (MDXQuerySpecification querySpecification)` will get invoked. This method will invoke the `MDXQuerySpecification` creation and from there the query creation will be invoked and the query will be returned. The `ExecutCellSet()` method receives the query and passes it to the data provider’s `ExecuteCellset` method. The query will be executed there on the connected database and a `CellSet` will be returned. From the `CellSet`, the `PivotEngine` will be created, from which the controls can get their input.

### 5.20 Handle Drill Down/Up Process

Whenever we collapse or expand the controls like a grid or chart, the level member items will change and the query will be regenerated to create the new `CellSet`.

The important methods that identify the drill-down members are:

- **ToggleExpandableState()**
- **UpdateDrillDowlItems()**
- **DrillUpDown()**

## Code Examples

```csharp
/// Displaying the Expander button in Controls
olapReport.ShowExpanders = false;
```

## Page-level Navigation/TOC (if applicable)

- 5.19 Process OlapReport Internally
  - NotifyReportChanged
  - NotifyElementModified
- 5.20 Handle Drill Down/Up Process

<!-- tags: [olapreport, drilldown, syncfusion, olapmanager, pivotengine] keywords: [notifyreportchanged, notifyelementmodified, excutecellset, mdxquery, drilldown, drillup, cellset, pivotengine, dataprovider] -->
```