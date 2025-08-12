```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_016.jpeg
document_name: Olap Common
page_number: 016
page_id: Olap Common#page_016
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:24Z
fidelity: lossless
-->

# Essential OlapCommon

---

## Overview

- Establishing a connection with the XMLA Server using web standards like HTTP, SOAP, and XML.
- Using MDX as the query language for accessing multi-dimensional data stores.
- Scenarios for efficient OLAP database access over the internet.
- Connection code examples for Mondrian and Active Pivot servers.

---

## Content

### Establishing connection with XMLA Server:

XML for Analysis (XMLA) is a standard that allows client applications to transfer multi-dimensional or OLAP data sources, which is available in the Mondrian Server. The back-and-forth communication is done using web standards – HTTP, SOAP, and XML. The query language used is MDX, which is most widely supported for reporting from multi-dimensional data stores.

#### Use Case Scenarios

XMLA provides the most efficient way to access an OLAP database over the Internet.

#### Connecting to Mondrian Server

The following code illustrates how to connect to the Mondrian server:

#### C#

```csharp
// Connecting to Mondrian Server
OlapDataManager DataManager = new OlapDataManager("Data Source = http://localhost:8080/mondrian/xmla; Initial Catalog = FoodMart;");
DataManager.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.Mondrian;
```

#### VB

```vb
' Connecting to Mondrian Server
Dim DataManager As OlapDataManager = New OlapDataManager("Datasource = http://bi.syncfusion.com:8080/mondrian/xmla; Initial Catalog=FoodMart;")
DataManager.DataProvider.ProviderName = Syncfusion.Olap.DataProvider.Providers.Mondrian
```

[Click here](#) for more information about Mondrian XMLA configurations.

### Connecting to Active Pivot Server

The following code illustrates how to connect to Active Pivot server:

---

## Page-level Navigation/TOC

- Establishing connection with XMLA Server
- Use Case Scenarios
  - Connecting to Mondrian Server
  - Connecting to Active Pivot Server

## Cross References

- See also: Mondrian XMLA configurations

---

<!-- tags: [syncfusion-sdk, olap, xmla, mondrian server, active pivot server, olapdata, winforms, multi-dimensional data, mdx, xmla configurations] keywords: [xmla, olap, mdx, mondrian server, active pivot, data connection, winforms, syncfusion] -->
```