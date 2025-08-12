```html
<!-- source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_959.jpeg
document_name: grid
page_number: 959
page_id: grid#page_959
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:52:38Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the use of Syncfusion's Essential Grid control in exporting data to Excel.
- Focuses on grouping and hierarchical data representation within a grid view.
- Provides a sample showcasing how to integrate grid data with an Excel spreadsheet.

## Content

### Grid In Excel

The image illustrates a grid structure within an Excel environment. The grid contains hierarchical data with a parent-child relationship. The Excel interface is set to display:

- **Parent Table (50 Items):**
  - Columns: `parentID`, `ParentName`, `GroupID`
  - Data: One visible record example:
    - `parentID: 1`
    - `ParentName: parentName1`
    - `GroupID: 100`

- **Child Table (4 Items) under the GroupID 100:**
  - Columns: `childID`, `Name`, `ChildGroupID`
  - Data: Four records, each with `childID`, `Name`, and `ChildGroupID`.

#### Hierarchical View

- The grid showsгруппированные данные на основании `GroupID`, с вложенными отцовскими и дочерними записями.
- Дочерние записи отображаются в раскрытом виде, демонстрируя ячейки с данными и примечания для каждой записи.

**Figure 353: Grid In Excel**

#### Note
For more details, refer to the following browser sample:

**<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Export\MS Excel Export Demo**

---

## Cross References
-参阅相关的示例和文档以了解更详细的信息和示例代码。

---

### RAG Annotations
<!-- tags: [Essential Grid, Windows Forms, Excel Export, Data Grid, Grouping] keywords: [Syncfusion, Grid, Excel, ParentTable, ChildTable, GroupID, Export] -->
