```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_008.jpeg
document_name: Olap Common
page_number: 008
page_id: Olap Common#page_008
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:14:54Z
fidelity: lossless
-->

# 3 Syncfusion OLAP Architecture

Syncfusion OLAP architecture allows you to build a full life cycle reporting solution for your enterprise. Here are the important pieces of the architecture:

- **OLAP Access Layer** - Built on top of ADOMD.NET and provides a high-level object model to let you easily define reports.
- **OLAP Controls** - Chart, Grid, Gauge, Client for ASP.NET (excluding Gauge), WPF, Silverlight, ASP.NET MVC (Grid only).
- **OLAP Report Builder** – RAD (Rapid Application Development) tool lets you select the dimensions you are interested in visualizing and also lets you define the appearance for the Chart and Grid.

## Overview
- The Syncfusion OLAP components enable the creation of a full life cycle reporting solution for your enterprise.

## Content
The following screenshot shows how the Syncfusion OLAP components allow you to build a full life cycle reporting solution for your enterprise.

### Diagram of Syncfusion OLAP Components

```markdown
UI Controls
|
v
Synfusion AdomdDataProvider ↔ OLAP DataManager (ODM)
|
v
Adomd.Net Provider (Microsoft.AnalysisServices.AdmdClient)
|
v
XML Data Provider
|
v
SOAP
|
v
XML Data Provider
|
v
OLAP Servers  SQL Server Analysis Server
```

### Explanation of the Diagram
1. **UI Controls**:
   - The user interacts with UI controls to visualize and manipulate data.

2. **Synfusion AdomdDataProvider**:
   - This component communicates with the OLAP DataManager (ODM) to access and manage OLAP data.

3. **OLAP DataManager (ODM)**:
   - Manages the data model for OLAP operations.

4. **Adomd.Net Provider**:
   - Connects to the OLAP server using the Microsoft.AnalysisServices.AdmdClient.

5. **Query Builder**:
   - Allows users to construct and define queries for data retrieval.

6. **XML Data Provider**:
   - Acts as a middleware for data communication.

7. **SOAP**:
   - Provides a communication protocol for data exchange.

## API Reference
- Not explicitly detailed in the image, but refers to ADOMD.NET and related interfaces for OLAP operations.

## Code Examples
- No explicit code examples provided in the text.

## RAG Annotations
<!-- tags: [Olap, OLAP, Syncfusion, Winforms, reporting, ADOMD.NET, architecture, OLAP Controls, Report Builder] keywords: [Syncfusion OLAP, reporting, UI Controls, OLAP Access Layer, OLAP Controls, OLAP Report Builder, AdomdDataProvider, OLAP DataManager, Adomd.Net Provider, Query Builder, XML Data Provider, SOAP, Microsoft.AnalysisServices.AdmdClient, SQL Server Analysis Server] -->
```