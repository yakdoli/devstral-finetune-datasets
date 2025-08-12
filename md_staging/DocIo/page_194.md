```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_194.jpeg
document_name: DocIo
page_number: 194
page_id: DocIo#page_194
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:40:10Z
fidelity: lossless
-->


# Break in Word Documents

## Overview
- Describes how to insert breaks in a Word document using the Break class.
- Explains the use of the `AppendBreak` function and supported break types.
- Outlines the class hierarchy and public constructors for the Break class.

## Break Class Overview

The **Break** class represents a break in the Word document. To insert a break in Microsoft Word:

1. Open the Insert menu.
2. Click **Break** in the menu.

### Break Dialog Box
- The Break dialog box provides options for inserting different types of breaks in the document.

#### Figure 68: Break Dialog Box
![Figure 68: Break Dialog Box](https://syncfusion.com/content/images/Screenshots/ tech escritio/ndocoword breakdocs/.png)

### Inserting Breaks Programmatically
You can use the `AppendBreak` function of `WParagraph` to insert a break by using DocIO. The `BreakType` property specifies the type of the break. The following are the types of breaks supported by the Break class:

- **PageBreak**
- **ColumnBreak**
- **LineBreak**

---

## Insert Section Breaks
- **Note:** Direct support is now provided to insert section breaks. Section breaks are inserted by calling the method `InsertSectionBreak`.

### Class Hierarchy
```
ParagraphItem
|
WSymbol
```

### Public Constructors
- **Break.Break (IWordDocument)**
  - Initializes a new instance of the Break class.

## API Reference
### Methods
- **AppendBreak(BreakType breakType)**
  - Inserts a break of the specified type into the document.

---

## Code Examples
### Example: Inserting a Page Break
```csharp
using (DocX document = new DocX())
{
    document.InsertParagraph()
           .AppendBreak(BreakType.PageBreak);
    document.InsertParagraph().AppendText("After page break.");

    document.Save();
}
```

---

## Page-level Navigation/TOC
- [Break Class Overview](#break-class-overview)
- [Inserting Breaks Programmatically](#inserting-breaks-programmatically)
- [Class Hierarchy](#class-hierarchy)
- [Public Constructors](#public-constructors)
- [API Reference](#api-reference)
- [Code Examples](#code-examples)

<!-- tags: break, word document, insertion, DocIO, Break class, InsertSectionBreak, WParagraph, PageBreak, ColumnBreak, LineBreak, Microsoft Word, section break, public constructors, class hierarchy, API reference keywords: break, docio, word documents, types of breaks, section break, programming example -->
```