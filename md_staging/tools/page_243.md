```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_243.jpeg
document_name: tools
page_number: 243
page_id: tools#page_243
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:01:27Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Enable tabbed MDI manager tabs rendering.
- Code snippets for dock control management.
- Handling dock controls parent relationships through code.
- Visual representation of tabbed dockable windows.

### Tabbed Dockable Window Sample

#### VB.NET Code Example
```vb.net
' Enable the rendering for the Tabbed MDI manager tabs.
Private Sub tm_TabControlAdded(ByVal sender As Object, ByVal args As TabbedMDITabControlEventArgs)
    args.TabControl.TabStyle = GetType(TabRendererWhidbey)
End Sub
```

### Figure 105: Tabbed Style Dockable Window

![Tabbed Style Dockable Window](image_description_here)

---

### See Also
- [Tabbed Docking](#tabbed-docking)

### How to get dock controls parent relationship through code?

#### Code Snippet for Initialization

This can be done using the below code snippet.

```csharp
private void InitializeDockControlState()
{
    this.dockingManager1.FloatControl(this.myUserControl1, new
```

--- 

### API Reference (if applicable)
- Refer to the Syncfusion documentation for specific namespaces, classes, and members related to `DockingManager`, `FloatControl`, and `TabRenderer`.

### Code Examples
- See the above VB.NET and C# code snippets for examples of enabling tabbed rendering and managing docked controls.

### Page-level Navigation/TOC (if applicable)
- This document covers enabling tabbed rendering and managing dock controls in Windows Forms applications.

### Cross References
- Refer to additional resources on tabbed docking and dock control management in the Syncfusion WinForms documentation.

---

<!-- tags: [syncfusion, windowsforms, tabbedmdi, dockcontrols, tabrenders, codeexamples, version:11.4.0.26] keywords: [tabbed MDI, dock controls, parent relationship, code snippets, tabbed rendering] -->
```