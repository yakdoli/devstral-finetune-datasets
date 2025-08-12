```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_136.jpeg
document_name: tools
page_number: 136
page_id: tools#page_136
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:44:23Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Docking Window Indicators

|            | Ctrl - Indicates the docking window. |
|------------|---------------------------------------|

### Code Examples

#### [C#]

```csharp
this.dockingManager.IsSameTabbedGroup(this.listBox1, this.checkedListBox1);
this.dockingManager1.GetTabPosition(this.listBox1);
this.dockingManager1.GetTabbedSiblings(this.listView1);
this.dockingManager1.IsTabbed(this.listBox1);
```

#### [VB.NET]

```vb
Me.dockingManager.IsSameTabbedGroup(Me.listBox1, Me.checkedListBox1)
Me.dockingManager1.GetTabPosition(Me.listBox1)
Me.dockingManager1.GetTabbedSiblings(Me.listView1)
Me.dockingManager1.IsTabbed(Me.listBox1)
```

### See Also

- [Getting Started, DockAllow Event, Dock Arrow Settings](Getting Started, DockAllow Event, Dock Arrow Settings)

### 3.4.3.1.3 Floating

#### Floating a Control

The FloatControl method enables the end users to float a particular control. Using this method, we can float a single control even if it is tabbed with many controls.

#### Code Examples

##### [C#]

```csharp
Rectangle rcfrm = this.Bounds;
this.dockingManager.FloatControl(this.listBox1, new Rectangle(rcfrm.Right + 25, rcfrm.Bottom - 150, 175, 200));
```

##### [VB.NET]

```vb
Dim rcfrm As Rectangle = Me.Bounds
Me.dockingManager.FloatControl(Me.listBox1, New Rectangle(rcfrm.Right + 25, rcfrm.Bottom - 150, 175, 200))
```

## Page-level Navigation/TOC (if applicable)

- Docking Window Indicators
- Code Examples
  - C#
  - VB.NET
- See Also
- 3.4.3.1.3 Floating
  - Floating a Control
  - Code Examples

## RAG Annotations

<!-- tags: [Product, Module, Control, API, Version] keywords: [DockingWindow, FloatControl, Toolbox, Windows Forms, Support, Event, Settings, TabPosition, TabbedSiblings, Tabbed, Bounds, Rectangle, C#, VB.NET] -->
```