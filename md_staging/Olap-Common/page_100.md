```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_100.jpeg
document_name: Olap Common
page_number: 100
page_id: Olap Common#page_100
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:31Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Understand how to manage reports in the OlapDataManager.
- Learn to use methods for removing and retrieving reports.
- Explore data communication between the OLAP control and the base.

## Content

### 5.13.2 RemoveReport

A report in the report collection of the OlapDataManager can be removed by invoking the RemoveReport method. This method will accept the report name as an argument and remove that report from the report collection of OlapDataManager.

The following code snippet will illustrate the removal of a report:

```csharp
olapDataManager.RemoveReport("SalesAnalysisOn2005");
```

```vb
olapDataManager.RemoveReport("SalesAnalysisOn2005")
```

### 5.14 Get the reports in the OlapDataManager as a stream

You can get the report collection in the OlapDataManager as a stream by using GetReportAsStream method. This method will return the current report collection of the OlapDataManager as a stream.

The following code snippet will explain obtaining the report as a stream:

```csharp
Stream reportStream = olapDataManager.GetReportAsStream();
```

```vb
Dim reportStream As Stream = olapDataManager.GetReportAsStream()
```

### 5.15 Communicate the OLAP control with the base

Each and every control has an OlapDataManager property. Through this property, the control sends and receives information to and from the base.

Below steps explains how to load data in an OLAP control:

1. Give the connection information and OlapReport to the OlapDataManager.
2. Assign this OlapDataManager to the control's OlapDataManager property.
3. By invoking the control's DataBind() method virtually when setting the value for the OlapDataManager property, the data processing will begin and the output is displayed in the Control.

---

## Page-level Navigation/TOC

- [5.13.2 RemoveReport]
- [5.14 Get the reports in the OlapDataManager as a stream]
- [5.15 Communicate the OLAP control with the base]

## Cross References

See also:
- OlapDataManager
- OlapReport
- DataBind()

<!-- tags: [Olap DataManager, Olap Report, RemoveReport, GetReportAsStream, DataBind] keywords: [Olap, WinForms, Report Management, Data Binding, Stream] -->
```