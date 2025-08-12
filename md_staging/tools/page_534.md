```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_534.jpeg
document_name: tools
page_number: 534
page_id: tools#page_534
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:19:20Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes how to configure and use Color Picker UIAdv1 to select and customize subitem colors.
- Demonstrates adding group and subitem colors to the recent color group using code.

## Content

### Color Picker UI Component Configuration

#### Selecting Subitem Color

![](./assets/tools/ColorItem_Collection_Editor.png)

**Figure 321: Selecting Subitem Color**

Code samples are provided to add and configure groupColor items in the Color Picker UIAdv1 control.

#### C#

```csharp
this.colorPickerUIAdv1.RecentGroup.Items.Add(groupColorItem0);
this.colorPickerUIAdv1.RecentGroup.IsSubItemsVisible = true;
this.colorPickerUIAdv1.RecentGroup.SubItemsDepth = 1;
```

#### VB.NET

```vb
Me.colorPickerUIAdv1.RecentGroup.Items.Add(groupColorItem0)
Me.colorPickerUIAdv1.RecentGroup.IsSubItemsVisible = True
Me.colorPickerUIAdv1.RecentGroup.SubItemsDepth = 1
```

#### GroupColor Item and Sub Item Added to Recent Color Group

![](./assets/tools/GroupColor_Item_Sub_Item.png)

**Figure 322: GroupColor Item and a Sub Item added to Recent Color Group**

## API Reference

### Members
- `Items.Add(groupColorItem0)`  
  Adds a group color item to the recent group of the Color Picker UIAdv1.
- `IsSubItemsVisible = true`  
  Enables the visibility of subitems within the recent group.
- `SubItemsDepth = 1`  
  Sets the depth level for subitems to ensure they are displayed.

## Code Examples

The provided C# and VB.NET code examples demonstrate how to configure the recent group in the Color Picker UIAdv1 control to display subitems.

### Additional Notes
- Ensure that the Color Picker UIAdv1 control is properly initialized before configuring the recent group.
- Adjust `SubItemsDepth` as needed to control the visibility of nested subitems.

### Cross References
- Refer to the "Color Picker UIAdv1 Overview" for a comprehensive understanding of its features and API.
- For more advanced styling options, see the "Custom Rendering in Color Picker UIAdv1" section.

## RAG Annotations
```html
<!-- tags: ["Syncfusion", "WinForms", "Color Picker UIAdv1", "GroupColorItem", "SubItemsDepth", "IsSubItemsVisible", "version 11.4.0.26"] keywords: [Color Picker, Group Color Item, Subitem, Recent Color, Visibility, Depth, Configuration] -->
```
``` 
