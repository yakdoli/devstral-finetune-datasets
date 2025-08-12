```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_881.jpeg
document_name: grid
page_number: 881
page_id: grid#page_881
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:46:00Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates retrieving cell style information using the `PointToTableCellStyle` method.
- Explains the concept of "Look and Feel" in GridGroupingControl.

## Content

### Retrieving Cell Style Information

![Figure: Retrieving Cell Style Information](images/figure_343.png)  
**Figure 343: Retrieving Cell Style Information by using the PointToTableCellStyle Method**

The image shows a GridGroupingControl displaying employee information grouped by their titles. The `Cell Style Information` section provides details about the cell being hovered over:
- **Mouse Position:** {X=267, Y=123}
- **Category Keys:** (Employees) 4-Items
- **Display Element Type:** GridRecordRow
- **Cell Information:** Field Name - FirstName, Field Value - "Margaret", Field Type - TextBox

### 4.3.4.5.8 Look and Feel

GridGroupingControl implements **Themes** and **VisualStyles** to establish a consistent Look and Feel across all components in the grid. The term 'Look and Feel' encompasses not only the appearance of grid elements but also their behavior in response to user interactions, such as hovering, clicking, etc. The Grid supports built-in support for the following skins:
- WindowsXP
- Office2007 (Blue/Black/Silver)
- Office2003

#### ThemesEnabled

Grouping Grid enables or disables XP themes using the `ThemesEnabled` property. When set to `true`, XP themes are enabled.

#### Code Example in C#

```csharp
// Code snippet for enabling/disabling XP themes
// Example to come in the actual document content
```

## API Reference

### Properties
- `ThemesEnabled`: A Boolean property to enable or disable XP themes.

### Methods
- `PointToTableCellStyle`: Retrieves detailed information about the cell at a specific mouse position.

### Events
- No specific events mentioned in the context.

## Code Examples

### C#
```csharp
// Example of enabling XP themes
gridGroupingControl.ThemesEnabled = true;
```

<!-- tags: [gridgroupingcontrol, cellstyles, lookandfeel, themes, visualeffects, xpthemes, office2007, office2003] keywords: [pointtotablecellstyle, themesenabled, cellinformation, mouserposition, displayelementtype] -->
``` 
