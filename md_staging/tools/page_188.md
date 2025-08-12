```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_188.jpeg
document_name: tools
page_number: 188
page_id: tools#page_188
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:19:08Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

| AutoScrollMargin                   | Indicates the margin around controls during auto scroll.                          |
|-------------------------------------|-----------------------------------------------------------------------------------|
| AutoScrollMinSize                  | Indicates the minimum logical size for auto scroll region.                          |

### Scroll Properties

[C#]

```csharp
this.dockingClientPanel1.AutoScroll = true;
this.dockingClientPanel1.AutoScrollMargin = new System.Drawing.Size(1, 1);
this.dockingClientPanel1.AutoScrollMinSize = new System.Drawing.Size(1, 1);
```

[VB.NET]

```vb
Me.dockingClientPanel1.AutoScroll = True
Me.dockingClientPanel1.AutoScrollMargin = New System.Drawing.Size(1, 1)
Me.dockingClientPanel1.AutoScrollMinSize = New System.Drawing.Size(1, 1)
```

![Scroll properties set for the DockingClientPanel](images/placeholder_for_scroll_properties.png)

**Figure 98: Scroll properties set for the DockingClientPanel**

### Sizing Properties

The **AutoSize** property, when set, will allow the control to automatically size itself to fit its contents. The resize mode can be specified using the **AutoSizeMode** property.

| DockingClientPanel Property | Description |
|-----------------------------|-------------|
| AutoSize                   | Specifies whether a control will automatically |

### Key Features

1. **AutoScrollMargin**
   - Indicates the margin around controls during auto scroll.
2. **AutoScrollMinSize**
   - Indicates the minimum logical size for the auto scroll region.
3. **AutoSize**
   - Allows automatic sizing of the control to fit its contents.
4. **AutoSizeMode**
   - Specifies the resizing mode to ensure the control adjusts correctly.

### References
- [DockingClientPanel Documentation](#)
- [Scrolling and Sizing Properties](#)

<!-- tags: [Syncfusion Winforms, DockClientPanel, AutoScrollMargin, AutoScrollMinSize, AutoSize, AutoSizeMode, version 11.4.0.26] keywords: [DockingClientPanel, AutoScroll, AutoSize, WinForms, version 11.4.0.26] -->
```