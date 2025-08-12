```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_260.jpeg
document_name: edit
page_number: 260
page_id: edit#page_260
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:12Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Content

### Event Handling and Properties

The following table lists the key properties and their descriptions:

| Member        | Description                                        |
|---------------|----------------------------------------------------|
| Cancel       | Gets / sets value indicating whether the user cancels the underlying event. |
| CollapsedText | Gets / sets collapsed text.                        |
| CollapseName  | Gets / sets collapse name.                        |
| Collapser    | Gets / sets collapser.                            |

#### C# Example

```csharp
private void editControl_OutliningBeforeExpand(object sender, Syncfusion.Windows.Forms.Edit.OutliningEventArgs e)
{
    Console.WriteLine(" OutliningBeforeExpand event is raised ");
}
```

#### VB.NET Example

```vb.net
Private Sub editControl1_OutliningBeforeExpand(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.OutliningEventArgs)
    Console.WriteLine(" OutliningBeforeExpand event is raised ")
End Sub
```

### 4.14.15.3 OutliningCollapse Event

This event is raised when a region collapses.

The event handler receives an argument of type `CollapseEventArgs`. The following `CollapseEventArgs` members provide information specific to this event:

| Member        | Description                              |
|---------------|------------------------------------------|
| CollapsedText | Gets / sets collapsed text.             |
| CollapseName  | Gets / sets collapse name.             |
| Collapser    | Gets / sets collapser.                 |

#### C# Example (Partial)

```csharp
private void editControl1_OutliningCollapse(object sender,
```

## API Reference

### CollapseEventArgs Members
- **CollapsedText**: Gets / sets the text that is collapsed.
- **CollapseName**: Gets / sets the name associated with the collapse.
- **Collapser**: Gets / sets the collapser control or object responsible for the collapse action.

### Event Handling

Events such as `OutliningBeforeExpand` and `OutliningCollapse` can be handled by subscribing to the event and providing a corresponding event handler that processes the event arguments.

## Code Examples

The examples above demonstrate how to handle `OutliningBeforeExpand` and `OutliningCollapse` events in both C# and VB.NET. These events allow developers to perform custom actions when a region is expanded or collapsed in a document control.

<!-- tags: [syncfusion, windows forms, outlining, event handling, collapse event, edit control] keywords: [OutliningBeforeExpand, OutliningCollapse, CollapseEventArgs, event handler, region collapse, document control, user interaction] -->
```