```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_438.jpeg
document_name: grid
page_number: 438
page_id: grid#page_438
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:16:29Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Overview of the properties used to configure the visibility of grid lines in the Essential Grid control.
- Explanation of how setting `DisplayHorzLines` and `DisplayVertLines` properties to `false` affects the visual appearance of the grid.

## Content

### DisplayHorzLines Property

The following illustration shows how the Grid in "Figure 1" is transformed when the `Properties.DisplayHorzLines` property is set to `false`.

```vb
' Enable DisplayHorzLines property.
Me.gridControl1.Properties.DisplayHorzLines = False
```

#### Figure: Horizontal Lines hidden in Grid
![](attachment:figure-163.png)

**Figure 163: Horizontal Lines hidden in Grid**

- **DisplayHorzLines**: Specifies whether horizontal grid lines marking the cells are to be displayed. Default value is set to `true`.

### DisplayVertLines Property

- **DisplayVertLines**: Specifies whether vertical grid lines marking the cells are to be displayed. Default value is set to `true`.

#### Setting the Property

The following code examples can be used to set this property:

1. **Using C#**
```csharp
// Enable DisplayVertLines property.
this.gridControl1.Properties.DisplayVertLines = false;
```

2. **Using VB.NET**
```vb
' Enable DisplayVertLines property.
Me.gridControl1.Properties.DisplayVertLines = False
```

#### Illustration

The following illustration shows how the Grid in "Figure 1" is transformed when the `Properties.DisplayVertLines` property is set to `false`.

### Conclusion

These properties allow for customization of grid lines visibility, enhancing the presentation of the grid in Windows Forms applications.

---

## Code Examples

### C#

```csharp
// Enabling DisplayVertLines property.
this.gridControl1.Properties.DisplayVertLines = false;
```

### VB.NET

```vb
' Enabling DisplayVertLines property.
Me.gridControl1.Properties.DisplayVertLines = False
```

---

## Related Sections

- [Grid Control Properties and Methods Overview](#)
- [Customizing Grid Appearance](#)

---

<!-- tags: [essential-grid, windows-forms, displayhorzlines, displayvertlines, grid-control, customization, syncfusion] keywords: [displayhorzlines, displayvertlines, grid, windows forms, customization, lines, properties, vertical lines, horizontal lines] -->
```