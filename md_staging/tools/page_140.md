```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_140.jpeg
document_name: tools
page_number: 140
page_id: tools#page_140
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:46:57Z
fidelity: lossless
-->

Essential Tools for Windows Forms

```csharp
Me.dockingManager1.AutoHideActiveControl = True
Me.dockingManager1.AutoHideInterval = 500
Me.DockingManager1.AutoHideSelectionStyle =
Syncfusion.Windows.Forms.Tools.AutoHideSelectionStyle.Click
```

### Displaying Full Caption In AutoHide Mode

Create a docked window with two listbox. Dock the controls. Tab the controls and set the `FullCaptionsInAutoHideMode` property. Setting this property to true, will display the full caption text in the auto hidden tabgroup's page. It displays full caption within the application if necessary with a scrollbar, so that end user can scroll and view the hidden tab's full caption.

```csharp
[C#]

this.dockingManager1.FullCaptionsInAutoHideMode = true;
```

```vbnet
[VB.NET]

Me.dockingManager1.FullCaptionsInAutoHideMode = True
```

![AutoHidden Tabs with truncated Caption Text](https://image.pollinations.ai/prompt=AutoHidden%20Tabs%20with%20truncated%20Caption%20Text)

**Figure 57: AutoHidden Tabs with truncated Caption Text**

## Page-level Navigation/TOC (if applicable)

- Displaying Full Caption In AutoHide Mode

## Cross References

- None

## RAG Annotations

<!-- tags: [tools, windows forms, autohide, captions, hidden tabs, scrollbar] keywords: [autohide, captions, hidden tabs, scrollbar, autohidden, display full caption, docked window, listbox, controls tab, end user scroll, full caption viewing] -->
```