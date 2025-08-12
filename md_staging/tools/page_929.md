```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_929.jpeg
document_name: tools
page_number: 929
page_id: tools#page_929
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:42:57Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Customizing the height and sorting of items in a FontComboBox control.
- Enabling Office2007 visual styles for the FontComboBox control.

## Content

### Customizing DropDown Items
The height of the FontComboBox items is specified in the `ItemHeight` property, and sorting of the items is enabled through the `Sorted` property.

```csharp
this.fontComboBox2.ItemHeight = 17;
this.fontComboBox2.Sorted = true;
```

```vb
Me.fontComboBox2.ItemHeight = 17
Me.fontComboBox2.Sorted = True
```

### 3.5.9.2.3.3 Visual Styles
The Office2007 visual style for the FontComboBox control can be enabled through the following properties.

| Properties                     | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| **VisualStyle**                | Sets the visual style for the control. The options are, <br> Default (default value) and Office2007. |
| **Office2007ColorScheme**     | Specifies the office color schemes. The color schemes are, <br> Blue, <br> Silver and <br> Black. |

```csharp
this.fontComboBox2.VisualStyle =
    Syncfusion.Windows.Forms.Tools.ThemedComboBoxStyles.Office2007;
this.fontComboBox2.Office2007ColorTheme =
    Syncfusion.Windows.Forms.Office2007Theme.Silver;
```

<!-- tags: [Syncfusion, Winforms, FontComboBox, ItemHeight, Sorted, VisualStyles, Office2007] keywords: [customizing dropdown items, visual styles, Office2007, control properties, C#, VB] -->
```