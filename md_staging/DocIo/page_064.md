```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_064.jpeg
document_name: DocIo
page_number: 064
page_id: DocIo#page_064
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:10Z
fidelity: lossless
-->

## <i>Essential DocIO</i>

### Document Methods and Descriptions

| Method Name               | Description                                                 |
|---------------------------|-------------------------------------------------------------|
| GetText                   | Gets the document's text.                                   |
| ImportContent             | Imports all content into document.                         |
| ImportSection             | Imports section into document.                             |
| Open                      | Opens doc file.                                            |
| OpenTxt                   | Opens the document in text format.                         |
| OpenXml                   | Opens the document in xml format.                          |
| Replace                   | Replaces all entries of given string.                     |
| Save                      | Saves WordDocument instance to the specified file format.  |
| OpenReadOnly              | Open the document in ReadOnly mode.                        |
| UpdateDocumentFields()    | Updates the fields present in the document.               |
| RemoveMacros              | Removes the macros in the document                         |

### Example of Using Open and Save Methods

#### Overview
This example demonstrates how to use the **Open** and **Save** methods provided by the Essential DocIO library. The example shows opening an existing document, creating a new document, cloning the content from the source document, and then saving the new document.

#### Code Examples

##### C#

```csharp
// Open the Word document
WordDocument sourceDoc = new WordDocument();
sourceDoc.Open("SourceDocument.doc", FormatType.Doc);

// Create a new word document with one section and one paragraph
WordDocument doc = new WordDocument();
doc.EnsureMinimal();

// Clone the content of source document to the newly created document
doc = sourceDoc.Clone();

// Save the document as xml
doc.Save("Document.doc", FormatType.Doc);
```

##### VB.NET

```vb
' Open the Word document
```

## Summary

This page provides a concise summary of the methods available for document manipulation using the Essential DocIO library, highlighting the use of the **Open** and **Save** methods through practical examples in C#. Users can leverage these methods to manage and modify documents effectively.

<!-- tags: [Essential DocIO, document manipulation, Open method, Save method, C# examples] keywords: [get text, import content, import section, open doc, open txt, open xml, replace, save, open read only, update document fields, remove macros] -->
```