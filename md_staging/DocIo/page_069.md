```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_069.jpeg
document_name: DocIo
page_number: 069
page_id: DocIo#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:47Z
fidelity: lossless
-->

# Essential DocIO

```csharp
WordDocument doc = new WordDocument();
doc.Open( "DocumentProperties.doc" );

string author = doc.BuiltinDocumentProperties.Author;
int bytesCount = doc.BuiltinDocumentProperties.BytesCount;
doc.BuiltinDocumentProperties.Keywords += "document properties";
doc.BuiltinDocumentProperties.Author = "Author's name";
doc.BuiltinDocumentProperties.Comments = "Document comments";
```

```vbnet
Dim doc As WordDocument = New WordDocument()
doc.Open("DocumentProperties.doc")

Dim author As String = doc.BuiltinDocumentProperties.Author
Dim bytesCount As Integer = doc.BuiltinDocumentProperties.BytesCount
doc.BuiltinDocumentProperties.Keywords &= "document properties"

doc.BuiltinDocumentProperties.Author = "Author's name"
doc.BuiltinDocumentProperties.Comments = "Document comments"
```

## Custom Properties

The `CustomDocumentProperties` class enables you to create and save custom properties. It contains a collection of `DocumentProperty` class instances. You can access a document property by indexing, i.e., by specifying the property name or index.

## API Reference

### Properties

- **BuiltinDocumentProperties**: 
  - Type: `DocumentPropertyCollection`
  - Contains a collection of built-in document properties such as `Author`, `BytesCount`, `Keywords`, etc.
  - Allows access to and modification of these properties.

## Code Examples

### Example: Accessing and Modifying Built-in Document Properties

```csharp
// Create a new Word document
WordDocument doc = new WordDocument();

// Open an existing document
doc.Open("DocumentProperties.doc");

// Access built-in properties
string author = doc.BuiltinDocumentProperties.Author;
int bytesCount = doc.BuiltinDocumentProperties.BytesCount;

// Modify built-in properties
doc.BuiltinDocumentProperties.Keywords += "document properties";
doc.BuiltinDocumentProperties.Author = "Author's name";
doc.BuiltinDocumentProperties.Comments = "Document comments";

// Save the modified document
doc.Save("ModifiedDocument.doc");
```

### Example: Accessing and Modifying Built-in Document Properties in VB.NET

```vbnet
' Create a new Word document
Dim doc As WordDocument = New WordDocument()

' Open an existing document
doc.Open("DocumentProperties.doc")

' Access built-in properties
Dim author As String = doc.BuiltinDocumentProperties.Author
Dim bytesCount As Integer = doc.BuiltinDocumentProperties.BytesCount

' Modify built-in properties
doc.BuiltinDocumentProperties.Keywords &= "document properties"
doc.BuiltinDocumentProperties.Author = "Author's name"
doc.BuiltinDocumentProperties.Comments = "Document comments"

' Save the modified document
doc.Save("ModifiedDocument.doc")
```

## References

- [Syncfusion DocIO Documentation](https://www.syncfusion.com/documentation/docio)
- [Custom Document Properties in Word Documents](https://www.syncfusion.com/kb/essentials/docio-custom-document-properties-in-word-documents)

<!-- tags: [syncfusion, winforms, docio, document properties] keywords: [custom properties, built-in properties, document properties, document comments] -->
```