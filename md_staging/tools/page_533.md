```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_533.jpeg
document_name: tools
page_number: 533
page_id: tools#page_533
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:18:05Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Adding GroupColor items.
- Accessing ColorItem Collection Editor using SubItems Property.
- Adding color / sub items to the GroupColor items.

---

### Adding GroupColor Items

The screen capture below illustrates how you can access the **ColorItem Collection Editor** using the **SubItems Property**. This interface allows you to organize and manipulate GroupColor items by adding sub-items with specific colors.

#### Figure 320: Accessing ColorItem Collection Editor using SubItems Property

![Figure 320: Accessing ColorItem Collection Editor using SubItems Property](https://example.com/figure320.png)

### Description of the Interface

The **ColorItem Collection Editor** is a tool provided by Syncfusion.Windows.Forms.Tools.Gro... (Note: The namespace is partially truncated in the image). The following sections highlight the key features of this interface:

#### Group Color Items List
- **Members Listbox**: Displays the existing GroupColor items in a list format. Each item listed corresponds to an instance of `Syncfusion.Windows.Forms.Tools.GroupColorItem`.
- **Add / Remove Buttons**: Allow you to add new items or remove existing ones from the list.
- **Up / Down Arrows**: Provide the functionality to reorder the items within the list.

#### Color and SubItems Editor
- **Misc Section**: Allows you to define detailed properties for the selected GroupColor item, such as:
  - **Color**: Specifies the color for the item (e.g., Green).
  - **SubItems**: Represents a collection of sub-items associated with the GroupColor item.

### Process of Adding Color / Sub Items

To add color or sub items to the GroupColor items:
1. Select a GroupColor item from the **Members Listbox**.
2. Use the **Misc section** to set the **Color** property for the selected item.
3. Extend or manage the **SubItems** collection by utilizing the embedded editor functionality.

## API Reference

### Namespace
- `Syncfusion.Windows.Forms.Tools`

### Members
- **Properties**
  - `Color`: Specifies the color of the GroupColor item.
  - `SubItems`: Represents a collection of sub-items, allowing further customization.

- **Methods**
  - `Add()`: Adds a new GroupColorItem to the collection.
  - `Remove()`: Removes a specific GroupColorItem from the collection.

## Code Examples

Here is an example of adding a new GroupColorItem with its sub-items programmatically:

```csharp
// Adding a new GroupColorItem
var groupColorItem = new GroupColorItem();
groupColorItem.Color = Color.Green;

// Adding sub-items
groupColorItem.SubItems.Add(new ColorItem() { Color = Color.Blue });
groupColorItem.SubItems.Add(new ColorItem() { Color = Color.Red });

// Adding it to the collection
ColorItemCollection.Add(groupColorItem);
```

## Conclusion

The ability to add GroupColor items and their sub-items using the **SubItems Property** in the **ColorItem Collection Editor** provides flexibility and enhances the customization options in your Windows Forms application. By leveraging this tool, you can dynamically manage and organize color groups effectively.

<!-- tags: [product, module, control, api, version?] keywords: [GroupColor, ColorItem, Collection, Editor, SubItems, Property, Tools, Syncfusion, WindowsForms] -->
```