```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_077.jpeg
document_name: grid
page_number: 077
page_id: grid#page_077
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:21:08Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Overview
- Demonstrates the use of grouped grids in the Essential Grid for Windows Forms.
- Explains the enhancements in Grid Control Design starting from Version 4.1.
- Introduces the new Designer Editor for Grid Control.

## Content

### 3.1.3 Lesson 2: Grid Control Designer

**Starting with Version 4.1, the design time support for the Grid control will be much more user friendly.** To make the task of designing the Grid control easier on a cell level, a new Designer Editor has been added. With the editor, the grid can be modified and saved (and loaded) to Xml formatted files, or Soap formatted templates. There is also no longer a Toggle Interactive Mode design verb that was present in versions prior to 4.1.

**In this lesson, you will learn about a basic Grid Control.**

## Code Examples

```csharp
// Example usage of the Grid Control
Syncfusion.Windows.Forms.Grid.GridControl grid = new Syncfusion.Windows.Forms.Grid.GridControl();
// Additional setup and configuration
grid.DataSource = dataSource;
// Attach custom editors, filters, etc.
```

## Additional Notes and References
**Note:** For more details, refer the following browser sample:
- `C:\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0\GettingStarted\Data Binding VS 2005 Demo`

### Figure 43: Grouped Grid
The figure shows a grouped grid, illustrating how data is organized and displayed in a hierarchical format. This is particularly useful for managing and presenting large datasets in an easy-to-navigate manner.

<!-- tags: [Essential Grid for Windows Forms, Grid Control Designer, Designer Editor, Grouped Grid, Version 4.1] keywords: [grouped grids, design time support, Designer Editor, xml formatted files, soap formatted templates, Interactive Mode, Grid Control] -->
```