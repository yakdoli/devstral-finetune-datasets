```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_882.jpeg
document_name: grid
page_number: 882
page_id: grid#page_882
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
this.gridGroupingControl1.ThemesEnabled = true;
```

```vbnet
Me.gridGroupingControl1.ThemesEnabled = True
```

![Figure 344: XP Themes for Grid Grouping Control](https://i.imgur.com/ExampleImage.png)

## GridVisualStyles

GridVisualStyles property is used to set different VisualStyles (skins) for grid like Office2007 and Office2003. Every component that is incorporated into the grid will be affected by these visual styles.

GridVisualStyles enumeration defines the skins exposed by the grouping grid. They are Office2003, Office2007Blue, Office2007Black, Office2007Silver, and SystemTheme. Default is SystemTheme.

Visual Styles can be set by assigning a GridVisualStyles enumeration value to the TableOptions.GridVisualStyles property.

```csharp
this.gridGroupingControl1.TableOptions.GridVisualStyles = GridVisualStyles.Office2007Blue;
```

## API Reference

### Namespaces and Classes
- **Syncfusion.Windows.Forms.Grid**
- **GridVisualStyles**

#### Enumeration: GridVisualStyles
- **Office2003**
- **Office2007Blue**
- **Office2007Black**
- **Office2007Silver**
- **SystemTheme**

### Properties
- **GridVisualStyles GridVisualStyles**
  - Type: `GridVisualStyles`
  - Description: Sets the visual style of the grid.
  - Default: `SystemTheme`

### Example Usage

In the following example, we set the visual style of the grid to `Office2007Blue`.

```csharp
// C#
this.gridGroupingControl1.TableOptions.GridVisualStyles = GridVisualStyles.Office2007Blue;
```

## Code Examples

### Visual Studio Designer
To set the GridVisualStyles at design time, use the Properties window to select the desired style from the dropdown list.

### Programmatic Setting
You can also set the GridVisualStyles programmatically as shown in the example above.

## RAG Annotations
<!-- tags: Essential Grid, Windows Forms, VisualStyles, Office2007, Syncfusion Winforms, version: 11.4.0.26 -->
<!-- per-section anchors: grid#page_882#gridvisualstyles, grid#page_882#api-reference, grid#page_882#code-examples -->
```