```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_862.jpeg
document_name: grid
page_number: 862
page_id: grid#page_862
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:48:25Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Properties

### Overview
- Displays properties related to the Essential Grid for Windows Forms.
- Focuses on customizing header images and their alignment.

### WinForms-specific conventions
- Includes properties such as `HeaderImage` and `HeaderAlignment`.

#### Table: Properties Table

| Property           | Description                                                                 | Type         | Data Type     |
|--------------------|-----------------------------------------------------------------------------|--------------|---------------|
| HeaderImage       | Gets or sets images to display in the header cells.                          | Image        | Image         |
| HeaderAlignment   | Get or sets the alignment of the image in the header.                        | Enumeration   | Enumeration    |

## Sample Link

### Overview
- Provides a location to find a sample of the application.

### Content
- **Find a sample in the following location:**
  ```
  <Install Location>\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\Grouping\Grouping Demo
  ```

## Adding Images at Header Cells to an Application

### Overview
- Explains how to display images in the header cells of the grid.

### Content
- **To display the images in the header cells, pass the image through the GridColumnDescriptor.**
- The following code helps you to set the image for a specific column header.

#### Code Examples

**C#**
```csharp
this.gridGroupingControl1.TableDescriptor.Columns[Name/Index].HeaderImage = Image.FromFile(@"\...\image.PNG");
```

**VB.NET**
```vb
Me.gridGroupingControl1.TableDescriptor.Columns(Name/Index).HeaderImage = Image.FromFile(@"\...\image.PNG")
```

### Switching Image Alignment

- **To switch the alignment of the image between right and left of the header cell, the enumeration property `HeaderImageAlignment` is used.**
- The code helps you to set the alignment.

#### Code Examples

**C#**
```csharp
this.gridGroupingControl1.TableDescriptor.Columns[Index].HeaderImageAlignment = Syncfusion.Windows.Forms.Grid.Grouping.HeaderImageAlignment.Right;
```

**VB.NET**
```vb
Me.gridGroupingControl1.TableDescriptor.Columns(Index).HeaderImageAlignment = Syncfusion.Windows.Forms.Grid.Grouping.HeaderImageAlignment.Right
```

## Page-level Navigation/TOC (if applicable)

### Content
- [Sample Link](#sample-link)
- [Adding Images at Header Cells to an Application](#adding-images-at-header-cells-to-an-application)

## Cross References

### Content
- Additional references or related sections are not explicitly mentioned in this document.

## RAG Annotations
<!-- tags: [essential-grid, windows-forms, header-image, grid-column-descriptor, image-alignment, syncfusion-windows-forms] keywords: [headerimage, headeralignment, gridgroupingcontrol, tabledescriptor, imagealignment] -->
```