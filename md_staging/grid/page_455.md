```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_455.jpeg
document_name: grid
page_number: 455
page_id: grid#page_455
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:17:51Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Describes the behavior and configuration of scroll bars in a grid control.
- Provides code examples for setting horizontal and vertical scroll bar behavior using C# and VB.NET.

## Content

### Scroll Bar Behavior

#### HscrollBehavior
Specifies the behavior of the horizontal scroll bar. `GridScrollbarMode` enumeration provides the following options to control the scroll bar behavior: `Automatic`, `AutoScroll`, `DetectIfShared`, `DisableAutoScroll`, `Disabled`, `Enabled`, and `Shared`.

The following code examples can be used to set this property:

1. **Using C#**

   ```csharp
   // Set the behavior of the horizontal scroll bar.
   this.gridControl1.HScrollBehavior = GridScrollbarMode.Shared;
   ```

2. **Using VB.NET**

   ```vb
   ' Set the behavior of the horizontal scroll bar.
   Me.gridControl1.HScrollBehavior = GridScrollbarMode.Shared
   ```

#### VScrollBehavior
Specifies the behavior of the vertical scroll bar. `GridScrollbarMode` enumeration provides the following options to control the scroll bar behavior: `Automatic`, `AutoScroll`, `DetectIfShared`, `DisableAutoScroll`, `Disabled`, `Enabled`, and `Shared`.

The following code examples can be used to set this property:

1. **Using C#**

   ```csharp
   // Set the behavior of the vertical scroll bar.
   this.gridControl1.VScrollBehavior = GridScrollbarMode.Shared;
   ```

2. **Using VB.NET**

   ```vb
   ' Set the behavior of the vertical scroll bar.
   Me.gridControl1.VScrollBehavior = GridScrollbarMode.Shared
   ```

### Figure: VerticalScrollTips = "True"
- **Figure 174:** Displays the vertical scroll behavior when `VerticalScrollTips` is set to `True`.

   ![](https://syncfusion.comantom/sl.png)

## API Reference

### Enumerations
- `GridScrollbarMode`:
  - `Automatic`
  - `AutoScroll`
  - `DetectIfShared`
  - `DisableAutoScroll`
  - `Disabled`
  - `Enabled`
  - `Shared`

### Properties
- `HScrollBehavior`
- `VScrollBehavior`

## Code Examples

### C# Example
```csharp
this.gridControl1.HScrollBehavior = GridScrollbarMode.Shared;
this.gridControl1.VScrollBehavior = GridScrollbarMode.Shared;
```

### VB.NET Example
```vb
Me.gridControl1.HScrollBehavior = GridScrollbarMode.Shared
Me.gridControl1.VScrollBehavior = GridScrollbarMode.Shared
```

## Page-level Navigation/TOC
- [HscrollBehavior](#hscrollbehavior)
- [VScrollBehavior](#vscrollbehavior)
- [Code Examples](#code-examples)

## Cross References
See also:
- `GridScrollbarMode`
- `gridControl1`

<!-- tags: [Essential Grid, Windows Forms, ScrollBar, ScrollBarBehavior, GridScrollbarMode, C#, VB.NET, SyncfusionSDK, version:11.4.0.26] keywords: [HScrollBehavior, VScrollBehavior, GridScrollbarMode, Automatic, AutoScroll, DetectIfShared, DisableAutoScroll, Disabled, Enabled, Shared, code examples] -->
```