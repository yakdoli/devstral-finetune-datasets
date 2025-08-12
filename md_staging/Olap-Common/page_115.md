<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_115.jpeg
document_name: Olap Common
page_number: 115
page_id: Olap Common#page_115
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:21:35Z
fidelity: lossless
-->

# Essential OlapCommon

## Overview
- Describes the process of inheriting a WCF service with `IOLapDataProvider`.
- Explains how to connect to a database using the WCF service.
- Provides a code snippet to implement the `IOLapDataProvider` interface.

## Content

### Adding a New WCF Service

**Figure 18: Add New Item Dialog (WCF Service)**  
![Add New Item Dialog (WCF Service)](image_link)

1. **Inherit the newly added WCF service with `IOLapDataProvider`**:  
   Ensure that the newly added WCF service is inherited with the `IOLapDataProvider` interface and explicitly implements it.

2. **Connecting to the database using the WCF service**:  
   The connection to the database is facilitated through the WCF service. The service must be created and instantiated as described in the following code snippet.

### Implementing the `IOLapDataProvider` Interface

The WCF Service must implement the `IOLapDataProvider` interface. To implement this interface, you require the `OlapDataProvider`, which can be instantiated by passing the connection string.

#### Code Snippet to Implement the `IOLapDataProvider` Interface

```csharp
public class OlapManager : IOLapDataProvider
{
    Syncfusion.OlapSilverlight.Manager.OlapDataProvider dataManager;

    /// <summary>
```

## API Reference (if applicable)
- Namespace and Class details for `IOLapDataProvider` and `OlapDataProvider`.

## Code Examples
- The provided code snippet demonstrates the implementation of the `IOLapDataProvider` interface.

## Page-level Navigation/TOC (if applicable)
- Refer to the OCR content for any local Table of Contents or section headings.

## Cross References
- Refer to related documentation for more information on `IOLapDataProvider` and `OlapDataProvider`.

## RAG Annotations
<!-- tags: [product: Syncfusion Winforms, module: Essential Olap, api: IOLapDataProvider, version: 11.4.0.26] keywords: [WCF Service, IOLapDataProvider, OlapDataProvider, database connection, implementation, code snippet] -->