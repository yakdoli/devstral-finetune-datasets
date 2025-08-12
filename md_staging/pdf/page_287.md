```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_287.jpeg
document_name: pdf
page_number: 287
page_id: pdf#page_287
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:17Z
fidelity: lossless
-->

## Essential PDF

### 4.2.10 Tutorial

This tutorial will show you how easy it is to get started using Essential PDF. It will give you a basic introduction to the concepts you need to know before getting started with the product and some tips and ideas on how to implement PDF into your projects. The lessons in this tutorial are meant to introduce you to PDF with simple step-by-step procedures.

---

## Features

### 4.2.10.1 Merge PDF

Essential PDF supports the merging of multiple PDF documents. It can merge multiple documents from stream as well as the files stored on the disk.

#### Merging Techniques Discussed in This Section:

- Merging Multiple Documents from Disk
- Merging Multiple Documents from Stream
- Merging Two Files using Append method
- Merging pages of different Documents

#### Merging Multiple Documents from Disk

The following code example illustrates how to merge multiple documents.

##### Example in C#:

```csharp
// Create a string array of source files which are to be merged.
string[] source = { source1, source2 };

// Merge PDFDocument.
PdfDocument.Merge(destination, source);
```

##### Example in VB.NET:

```vb.net
' Create a string array of source files which are to be merged.
Dim source As String() = { source1, source2 }

' Merge PDFDocument.
PdfDocument.Merge(destination, source)
```

#### Merge Multiple Documents from Stream
