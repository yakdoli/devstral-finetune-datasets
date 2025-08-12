```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_058.jpeg
document_name: DocIo
page_number: 058
page_id: DocIo#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:31:14Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Describes the IEntity interface and its properties and methods.
- Shows the structure of a tree-like data model using nodes.
- Introduces the ICompositeEntity interface for managing composite elements with children.

## Content

### IEntity Interface

#### Figure 24: IEntity Interface

![Figure 24: IEntity Interface](#)

The figure illustrates a parent node with three child nodes, showcasing the structure managed by the IEntity interface.

#### IEntity Public Properties

| Name        | Description                                                  |
|-------------|--------------------------------------------------------------|
| Document    | Gets the document of this entity.                            |
| EntityType  | Gets the type of the entity.                                 |
| IsComposite | Gets a value indicating whether this instance is composite.  |
| NextSibling | Gets the next sibling.                                       |
| Owner       | Gets the owner of this entity.                               |
| PreviousSibling | Gets the previous sibling.                                |

#### IEntity Public Methods

| Name       | Description                |
|------------|----------------------------|
| Clone      | Creates a duplicate of the entity. |

### ICompositeEntity

#### ICompositeEntity Description

ICompositeEntity interface represents an element which has "children". A child element is an element that supports the ICompositeEntity (and also has children) or a "leaf" (element without children).

#### ICompositeEntity Public Property

| Name         | Description                     |
|--------------|----------------------------------|
| ChildEntities | Gets the child entities.        |

## API Reference (if applicable)

### Namespace and Class

- **Namespace**: Syncfusion.DocIO
- **Class**: IEntity
  - **Properties**
    - Document
    - EntityType
    - IsComposite
    - NextSibling
    - Owner
    - PreviousSibling
  - **Methods**
    - Clone()
- **Class**: ICompositeEntity
  - **Property**
    - ChildEntities

## Code Examples (multi-language supported)

No code examples are provided in the current context.

## Cross References

- See also: [Context values and related documentation as needed.]

## RAG Annotations

<!-- tags: [Syncfusion, DocIO, Winforms, IEntity, ICompositeEntity, tree structure, parent node, child node, composite, leaf] keywords: [IEntity, ICompositeEntity, Document, EntityType, IsComposite, ChildEntities, Clone, tree structure, parent node, child node, composite, leaf] -->
```