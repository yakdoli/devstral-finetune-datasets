```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_301.jpeg
document_name: DocIo
page_number: 301
page_id: DocIo#page_301
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:48:22Z
fidelity: lossless
-->

# Essential DocIO

The following is the sample image of the output EPub document when converted, using the above code.

![Figure: Output EPub document](https://i.imgur.com/Screen Shot 2023-06-08 at 4.56.15 PM.png)

## Embedding Font

Conversion of EPub using default options does not embed font files. Hence, the reading device uses its own default font for the texts in the document, which may vary depending on the reader being used. To read the texts in the same font as used in the input word document, the user should embed the font files into the generated EPub. This can be done by turning on EPubExportFont property. By default, this property is set to false since this actually embeds the exact font file from the machine, which may increase the size of the EPub document.

The following code illustrates how to embed font file.

```csharp
[C#]
```

- - -
### Page-level Navigation/TOC

### Cross References

### RAG Annotations
<!-- tags: [Essential DocIO, EPub, font embedding, Winforms, EPubExportFont, Syncfusion, conversion] keywords: [font embedding, default font, EPub, EPubExportFont, Winforms, font files, document conversion] -->
```