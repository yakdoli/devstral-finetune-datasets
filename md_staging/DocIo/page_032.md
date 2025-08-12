```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_032.jpeg
document_name: DocIo
page_number: 032
page_id: DocIo#page_032
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:06Z
fidelity: lossless
-->

## Essential DocIO

### Overview
- It describes the DLLs to be referenced in the application for proper deployment of applications using Essential DocIO.
- Provides a brief on the dependent assemblies and namespaces required.

### Content

#### Note: Application with Essential DocIO
**Figure 16: DLLs to be referenced in the Application**

Note: Application with Essential DocIO needs the following dependent assemblies for deployment:
- Syncfusion.Core.dll
- Syncfusion.Compression.dll
- Syncfusion.DocIO.Base.dll

Note: For detailed documentation on Windows Application deployment, see [http://www.syncfusion.com/support/user/uploads/DeployingWindowsApplication_bdaf76f7.pdf](http://www.syncfusion.com/support/user/uploads/DeployingWindowsApplication_bdaf76f7.pdf).

Essential DocIO is deployed in the Windows application.

#### Creating a Word Document

**In this section, you will learn how to create a simple Word document with "Hello World" written on the first paragraph of the first section.**

1. Include the following namespaces in your application.
   - Syncfusion.DocIO.DLS (using Syncfusion.DocIO.DLS)
   - Syncfusion.DocIO (using Syncfusion.DocIO)

2. Instantiate the `WordDocument` class.

##### Code Example: Creating a Word Document

**C#**
```csharp
// Create a new Word document.
// This document has no section and no paragraph by default.
WordDocument document = new WordDocument();
```

**VB.NET**
```vbnet
' Create a new Word document.
' This document has no section and no paragraph by default.
Dim document As WordDocument = New WordDocument()
```

### RAG Annotations
<!-- tags: [Essential DocIO, Syncfusion Winforms, DocIO deployment, namespaces, dependent assemblies] keywords: [DocIO, WordDocument, namespaces, deployment, Hello World, code example, C#, VB.NET] -->
```