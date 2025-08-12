```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_057.jpeg
document_name: DocIo
page_number: 057
page_id: DocIo#page_057
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:06Z
fidelity: lossless
-->

# Essential DocIO

Every element of a tree has a reference to the document it refers. Elements also have the `Owner` property, which shows whether the current element is attached to the document. If an element is not attached to the document, it won't be available in the resultant document after saving the document.

## Composite Design Patterns

### Overview

Object model of Word document in DocIO uses the idea of "Composite Design" pattern. The following screen shot illustrates the classic structure of the Composite Design pattern.

![Figure 23: Composite Design Pattern](https://example.com/figure23_composite_design_pattern)

### IEntity

The `IEntity` interface represents the "Component" block in DocIO. `IEntity` interface supports all the elements which have content. Composite block is represented by the `ICompositeEntity` interface. Composite block has child nodes. Classes which implement only the `IEntity` (which don't have child nodes) are "leafs" for DocIO.

#### Specific Properties of IEntity Interface

- **IsComposite**: defines whether the current element is composite (elements which have child nodes are composite).
- **NextSibling**: returns the next sibling. For example, in the following screen shot, the `NextSibling` property for Child node 2 will return Child node 3 element.
- **PreviousSibling**: returns the previous sibling. For example, in the following screen shot, the `PreviousSibling` property for Child node 2 will return Child node 1 element.

<!-- tags: [DocIO, Composite Design Pattern, IEntity, ICompositeEntity, WinForms, word document] keywords: [element, reference, Owner, attached, resultant document, structure, child nodes, composite, leafs, IsComposite, NextSibling, PreviousSibling, version 11.4.0.26] -->
```