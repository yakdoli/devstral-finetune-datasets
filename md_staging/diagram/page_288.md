```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_288.jpeg
document_name: diagram
page_number: 288
page_id: diagram#page_288
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:49Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Content

```csharp
Dim port As ConnectionPoint = HandlesHitTesting.GetConnectionPointAtPoint(circle, New Point(120, 120))
```

### 5.29 How To Serialize the Custom Property Of a Node

Essential Diagram supports custom serialization. To serialize the custom property, you should derive the `Group` class and create a custom node. After creating a custom node, you should override the `GetObjectData()` method and add the custom property in the `SerializationInfo`. This is illustrated in the below code snippet.

#### C#
```csharp
[Serializable()]
public class CustomNode : Group
{
    protected CustomNode(SerializationInfo info, StreamingContext context) : base(info, context)
    {
        this.m_nodeInformation = info.GetString("strDescription");
    }
    protected override void GetObjectData(SerializationInfo info, StreamingContext context)
    {
        base.GetObjectData(info, context);

        // Additional member variables are serialized here.
        info.AddValue("strDescription", this.NodeInformation);
    }
}
```

#### VB.NET
```vbnet
<Serializable()>
Public Class CustomNode
    Inherits Group
    Public Sub New()
    End Sub

    Protected Sub New(ByVal info As SerializationInfo, ByVal context As StreamingContext)
        MyBase.New(info, context)
        Me.m_nodeInformation = info.GetString("strDescription")
    End Sub
End Class
```

## API Reference

### Constructors
- `CustomNode(SerializationInfo info, StreamingContext context)`  
  Initializes a new instance of the `CustomNode` class.

### Methods
- `GetObjectData(SerializationInfo info, StreamingContext context)`  
  Called by the formatter to populate a `SerializationInfo` with the data needed to serialize the object.

## Code Examples

### C#
```csharp
[Serializable()]
public class CustomNode : Group
{
    public string NodeInformation { get; protected set; }

    protected CustomNode(SerializationInfo info, StreamingContext context) : base(info, context)
    {
        NodeInformation = info.GetString("strDescription");
    }

    protected override void GetObjectData(SerializationInfo info, StreamingContext context)
    {
        base.GetObjectData(info, context);
        info.AddValue("strDescription", NodeInformation);
    }
}
```

### VB.NET
```vbnet
<Serializable()>
Public Class CustomNode
    Inherits Group

    Public Property NodeInformation As String

    Public Sub New(ByVal info As SerializationInfo, ByVal context As StreamingContext)
        MyBase.New(info, context)
        NodeInformation = info.GetString("strDescription")
    End Sub

    Protected Overloads Overrides Sub GetObjectData(ByVal info As SerializationInfo, ByVal context As StreamingContext)
        MyBase.GetObjectData(info, context)
        info.AddValue("strDescription", NodeInformation)
    End Sub
End Class
```

## Cross References

See also: Essential Diagram serialization, custom serialization, serialization of custom properties, serializationinfo, streamingcontext, group class

<!-- tags: [syncfusion, windowsforms, diagram, serialization, custom property, essential diagram] keywords: [serialization, custom property, group class, serializationinfo, streamingcontext, object data] -->
```