<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_984.jpeg
document_name: grid
page_number: 984
page_id: grid#page_984
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:54:08Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- The document demonstrates how to customize the appearance of a grid in Windows Forms.
- It covers the appearance settings for `AlternateRecordFieldCell` and introduces skins for enhancing grid aesthetics.
- Provides detailed guidance on applying skins to change the look and feel of grid elements.

## Content

### Grid Designer with Appearance Settings

![Grid Designer showing the appearance settings for AlternateRecordFieldCell](#)
**Figure 379: Grid Designer showing the appearance settings for AlternateRecordFieldCell**

#### Skins

You can change the appearance and behavior of every grid element to provide grid with a rich look and feel by setting skins. Grouping Grid currently offers five such skins: Office2007Blue, Office2007Silver, Office2007Black, Office2003, and SystemTheme (Default XP theme). To set a skin, the `GridVisualStyles` property which is under `TableOptions` section is used. It lists the possible skin options in a drop down, which will make the entire grid redrawn with the chosen style.

### WinForms-specific conventions

- The document utilizes C# syntax for examples.
- Control names, namespaces, and types are explicitly stated, e.g., `Syncfusion.Windows.Forms.Grid.Grouping.GridTableFieldCellAppearance`.
- The design-time and runtime features are distinguished, as indicated by the Grid Designer interface.

### Code Examples

```csharp
// Example of setting a skin programmatically
GridVisualStyles gridViewStyles = new GridVisualStyles();
gridViewStyles.CurrentStyle = GridVisualStyles.Styles.Office2007Blue;
```

### Related Topics

- For more details on customizing grid elements, refer to the Grid documentation section on cell styling.
- To explore additional skin options, check the Visual Styles documentation.

## RAG Annotations

<!-- tags: [grid, windowsforms, appearance, skins] keywords: [AlternateRecordFieldCell, GridVisualStyles, Office2007Blue, Office2007Silver, Office2007Black, Office2003, SystemTheme] -->