```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_615.jpeg
document_name: tools
page_number: 615
page_id: tools#page_615
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:24:45Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to apply custom colors and themes to a `MultiColumnComboBox`.
- Explains the event handling mechanism of the `ComboBoxAdv` control in the `MultiColumnComboBox`.

## Content

### Applying Custom Colors and Themes

#### C#
```csharp
this.multiColumnComboBox1.Office2007ColorTheme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyResourcesColors(this, Color.Orchid);
```

#### VB.NET
```vb
Me.multiColumnComboBox1.Office2007ColorTheme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyResourcesColors(Me, Color.Orchid)
```

**Figure 379: Custom Color = "Orchid"**

![multiColumnComboBox](attachment://505_UEAE.png)

### 3.5.5.4.4 Event Handling

The events of `ComboBoxAdv` present in the `MultiColumnComboBox`.

#### Selection Events

The `MultiColumnComboBox` fires different events for the different user interaction scenarios. The occurrence and order of the events are tabulated below:

| Scenarios                         | Selection Changed Commited | Selected Value Changed | Selected Index Changed | Validating/Validated |
|------------------------------------|-----------------------------|-------------------------|-------------------------|-----------------------|
| TextArea-Change Selection by Keys | Yes:1                       | Yes:2                   | Yes:3                   | No                    |
| TextArea-On AutoComplete          | No                          | No                      | No                      | No                    |
| Drop-Down List-Change Selection by Keys | No                         | Yes:1                   | Yes:2                   | No                    |
| Drop-Down List-Change Selection by Mouse Move | No                     | No                      | No                      | No                    |
| Drop-Down Close by Enter Key      | Yes:1                       | No                      | No                      | No                    |

## References

- Copyright © 2013 Syncfusion. All rights reserved.

<!-- tags: [WinForms, MultiColumnComboBox, Office2007Theme, EventHandling, ComboBoxAdv] keywords: [Syncfusion, Windows Forms, Office2007ColorTheme, MultiColumnComboBox, Selection Events, CustomColor, Theme, EventHandling, AutoComplete, DropDown, Validated, SelectionChanged] -->
```