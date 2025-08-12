```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_254.jpeg
document_name: tools
page_number: 254
page_id: tools#page_254
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:02:57Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- Describes techniques to avoid flickering while loading dock state.
- Explains how to restore the original docking windows layout using the `LoadDesignerDockState()` method.

## Content

### 3.4.4.2.1 How to avoid flickering while loading dock state?

Flickering can be avoided by calling the below methods.

#### LockDockPanelsUpdate and UnLockDockPanelsUpdate Methods - The

LockDockPanelsUpdate and UnLockDockPanelsUpdate methods are used to lock and unlock the panel's repaint ing respectively. For example to avoid flickering while loading a dock state, these methods can be used in the following way.

```csharp
//Avoids flickering while loading dock state
this.dockingManager1.LockHostFormUpdate();
this.dockingManager1.LoadDockState();
this.dockingManager1.UnlockHostFormUpdate();
```

```vbnet
'Avoids flickering while loading dock state
Me.dockingManager1.LockHostFormUpdate()
Me.dockingManager1.LoadDockState()
Me.dockingManager1.UnlockHostFormUpdate()
```

#### See Also

- [Persistence](Persistence)

### 3.4.4.2.2 How to restore the original docking windows layout that was set within the Windows Forms designer?

Calling `LoadDesignerDockState()` method at run time, will restore the docking windows layout that was set in the Designer.

```csharp
this.dockingManager1.LoadDesignerDockState();
```

```vbnet
Me.dockingManager1.LoadDesignerDockState()
```

### Permissions

This content is copyrighted by Syncfusion as of 2013, and all rights are reserved.

## Footer

© 2013 Syncfusion. All rights reserved. 254 | Page

<!-- tags: [product, module, control, api, version?] keywords: [Flickering, Docking, Windows Forms, LoadDockState, DockManager, LoadDesignerDockState, Persistence, FlickerAvoidance, WinForms, DockState, Visual Basic.NET, C#, Syncfusion Windows Forms, Essential Tools] -->
```