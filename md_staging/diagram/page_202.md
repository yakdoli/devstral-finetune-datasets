```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_202.jpeg
document_name: diagram
page_number: 202
page_id: diagram#page_202
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:21:00Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Content

### C#

```csharp
Diagram1_EventSink.Events.Add(new CollectionExEventHandler(e1_NodeCollectionChanging));
{
    RectangleF rect = new RectangleF(100, 100, 100, 100);
    RichTextNode richText = new RichTextNode("", rect);
    richText.Text = "Rich text box";

    NodeCollection nodeStack = new NodeCollection();
    nodeStack.Add(richText);
    MessageBox.Show(nodeStack.Count.ToString());
}

private void Form1_NodeCollectionChanging(CollectionExEventArgs e)
{
    MessageBox.Show("NodeCollectionChanging event fired");
}
```

### VB

```vb
Private Sub Form1_Load(ByVal sender As Object, ByVal e As EventArgs)
    DirectCast(diagram1.EventSink, DiagramViewerEventSink).NodeCollectionChanged += New CollectionExEventHandler(Form1_NodeCollectionChanged)
    (DirectCast(diagram1.EventSink, DiagramViewerEventSink)).NodeCollectionChanging += New CollectionExEventHandler(Form1_NodeCollectionChanging)

    Dim rect As New RectangleF(100, 100, 100, 100)
    Dim richText As New RichTextNode("", rect)
    richText.Text = "Rich text box"

    Dim nodeStack As New NodeCollection()
    nodeStack.Add(richText)

    MessageBox.Show(nodeStack.Count.ToString())
End Sub

Private Sub Form1_NodeCollectionChanging(ByVal e As CollectionExEventArgs)
    MessageBox.Show("NodeCollectionChanging event fired")
End Sub
```

### Sample Diagrams

Sample diagrams are as follows,

<!-- tags: [syncfusion, winforms, diagram control, event handling, essential diagram, vb, csharp, node collection changing, user guide] -->
```