```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_982.jpeg
document_name: grid
page_number: 982
page_id: grid#page_982
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:56:35Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This page discusses the grouping grid functionality in Syncfusion Winforms.
- Focuses on the use of `ExpressionField` in grids, specifically with an example showing winning percentages.
- Explains how to specify relations across tables using the `TableDescriptor.Relations` property.

## Content

### Grouping Grid with ExpressionField

#### Figure: Grouping Grid showing the ExpressionField 'Winning%'
![Grouping Grid showing the ExpressionField 'Winning%'](image)

This figure illustrates a grid showing basketball statistics for various schools. The grid includes details such as ties, wins, year, and winning percentages for each school. The grid control is named `gridGroupingControl1`.

### Relations

It is possible to specify the relation to be used across the tables in case multiple tables are used. It can be done by accessing the `TableDescriptor.Relations` property wherein you can specify the relation type, name of the child table, relation keys consisting of the keys in parent and child tables and other information necessary to setup the relation.

## API Reference (if applicable)
- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridGroupingControl
- **Properties**:
  - `TableDescriptor`
    - `Relations`
      - Specifies the relation to be used across tables.

## Code Examples

### Configuration of Relations Example

```csharp
using Syncfusion.Windows.Forms.Grid.Grouping;
using Syncfusion.Windows.Forms.Grid;

// Assuming gridGroupingControl1 is declared and initialized

// Accessing TableDescriptor and configuring relations
TableDescriptor tableDescriptor = gridGroupingControl1.TableDescriptor;
RelationDescriptor relation = new RelationDescriptor();
relation.RelationType = RelationType.ParentChild;
relation.ParentTableName = "ParentTable";
relation.ChildTableName = "ChildTable";
relation.RelationKeys.AddRange(new RelationKeyDescriptor[]
{
    new RelationKeyDescriptor("ParentKey", "ChildKey")
});

tableDescriptor.Relations.Add(relation);
```

## Page-level Navigation/TOC (if applicable)
- Overview
- Content
  - Grouping Grid with ExpressionField
  - Relations
- API Reference
- Code Examples

## Cross References
- See also: Grid Control in Syncfusion Winforms documentation for more detailed information on relation configurations.

## RAG Annotations
<!-- tags: grid, grouping, winforms, expressionfield, relations, tabledescriptor, syncfusion keywords: groupinggrid, wins, tie, winning percentage, basketball, schools, stats, relationtype, parenttablename, childtablename, relationkeys -->
```