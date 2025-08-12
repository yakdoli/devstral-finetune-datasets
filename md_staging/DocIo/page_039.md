```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_039.jpeg
document_name: DocIo
page_number: 039
page_id: DocIo#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:27Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates how to deploy and use Essential DocIO in a WPF application.
- Includes detailed steps for adding references and creating a Word document programmatically.
- Provides C# and VB.NET code examples for creating a `WordDocument` object.

## Content

### Deploying Essential DocIO in a WPF Application

1. Go to the **Solution Explorer** of the application you have created. Right-click the **Reference** folder and then click **Add References**.
2. Add the following assemblies as references in the application:
   - `Syncfusion.Core.dll`
   - `Syncfusion.Compression.Base.dll`
   - `Syncfusion.DocIO.Base.dll`

**Note:** There is no toolbox support for DocIO in WPF application.

Essential DocIO is now deployed in the WPF application.

### Creating a Word Document

In this section, you will learn how to create a simple Word document with "Hello World" written on the first paragraph of the first section.

#### Steps to Create a Word Document

1. Include the following namespaces in your application:
   - `Syncfusion.DocIO.DLS` (using `Syncfusion.DocIO.DLS`)
   - `Syncfusion.DocIO` (using `Syncfusion.DocIO`)
2. **Instantiate the `WordDocument` class**.

   **C#**
   ```csharp
   // Create a new Word document.
   // This document has no section and no paragraph by default.
   WordDocument document = new WordDocument();
   ```

   **VB.NET**
   ```vb.net
   ' Create a new Word document.
   ' This document has no section and no paragraph by default.
   Dim document As WordDocument = New WordDocument()
   ```

**Note:** The `WordDocument` class represents the Word documents created in memory. This is the memory representation of the Word document written to disk.

3. Add a section to the newly created Word document by using the following code.

## API Reference

### Namespaces Used
- `Syncfusion.DocIO.DLS`
- `Syncfusion.DocIO`

## Code Examples

### Creating a `WordDocument`

#### C#
```csharp
WordDocument document = new WordDocument();
```

#### VB.NET
```vb.net
Dim document As WordDocument = New WordDocument()
```

## Page-level Navigation/TOC
- Deploying Essential DocIO in a WPF Application
- Creating a Word Document

### Cross References
See also:
- [Syncfusion DocIO Documentation](#)
- [Reference Documentation for Essential DocIO](#)

<!-- tags: [Essential DocIO, WPF, Word Document, Syncfusion Winforms, C#, VB.NET, API Reference] keywords: [DocIO, WPF, Word Document, Syncfusion, C#, VB.NET, namespaces, WordDocument, Section] -->
```