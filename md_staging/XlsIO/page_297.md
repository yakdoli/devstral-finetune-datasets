```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_297.jpeg
document_name: XlsIO
page_number: 297
page_id: XlsIO#page_297
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:08:25Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- Demonstrates how to embed a package and display it as an icon.
- Explains setting the location of an object within a worksheet.

## Content

### Displaying a Package as an Icon

Run the code. The following output is generated.

![Figure 100: Displayed as Icon](https://example.com/figure100.png)

*Figure 100: Displayed as Icon*

### Setting the Location of an Object

The following set of code sample illustrates the condition when the location is set to K column, 8th cell.

#### Code Snippets

- **C#**
  ```csharp
  oleObject1.Location = sheet["K8"];
  ```

- **VB.NET**
  ```vb
  oleObject1.Location = sheet("K8")
  ```

### Output Generation

Run the code. The following output is generated.

## API Reference
- **Methods:** `oleObject1.Location = sheet["K8"]`

## Code Examples
- **C# Example**
  ```csharp
  oleObject1.Location = sheet["K8"];
  ```

- **VB.NET Example**
  ```vb
  oleObject1.Location = sheet("K8")
  ```

<!-- tags: [XlsIO, package embedding, object location, icon display] keywords: [oleObject1, sheet, K8, C#, VB.NET] -->
```