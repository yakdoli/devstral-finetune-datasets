```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_020.jpeg
document_name: Olap Common
page_number: 020
page_id: Olap Common#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:39Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Provides details about methods within the `OlapCommon` namespace.
- Enables retrieval and manipulation of OLAP reports and data managers.
- Includes utility methods for handling report files, streams, and events.

## Content

### Method Details

Below is a table detailing the methods and their functionalities within the `OlapCommon` namespace:

| Method Name               | Description                                                                 | Parameters           | Return Type            | Reference Link               |
|---------------------------|-----------------------------------------------------------------------------|-----------------------|-------------------------|------------------------------|
|                           | return the query as a string.                                              |                       |                         |                              |
| GetReport                 | This method will return the OlapReport collection by giving the Xml report file name as an input. | string               | OlapReportCollection    |                              |
| GetReportAsStream         | This method will return the current report collection along with the current state of OlapDataManager as a Stream. |                       | Stream                  | GetReportAsStream           |
| LoadOlapDataManager       | Will accept the OlapReport as an argument and Load the OlapDataManager with the given OlapReport. | OlapReport            | Void                    | LoadOlapDataManager         |
| LoadReport                | Used to get the report name as an argument and pick the specified report from the report collection to load the OlapDataManager with that report. | string               | Void                    |                              |
| LoadReportDefinitionFile  | Used to get the XML report file as input and load the OlapDataManager with the report in that file. | string               | Void                    | LoadReportDefinitionFile    |
| LoadReportDefinitionFromStream | Used to get a stream as input and read the report from that stream and load the OlapDataManager with that report. | Stream               | Void                    | LoadReportDefinitionFromStream |
| NotifyElementModified     | Used to trigger the `ElementModified` event.                                   |                       | Void                    |                              |

## API Reference

### Methods

#### `GetReport`
- **Description**: Returns the `OlapReport` collection by providing the XML report file name as input.
- **Parameters**: 
  - `string`: The XML report file name.
- **Return Type**: `OlapReportCollection`
- **Reference Link**: [GetReport]

#### `GetReportAsStream`
- **Description**: Returns the current report collection along with the current state of the `OlapDataManager` as a `Stream`.
- **Parameters**: None.
- **Return Type**: `Stream`
- **Reference Link**: [GetReportAsStream]

#### `LoadOlapDataManager`
- **Description**: Accepts an `OlapReport` as an argument and loads the `OlapDataManager` with the given `OlapReport`.
- **Parameters**: 
  - `OlapReport`: The report to load into the `OlapDataManager`.
- **Return Type**: `Void`
- **Reference Link**: [LoadOlapDataManager]

#### `LoadReport`
- **Description**: Gets the report name as an argument and picks the specified report from the report collection to load the `OlapDataManager` with that report.
- **Parameters**: 
  - `string`: The report name.
- **Return Type**: `Void`
- **Reference Link**: N/A

#### `LoadReportDefinitionFile`
- **Description**: Gets the XML report file as input and loads the `OlapDataManager` with the report in that file.
- **Parameters**: 
  - `string`: The XML report file name.
- **Return Type**: `Void`
- **Reference Link**: [LoadReportDefinitionFile]

#### `LoadReportDefinitionFromStream`
- **Description**: Gets a stream as input, reads the report from that stream, and loads the `OlapDataManager` with that report.
- **Parameters**: 
  - `Stream`: The stream containing the report.
- **Return Type**: `Void`
- **Reference Link**: [LoadReportDefinitionFromStream]

#### `NotifyElementModified`
- **Description**: Triggers the `ElementModified` event.
- **Parameters**: None.
- **Return Type**: `Void`
- **Reference Link**: N/A

## Code Examples

### Example of `GetReport`

```csharp
using Syncfusion.Olap.OlapCommon;

// Example code snippet to demonstrate the usage of GetReport
string reportFileName = "SampleReport.xml";
OlapReportCollection reports = OlapCommon.GetReport(reportFileName);
```

### Example of `LoadOlapDataManager`

```csharp
using Syncfusion.Olap.OlapCommon;

// Example code snippet to demonstrate the usage of LoadOlapDataManager
OlapReport report = new OlapReport();
OlapCommon.LoadOlapDataManager(report);
```

## Cross References

- See also: [Syncfusion OLAP Report documentation](https://www.syncfusion.com/documentation/olap/report-creation)
- See also: [OlapDataManager documentation](https://www.syncfusion.com/documentation/olap/data-manager)

### Tags and Keywords
<!-- tags: olap, report, olapreportcollection, stream, datamanager, reportfile, xml, event triggers, winforms, syncfusion -->
```