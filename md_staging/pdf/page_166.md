```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_166.jpeg
document_name: pdf
page_number: 166
page_id: pdf#page_166
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:55Z
fidelity: lossless
-->

# Essential PDF

- **PdfOrderedMarker(PdfNumberStyle style, PdfFont font)**: Creates marker by using the PdfNumberStyle and specified font.
- **PdfOrderedMarker(PdfNumberStyle style, string finalizer, PdfFont font)**: Creates marker with number style, font, finalizer, and the specified symbol that follows after number. Default value for finalizer is '.'.
- **PdfOrderedMarker(PdfNumberStyle style, string delimiter, string finalizer, PdfFont font)**: Creates marker with the number style, font, finalizer, delimiter, and the specified symbol located between numbers. It is used when the `MarkerHierarchy` property of the `PdfOrderedList` class is set `True`. Default value for delimiter is '.'.

**Default list marker has Number style.**

## Features

Also, `PdfOrderedList` enables you to use numbering hierarchy, which means if you have an ordered list and one of its item has an ordered sublist, marker of it will contain the number of its parent item. This number is split by the delimiter.

To use numbering hierarchy, just set the `MarkerHierarchy` property of the `PdfOrderedList` class to `True`. Default value is `False`.

## Unordered List

The `PdfUnorderedList` class represents an unordered list.

### Initialize Lists

You can create a new instance of the `PdfUnorderedList` class by using the following constructors.

- **PdfUnorderedList()**: Creates list with default settings
- **PdfUnorderedList(PdfListItemCollection items)**: Creates list with the specified collection of items
- **PdfUnorderedList(PdfUnorderedMarker marker)**: Creates list with the specified marker
- **PdfUnorderedList(PdfListItemCollection items, PdfUnorderedMarker marker)**: Creates list with the specified items collection and marker
- **PdfUnorderedList(string text)**: Creates list from the specified text. It splits the text by using the `\n` symbol and creates a collection of items.
- **PdfUnorderedList(string text, PdfUnorderedMarker marker)**: Creates list from the specified text and with the specified marker. It splits text by using the `\n` symbol and creates a collection of items.

## List Marker
```markdown

## Cross References
- **See also**:
```markdown

### RAG Annotations
<!-- tags: [pdf, orderedlist, unorderedlist, marker] keywords: [PdfNumberStyle, PdfFont, finalizer, delimiter, MarkerHierarchy, PdfUnorderedMarker, PdfListItemCollection] -->
```