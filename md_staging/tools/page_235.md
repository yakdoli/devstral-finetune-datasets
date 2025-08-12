```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_235.jpeg
document_name: tools
page_number: 235
page_id: tools#page_235
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:53:37Z
fidelity: lossless
-->

## Overview

- The page explains the docking manager event `InitializeControlOnLoad` in VB.NET.
- Discusses handling events for different controls such as "Suite Logo," "Suite Info," "Tools Info," etc.
- Covers the `ProvideGraphicsItems` event related to paint actions for dockable control captions in the Syncfusion Winforms control suite.

## Content

### Event Handling in VB.NET

```vb
[VB.NET]

Protected Sub DockingManager_InitializeControlOnLoad(ByVal sender As Object, ByVal args As InitializeControlOnLoadEventArgs)
    Console.WriteLine("InitializeControlOnLoad Event is Raised for the Control : " + args.ControlName)
    Dim dockingmgr As DockingManager = CType(ConversionHelpers.AsWorkaround(sender, GetType(DockingManager)), DockingManager)
    Select Case args.ControlName
        Case "Suite Logo"
            Me.ActivateSuiteLogoControl(dockingmgr, False)
            ' break
        Case "Suite Info"
            Me.ActivateSuiteInfoControl(dockingmgr, False)
            ' break
        Case "Tools Info"
            Me.ActivateToolsInfoControl(dockingmgr, False)
            ' break
        Case "Tools Logo"
            Me.ActivateToolsLogoControl(dockingmgr, False)
            ' break
        Case "Grid Logo"
            Me.ActivateGridLogoControl(dockingmgr, False)
            ' break
        Case "Grid Info"
            Me.ActivateGridInfoControl(dockingmgr, False)
            ' break
    End Select
End Sub
```

#### 3.4.3.8.11 ProvideGraphicsItems Event

The `ProvideGraphicsItems` event occurs whenever a dockable control's caption needs to be painted. The background, foreground, etc., of the control's caption, when needing to be painted, triggers this event. The docked control name, which is to be painted, can be displayed using the `control` property.

## Page-level Navigation/TOC (if applicable)
- [unclear] (From the image, no explicit table of contents is visible, but this could be inferred based on the structure of the user guide.)

## Cross References
- See also: Windows Forms, Docking Manager, Visual Basic.NET, Event Handling

<!-- tags: [Syncfusion Winforms, Docking Manager, VB.NET, EventHandling, UI-SDK, version:11.4.0.26] keywords: [InitializeControlOnLoad, ProvideGraphicsItems, Dockable Controls, CaptionPainting, Event, UI, Syncfusion] -->
```