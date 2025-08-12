```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_532.jpeg
document_name: tools
page_number: 532
page_id: tools#page_532
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:18:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

This section discusses the properties in the below topics, which customizes the color groups.

## Adding Color Items and sub items to Color Groups

The below properties lets you add color items and sub items.

| **ColorPickerUIAdv Properties** | **Description** |
| --- | --- |
| **Items** | This property invokes a ColorItem Collection Editor, which lets you add the colors to the group. You can also add sub items to this particular color item using another ColorItem Collection Editor which is invoked using SubItems property. |
| **IsSubItemsVisible** | Specifies if sub items should be visible. |
| **SubItemsDepth** | Specifies the depth of the sub items, i.e the number of sub items that can be added to a color item. |

### Opening ColorItem Collection Editor using Items property.

![Accessing ColorItem Collection Editor Through Property Grid](https://user-images.githubusercontent.com/91532585/220816795-d4f0f0c4-4d9d-496f-8dc9-131a94647c59.png)

*Figure 319: Accessing ColorItem Collection Editor Through Property Grid*

## API Reference

### Namespace: Syncfusion.Windows.Forms.Tools

#### Class: ColorPickerUIAdv

##### Properties:
1. **Items**: Collection of ColorItem objects.
2. **IsSubItemsVisible**: Boolean indicating visibility of sub items.
3. **SubItemsDepth**: Integer specifying the number of sub items per color item.

## Code Examples

### C#

```csharp
using Syncfusion.Windows.Forms.Tools;

// Accessing and configuring Color Picker
ColorPickerUIAdv colorPicker = new ColorPickerUIAdv();
colorPicker.Items.Add(new ColorItem("Red", Color.Red));
colorPicker.Items.Add(new ColorItem("Blue", Color.Blue));

// Configuring SubItems
colorPicker.Items[0].SubItems.Add(new ColorItem("Light Red", Color.LightCoral));

// Setting visibility of sub items
colorPicker.IsSubItemsVisible = true;

// Setting depth of sub items
colorPicker.SubItemsDepth = 5;
```

## Related Topics

See also:
- [ColorItem Collection Editor](#color-item-collection-editor)
- [Customizing Color Groups](#customizing-color-groups)

<!-- tags: [colorpickeruiadv, coloritem, subitems, properties, windows forms] keywords: [color picker, edit colors, add subitems, visibility, depth] -->
```