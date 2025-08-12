```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_866.jpeg
document_name: tools
page_number: 866
page_id: tools#page_866
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:55Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- Describes the handling of **MaskSatisfied** and **MaximumSizeChanged** events in Windows Forms.
- Provides examples in both **C#** and **VB.NET** for event handling.

### Content

#### MaskSatisfied Event

##### Overview
- Triggered when the **MaskSatisfied** property of a control is satisfied.

##### Event Handler
The event handler receives arguments of type `EventArgs` to handle the raised event.

##### Code Examples

**[C#]**
```csharp
private void maskedEditBox1_MaskSatisfied(object sender, EventArgs e)
{
    Console.WriteLine(" MaskSatisfied event is raised ");
}
```

**[VB.NET]**
```vb
Private Sub maskedEditBox1_MaskSatisfied(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" MaskSatisfied event is raised ")
End Sub
```

#### MaximumSizeChanged Event

##### Overview
- Triggered when the **MaximumSize** property of a control is changed.
- The **MaximumSize** property dictates the maximum dimensions of the control.

##### Event Handler
The event handler receives arguments of type `EventArgs` to handle the raised event.

##### Code Examples

**[C#]**
```csharp
private void maskedEditBox1_MaximumSizeChanged(object sender, EventArgs e)
{
    Console.WriteLine(" MaximumSizeChanged event is raised ");
}
```

**[VB.NET]**
```vb
Private Sub maskedEditBox1_MaximumSizeChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" MaximumSizeChanged event is raised ")
End Sub
```

#### MinimumSizeChanged Event

##### Overview
- Triggered when the **MinimumSize** property of a control is changed.
- The **MinimumSize** property dictates the minimum dimensions of the control.

##### Event Handler
The event handler receives arguments of type `EventArgs` to handle the raised event.

##### Code Examples

**[C#]**
```csharp
private void maskedEditBox1_MinimumSizeChanged(object sender, EventArgs e)
{
    Console.WriteLine(" MinimumSizeChanged event is raised ");
}
```

## API Reference

### Events
- **MaskSatisfied**
- **MaximumSizeChanged**
- **MinimumSizeChanged**

### Code Examples

**[C#]**
```csharp
private void maskedEditBox1_MinimumSizeChanged(object sender, EventArgs e)
{
    Console.WriteLine(" MinimumSizeChanged event is raised ");
}
```

**[VB.NET]**
```vb
Private Sub maskedEditBox1_MinimumSizeChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" MinimumSizeChanged event is raised ")
End Sub
```

## RAG Annotations
<!-- tags: [winforms, events, mask, maximumsize, minimumsize, syncfusion] keywords: [MaskSatisfied, MaximumSizeChanged, MinimumSizeChanged, C#, VB.NET, EventHandler, Console.WriteLine, Mask, MaximumSize, MinimumSize] -->
```