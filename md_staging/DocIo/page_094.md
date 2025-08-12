<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_094.jpeg
document_name: DocIo
page_number: 094
page_id: DocIo#page_094
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:23Z
fidelity: lossless
-->

## Summary

This page discusses font substitution tables and provides examples in C# and VB.NET for modifying such tables. It also delves into the `WSection` class, which represents a single section in a document, focusing on its properties, collections, and configurations.

## Font Substitution Table

### Font Substitution Table Overview

- **Note**: In some cases, MS Word preserves the alternate font based on information stored in the application cache. To overcome this, close all open instances of MS Word and re-instantiate the document.

- The following code snippets illustrate how to access and modify the font substitution table in both C# and VB.NET.

#### C# Code Example

```csharp
// Updating alternate font name in font substitution table
if (document.FontSubstitutionTable.ContainsKey("Arial (W1)"))
    document.FontSubstitutionTable["Arial (W1)"] = "Gabriola";
else
    document.FontSubstitutionTable.Add("Arial (W1)", "Gabriola");
```

#### VB.NET Code Example

```vb.net
' Updating alternate font name in font substitution table
If document.FontSubstitutionTable.ContainsKey("Arial (W1)") Then
    document.FontSubstitutionTable("Arial (W1)") = "Gabriola"
Else
    document.FontSubstitutionTable.Add("Arial (W1)", "Gabriola")
End If
```

### Section Properties

The `WSection` class represents a single section in a document. Each section is a region with its own:

- **PageSetup Options**
- **HeadersFooters**
- **Paragraphs Collection**

#### Validating a Section

- **Minimum Requirement**: A valid section must contain at least one empty paragraph.
- **Page Setup**: Each section can have its own page setup, accessible through the `PageSetup` property. This allows setting page size, orientation, margins, etc.

#### Section Collections

The `WSection` section holds four different collections:

- **Paragraphs**: Collection of section paragraphs.
- **Tables**: Collection of section tables.
- **ChildEntities**: General collection that includes paragraphs and tables.
- **Columns**: Collection of columns, which logically divides a page into multiple printing/publishing areas.

### Page-Level Properties

- **Page Setup**:
  - **Accessible Through**: `PageSetup` property.
  - **Configurable Attributes**: Page size, orientation, margins, etc.

## RAG Annotations

<!-- tags: [DocIo, WSection, font substitution, section properties, page setup, VB.NET, C#] keywords: [alternate font, page subdivision, paragraphs, tables, headers, footers, columns, font substitution table, document section, section collections, WSection] -->