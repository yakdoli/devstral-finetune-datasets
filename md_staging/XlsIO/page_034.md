```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_034.jpeg
document_name: XlsIO
page_number: 034
page_id: XlsIO#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:50:10Z
fidelity: lossless
-->

# Essential XlsIO

The following steps will guide you to create and add XlsIO document to this application:

## Overview
- Import the Syncfusion.XlsIO namespace.
- Create an instance of XlsIO using the ExcelEngine class.
- Instantiate the Excel application interface through the `IApplication` object.

## Content

### Importing the Syncfusion.XlsIO Namespace

1. **Add the following C# code to import the Syncfusion.XlsIO namespace.**

   ```csharp
   using Syncfusion.XlsIO;
   ```

   The Syncfusion.XlsIO namespace is imported.

### Creating an Instance of XlsIO

2. **Create an instance of XlsIO by using the following code.**

   **C#**
   ```csharp
   // New instance of XlsIO is created. [Equivalent to launching MS Excel with no workbooks open].
   // Instantiate the spreadsheet creation engine.
   ExcelEngine excelEngine = new ExcelEngine();
   ```

   **VB.NET**
   ```vb.net
   ' New instance of XlsIO is created. [Equivalent to launching MS Excel with no workbooks open].
   ' Instantiate the spreadsheet creation engine.
   Dim excelEngine As ExcelEngine = New ExcelEngine()
   ```

   An instance of XlsIO is created.

   **Note:** See `Excel Engine` for more details.

### Creating the Excel Application Instance

3. **Create an instance of the Excel application through the `IApplication` interface.**

   **C#**
   ```csharp
   // Instantiate the Excel application object.
   IApplication application = excelEngine.Excel;
   ```

   **VB.NET**
   ```vb.net
   ' Instantiate the Excel application object.
   ```

   <!-- tags: [syncfusion, xlsio, namespace, excelengine, iapplication, winforms, sdk, version] keywords: [xlsio, syncfusion, csharp, vb.net, namespace, excelengine, iapplication] -->
```