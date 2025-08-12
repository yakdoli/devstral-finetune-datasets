```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_883.jpeg
document_name: grid
page_number: 883
page_id: grid#page_883
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:47:04Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates how to apply visual styles to the `GridGroupingControl` in VB.NET.
- Includes examples of Office 2007 Blue and Office 2003 visual styles.
- Shows the UI changes reflecting the applied styles.

## Content

### Applying Visual Styles to GridGroupingControl

The following example demonstrates how to apply the Office 2007 Blue visual style to a `GridGroupingControl` in VB.NET:

```vb
Me.gridGroupingControl1.TableOptions.GridVisualStyles = GridVisualStyles.Office2007Blue
```

#### Office 2007 Blue Style

![Figure 345: Grid Grouping Control with Office 2007 Blue Visual Style](https://<image_url>)

**Figure 345: Grid Grouping Control with Office 2007 Blue Visual Style**

The image shows the `GridGroupingControl` with the Office 2007 Blue visual style applied. This style includes specific color schemes and fonts that match the Office 2007 Blue theme.

#### Office 2003 Style

![Figure 346: Grid Grouping Control with Office 2003 Visual Style](https://<image_url>)

**Figure 346: Grid Grouping Control with Office 2003 Visual Style**

The image shows the `GridGroupingControl` with the Office 2003 visual style applied. This style includes a color scheme and fonts that match the Office 2003 theme.

### API Reference

- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridGroupingControl
- **Property**: TableOptions.GridVisualStyles
- **Enum**: GridVisualStyles (Office2007Blue, Office2003)

### Code Examples

#### VB.NET: Applying Office 2007 Blue Visual Style

```vb
Me.gridGroupingControl1.TableOptions.GridVisualStyles = GridVisualStyles.Office2007Blue
```

#### VB.NET: Applying Office 2003 Visual Style

```vb
Me.gridGroupingControl1.TableOptions.GridVisualStyles = GridVisualStyles.Office2003
```

---

<!-- tags: Syncfusion Winforms, Office Styles, GridGroupingControl, Visual Styles, Office2007Blue, Office2003, VB.NET -->
```