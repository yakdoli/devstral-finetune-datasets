```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_011.jpeg
document_name: Olap Common
page_number: 011
page_id: Olap Common#page_011
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:15:06Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Provides an overview of how the class library is organized under the Syncfusion.OlapSilverlight.BaseWrapper assembly.
- Describes the use of WCF Service in OLAP Silverlight controls for querying the database.
- Explains the role of the DataProvider property of OlapDataManager in service call operations.
- Guides on creating and connecting a WCF Service.

## Content

### 3.3.1 WCF Service

**Note:** This class library was organized under `Syncfusion.OlapSilverlight.BaseWrapper` assembly.

To query the database, OLAP Silverlight controls use WCF Service. The `DataProvider` property of `OlapDataManager` performs the service call operations. For more details on creating and connecting a WCF Service, refer to the section **Creating and connecting a WCF Service.**

## API Reference

- **Namespace:** Syncfusion.OlapSilverlight.BaseWrapper
- **Class:** OlapDataManager
  - Properties:
    - `DataProvider`: Handles service call operations for database queries.

## Code Examples

```csharp
// Example of setting up WCF Service connection
using Syncfusion.OlapSilverlight.BaseWrapper;

var olapDataManager = new OlapDataManager();
olapDataManager.DataProvider = new WCFServiceDataProvider();
```

## Page-level Navigation/TOC (if applicable)

- [3.3.1 WCF Service]
  - Overview
  - Creating and connecting a WCF Service

## Cross References

See also:
- Syncfusion.OlapSilverlight.BaseWrapper assembly
- WCFServiceDataProvider

## RAG Annotations

<!-- tags: [syncfusion, winforms, olapcontrols, wcf, dataprovider] keywords: [syncfusion, olap, silverlight, basewrapper, wcf, service, database, query, dataprovider, wcfserVICEDataprovider] -->
```