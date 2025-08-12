```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_018.jpeg
document_name: Olap Common
page_number: 018
page_id: Olap Common#page_018
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:36Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Describes the essential properties and their functionalities in the OlapCommon namespace.
- Provides details on how to set or retrieve properties related to cube names, schemas, reports, data providers, and more.
- Includes references to additional resources for specific properties.

## Content

### Property Description Table

| Property Name                   | Description                                                                                                             | Type                      | Value it Accepts         | Reference Link           |
|---------------------------------|-------------------------------------------------------------------------------------------------------------------------|---------------------------|--------------------------|--------------------------|
|                               | here.                                                                                                                   |                           |                          |                          |
| CurrentCubeName                | Used to set or get the current cube name. When set, the whole data process will change to the specified cube name. | String                    | String                   |                          |
| CurrentCubeSchema              | The user can get the CubeSchema of the currently connected cube.                                                        | CubeSchema                |                          |                          |
| CurrentReport                  | Used to load an OlapReport or get the currently loaded report.                                                          | OlapReport                | OlapReport               | OlapReport                |
| DataProvider                   | Used to set a data provider and get the existing data provider.                                                          | IDataProvider              | IDataProvider            | DataProvider               |
| IsCurrentReportModified        | Used to get or set the modified status of the currently loaded report.                                                  | bool                      | True/False               |                          |
| Itemsource                     | Used to bind the Non-OLAP data to OlapDataManager.                                                                      | Object                    | Enumerable collection/ ITyped List |                          |
| MdxQuery                       | Used to pass the MDX query as input.                                                                                   | string                    | String                   | MdxQuery                  |
| PivotEngine                    | Used to get the PivotEngine for the given input.                                                                       | PivotEngine               | PivotEngine              |                          |
| QuerySpecification              | Used to get the MDXQuerySpecification for the given OlapReport.                                                         | MDXQuerySpecification      |                          | QuerySpecification         |
| ReportPath                     | Used to get or set the report path to store the report as an XML file.                                                  | string                    |                          |                          |
| Reports                        | Contains the report collection of the OlapReportCollection.                                                            | OlapReportCollection      | OlapReportCollection     |                          |

## API Reference

- **Properties**
  - `CurrentCubeName`: Allows setting or retrieving the current cube name.
  - `CurrentCubeSchema`: Provides access to the `CubeSchema` of the currently connected cube.
  - `CurrentReport`: Facilitates loading or retrieving the current `OlapReport`.
  - `DataProvider`: Sets or retrieves the data provider.
  - `IsCurrentReportModified`: Indicates whether the current report has been modified.
  - `Itemsource`: Binds Non-OLAP data to the `OlapDataManager`.
  - `MdxQuery`: Passes an MDX query for processing.
  - `PivotEngine`: Retrieves the `PivotEngine` for the given input.
  - `QuerySpecification`: Retrieves the `MDXQuerySpecification` for the current `OlapReport`.
  - `ReportPath`: Sets or retrieves the report's storage path as an XML file.
  - `Reports`: Contains the collection of reports in the `OlapReportCollection`.

## Code Examples

### Sample Code Using `CurrentCubeName`

```csharp
using Syncfusion.OlapCommon;

var olapCommon = new OlapCommon();
// Set the current cube name.
olapCommon.CurrentCubeName = "SalesCube";

// Get the current cube name.
string currentCubeName = olapCommon.CurrentCubeName;
```

### Sample Code Using `MdxQuery`

```csharp
using Syncfusion.OlapCommon;

var olapCommon = new OlapCommon();
// Set the MDX query.
olapCommon.MdxQuery = "SELECT NON EMPTY Measures.[Sales Amount] ON COLUMNS, NON EMPTY [Product].[Product Category] ON ROWS FROM [SalesCube]";

// Execute the query.
var pivotEngine = olapCommon.PivotEngine;
pivotEngine.Refresh();
```

### Sample Code Using `CurrentReport`

```csharp
using Syncfusion.OlapCommon;

var olapCommon = new OlapCommon();

// Load an OlapReport.
olapCommon.CurrentReport = new OlapReport();
olapCommon.CurrentReport.Load("report.xml");

// Get the current report.
OlapReport currentReport = olapCommon.CurrentReport;
```

## Page-level Navigation/TOC

- [x] Property Description Table
- [x] API Reference
- [x] Code Examples

## Cross References

See also:
- MDXQuery
- OlapReport
- QuerySpecification
- DataProvider

## RAG Annotations

<!-- tags: [OlapCommon, MDXQuery, OlapReport, DataProvider, PivotEngine, OlapDataManager] keywords: [cube name, cube schema, report path, modified status, MDX query, PivotEngine] -->
```