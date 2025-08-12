```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: Olap Common
page_number: 068
page_id: Olap Common#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:19Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview

- Demonstrates the use of MDX queries in OlapGrid, OlapChart, and OlapClient in Silverlight applications.
- Explains how to enable and disable MDX to OLAP parsing in applications.

## Content

### Navigation Paths

#### OlapGrid [Silverlight]

- `<InstalledDrive>\Users\<UserName>\AppData\Local\Syncfusion\EssentialStudio\<Version>\BI\Silverlight\OlapGrid.Silverlight\ReportDefinition\GridMDXQueryDemo`

#### OlapChart [Silverlight]

- `<InstalledDrive>\Users\<UserName>\AppData\Local\Syncfusion\EssentialStudio\<Version>\BI\Silverlight\OlapChart.Silverlight\DefiningReports\ChartMDXQueryDemo`

#### OlapClient [Silverlight]

- `<InstalledDrive>\Users\<UserName>\AppData\Local\Syncfusion\EssentialStudio\<Version>\BI\Silverlight\OlapClient.Silverlight\ProductShowcase\MDXQueryDemo`

### 4.3.16.2 Adding MDX Query binding with drill up and drill down operations to an Application

#### Overview

The following code samples are used to enable and disable the MDX to OLAP parsing and processing of an MDX query into OLAP data.

#### Code Examples

**[C#]**

```csharp
// Enable MDX to OLAP parsing.
OlapDataManager olapDataManager = new OlapDataManager();
olapDataManager.MdxQuery = "MDX Query Here";
olapDataManager.ExecuteCellSet();

// Disable MDX to OLAP parsing.
OlapDataManager olapDataManager = new OlapDataManager();
olapDataManager.AllowMdxToOlapReportParse = false;
olapDataManager.MdxQuery = "MDX Query Here";
olapDataManager.ExecuteCellSet();
```

**[VB]**

```vb
' Enable MDX to OLAP parsing.
Dim olapDataManager As New OlapDataManager()
olapDataManager.MdxQuery = "MDX Query Here"
olapDataManager.ExecuteCellSet()

' Disable MDX to OLAP parsing.
Dim olapDataManager As New OlapDataManager()
olapDataManager.AllowMdxToOlapReportParse = False
```

## Page-level Navigation/TOC

- [OlapGrid [Silverlight]](#olapgrid-silverlight)
- [OlapChart [Silverlight]](#olapchart-silverlight)
- [OlapClient [Silverlight]](#olapclient-silverlight)
- [4.3.16.2 Adding MDX Query binding with drill up and drill down operations to an Application](#43162-adding-mdx-query-binding-with-drill-up-and-drill-down-operations-to-an-application)

## Cross References

- See also:
  - [Olap Grid Documentation](#olap-grid-documentation)
  - [Olap Chart Documentation](#olap-chart-documentation)
  - [Olap Client Documentation](#olap-client-documentation)

<!-- tags: [syncfusion, winforms, olap, mdx, silverlight] keywords: [MDX query, OLAP parsing, drill up, drill down, Enable, Disable, OlapGrid, OlapChart, OlapClient, Silverlight] -->
```
