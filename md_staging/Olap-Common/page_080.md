```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_080.jpeg
document_name: Olap Common
page_number: 080
page_id: Olap Common#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:07Z
fidelity: lossless
-->

## Essential OlapCommon

```csharp
Syncfusion.Olap.DataProvider.IDataProvider dataProvider = new Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource=AdventureWorks_Ext.cub; Provider=MSOLAP");
OlapDataManager dataManager = new OlapDataManager(dataProvider);
```

```vb
Dim dataProvider As Syncfusion.Olap.DataProvider.IDataProvider = New Syncfusion.Olap.DataProvider.AdomdDataProvider("DataSource=AdventureWorks_Ext.cub; Provider=MSOLAP")
Dim dataManager As New OlapDataManager(dataProvider)
```

### 5.3 Establish Role-based Connection

You can apply Role-based filtering to OLAP components by specifying the appropriate role name designed for specific set of users in the SSAS Cube. You must specify the role name in the "Roles" attribute of the connection string. The following code example illustrates this.

```csharp
OlapDataManager olapDataManager = new OlapDataManager(@"DataSource=http://bi.syncfusion.com/olap/msmdpump.dll; Roles=Role1; Initial Catalog=Adventure Works DW 2008 SE;");
```

```vb
Dim olapDataManager As OlapDataManager = New OlapDataManager("DataSource=http://bi.syncfusion.com/olap/msmdpump.dll; Roles=Role1; Initial Catalog=Adventure Works DW 2008 SE;")
```

### 5.4 Connecting to Mondrian Server through XMLA

The following code illustrates how to connect to the Mondrian server:

```csharp
// Connecting to Mondrian Server

OlapDataManager DataManager = new OlapDataManager("Data Source = http://localhost:8080/mondrian/xmla; Initial Catalog = FoodMart;");
// Where localhost is the machine name which has installed Mondrian Services. For example http://bi.syncfusion.com:8080/mondrian/xmla
DataManager.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.Mondrian;
```

## Page-level Navigation/TOC (if applicable)
- Overview
  - Olap Common
  - Establish Role-based Connection
  - Connecting to Mondrian Server through XMLA

## API Reference (if applicable)
- `Syncfusion.Olap.DataProvider.IDataProvider`
- `Syncfusion.Olap.DataProvider.AdomdDataProvider`
- `OlapDataManager`

### WinForms-specific conventions
- `Syncfusion.Olap.DataProvider.IDataProvider`
- `Syncfusion.Olap.DataProvider.AdomdDataProvider`
- `OlapDataManager`

## Code Examples (multi-language supported)
- C# Example for establishing a Role-based connection
  ```csharp
  OlapDataManager olapDataManager = new OlapDataManager(@"DataSource=http://bi.syncfusion.com/olap/msmdpump.dll; Roles=Role1; Initial Catalog=Adventure Works DW 2008 SE;");
  ```
- VB Example for establishing a Role-based connection
  ```vb
  Dim olapDataManager As OlapDataManager = New OlapDataManager("DataSource=http://bi.syncfusion.com/olap/msmdpump.dll; Roles=Role1; Initial Catalog=Adventure Works DW 2008 SE;")
  ```
- C# Example for connecting to Mondrian Server
  ```csharp
  OlapDataManager DataManager = new OlapDataManager("Data Source = http://localhost:8080/mondrian/xmla; Initial Catalog = FoodMart;");
  DataManager.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.Mondrian;
  ```

## Cross References
- See also: [MSOLAP Provider](https://docs.syncfusion.com/windowsforms/olap/msolap-provider/)

<!-- tags: [product, module, control, api, version?] keywords: [Olap Common, Role-based Connection, Mondrian Server, XMLA, C#, VB, Syncfusion Winforms, 11.4.0.26] -->
```