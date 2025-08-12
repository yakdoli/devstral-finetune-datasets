```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_411.jpeg
document_name: grid
page_number: 411
page_id: grid#page_411
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:15:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- This document provides examples of serializing and deserializing grid schema information using Binary and XML techniques in both C# and VB.NET.

## Content

### Serializing Grid Schema Information Using Binary Technique

- **Using C#**
  ```csharp
  [C#]
  this.gridControl1.Model.SaveBinary(dlg.FileName);
  ```

- **Using VB.NET**
  ```vb
  [VB.NET]
  Me.gridControl1.Model.SaveBinary(dlg.FileName);
  ```

### Deserializing Grid Schema Information Using Binary Technique

- **Using C#**
  ```csharp
  [C#]
  this.gridControl1.Model = GridModel.LoadBinary(dlg.FileName);
  this.gridControl1.Refresh();
  ```

- **Using VB.NET**
  ```vb
  [VB.NET]
  Me.gridControl1.Model = GridModel.LoadBinary(dlg.FileName)
  Me.gridControl1.Refresh()
  ```

### XML

- **Using C#**
  ```csharp
  [C#]
  ```
  
  - This example demonstrates serialization of grid schema information using the XML technique.

## Code Examples

- **Serialization Using XML in C#**
  ```csharp
  [C#]
  ```

<!-- tags: [grid, schema, serialization, deserialization, binary, xml, c#, vb.net] keywords: [Essential Grid, GridControl, SaveBinary, LoadBinary, Model, Refresh, XML] -->
```