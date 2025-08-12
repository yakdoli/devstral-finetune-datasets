```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_798.jpeg
document_name: grid
page_number: 798
page_id: grid#page_798
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:44:14Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

| RelationKind | Specifies the type of the relation. |
| --- | --- |
| Specifies the table schema of Child Table. | The options included are as follows. |
|  | • RelatedMasterDetails |
|  | • Foreign Key Reference |
|  | • Foreign Key KeyWords |
|  | • UniformChildList |
|  | • ListItemReference |
| AllowCacheChildList | Indicates whether the ChildList associated with a view can be cached. |
|  | • Used with UniformChildList relation. |
| ChildTableDescriptor |  |

## Different RelationKinds

Apart from the default Master-Detail type, Essential Grouping Grid supports a number of relations which could be enabled by specifying the relations manually in the grouping engine. In case of manual relations, the dataset does not need to have relations. This is the same approach that should be used if you want to setup relationships between independent IList collections.

## Supported Relations

- RelatedMasterDetails
- Foreign Key Reference
- Foreign Key KeyWords
- ListItemReference
- UniformChildList

## The ForeignKey DropDown

When a Foreign Key relation (a relation for looking up values into a related child table using a key) is used, the child records are displayed using a DropDownList. Using this foreign key drop down, you could be able to edit the record. Here are the screen shots of the foreign key drop down.

<!-- tags: [EssentialGrid, Windows Forms, RelationKinds,ForeignKeyDropDown, Supported Relations] keywords: [RelationKind, AllowCacheChildList, ChildTableDescriptor, RelatedMasterDetails, Foreign Key Reference, Foreign Key KeyWords, ListItemReference, UniformChildList] -->
```