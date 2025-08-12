```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_692.jpeg
document_name: tools
page_number: 692
page_id: tools#page_692
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:28:41Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Content

```csharp
args.OldSplitPosition.ToString() + " to " + 
args.NewSplitPosition.ToString());
}
```

```vb
[VB.NET]

Private Sub splitContainerAdv2_SplitterMoved(ByVal sender As Object, ByVal args As SplitterMoveEventArgs)
    MessageBox.Show("The Splitter has moved from : " + 
args.OldSplitPosition.ToString() + " to " + 
args.NewSplitPosition.ToString())
End Sub
```

![SplitterMoved Event Illustrated](attachment://image.png)
**Figure 430: SplitterMoved Event Illustrated**

#### SplitterMoving Event
- This event is handled while the splitter is moving.

```csharp
[C#]

private void splitContainerAdv2_SplitterMoving(object sender, SplitterMoveEventArgs args)
{
    MessageBox.Show("The splitter is moving to : " + 
args.NewSplitPosition.ToString());
}
```

```vb
[VB.NET]

Private Sub splitContainerAdv2_SplitterMoving(ByVal sender As Object, ByVal args As SplitterMoveEventArgs)

End Sub
```

### API Reference
- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Class**: SplitContainerAdv
- **Event**: SplitterMoved
- **Event**: SplitterMoving

### Code Examples

#### C#

```csharp
private void splitContainerAdv2_SplitterMoved(object sender, SplitterMoveEventArgs args)
{
    MessageBox.Show("The Splitter has moved from : " + 
args.OldSplitPosition.ToString() + " to " + 
args.NewSplitPosition.ToString());
}
```

```csharp
private void splitContainerAdv2_SplitterMoving(object sender, SplitterMoveEventArgs args)
{
    MessageBox.Show("The splitter is moving to : " + 
args.NewSplitPosition.ToString());
}
```

#### VB

```vb
Private Sub splitContainerAdv2_SplitterMoved(ByVal sender As Object, ByVal args As SplitterMoveEventArgs)
    MessageBox.Show("The Splitter has moved from : " + 
args.OldSplitPosition.ToString() + " to " + 
args.NewSplitPosition.ToString())
End Sub
```

```vb
Private Sub splitContainerAdv2_SplitterMoving(ByVal sender As Object, ByVal args As SplitterMoveEventArgs)

End Sub
```

---

<!-- tags: [Syncfusion, Winforms, SplitContainerAdv, SplitterMoved, SplitterMoving, Event] keywords: [Windows Forms, splitter, splitter moved event, splitter moving event, Windows Forms SplitContainerAdv, event handling, MessageBox] -->
```