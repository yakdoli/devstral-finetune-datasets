```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_091.jpeg
document_name: Olap Common
page_number: 091
page_id: Olap Common#page_091
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:22Z
fidelity: lossless
-->

## Essential OlapCommon

```csharp
OlapDataManager.LoadOlapDataManager(olapReport);
```

```vb
OlapDataManager.LoadOlapDataManager(olapReport)
```

### 5.8.4 LoadReportDefinitionFile

You can bind the OlapReport as xml file to OlapDataManager using the LoadReportDefinitionFile method. This contains two steps as follows:

1.  Loading the report definition file and
2.  Loading a specific report in that file by giving its name

The following code snippet will illustrate the loading of the report definition file:

```csharp
olapDataManager.LoadReportDefinitionFile(@"C:\SampleReports\SalesAnalysis.xml");
olapDataManager.LoadReport("SalesOn2003");
```

```vb
olapDataManager.LoadReportDefinitionFile("C:\SampleReports\SalesAnalysis.xml")
olapDataManager.LoadReport("SalesOn2003")
```

### 5.8.5 LoadReportDefinitionFromStream

You can load the OlapReport as a stream to the OlapDataManager using LoadReportDefinitionFromStream method. This contains two steps as follows:

1.  Loading the report stream
2.  Loading the specific report in that stream by giving its name

The following code snippet will illustrate the loading of the report definition from a stream:

```csharp
olapDataManager.LoadReportDefinitionFromStream(reportStream);
olapDataManager.LoadReport("SalesOn2003");
```

```vb
olapDataManager.LoadReportDefinitionFromStream(reportStream)
olapDataManager.LoadReport("SalesOn2003")
```
```