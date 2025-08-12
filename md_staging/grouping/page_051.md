<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: grouping
page_number: 051
page_id: grouping#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:00:44Z
fidelity: lossless
-->

# Essential Grouping

## 4.3.4 Custom Sorting

We used a simplest overload in the previous section for sorting the data. The `TableDescriptor.SortedColumns.Add` method has three overloads as shown below:

- `Add(string propertyName)`
- `Add(string propertyName, ListSortDirection dir)`
- `Add(SortColumnDescriptor sdc)`

The following code snippets illustrate the syntax for these overloads:

```csharp
[C#]

public int Add(string propertyName);
public int Add(string propertyName, ListSortDirection dir);
public int Add(SortColumnDescriptor sdc);
```

## Page-Level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, include it here with links/text as shown.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Code Examples (multi-language supported)
- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.

## RAG Annotations
- Add tags and keywords derived ONLY from visible content:
  <!-- tags: [Syncfusion, WinForms, CustomSorting, TableDescriptor, SortedColumns, Add, Overloads] keywords: [Custom Sorting, TableDescriptor, SortedColumns, Add, Overloads, C# Syntax, Property Sorting, ListSortDirection, SortColumnDescriptor] -->
