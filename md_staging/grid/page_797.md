```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_797.jpeg
document_name: grid
page_number: 797
page_id: grid#page_797
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:40:26Z
fidelity: lossless
 -->

---

## Overview

- Demonstrates setting up relations in the Essential Grid using the GridRelationDescriptor Collection Editor.
- Explains the properties required to define master-child relationships between tables.
- Provides a visual guide and description for configuring relation settings.

---

## Content

### Setting Up Relations in the Grid

#### Figure 318: Setting Up Relations by using the GridRelationDescriptor Collection Editor

The image shows a configuration screen for setting up a relation between two tables, "Customers" and "Orders," using the GridRelationDescriptor Collection Editor. The editor allows users to define the relationship between the parent ("Customers") and child ("Orders") tables.

---

### Properties

#### Overview of Properties Used to Setup a Relation

Here is a brief description of the properties used to set up a relation:

| **GridRelationDescriptor Property** | **Description** |
|---|---|
| Name | Specifies the relation name. |
| ChildTableName | Specifies the name of the ChildTable. |
| RelationKeys | Defines the mapping between the parent and child columns in a master-detail relation. |
| MappingName | Specifies the name of the PropertyDescriptor in the parent table that contains the details about the relation. |

---

## Cross References

- See also:
  - Related topics on configuring hierarchical data in the Essential Grid.
  - Instructions on using the GridRelationDescriptor for advanced data binding.

---

<!-- tags: [Syncfusion Winforms, GridRelationDescriptor, Master-Detail Relation] keywords: [Grid, Relation, Collection Editor, Customer Orders] -->
```