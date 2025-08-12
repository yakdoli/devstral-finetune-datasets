```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_014.jpeg
document_name: Olap Common
page_number: 014
page_id: Olap Common#page_014
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:22Z
fidelity: lossless
-->

# Essential OlapCommon

| Method Name             | Description                                                                 | Parameters | Return Type | Reference Link |
|-------------------------|-----------------------------------------------------------------------------|------------|--------------|----------------|
|                         | member.                                                                     | -          | -            | -              |
| ValidateConnectionString | This method will validate the specified connection string in the data manager or in the data provider and return the validated status. | -          | bool         | -              |

## OlapDataManager

OlapDataManager is the most important class in the whole OLAP Base. All the information transfers from the control to OLAP base will happen through this class and this will retain the current state of the base objects. The connection is established in the Data provider of the OLAP Base, but the information required in establishing the connection is given to the data provider through the OlapDataManager.

### Table 3: Constructors

| Constructors                         | Description                                                                 | Parameters              | Return Type | Reference Link |
|--------------------------------------|-----------------------------------------------------------------------------|--------------------------|--------------|----------------|
| OlapDataManager()                   | Default constructor                                                      | -                        | Void         | -              |
| OlapDataManager(string)             | Accepts the connection string as argument and passes it to the Data Provider to establish the connection with data source. | String                 | Void         | -              |
| OlapDataManager(AdomdDataProvider)  | Accepts the Data Provider as argument and processes the cube that is connected with the given data provider.          | AdomdDataProvider      | Void         | -              |

### Establishing connection with the SSAS server

The following code snippet describes establishing connection with the server:

```csharp
OlapDataManager olapDataManager = new OlapDataManager("DataSource=local
```

## Code Examples

### C#

```csharp
OlapDataManager olapDataManager = new OlapDataManager("DataSource=local);
```

<!-- tags: [olapcommon, olapdata-manager, object-oriented-programming, cis, sql server] keywords: [essentials, connection string, data manager, constructor, adomd-data-provider, ssas server] -->
```