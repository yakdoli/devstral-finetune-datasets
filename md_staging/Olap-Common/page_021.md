```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_021.jpeg
document_name: Olap Common
page_number: 021
page_id: Olap Common#page_021
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:16:00Z
fidelity: lossless
-->

## Overview

- Details the methods related to managing and manipulating reports in the Essential OlapCommon framework.
- Describes how to trigger events, remove, rename, save, and set reports.
- Focuses on the UseWhereClauseForSlicing property and its role in handling data slicing in MDX queries.

## Content

### Methods in OlapCommon

The following table outlines the methods available in the Essential OlapCommon framework for managing reports:

| Method Name          | Description                                                                 | Parameters                                 | Return Type | Reference Link         |
|----------------------|-----------------------------------------------------------------------------|--------------------------------------------|--------------|------------------------|
| NotifyReportChanged  | Used to trigger the ReportChanged event.                                    | -                                          | Void         | -                      |
| RemoveReport         | Used to get the report name as input and remove that report from report collection. | string                                     | Void         | RemoveReport           |
| RenameReport         | Used to rename the current report of OlapDataManager.                       | Index as int and new Report Name as string | Void         | RenameReport           |
| SaveReport           | Used to get the file name and store the current report collection along with the current state of the OlapDataManager as an Xml file. | string                                     | Void         | SaveReport             |
| SetCurrentReport     | Used to set an OlapReport as the current report of the OlapDataManager. This method is the initial method that will start data processing. | OlapReport                                | Void         | SetCurrentReport       |

### 4.2.2 UseWhereClauseForSlicing

The UseWhereClauseForSlicing property facilitates the user to decide whether the MDX query parser engine should consider 'Where' or 'Select' clause for slicing data.

#### Use Case Scenarios

While slicing dimensions with a specific range of measures using the 'Select' clause in MDX query, an exception is thrown. This can be resolved by using the 'Where' clause for slicing.

#### Example

Slicing the Date dimension from months of 2002 to months of 2003 will throw an exception when the 'Select' clause is used.

### Properties

#### Table 6: Property Table

| Property          | Description | Type     | Data Type | Reference links |
|-------------------|-------------|----------|-----------|-----------------|
| UseWhereClauseForSlicing | Specifies whether the MDX query parser engine should consider 'Where' or 'Select' clause for slicing data. | -         | -         | -           |

## API Reference

### Methods Summary

- **NotifyReportChanged**
  - **Purpose:** Used to trigger the ReportChanged event.
  - **Parameters:** None
  - **Return Type:** Void

- **RemoveReport**
  - **Purpose:** Used to remove a report from the collection based on the report name.
  - **Parameters:** string (report name)
  - **Return Type:** Void

- **RenameReport**
  - **Purpose:** Used to rename the current report.
  - **Parameters:** Index as int and new Report Name as string
  - **Return Type:** Void

- **SaveReport**
  - **Purpose:** Used to save the current report as an Xml file.
  - **Parameters:** string (file name)
  - **Return Type:** Void

- **SetCurrentReport**
  - **Purpose:** Used to set the current report and start data processing.
  - **Parameters:** OlapReport
  - **Return Type:** Void

## Code Examples

Example usage of the SetCurrentReport method:

```csharp
OlapReport report = new OlapReport();
OlapDataManager.SetCurrentReport(report);
```

## Page-level Navigation/TOC (if applicable)

- Methods in OlapCommon
- UseWhereClauseForSlicing
  - Use Case Scenarios
  - Example

## Cross References

See also:
- [OlapDataManager Class Reference](#)
- [MDX Query Handling in Olap Applications](#)

<!-- tags: [syncfusion-sdk, olap, mdx-query, report-management, syncfusion-winforms] keywords: [notifyreportchanged, removereport, renamereport, savereport, setcurrentreport, usewhereclauseforslicing, mdx, report, synchronization, data-processing] -->
```