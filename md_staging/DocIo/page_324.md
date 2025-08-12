```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_324.jpeg
document_name: DocIo
page_number: 324
page_id: DocIo#page_324
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:49:40Z
fidelity: lossless
-->

# Essential DocIO

## 5.8 How to set the Page Size of the Document Section?

The page size of the document section is set by using the `PageSize` property of the PageSetup object. The following code snippet illustrates how to set this property.

### Code Examples

#### C#
```csharp
document.Sections[0].PageSetup.PageSize = PageSize.B6;
```

#### VB.NET
```vb
document.Sections(0).PageSetup.PageSize = PageSize.B6
```

## 5.9 How to set OpenType features?

The open type features provide special effects for text, in order to make them more refined and easier to read. This support is provided specifically for Word 2010 documents. Microsoft Word 2010 has new open type features for a font that supports these features, to make your documents look professional when printed. When font designers create fonts, they often add designs for special features.

### Overview of OpenType features

The OpenType features include:

- Ligatures
- Use Contextual Alternates
- Number spacing
- Number forms
- Stylistic sets

### Ligatures

#### Example of OpenType Features in MS Word

![](Figure: MS Word Open Type Features for Font)

Figure 88: MS Word Open Type Features for Font

### Ligatures

#### Explanation

Ligatures are a specific design feature in fonts where certain letter combinations are replaced with a single, more aesthetically pleasing character. This feature enhances the readability and style of the text, making it look more refined and professional.

---

## API Reference

This section provides references to the properties and methods mentioned in the document.

### Properties

- **PageSize**  
  Property of the `PageSetup` object used to set the size of the document section.

### Enumerations

- **PageSize**  
  Enum used to specify different page sizes, such as B6.

## Cross References

- For more information on OpenType features and their implementation, refer to the Word 2010 documentation or additional resources.

<!-- tags: [DocIO, opensource, document formatting, page setup, OpenType features, Word 2010, Microsoft Word, fonts, ligatures, numner spacing, numner forms, stylistic sets] keywords: [OpenType, document section, page size, formatting, font features, Word 2010, Microsoft Word, ligatures, number spacing, number forms, stylistic sets] -->
```