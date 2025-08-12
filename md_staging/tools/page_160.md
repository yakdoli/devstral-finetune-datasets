```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_160.jpeg
document_name: tools
page_number: 160
page_id: tools#page_160
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:00:19Z
fidelity: lossless
--> 

# Essential Tools for Windows Forms

## Overview
- The Docking Manager provides tab and label settings for docked windows.
- Allows control over the appearance of dock tabs through font style and height properties.

## Dock Tab and Label Settings

The Docking Manager provides tab and label settings for the docked windows. These settings let you control the appearance of the dock tabs.

### Foreground Settings for the Dock Tabs

The font style and the height of the tab controls in a tabbed docking group can be controlled using the following properties:

| DockingManager Property      | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| DockTabFont                  | Gets or sets the font for the tab control used in tabbed docking group.     |
| DockTabHeight                | Gets or sets the height for the tab control used in tabbed docking group.    |

### Code Examples

#### C#

```csharp
this.dockingManager1.DockTabFont = new System.Drawing.Font("Arial", 9F, 
    (System.Drawing.FontStyle)(System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline),
    System.Drawing.GraphicsUnit.Point, ((System.Byte)(0)));
this.dockingManager1.DockTabHeight = 30;
```

#### VB.NET

```vb
Me.DockingManager1.DockTabFont = New System.Drawing.Font("Arial", 9.0!, 
    CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Underline), System.Drawing.FontStyle),
    System.Drawing.GraphicsUnit.Point, CType(0, Byte))
Me.DockingManager1.DockTabHeight = 30
```

## API Reference

- **DockTabFont**: Gets or sets the font for the tab control used in tabbed docking group.
- **DockTabHeight**: Gets or sets the height for the tab control used in tabbed docking group.

## Cross References

See also: [unclear]

<!-- tags: [Docking Manager, Windows Forms, Font Settings, Tab Settings] keywords: [DockTabFont, DockTabHeight, tabbed docking group, tab settings, font style] -->
```