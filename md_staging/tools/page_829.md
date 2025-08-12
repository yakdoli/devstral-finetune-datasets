```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_829.jpeg
document_name: tools
page_number: 829
page_id: tools#page_829
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:36:39Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### EditableList Property - DockPadding

The following image displays the EditableList control with the dock padding for all the edges set to 5.

| EditableList Property | Description |
|-----------------------|-------------|
| DockPadding | Gets the dock padding for all edges of the control. |

![](https://example.com/image_url.jpg)

**Figure 528: DockPadding.All set to 5**

#### Code Examples

**[C#]**

```csharp
this.editableList1.DockPadding.All = 5;
```

**[VB.NET]**

```vb
Me.editableList1.DockPadding.All = 5
```

### Want Button

You can display the button to the right while editing the items in the EditableList control by setting `WantButton` to `true`.

| EditableList Property | Description |
|-----------------------|-------------|
| WantButton | Specifies whether to show button to the right while editing. |

**Figure 529: Want Button**

![](https://example.com/image_url.jpg)

- **With Want Button**
- **Without Want Button**

#### Code Examples

**[C#]**

```csharp
this.editableList1.WantButton = true;
```

## API Reference

### Properties

- **DockPadding**: Gets the dock padding for all edges of the control.
- **WantButton**: Specifies whether to show button to the right while editing.

## Cross References

See also:
- [EditableList control](#editableList-control)

<!-- tags: [Syncfusion, Windows Forms, EditableList, DockPadding, WantButton] keywords: [control, property, editableList, dockPadding, wantButton, WindowsForms, SyncfusionWinforms] -->
```