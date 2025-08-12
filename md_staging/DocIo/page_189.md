```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_189.jpeg
document_name: DocIo
page_number: 189
page_id: DocIo#page_189
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:40:28Z
fidelity: lossless
-->

# Essential DocIO

## Reference Table: Footnote and Endnote Properties

The table below details properties related to formatting markers in footnotes and endnotes:

| Property                   | Description                                                                      |
|----------------------------|--------------------------------------------------------------------------------------|
| `MarkerCharacterFormat`    | Gets the marker character format.                                                 |
| `TextBody`                 | Gets the text body.                                                              |
| `SymbolCode`               | Gets or sets the marker Symbol code.                                             |
| `CustomMarker`             | Defines custom (string) marker for footnote. If footnote is autonumbered, this property won’t have any influence (footnote will be autonumbered). |

## Overview

This page demonstrates how to create and manage footnotes and endnotes using the Essential DocIO library. The code example provided illustrates the process step-by-step, from creating a new document to saving it with added footnotes and endnotes.

## Content

### Creating a Footnote and Endnote Using Essential DocIO

The following code snippet shows how to programmatically add a footnote and an endnote to a document using the Essential DocIO library in C#:

```csharp
[C#]

// Creating a new document
WordDocument document = new WordDocument();

// Creating a section
IWSection section1 = document.AddSection();

// Adding a paragraph to a section
IWParagraph paragraph = section1.AddParagraph();

// Creating a footnote
WFootnote footnote = new WFootnote(document);

// Appending endnote
footnote = paragraph.AppendFootnote(Syncfusion.DocIO.FootnoteType.Endnote);

// Setting the footnote character format
footnote.MarkerCharacterFormat.SubSuperScript = SubSuperScript.SubScript;

// Inserting Text into the paragraph
paragraph.AppendText("Essential DocIO").CharacterFormat.Bold = true;

// Adding footnote text
paragraph = footnote.TextBody.AddParagraph();

paragraph.AppendText("Essential DocIO is a .NET library that has a simple yet and powerful object model which provides the ability to customize the document to a great extent. ");

// Saving the document to disk
document.Save("Sample.doc", Syncfusion.DocIO.FormatType.Doc);
```

### Explanation of Key Steps

1. **Creating a New Document**:
   - A new `WordDocument` object is instantiated to start building the document.

2. **Adding Sections and Paragraphs**:
   - A section is added using `document.AddSection()`, and a paragraph is appended to this section for content insertion.

3. **Creating and Adding Footnotes/Endnotes**:
   - A `WFootnote` object is created and associated with the paragraph.
   - The footnote type is specified as an endnote using `FootnoteType.Endnote`.

4. **Formatting the Footnote**:
   - The footnote's marker character format is configured, specifically setting the	subscript property.

5. **Inserting Text**:
   - Text is appended to both the main paragraph and the footnote, with formatting (e.g., bold text) applied as needed.

6. **Saving the Document**:
   - The final document is saved to disk in `.doc` format using the `Save` method.

## Key Points

- **Footnote Character Format**: The `MarkerCharacterFormat` property allows customization of the footnote marker (e.g., subscript).
- **Footnote Type**: The `FootnoteType` enumeration specifies whether it's a footer or endnote.
- **Text Formatting**: Text properties like bold can be applied using the `CharacterFormat` object.

### Notes

- Ensure that the `Syncfusion.DocIO` library is properly referenced in your project.
- Adjust the file path in the `Save` method as needed based on your application's requirements.

## References and Cross-References

For more details on working with footnotes and endnotes or other features of Essential DocIO, refer to the [Syncfusion Documentation](https://help.syncfusion.com/).

<!-- tags: [syncfusion-sdk, essential-docio, footnote, endnote, csharp] keywords: [footnote, endnote, markercharacterformat, textbody, symbolcode, custommarker, syncfusion.docio, iwsection, iwparagraph, wfootnote, footnote type, marker character format, text formatting] -->
```