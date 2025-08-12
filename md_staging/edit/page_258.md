```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_258.jpeg
document_name: edit
page_number: 258
page_id: edit#page_258
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:34Z
fidelity: lossless
-->

## 4.14.14.2 OperationStopped Event

This event occurs when an operation ends.

The event handler receives an argument of type `ILongOperation`. The following `ILongOperation` members provide information specific to this event.

| Member         | Description                                        |
|----------------|----------------------------------------------------|
| ID             | Gets ID of the operation.                         |
| IsRunning      | Gets value indicating whether operation is running now. |
| Name           | Gets name of the operation.                       |
| RunningTime    | Gets time of the operation activity.              |

### [C#]

```csharp
private void editControl1_OperationStopped(Syncfusion.Windows.Forms.Edit.Interfaces.ILongOperation operation)
{
    Console.WriteLine(" OperationStopped event is raised ");
}
```

### [VB.NET]

```vb
Private Sub editControl1_OperationStopped(ByVal operation As Syncfusion.Windows.Forms.Edit.Interfaces.ILongOperation)
    Console.WriteLine(" OperationStopped event is raised ")
End Sub
```

## 4.14.15 Outlining Events

This section discusses the below given outlining events.
```