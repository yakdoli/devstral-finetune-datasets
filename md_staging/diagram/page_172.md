```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_172.jpeg
document_name: diagram
page_number: 172
page_id: diagram#page_172
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:17:06Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Overview of the rejected connection feature in the diagram.
- Explanation of undo/redo functionality in the history manager.

## Content

### 4.6.3 Undo / Redo

**Figure 107: Rejected Connection**

The actions can be recorded into the history manager such that the undo and redo operations can be performed. The recording can be controlled, and the undo and redo actions can be performed using the following tools.

| History Manager Tool         | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| Undo                        | Undo the previous action.                                                   |
| Redo                        | Redo the previous action. Redo action can be performed only after an undo action. |
| StartAtomicAction           | Stops recording the actions and hence will not be added to the undo history manager. |
| EndAtomicAction             | Cancels the StartAtomicAction process and turns on the recording of actions in the history manager. |

#### Programmatic Implementation

Programmatically, it is implemented as follows:

#### C#

```csharp
this.diagram1.Model.HistoryManager.Undo();
this.diagram1.Model.HistoryManager.Redo();
this.diagram1.Model.HistoryManager.StartAtomicAction("Custom Action");
this.diagram1.Model.HistoryManager.EndAtomicAction();
```

#### VB

```vb
Me.diagram1.Model.HistoryManager.Undo()
Me.diagram1.Model.HistoryManager.Redo()
Me.diagram1.Model.HistoryManager.StartAtomicAction("Custom Action")
```

## API Reference (if applicable)

## Code Examples (multi-language supported)

- **C#:**
```csharp
this.diagram1.Model.HistoryManager.Undo();
this.diagram1.Model.HistoryManager.Redo();
this.diagram1.Model.HistoryManager.StartAtomicAction("Custom Action");
this.diagram1.Model.HistoryManager.EndAtomicAction();
```

- **VB:**
```vb
Me.diagram1.Model.HistoryManager.Undo()
Me.diagram1.Model.HistoryManager.Redo()
Me.diagram1.Model.HistoryManager.StartAtomicAction("Custom Action")
```

## Page-level Navigation/TOC (if applicable)

None.

## Cross References

None.

<!-- tags: [product, module, control, api, version?] keywords: [history manager, undo, redo, rejected connection, syncfusion, windows forms, essential diagram, actions, atomic action, functionality, recording] -->
```