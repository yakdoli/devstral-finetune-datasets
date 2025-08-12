```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_422.jpeg
document_name: tools
page_number: 422
page_id: tools#page_422
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:12:55Z
fidelity: lossless
-->

## Grid with Dates Separated by Grid Lines

### Overview

- This page explains how to modify the appearance of the grid within the `MonthCalendarAdv` control.
- It covers properties for changing the grid's background color and line styles.
- Code examples in C# and VB.NET are provided for customization.

### Content

#### Properties for Changing the Grid Appearance in MonthCalendarAdv

| MonthCalendarAdv Properties | Description |
|-----------------------------|-------------|
| **GridBackColor**           | Gets or Sets the back color of the Grid. |
| **GridLines**               | Gets or Sets the style of the Grid lines. The options are <br> - NotSet <br> - None <br> - Dashed <br> - Dotted <br> - DashDot <br> - DashDotDot <br> - Solid <br> - Standard <br> The default value is 'Dotted'. |

#### Code Examples

##### C#

```csharp
this.monthCalendarAdv1.GridBackColor = 
    System.Drawing.Color.FloralWhite;
this.monthCalendarAdv1.GridLines = 
    Syncfusion.Windows.Forms.Grid.GridBorderStyle.Dashed;
```

##### VB.NET

```vb
Me.monthCalendarAdv1.GridBackColor = System.Drawing.Color.FloralWhite
Me.monthCalendarAdv1.GridLines = 
    Syncfusion.Windows.Forms.Grid.GridBorderStyle.Dashed
```

### Credits

- © 2013 Syncfusion. All rights reserved.

<!-- tags: [Syncfusion Winforms, MonthCalendarAdv, GridLines, GridBackColor, C#, VB.NET] keywords: [MonthCalendarAdv, GridLines, GridBackColor, customization, Syncfusion Windows Forms, grid appearance, properties, C#, VB.NET] -->
```