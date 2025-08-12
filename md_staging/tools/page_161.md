```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_161.jpeg
document_name: tools
page_number: 161
page_id: tools#page_161
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:02:37Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Docking Window Appearance

Figure 76: FontStyle = "Arial 9, Bold, Underline"; TabHeight = "30"

![DockingWindow Appearance](image.png)

**Note:** `ResetDockTabFont` and `ResetDockTabHeight` methods let you reset the above settings.

### Code Examples

**[C#]**

```csharp
// Restoring to default settings
this.dockingManager1.ResetDockTabFont();
this.dockingManager1.ResetDockTabHeight();
```

**[VB.NET]**

```vb
' Restoring to default settings
Me.dockingManager1.ResetDockTabFont()
Me.dockingManager1.ResetDockTabHeight()
```

### See Also

- Tabbing the Docked controls in *Tabbed Docking*
- 3.4.3.5.1.2 *AutoHidden Tabs*

The font style for the **autohidden tabs** can be specified in the **AutoHideTabFont** property.

### Properties

| DockingManager Property       | Description                     |
|-------------------------------|----------------------------------|
| AutoHideTabFont              | Gets or sets the tab for the autohide tab control. |

## Page-level Navigation/TOC
- None

## Cross References
- None

## API Reference

### Properties

- **AutoHideTabFont**
  - Description: Gets or sets the font for the autohide tab control.

<!-- tags: [syncfusion-sdk, winforms, essential-tools, docking, fontstyle, tabbed-docking, autohide-tabs] keywords: [docktabfont, docktabheight, resetdocktabfont, resetdocktabheight, tab样式, 自动隐藏标签, AutoHideTabFont, tabbed docking, auto hidden tabs] -->
```