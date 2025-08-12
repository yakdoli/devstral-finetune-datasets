```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_206.jpeg
document_name: DocIo
page_number: 206
page_id: DocIo#page_206
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:41:06Z
fidelity: lossless
-->

# Essential DocI0

```csharp
// Get a collection of styles defined in the document.
IStyleCollection coll = document.Styles;

// Access particular style.
IStyle style= coll.FindByName(string StyleName) ;
IStyle style= coll.FindByName(string StyleName, StyleType styleType) ;
IStyle style1 = coll[0];
```

```vb.net
' Get a collection of styles defined in the document.
Dim coll As IStyleCollection = document.Styles

' Access particular style.
Dim style As IStyle = coll.FindByName(String StyleName)
Dim style As IStyle = coll.FindByName(String StyleName, StyleType styleType)
Dim style1 As IStyle = coll(0)
```

## 4.4.2.2 Character Styles and Formats

### Character Styles

The CharacterStyle class represents character style in the Word document. CharacterStyle has two properties:

- **StyleType**: returns the StyleType.CharacterStyle
- **BaseStyle**: defines the base character style

The collection of DocI0 character styles is accessible through the **WordDocument.Styles** property.

> **Note:** DocI0 does not provide support to add user-defined character styles to the document.

### Class Hierarchy

- Style
  - CharacterStyle

<!-- tags: [DocIo, Syncfusion, Winforms, CharacterStyles, WordDocument, IStyleCollection, IStyle, StyleType] keywords: [character styles, formatting, DocI0, Word document, style types, base styles] -->
```