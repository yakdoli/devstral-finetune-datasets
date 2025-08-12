```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_921.jpeg
document_name: tools
page_number: 921
page_id: tools#page_921
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:42:29Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Configuring properties of FontListBox in WinForms.
- Horizontal scrolling and item height customization.

## Content

### FontListBox Configuration

```vb
[VB.NET]
Me.fontListBox1.HorizontalExtent = 150
Me.fontListBox1.HorizontalScrollbar = True
```

#### Horizontal Scrolling Example

![Figure 587: HorizontalScrollBar = "True"; HorizontalExtent = "150"](image1.png)

**See Also**

- [How to display the scrollbars always, irrespective of the number of items?](https://www.syncfusion.com/kb/how-to-display-the-scrollbars-always-irrespective-of-the-number-of-items)
- 3.5.9.1.3.2.1 FontListBox Items

### Height of the FontList Items

We can set the height of the item inside the listbox through the **ItemHeight** property. The default value is 15.

```csharp
[C#]
this.fontListBox1.ItemHeight = 20;
```

```vb
[VB.NET]
Me.fontListBox1.ItemHeight = 20
```

#### Item Height Example

![Figure 588: ItemHeight = "20"](image2.png)

## API Reference

- **HorizontalExtent**: Sets or gets the width of the FontListBox area.
- **HorizontalScrollbar**: Enables or disables the horizontal scrollbar.
- **ItemHeight**: Sets or gets the height of each item.

## Code Examples

### C#

```csharp
this.fontListBox1.ItemHeight = 20;
```

### VB.NET

```vb
Me.fontListBox1.ItemHeight = 20
```

<!-- tags: [Syncfusion Winforms, FontListBox, Windows Forms, ItemHeight, HorizontalScrollbar, HorizontalExtent] keywords: [FontListBox, ItemHeight, horizontal scrolling, Windows Forms, Syncfusion] -->
```