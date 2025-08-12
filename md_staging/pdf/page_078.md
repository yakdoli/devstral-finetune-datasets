```markdown
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_078.jpeg
document_name: pdf
page_number: 078
page_id: pdf#page_078
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:28:50Z
fidelity: lossless
-->

## Essential PDF

### Overview
- This section discusses two types of fonts: PdfStandardFont and PdfTrueTypeFont, their characteristics, and usage scenarios.

## Content

### 1. PdfStandardFont
PdfStandardFont represents a font that is recognized by any Adobe Reader. It supports 14 types of fonts.

The following are some of the fonts supported by this class:

- Times-Roman (Regular, Bold, Italic, Bold Italic)
- Helvetica (Regular, Bold, Italic, Bold Italic)
- Courier (Regular, Bold, Italic, Bold Italic)
- Symbol
- ZapfDingbats

**Note:** Fonts that belong to this type do not support Unicode symbols. They take very less memory space, and it is suggested to use these fonts only when ASCII text has to be printed.

### 2. PdfTrueTypeFont
PdfTrueTypeFont fonts are created from TrueType fonts. The PdfTrueTypeFont fonts are created either from the System.Drawing.Font class or TTF file (a file containing the information about TrueType font). There are a variety of constructors that can enable to create fonts with different settings. This class is used to embed the specified font in the PDF document.

**Note:** There is a unicode parameter in some of the constructors that indicate whether the font should support unicode symbols. The fonts created from a TTF file support unicode symbols, by default. If there is no need to use Unicode symbols, it is suggested to set the unicode parameter to False. Fonts that do not support Unicode takes less memory space in the file.

#### Right To Left Support
Unicode TrueType fonts created from the System.Drawing.Font class are used for RTL text output. Also, the languages with symbols substitution (like Arabic) are supported. To enable RTL and characters substitution, set `RightToLeft` property to `True` in the `PdfStringFormat` class.
```


## Page-level Navigation/TOC (if applicable)
- The document describes two font types, their features, and usage guidelines, emphasizing the support for Unicode and memory considerations.

## Cross References
- The section references `System.Drawing.Font` and `PdfStringFormat` classes, indicating a connection to font handling and formatting in PDF documents.

## RAG Annotations
<!-- tags: [Essential PDF, PdfStandardFont, PdfTrueTypeFont, TrueType fonts, Unicode symbols, memory space, Adobe Reader, RTL support, font embedding] keywords: [PdfStandardFont, PdfTrueTypeFont, TrueType fonts, Unicode, memory usage, ASCII text, font embedding, System.Drawing.Font, PdfStringFormat, RTL text output] -->

```