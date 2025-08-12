```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_010.jpeg
document_name: Olap Common
page_number: 010
page_id: Olap Common#page_010
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:00Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- This page describes the OLAP Silverlight Base and its wrapper, focusing on data processing and conversion features.
- Highlights the role of namespaces and classes in performing data conversion between OLAP Silverlight Base and OLAP Base.
- Explains the flow of data in Silverlight applications.

## Content

### 3.2 OLAP Silverlight Base
OLAP Silverlight Base is a class library containing several namespaces and classes to perform data processing operations required by OLAP Silverlight controls. The `OlapDataManager` retrieves OLAP data and binds the result to an OLAP Control.

#### Note:
This class library was organized under `Syncfusion.Olap.Base` assembly.

### 3.3 OLAP Silverlight Base Wrapper
The OLAP Silverlight Base Wrapper is a class library containing several namespaces and classes. This library helps perform data conversion between OLAP Silverlight Base and OLAP Base. The Data Conversion process is used to achieve the following features:

1. Establishing the connection and retrieving data by converting OLAP Silverlight Base information to OLAP Base information.
2. Sending retrieved data to OLAP Silverlight Base by converting OLAP Base data to OLAP Silverlight Base data.

#### Dataflow in Silverlight

![Dataflow in Silverlight](attachment)

### Diagram Explanation
- **OlapReport**: Serves as the starting point for reporting operations.
- **OlapDataManager**: Manages data retrieval and binding to the OLAP Control.
- **Control**: The UI component that interacts with the user.
- **CellSet Pivot Engine**: Handles cell set and pivot operations.
- **Virtual Channel (IOLapDataProvider)**: Acts as a middleware for asynchronous calls.
- **Olap Base**: Includes components like `MDX Query Specification`, `QueryBuilderEngine`, and `Data Provider` for query processing.

#### Note:
This class library was organized under `Syncfusion.OlapSilverlight.Base` assembly.

### Key Components
- **OlapReport**: Facilitates reporting operations.
- **OlapDataManager**: Manages data operations and binds data to the OLAP Control.
- **Control**: The user interface component for data interaction.
- **CellSet Pivot Engine**: Handles data pivoting and cell operations.
- **Virtual Channel (IOLapDataProvider)**: Middleware for asynchronous communication.
- **Olap Base**: Includes components like `MDX Query Specification`, `QueryBuilderEngine`, and `Data Provider`.

## API Reference

### namespaces
- `Syncfusion.Olap.Base`
- `Syncfusion.OlapSilverlight.Base`

### Classes
- `OlapDataManager`
- `OlapReport`
- `Control`
- `CellSet`
- `PivotEngine`
- `Virtual Channel (IOLapDataProvider)`
- `MDX Query Specification`
- `QueryBuilderEngine`
- `Data Provider`

## Code Examples

### C#
```csharp
// Sample code for retrieving OLAP data
using Syncfusion.Olap.Base;

public class DataRetriever
{
    public void RetrieveData()
    {
        var olapDataManager = new OlapDataManager();
        var cellSet = olapDataManager.GetData(); // Retrieve data from OLAP Base
        // Further processing and binding logic
    }
}
```

## Page-level Navigation/TOC
- 3.2 OLAP Silverlight Base
- 3.3 OLAP Silverlight Base Wrapper

## Cross References
- Refer to the `OlapDataManager` documentation for more details on data retrieval.
- See the `OlapBase` section for insights into query processing components.

<!-- tags: [Syncfusion, OLAP, Silverlight, Winforms, Base] keywords: [OlapDataManager, DataConversion, OLAP, Silverlight, Winforms, Dataflow] -->
```