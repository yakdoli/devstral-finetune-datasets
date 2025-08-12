```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_165.jpeg
document_name: pdf
page_number: 165
page_id: pdf#page_165
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:34:06Z
fidelity: lossless
-->

# Essential PDF

## Lists

### Overview
- Lists in Essential PDF are used to organize items in a collection for better readability.
- There are two types of lists: Ordered list and Unordered list.
- These lists are represented by specific classes for structured implementation.

## Content

### Lists in Essential PDF
Lists in the Essential PDF are used to list out the items in a collection in some order to provide readability. There are two kinds of lists. They are:

- Ordered list, which is represented by the PdfOrderedList class
- Unordered list, which is represented by the PdfUnorderedList class

#### Base Classes and Representation
Base class for the preceding classes is the **PdfList** class, which contains an item collection represented by the **PdfListItemCollection** class. The items from the collection are represented by the **PdfListItem** class.

#### Ordered List
The **PdfOrderedList** class represents an ordered list.

#### Initialize Lists
You can create new instances of the PdfOrderedList class by using the following constructors:

- **PdfOrderedList()**: Creates list with default settings
- **PdfOrderedList(PdfListItemCollection items)**: Creates list with the specified collection of items
- **PdfOrderedList(PdfOrderedMarker marker)**: Creates list with the specified marker
- **PdfOrderedList(PdfListItemCollection items, PdfOrderedMarker marker)**: Creates list with the specified items collection and marker
- **PdfOrderedList(string text)**: Creates list from the specified text. It splits text by using the "\n" symbol and creates a collection of items.
- **PdfOrderedList(string text, PdfOrderedMarker marker)**: Creates list from the specified text and with specified marker. It splits text by using the "\n" symbol and creates a collection of items.

#### List Marker
Ordered list has ordered markers that are represented by the **PdfOrderedMarker** class. To create a new instance of the ordered marker, use the following constructors.

## API Reference (if applicable)
<!-- Add API details if available -->

## Code Examples
<!-- Add code snippets if available -->

## Cross References
- For more details on PdfGridImagePosition, check the following FAQ: [PdfGridCell background image](PdfGridCell background image)

### RAG Annotations
<!-- tags: [essentialpdf, list, orderedlist, unorderedlist, pdflistitemcollection, pdflistitem, pdforderedmarker, pdforderedlist] keywords: [ordered list, unordered list, pdforderedlist, pdfunorderedlist, pdflistitem, pdflistitemcollection, pdfitemlist, marker, pdforderedmarker, ordered list markers, text splitting, collection of items] -->
```