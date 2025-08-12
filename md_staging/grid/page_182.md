```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_182.jpeg
document_name: grid
page_number: 182
page_id: grid#page_182
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:59:31Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

To work with BaseStyles from within the Visual Studio designer, you need to use the **Edit base styles** verb that appears at the bottom of the Grid control's property grid.

## Working with BaseStyles

When you click the **Edit base styles** verb, the **GridBaseStyle Collection Editor** dialog box is displayed. You can use the **GridBaseStyle Collection Editor** to edit the existing BaseStyles or add new ones.

### Visual Studio PropertyGrid Example

The following screenshot shows the property grid with the **Edit base styles** option:

```markdown
Properties
- **gridControl1**: Syncfusion.Windows.Forms.Grid.GridControl
  - **Grid Contents**
    - BandedRanges: (Collection)
    - BaseStylesMap: (Collection)
    - ColCount: 10
    - ColHiddenEntries: (Collection)
    - ColWidthEntries: (Collection)
    - CoveredRanges: (Collection)
    - DefaultColWidth: 65
    - DefaultRowHeight: 17
  - **Properties**
    - RangeStyles: (Collection)
    - ReadOnly: False
    - RowCount: 10
    - RowHeightEntries: (Collection)
    - RowHiddenEntries: (Collection)
    - SerializeCellsBehavior: SerializeAsRangeStylesIntoCode
    - **Edit, Touch It, Edit base styles**
```

### Figure Reference

**Figure 100: PropertyGrid with Edit BaseStyles Option**

This figure illustrates the property grid with the **Edit base styles** option highlighted. You can use the **GridBaseStyle Collection Editor** to manage BaseStyles within the Visual Studio designer.

## API Reference
- Namespace: Syncfusion.Windows.Forms.Grid
- Class: GridControl
- Member: Edit base styles verb

### Methods
- **Edit base styles**: Displays the **GridBaseStyle Collection Editor** to manage BaseStyles.

### Properties
- **BaseStylesMap**: Collection for managing BaseStyles.
- **Edit base styles**: Verb for accessing the **GridBaseStyle Collection Editor**.

## Code Examples

### Using the GridBaseStyle Collection Editor in C#
```csharp
// Example of accessing and editing BaseStyles through code
GridBaseStyle baseStyle = new GridBaseStyle();
baseStyle.Name = "CustomBaseStyle";
baseStyle.BackColor = System.Drawing.Color.LightGray;

// Add the BaseStyle to the collection
gridControl1.BaseStyles.Add(baseStyle);
```

## Cross References
- See also: GridBaseStyle, GridControl, Visual Studio Designer

<!-- tags: [Essential Grid, Windows Forms, BaseStyles, Visual Studio Designer, GridBaseStyle Collection Editor] keywords: [Edit base styles, BaseStylesMap, GridControl, Visual Studio property grid, GridBaseStyle] -->
```