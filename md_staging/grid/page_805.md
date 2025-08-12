```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_805.jpeg
document_name: grid
page_number: 805
page_id: grid#page_805
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:40:52Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the implementation of Master-Detail relationships in a Grid control.
- Provides code samples in C# and VB.NET for setting up the data source.
- Explains the concept of 'Record PlusMinus Button' for navigating records.

## Content

### Setting the Data Source

#### Code Examples

\[C#\]
```csharp
this.gridGroupingControl.DataSource = parentTable;
```

\[VB.NET]
```vb
Me.gridGroupingControl.DataSource = parentTable
```

#### Explaining the Master-Detail Relationship

5. When you run the sample, you could find the tables connected with Master-Details relation.
   
**Figure 321: RelatedMasterDetails Relation**

**Description of the Diagram:**
- **Parent Table Record:** Shows an entry in the parent table with columns `parentID`, `ParentName`, and `ParentDec`.
- **Related Records in Child Table:** Expands to show details related to the parent entry, including `childID` and `Name`.
- **Record PlusMinus Button:** A control used to expand or collapse details in the grid.
- **Related Records in Grand Child Table:** Further nested details are displayed based on the relationships defined between the tables.

**Example Hierarchy in the Diagram:**
- **Parent Table:** Contains entries like `parentName0`.
- **Child Table:** Contains related records for each parent entry.
- **Grand Child Table:** Contains records related to the child records, expanding the hierarchy.

### Note: For more details, refer the following browser sample:

- Location: `<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Relations And Hierarchy\Related Master Details Demo`

## References
- The example demonstrates the use of nested relationships in a grid control, allowing users to visualize hierarchical data structures.
- Users can interact with the grid using the 'Record PlusMinus Button' to view or collapse detailed information.

<!-- tags: grid, master-detail, windows forms, data source, csharp, vb.net, hierarchy, syncfusion, grid grouping control keywords: relatedmasterdetails, recordplusminus, parent-child, nested relationships -->
```