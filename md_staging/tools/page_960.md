```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_960.jpeg
document_name: tools
page_number: 960
page_id: tools#page_960
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:44:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Code Example

```vb
Me.checkBoxAdv1.ShadowColor = System.Drawing.Color.BurlyWood
Me.checkBoxAdv1.ShadowOffset = New System.Drawing.Point(8, 8)
Me.checkBoxAdv1.WrapText = True
```

#### Figure 617: Text Shadow Settings

![checkBoxAdv1 with shadow settings](./checkboxadv_shadow.png)

#### Figure 618: WrapText property Set

![Comparison of WrapText property](./wraptext_property_comparison.png)

A sample which demonstrates the TextShadow property of CheckBoxAdv is available in the below sample installation path.

```
..My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0\Editors Package\OptionControls
```

### See Also

- [Alignment Settings](#)
- [3.5.11.1.3.3 Appearance and Behavior Settings](#)

This section discusses the appearance and behavior settings of the CheckBoxAdv control.

#### Appearance Settings

##### DrawFocusRectangle

The focus rectangle can be hidden or made visible using the below given property.

| CheckBoxAdv Property      | Description                                                                                                     |
|---------------------------|-----------------------------------------------------------------------------------------------------------------|
| DrawFocusRectangle        | Determines if the focus rectangle is visible when it gets the focus. The default value is set to 'True'.       |

---

© 2013 Syncfusion. All rights reserved. | 960

## API Reference

### CheckBoxAdv Properties

- **DrawFocusRectangle**  
  Determines if the focus rectangle is visible when it gets the focus. The default value is set to 'True'.

---

## Code Examples

- **VB.NET**

```vb
Me.checkBoxAdv1.DrawFocusRectangle = False
```

<!-- tags: [Syncfusion, Winforms, CheckBoxAdv, Appearance, Behavior] keywords: [CheckBoxAdv, DrawFocusRectangle, ShadowColor, ShadowOffset, WrapText, Appearance, Behavior, FocusRectangle] -->
```