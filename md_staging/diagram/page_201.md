```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_201.jpeg
document_name: diagram
page_number: 201
page_id: diagram#page_201
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:21:09Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

This topic discusses the events that are fired while adding or removing the node to or from the node collection. The below table discusses all the available node collection events.

| DiagramViewerEventSink             | Description                                         |
|------------------------------------|-----------------------------------------------------|
| NodeCollectionChanged             | Triggered after the node collection changes are completed. |
| NodeCollectionChanging            | Triggered when the node collection is edited.       |

## Event Args

EventArgs members can be accessed using the following members.

| NodeCollection EventArgs Member    | Description                                         |
|------------------------------------|-----------------------------------------------------|
| Cancel                           | Indicates whether the NodeCollectionChanged event should be canceled. |
| ChangeType                       | It returns the following possible values:<br>- Insert - whether the node is inserted<br>- Remove – whether the node is removed |
| Element                          | Returns whether the head or tail end is moved.      |
| Elements                         | Returns the elements collection on which the event occurs. |
| Index                            | Returns the zero-based index into the collection on which the event occurred. |
| Owner                            | Returns the base class onto which the node is added. |

Inside the NodeCollectionChanged event handler, user can identify whether a node is added or removed from the node collection using simple message box as follows.

### C#

```csharp
private void Form1_Load(object sender, EventArgs e)
{
    ((DiagramViewerEventSink)diagram1.EventSink).NodeCollectionChanged
        += new CollectionExEventHandler(Form1_NodeCollectionChanged);
    ((DiagramViewerEventSink)diagram1.EventSink).NodeCollectionChanging
        += new 
```

## References

See also: NodeCollectionChanged, NodeCollectionChanging, EventSink.

<!-- tags: [node collection, events, Windows Forms, Diagram Viewer, Syncfusion Winforms] keywords: [node addition, node removal, event handling, NodeCollectionChanged, NodeCollectionChanging] -->
```