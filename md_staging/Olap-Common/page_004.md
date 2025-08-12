```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_004.jpeg
document_name: Olap Common
page_number: 004
page_id: Olap Common#page_004
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:14:30Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Step-by-step guide to connecting with SSAS Server and Cube files.
- Instructions on establishing role-based connections and interacting with Mondrian Server via XML.
- Details on configuring WCF services for Silverlight OLAP controls.
- Comprehensive process on managing OlapDataManagers and OlapReports.
- Techniques for handling MDX queries and non-OLAP data within Olap controls.
- Procedures for saving, renaming, and removing reports in XML format.
- Methods for filtering, drilling, and exporting Olap data.

## Content

### 5.1 Establish the connection for an SSAS Server
- Page 79

### 5.2 Establish the connection for a Cube file
- Page 79

### 5.3 Establish Role-based Connection
- Page 80

### 5.4 Connecting to Mondrian Server through XML
- Page 80

### 5.5 Connect ActivePivot Server through XML
- Page 81

### 5.6 Create a WCF Service for Silverlight OLAP control
- Page 81

### 5.7 Connect WCF Service in Silverlight application
- Page 87

### 5.8 Bind an OlapReport with OlapDataManager
- Page 88

#### 5.8.1 CurrentReport
- Page 90

#### 5.8.2 SetCurrentReport
- Page 90

#### 5.8.3 LoadOlapDataManager
- Page 90

#### 5.8.4 LoadReportDefinitionFile
- Page 91

#### 5.8.5 LoadReportDefinitionFromStream
- Page 91

### 5.9 Bind the MDX query to OlapDataManager
- Page 92

### 5.10 Bind the Non-OLAP data to OlapDataManager
- Page 95

### 5.11 Save the report as xml file
- Page 96

### 5.12 Load xml report file
- Page 97

### 5.13 Rename and remove a report
- Page 99
  - **5.13.1 RenameReport**
  - Page 99
  - **5.13.2 RemoveReport**
  - Page 100

### 5.14 Get the reports in the OlapDataManager as a stream
- Page 100

### 5.15 Communicate the OLAP control with the base
- Page 100

### 5.16 Add the elements to an Axis
- Page 101

### 5.17 Apply the Filter through filter element
- Page 101

### 5.18 Show/hide the Expander buttons in OLAP controls
- Page 103

### 5.19 Process OlapReport Internally
- Page 104

### 5.20 Handle Drill Down/Up Process
- Page 104

### 5.21 Connect WCF Service by an additional Binding Type in Silverlight application
- Page 106

### 5.22 Retrieve the MDX Query of a CurrentReport
- Page 108

### 5.23 Add UseWhereClauseForSlicing to an Application
- Page 109

### 5.24 Edit MDX Query before Its Execution
- Page 110

### 5.25 Host BI Silverlight component in ASP.NET MVC Web Project
- Page 110

## API Reference (if applicable)
- **Namespace:** Essential.OlapCommon
- **Classes:** OlapDataManager, OlapReport
- **Members:**
  - Methods: LoadOlapDataManager(), LoadReportDefinitionFile()
  - Properties: CurrentReport, NonOlapData

## Code Examples (multi-language supported)
```csharp
// Example: Establishing a connection with SSAS Server
using Syncfusion.Olap.Common;
var connectionString = "Provider=MSOLAP;Data Source=ServerName;Initial Catalog=CubeName";
var olapConnection = new OlapConnection(connectionString);
```

## Cross References
- See also: Section 6: Advanced OLAP Reporting Techniques
- See also: Section 7: Troubleshooting OLAP Connections

<!-- tags: [Olap, OLAP control, WCF service, Silverlight, MDX query, OlapDataManager, OlapReport, SSAS Server] keywords: [essential olapcommon, olap connection, olap filtering, olap drilling, olap reporting, silverlight integration, wcf integration] -->
```