```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_187.jpeg
document_name: tools
page_number: 187
page_id: tools#page_187
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:20:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Setting Foreground and Background Properties

- **C#**
  ```csharp
  this.dockingClientPanel1.Font = new System.Drawing.Font("Arial", 9F,
  System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point,
  ((byte)(0)));
  this.dockingClientPanel1.ForeColor = System.Drawing.Color.RoyalBlue;
  ```
  
- **VB.NET**
  ```vb
  Me.dockingClientPanel1.Font = New System.Drawing.Font("Arial", 9.0F,
  System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point,
  CType((0), Byte))
  Me.dockingClientPanel1.ForeColor = System.Drawing.Color.RoyalBlue
  ```

### Visual Representation

The following image illustrates a `DockingClientPanel` with the foreground and background properties set.

![DockingClientPanel with Foreground and Background Properties](https://example.com/image_of_dockingclientpanel.png)

**Figure 97: Foreground and Background properties set for the DockingClientPanel**

## Scroll properties

When the control contents are larger than its visible area, the scroll bars will automatically appear by enabling the `AutoScroll` property. The margin for the control during autoscroll is specified using the `AutoScrollMargin` property, and the minimum size for the auto scroll area can be specified using the `AutoScrollMinSize` property.

### DockingClientPanel Properties

| DockingClientPanel Property | Description |
|------------------------------|-------------|
| AutoScroll                   | Indicates whether scroll bars automatically appear when the control contents are larger than its visible area. |

## Page-level Navigation/TOC

1. Essential Tools for Windows Forms
   - Setting Foreground and Background Properties
   - Visual Representation
   - Scroll properties
     - DockingClientPanel Properties

## Cross References

- **See also:** Related sections or controls in the user guide.

<!-- tags: [DockingClientPanel, foreground, background, scroll, autoscroll, AutoScroll, AutoScrollMargin, AutoScrollMinSize] keywords: [dockingclientpanel, foreground, background, scroll, autoscroll, property, margin, minsize] -->
```