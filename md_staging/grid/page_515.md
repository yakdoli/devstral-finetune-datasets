```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_515.jpeg
document_name: grid
page_number: 515
page_id: grid#page_515
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:21:40Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to implement a Microsoft Excel 2007-like UI using the Grid control.
- Highlights a feature sample available under a specified installation path.
- Explains the use of the Grid control to create a TreeView control with custom TreeCell type.

## Content

### Figure 200: Microsoft Excel 2007-like UI implemented by using Grid

The figure shows the interface of Microsoft Excel 2007-like UI implemented by using the Grid control.

**A sample demonstrating this feature is available under the following sample installation path:**

```
<Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0\Product Showcase\Excel Like UI Demo
```

### 4.1.4.27.3 Grid Folder Browser

#### Overview
- The Essential Grid can be used to develop a powerful TreeView control due to its flexibility.
- Tree nodes are created through a custom `TreeCell` cell type, which inherits from the `GridStaticCellModel` class.
- The plus/minus buttons of the tree nodes are selected using the `ImageIndex` property.

#### Detailed Explanation
The Essential Grid provides the flexibility to create a powerful TreeView control. To achieve this, custom `TreeCell` types can be defined. The `TreeCell` type is based on the `GridStaticCellModel` class, allowing for the creation of hierarchical tree structures. The expand/collapse functionality of tree nodes is managed by using the `ImageIndex` property.

---

## API Reference

- **Class**: `TreeCell`
  - Inherits from `GridStaticCellModel`
  - Provides the foundational structure for creating custom tree cell types.
  
- **Property**: `ImageIndex`
  - Type: `int`
  - Specifies the image index for the plus/minus buttons of tree nodes.

---

## Code Examples

The following code snippet demonstrates how to create a `TreeCell` type and use the `ImageIndex` property to manage tree node expansion and collapse:

```csharp
// Example: Creating a custom TreeCell type
public class CustomTreeCell : GridStaticCellModel
{
    public void SetTreeCellAppearance()
    {
        // Configure tree cell appearance using ImageIndex
        this.ImageIndex = 1; // Image index for the plus/minus buttons
    }
}
```

---

## RAG Annotations
<!-- tags: [EssentialGrid, WindowsForms, TreeView, TreeCell] keywords: [Grid, TreeView control, custom TreeCell, GridStaticCellModel, ImageIndex, flexibility, creation,树结构, 展示,脚本] -->
```