```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_154.jpeg
document_name: tools
page_number: 154
page_id: tools#page_154
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:58:04Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Setting Browsing Key for the Docking Manager

### Overview
- Configures the `BrowsingKey` property for the `DockingManager`.
- Requires setting `TabStop` to `true` and assigning an appropriate `TabIndex` to ensure functionality.

### Content

#### Figure 69: Browsing Key set for the Docking Manager
![Figure 69: Browsing Key set for the Docking Manager](https://example.com/figure69.png)
**Figure 69: Browsing Key set for the Docking Manager**

**Note:** Before setting the `BrowsingKey` property for the docking manager, we have to set `TabStop` property to `true` and `TabIndex` property with the appropriate value. Otherwise, its `BrowsingKey` property will not work.

##### DockingManager Property
| Property         | Description                                                                 |
|------------------|------------------------------------------------------------------------------|
| Browsing Key     | Determines the value of the key which can be used to tab through the docked controls. |

##### DockedControl Property
| Property         | Description                                                                 |
|------------------|------------------------------------------------------------------------------|
| TabStop          | Indicates whether TAB key can be used to focus the control.               |
| TabIndex         | Determines the index in the tab order that this control will occupy.      |

#### Setting Properties Through Code
These properties can be set through code by using the following code.

```csharp
[C#]
```

## API Reference

### DockingManager Properties
- `BrowsingKey`: Determines the value of the key for tabbing through docked controls.
- `TabStop`: Indicates whether TAB can be used to focus the control.
- `TabIndex`: Determines the control's position in the tab order.

## Code Examples

### C#
```csharp
// Example code for setting properties
```

<!-- tags: [Docking Manager, BrowsingKey, TabStop, TabIndex] keywords: [DockingManager, BrowsingKey, TabStop, TabIndex, Windows Forms, property settings, code examples] -->
```