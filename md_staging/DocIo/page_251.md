```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_251.jpeg
document_name: DocIo
page_number: 251
page_id: DocIo#page_251
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:43:55Z
fidelity: lossless
-->

## TextBodyPart Class

The following table outlines the constructors and methods available for the `TextBodyPart` class, which is part of the `DocIO` library for handling Word documents. This class allows developers to manipulate and interact with the content of a Word document by working with specific sections or parts of the document, such as the body.

### Constructors

| Constructor | Description |
|-------------|-------------|
| `TextBodyPart.TextBodyPart (TextBodySelection)` | Initializes a new instance of the `TextBodyPart` class. |
| `TextBodyPart.TextBodyPart (TextSelection)` | Initializes a new instance of the `TextBodyPart` class. |
| `TextBodyPart.TextBodyPart (WordDocument)` | Initializes a new instance of the `TextBodyPart` class. |

### Public Properties

| Name        | Description         |
|-------------|---------------------|
| `BodyItems` | Gets the body items. |

### Public Methods

| Name         | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `Clear`      | Clears this instance.                                                       |
| `Copy`       | Copies the specified item.                                                  |
| `PasteAfter` | Pastes ParagraphItem or TextBodyItem after specified item.                |
| `PasteAt`    | Pastes ITextBody at specified position.                                    |
| `PasteAtEnd` | Pastes ITextBody at end of textbody.                                       |

### Using the TextBodyPart Class

The following example illustrates how to use the `TextBodyPart` class in both C# and VB.NET.

#### Example: Using TextBodyPart in C#

```csharp
WordDocument doc = new WordDocument("sample.doc");
BookmarksNavigator bn = new BookmarksNavigator(doc);
bn.MoveToBookmark("bookmark1");
TextBodyPart bodyPart = bn.GetBookmarkContent();
```

#### Example: Using TextBodyPart in VB.NET

```vb
Dim doc As WordDocument = New WordDocument("sample.doc")
```

## API Reference

### Methods

- **Clear**: Clears the content of this `TextBodyPart` instance.
- **Copy**: Creates a copy of the specified item in the document.
- **PasteAfter**: Pastes a paragraph or text element after a specified item in the document.
- **PasteAt**: Pastes a paragraph or text element at a specific position within the document.
- **PasteAtEnd**: Pastes a paragraph or text element at the end of the document.

### Properties

- **BodyItems**: Provides access to the items within the body of the document.

### Constructors

- **TextBodyPart (TextBodySelection)**: Initializes a new instance of the `TextBodyPart` class using a `TextBodySelection`.
- **TextBodyPart (TextSelection)**: Initializes a new instance of the `TextBodyPart` class using a `TextSelection`.
- **TextBodyPart (WordDocument)**: Initializes a new instance of the `TextBodyPart` class using a `WordDocument`.

## Summary
This section provided an overview of the `TextBodyPart` class and its key methods and properties. The examples illustrate how to initialize and manipulate document content using this class.

<!-- tags: [DocIo, TextBodyPart, WordDocument, BookmarksNavigator] keywords: [text body, document manipulation, bookmarks, navigation] -->
```