```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_015.jpeg
document_name: Olap Common
page_number: 015
page_id: Olap Common#page_015
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:19Z
fidelity: lossless
-->

# Essential Olap Common

## Overview
- Explains how to establish connections to the SSAS server and offline cubes using OlapDataManager.
- Demonstrates the use of C# and VB.NET code snippets for connection procedures.

## Content

### Establishing Connection with the SSAS server
By default, the `OlapDataManager` uses the MSOLAP native provider to establish a connection with the SSAS server.

#### C#
```csharp
OlapDataManager olapDataManager = new OlapDataManager("DataSource=localhost;
    Initial Catalog=Adventure Works DW");
```

#### [VB]
```vb
OlapDataManager olapDataManager = New OlapDataManager("DataSource=localhost;
    Initial Catalog=Adventure Works DW")
```

**Or**

### Establishing Connection with the SSAS server through Data Provider
The following code snippet describes establishing connection with the server:

#### C#
```csharp
AdomdDataProvider dataProvider = new AdomdDataProvider("DataSource=localhost;
    Initial Catalog=Adventure Works DW");
OlapDataManager olapDataManager = new OlapDataManager(dataProvider);
```

#### [VB]
```vb
Dim dataProvider As AdomdDataProvider = New AdomdDataProvider("DataSource=localhost;
    Initial Catalog=Adventure Works DW")
Dim olapDataManager As OlapDataManager = New OlapDataManager(dataProvider)
```

### Establishing connection with the offline cube
The following code snippet describes establishing connection with the offline cube:

#### C#
```csharp
OlapDataManager olapDataManager = new OlapDataManager(@"Data Source = 
    C:\Common\Data\OfflineCube\Adventure Works Ext.cub; Provider =
    MSOLAP;");
```

#### [VB]
```vb
OlapDataManager olapDataManager = New OlapDataManager("Data Source = 
    C:\\Common\\Data\\OfflineCube\\Adventure Works Ext.cub; Provider =
    MSOLAP;")
```

<!-- tags: [syncfusion winforms, olap common, olap data manager, ssas server connection, offline cube connection, c#, vb.net] keywords: [OlapDataManager, MSOLAP native provider, AdomdDataProvider, SSAS server, offline cube, connection examples] -->
```