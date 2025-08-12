```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_078.jpeg
document_name: edit
page_number: 078
page_id: edit#page_078
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:58:56Z
fidelity: lossless
-->

### WinForms-specific conventions
In this section, we will cover specific features related to the handling of spaces and tabs within the `EditControl` component of Syncfusion WinForms. Below are the key operations available for managing tab and space handling, presented in both C# and VB.NET.

#### Example Code in C#
```csharp
// Convert spaces to tabs.
this.editControl.TabifySelection();

// Converts tabs to spaces.
this.editControl.UntabifySelection();

// Add or insert leading tab symbol to selected lines.
this.editControl.AddTabsToSelection();

// Remove leading tab symbol from selected lines.
this.editControl.RemoveTabsFromSelection();
```

#### Example Code in VB.NET
```vb
' Covert spaces to tabs.
Me.editControl.TabifySelection()

' Converts tabs to spaces.
Me.editControl.UntabifySelection()

' Add or insert leading tab symbol to selected lines.
Me.editControl.AddTabsToSelection()

' Remove leading tab symbol from selected lines.
Me.editControl.RemoveTabsFromSelection()
```

### 4.4.6.1 WhiteSpace Indicators
- **Objective:** Enable the `EditControl` to indicate whitespaces in its content using default indicators.

#### Feature Details
The `EditControl` is capable of showing white spaces within its contents using predefined indicators as described below:

1. **Single Spaces:** Indicated by using Dots.
2. **Tabs:** Indicated by using Right Arrows.
3. **Line Feeds:** Indicated by using a special Line Feed Symbol.

---

<!-- tags: [WinForms, EditControl, WhiteSpace Indicators, Tab Handling] keywords: [EditControl, Whitespace, TabifySelection, UntabifySelection, AddTabsToSelection, RemoveTabsFromSelection, Single Spaces, Tabs, Line Feeds] -->
```