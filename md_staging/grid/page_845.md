```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_845.jpeg
document_name: grid
page_number: 845
page_id: grid#page_845
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:43:22Z
fidelity: lossless
-->

## Overview
- The page displays the **Properties** window for templates associated with the **gridGroupingControl** in a Windows Forms application.
- Focuses on the **Appearance** section, listing various cell types for UI customization.
- Provides control over the visual aspects of grid components, including rows, fields, headers, summaries, and more.

## Content
### Properties in the Appearance Section
The **Appearance** section of the **gridGroupingControl** provides extensive customization options for grid components. Below is a detailed list of the cell types included:

#### List of Appearance Templates
- **AddNewRecordFieldCell**
- **AddNewRecordRowHeaderCell**
- **AlternateRecordFieldCell**
- **AlternateRecordRowHeaderCell**
- **AnyCell**
- **AnyGroupCell**
- **AnyHeaderCell**
- **AnyIndentCell**
- **AnyNestedTableCell**
- **AnyPreviewCell**
- **AnyRecordFieldCell**
- **AnySummaryCell**
- **AnyColumnHeaderCell**
- **AnyColumnHeaderWithFilterCell**
- **AnyEmptyCell**
- **AnyEmptySectionRowHeaderCell**
- **AnyFilterBarCell**
- **AnyFilterBarRowHeaderCell**
- **AnyGroupCaptionCell**
- **AnyGroupCaptionPlusMinusCell**
- **AnyGroupCaptionRowHeaderCell**
- **AnyGroupCaptionSummaryCell**
- **AnyGroupFooterIndentCell**
- **AnyGroupFooterRowHeaderCell**
- **AnyGroupFooterSectionCell**
- **AnyGroupHeaderIndentCell**
- **AnyGroupHeaderRowHeaderCell**
- **AnyGroupHeaderSectionCell**
- **AnyGroupIndentICell**
- **AnyGroupIndentLCell**
- **AnyGroupIndentTCell**
- **AnyGroupPreviewCell**
- **AnyGroupPreviewRowHeaderCell**
- **AnyNestedTableCell**
- **AnyNestedTableIndentCell**
- **AnyNestedTableIndentICell**
- **AnyNestedTableIndentLCell**
- **AnyNestedTableIndentTCell**
- **AnyNestedTableRowHeaderCell**
- **AnyRecordFieldCell**
- **AnyRecordPlusMinusCell**
- **AnyRecordPreviewCell**
- **AnyRecordPreviewRowHeaderCell**
- **AnyRecordRowHeaderCell**
- **AnyRowHeaderCell**
- **AnyStackedHeaderCell**
- **AnySummaryEmptyCell**
- **AnySummaryFieldCell**
- **AnySummaryFillRowCell**
- **AnySummaryRowHeaderCell**
- **AnySummaryTitleCell**
- **AnyTopLeftHeaderCell**

### Purpose of Appearance Templates
These templates allow developers to customize the visual representation of grid elements to match application themes or user requirements. Each template corresponds to a specific type of grid cell, enabling precise control over formatting, fonts, and colors.

## API Reference
### Namespace
- `Syncfusion.Windows.Forms.Grid`

### Classes and Members
- gridGroupingControl (Primary control for the grid)
- Appearance (Child section for UI customization)

#### Templates
- **List of Templates**
  Each template listed above can be accessed and modified to adjust the appearance of the corresponding grid elements. For example:
  - **AddNewRecordFieldCell**: Configures the appearance of fields in a new record.
  - **GroupCaptionCell**: Customizes the appearance of group caption headers.

### Events (Relevant for Appearance)
- **TemplateSelectionEvent**: Triggered when a template is selected for customization.
- **AppearanceChanged**: Notifies when any appearance settings are modified.

## Code Examples
### Example: Modifying the Appearance of a Grid
```csharp
// Example of setting a custom appearance for a specific cell type
gridGroupingControl.Appearance.AnyRecordFieldCell.Font = new Font("Arial", 12, FontStyle.Bold);
gridGroupingControl.Appearance.AnyFooterRowHeaderCell.BackColor = Color.LightGray;
```

## Cross References
- **Related Documentation**: For more details on grid customization and template management, refer to the **GridGroupingControl API Documentation**.
- **Sample Projects**: Explore Syncfusion's grid sample projects for practical examples of appearance customization.

<!-- tags: [Syncfusion, WinForms, gridGroupingControl, UI customization, appearance, templates] keywords: [grid, appearance, templates, customization, cell types, UI, Windows Forms, C#, properties, appearance] -->
```