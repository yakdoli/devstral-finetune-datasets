```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_005.jpeg
document_name: grouping
page_number: 005
page_id: grouping#page_005
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:58:20Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- The document focuses on the **Essential Grouping** feature in Syncfusion Winforms, detailing its key functionalities and technical aspects.

## Content

### Grouping in Data Grid

#### Key Features
Some of the key features of Essential Grouping are listed below:

- **Grouping supports data presentation techniques** like sorting, grouping, adding caption, and summary information for the groups.
- **Grouping also supports nested tables and hierarchies** in the form of related tables.
- **The grouping technology uses balanced binary trees** as the core data structure instead of arrays. Binary trees have the advantage where parent branches can cache information about their children. This allows position information and summary information to be cached in parent branches, facilitating quick inserts of new records honoring any sort of criteria that is applied. Inserting, removing, and moving of records takes \(\text{Log}_2(n)\) operations. With linear lookup structures such as an ArrayList, each of these operations would take \(O(n)\) operations.
- **Expressions can be any well-formed algebraic combination** of property (column) names enclosed with brackets (\[\]), numerical constants and literals, and the algebraic and logical operators.

Figures and tables, as shown in the image, provide a visual representation of these key features, including a data grid with summary statistics for columns A and B.

### Visual Representation

#### Figure 1: Grouping in Data Grid
The figure showcases a data grid with rows of numerical data under columns A and B. Summary statistics for columns A and B, such as Maximum, Minimum, Total, and Count, are displayed. Additionally, there is functionality to generate new data, indicating the dynamic nature of grouping.

## Cross References
- For further information, refer to the related sections on nested tables, binary tree caching, and grouping expressions.

<!-- tags: [grouping, data grid, balanced binary trees, data presentation, sorting, nested tables, hierarchical data, algebraic expressions, arrays, ArrayList] keywords: [syncfusion, grouping, data presentation, binary trees, summary statistics, grouping expressions] -->
```