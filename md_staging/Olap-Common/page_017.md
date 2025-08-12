```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_017.jpeg
document_name: Olap Common
page_number: 017
page_id: Olap Common#page_017
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:47Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Connecting to the **Active Pivot Server** using **C#** and **VB** code examples.
- Detailed explanation of properties and their descriptions in a table format.

## Content

### Connecting to Active Pivot Server

#### C#
```csharp
// Connecting to Active Pivot Server
OlapDataManager DataManager = new
OlapDataManager(@"Data Source=http://localhost:8081/var_s/xmla;
Initial Catalog=VarCubes;
User ID=; Password=; Transport Compression=None;");
DataManager.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.ActivePivot;
```

#### VB
```vb
' Connecting to Active Pivot Server
Dim DataManager As OlapDataManager = New OlapDataManager("Data
Source=http://localhost:8081/var_s/xmla;  Initial Catalog=VarCubes;
User ID=; Password=; Transport Compression=None;")
DataManager.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.ActivePivot
```

Click [here](#) for more information on Active Pivot server.

### 4.2.1 Properties and Methods

#### Properties

The properties and their descriptions are tabulated below:

| Property Name   | Description                                                                 | Type       | Value it Accepts | Reference Link |
|-----------------|------------------------------------------------------------------------------|------------|------------------|----------------|
| **ConnectionString** | Used to pass the connection string to establish the connection.<br>The user can also get the connection string using this property. | string     | String          | -              |
| **CurrentCellSet**   | The user can get the CellSet of their input from                             | CellSet    | -               | -              |

<!-- tags: [Olap, Active Pivot, C#, VB, Properties, Methods, ConnectionString, CurrentCellSet] keywords: [Syncfusion, OLAP, connection, properties, methods, string, cellset, data] -->
```