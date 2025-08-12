<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_079.jpeg
document_name: Olap Common
page_number: 079
page_id: Olap Common#page_079
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:19:29Z
fidelity: lossless
-->

# Essential OlapCommon

## 5 How To

### 5.1 Establish the connection for an SSAS Server

A valid string is required to establish connection for an OlapDataManager.

Here is the code snippet that demonstrates how to connect SSAS by using connection string:

**[C#]**

```csharp
OlapDataManager dataManager = new OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW");
```

**[VB]**

```vb
Dim dataManager As New OlapDataManager("DataSource=localhost; Initial Catalog=Adventure Works DW")
```

Or

**[C#]**

```csharp
Syncfusion.Olap.DataProvider.IDataProvider dataProvider = new Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource=localhost; Initial Catalog=Adventure Works DW");
OlapDataManager dataManager = new OlapDataManager(dataProvider);
```

**[VB]**

```vb
Dim dataProvider As Syncfusion.Olap.DataProvider.IDataProvider = New Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource=localhost; Initial Catalog=Adventure Works DW")
Dim dataManager As New OlapDataManager(dataProvider)
```

### 5.2 Establish the connection for a Cube file

A valid string is required to establish connection for an OlapDataManager.

Here is the code snippet that demonstrates how to connect cube file by using connection string:

**[C#]**

```csharp
OlapDataManager dataManager = new OlapDataManager("DataSource=AdventureWorks_Ext.cub; Provider=MSOLAP");
```

**[VB]**

```vb
Dim dataManager As New OlapDataManager("DataSource=AdventureWorks_Ext.cub; Provider=MSOLAP")
```

Or

**[C#]**

<!-- tags: [syncfusion, winforms, olap, datamanager, ssas, cube, connectionstring] keywords: [olapdatamanager, adomddataprovider, connectionstring, ssas, cube, dataprovider] -->