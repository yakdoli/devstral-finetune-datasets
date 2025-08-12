```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_920.jpeg
document_name: tools
page_number: 920
page_id: tools#page_920
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:42:37Z
fidelity: lossless
-->

## Windows Forms Selection Modes

### SelectionMode Property Example

```csharp
this.fontListBox1.SelectionMode = 
System.Windows.Forms.SelectionMode.MultiExtended;
```

```vb
Me.fontListBox1.SelectionMode = 
System.Windows.Forms.SelectionMode.MultiExtended
```

**Figure 586: Selection Modes of FontListBox**

### ScrollBar Settings

#### Horizontal Scrollbar

FontListbox control by default has a vertical scrollbar. It can also have a horizontal scrollbar. This section will discuss the properties which set the scrollbar for the control.

### Horizontal Scrollbar

Horizontal scrollbar can be displayed if the items are beyond the right edge of the FontListBox. The below properties let you do that.

| Properties               | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| HorizontalScrollbar      | Sets the horizontal scrollbar for the control if the item exceeds beyond the right edge of the FontListBox control. |
| HorizontalExtent         | Specifies the width of the control, when HorizontalScrollbar property is set to true.                            |

### C# Example

```csharp
this.fontListBox1.HorizontalExtent = 150;
this.fontListBox1.HorizontalScrollbar = true;
```

## API Reference

### Properties

- **HorizontalScrollbar**: Sets the horizontal scrollbar for the control if the item exceeds beyond the right edge of the FontListBox control.
- **HorizontalExtent**: Specifies the width of the control, when HorizontalScrollbar property is set to true.

### Methods

- **Enable**: Enables the horizontal scrollbar.
- **Disable**: Disables the horizontal scrollbar.

### Events

- **Scroll**: Triggered when the scrollbar is scrolled.

## Code Examples

### C#

```csharp
// Enable horizontal scrollbar
this.fontListBox1.HorizontalScrollbar = true;

// Set horizontal extent
this.fontListBox1.HorizontalExtent = 150;
```

### VB.NET

```vb
' Enable horizontal scrollbar
Me.fontListBox1.HorizontalScrollbar = True

' Set horizontal extent
Me.fontListBox1.HorizontalExtent = 150
```

### RAG Annotations

<!-- tags: windows forms, fontlistbox, selectionmode, scrollbars, horizontalscrollbar, horizontalextent -->
```