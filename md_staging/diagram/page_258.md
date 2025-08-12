```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_258.jpeg
document_name: diagram
page_number: 258
page_id: diagram#page_258
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:25Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
    ((SelectTool)evtArgs.Tool).SelectMode = 
    SelectMode.Intersecting;
}
}
```

### [VB]

```vb
AddHandler (CType(Diagram1.EventSink, 
DiagramViewerEventSink)).ToolActivated, AddressOf Diagram_ToolActivated

Private Sub Diagram_ToolActivated(ByVal evtArgs As ToolEventArgs)
    If TypeOf evtArgs.Tool Is SelectTool Then
        ' change the SelectionMode as "Intersecting" which Specifies 
        ' that objects intersecting the tracking rectangle will be selected by 
        ' the tool.
        CType(evtArgs.Tool, SelectTool).SelectMode = 
        SelectMode.Intersecting
    End If
End Sub
```

## 5.5 How To Combine Different Actions Into One Atomic Action To Avoid the Undo Operation On Certain Actions

This is done by calling the Model.HistoryManager.StartAtomicAction(string description) / EndAtomicAction() methods.

The actions can be recorded into the history manager such that the undo and redo operations can be performed. The recording can be controlled and the undo and redo actions can be performed using the following tools.

- **StartAtomicAction**-This tool, when called, stops recording the actions and hence will not be added to the undo history manager.
- **EndAtomicAction**-This tool cancels the StartAtomicAction process and turns on the recording of actions in the history manager.

### [C#]

```csharp
[C#]
```
```