```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_033.jpeg
document_name: edit
page_number: 033
page_id: edit#page_033
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:56:11Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Demonstrates the capabilities of the Edit Control in Syncfusion Winforms for managing Undo/Redo actions and enabling action grouping.
- Provides sample code and a screenshot showcasing the grouping actions feature.

## Content

### Code Example: Managing Undo/Redo and Grouping Actions

```vb
Dim canUndo As Boolean = Me.editControl.CanUndo

' Indicates whether it is possible to Redo in the Edit Control.
Dim canRedo As Boolean = Me.editControl.CanRedo

' Clears the Undo buffer.
Me.editControl.ResetUndoInfo()

' Enable grouping for Undo / Redo actions.
Me.editControl.GroupUndo = True
```

### Screenshot: Action Grouping in Edit Control

The following screenshot shows action grouping in Edit Control.

![Grouping Actions in Edit Control](https://<image-source-url>)

**Figure 9: Grouping Actions in Edit Control**

A sample which demonstrates Action Grouping is available in the following sample installation location.

## API Reference

### Properties
- `CanUndo`: Indicates whether it is possible to Undo actions in the Edit Control.
- `CanRedo`: Indicates whether it is possible to Redo actions in the Edit Control.
- `GroupUndo`: Enables or disables the grouping of Undo/Redo actions.

### Methods
- `ResetUndoInfo()`: Clears the Undo buffer.

## Code Examples

### Example: Enabling Action Grouping

```vb
Me.editControl.GroupUndo = True
```

## Page-level Navigation/TOC
- [Action Grouping Example](#action-grouping-example)

## Cross References
- See also: [Undo/Redo Actions in Edit Control](#undo-redo-actions-in-edit-control)

<!-- tags: [syncfusion-sdk, winforms, edit control, undo, redo, action grouping] keywords: [Edit Control, Undo, Redo, GroupUndo, Action Grouping, canUndo, canRedo, ResetUndoInfo] -->
```