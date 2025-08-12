```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_081.jpeg
document_name: Olap Common
page_number: 081
page_id: Olap Common#page_081
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:20:19Z
fidelity: lossless
-->

## Essential OlapCommon

### Code Example: Connecting to Mondrian Server

```vb
' Connecting to Mondrian Server
Dim DataManager As OlapDataManager = New OlapDataManager("Datasource = http://bi.syncfusion.com:8080/mondrian/xmla; Initial Catalog=FoodMart;")
DataMgr.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.Mondrian
```

Click [here](#more-information-about-mondrian-xmla-configurations) for more information about Mondrian XMLA configurations.

### 5.5 Connect ActivePivot Server through XMLA

The user can connect the Active Pivot server through XMLA (XML for Analysis) services using the OlapDataManager in our OLAP controls.

The following code illustrates how to connect to Active Pivot server:

#### C#

```csharp
// Connecting to Active Pivot Server
OlapDataManager DataManager = new OlapDataManager(@"Data Source=http://localhost:8081/var_s/xmla; Initial Catalog=VaRCubes; User ID=; Password=; Transport Compression=None;");
DataManager.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.ActivePivot;
```

#### VB

```vb
' Connecting to Active Pivot Server
Dim DataManager As OlapDataManager = New OlapDataManager("Data Source=http://localhost:8081/var_s/xmla; Initial Catalog=VaRCubes; User ID=; Password=; Transport Compression=None;")
DataMgr.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.ActivePivot
```

Click [here](#more-information-about-active-pivot-server) for more information about Active Pivot server.

### 5.6 Create a WCF Service for Silverlight OLAP Control

The following steps will define the adding of WCF Service to the Web project and configuring it with `IOLapDataProvider`:

## API Reference

### WinForms-specific conventions

Namespaces, Classes, Members (Methods/Properties/Events/Enums) in subsections.
- Parameters table: Name | Type | Description | Default | Required
- Returns: Type + description.
- Exceptions: bullet list.

## Code Examples

Extract all code exactly. Use fenced blocks with language: `csharp`, `vb`, `xml`, `xaml`, `js`, `css`, `ts`, `python`.

## Cross References

See also:موندريان، إيس بي، XMLA، بروسرس، مشيف وشقف للو想到了

## RAG Annotations

Tags: [Syncfusion Winforms, Olap Common, Mondrian Server, XMLA, ActivePivot, WCF Service, Silverlight OLAP Control]
Keywords: [OlapDataManager, ProviderName, DataProvider, Mondrian, ActivePivot, WCF Service, Silverlight, OLAP]
```

<!-- tags: [Syncfusion Winforms, Olap Common, Mondrian Server, XMLA, ActivePivot, WCF Service, Silverlight OLAP Control] keywords: [OlapDataManager, ProviderName, DataProvider, Mondrian, ActivePivot, WCF Service, Silverlight, OLAP] -->
```