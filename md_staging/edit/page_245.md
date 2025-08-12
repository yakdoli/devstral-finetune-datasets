```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_245.jpeg
document_name: edit
page_number: 245
page_id: edit#page_245
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:29Z
fidelity: lossless
--> 

## Essential Edit for Windows Forms

### Handling the `CollapsingAll` Event

#### C#

```csharp
// Handle the CollapsingAll event.
this.editControl.CollapsingAll += new EventHandler(editControl_CollapsingAll);

// Call the CollapseAll method.
this.editControl.CollapseAll();

private void editControl_CollapsingAll(object sender, CancelEventArgs e)
{
    // The below given line will be displayed in the output window at runtime.
    Console.WriteLine(" CollapsingAll event is raised ");

    // Cancels the event.
    e.Cancel = true;
}
```

#### VB.NET

```vb
' Handle the CollapsingAll event.
Me.editControl.CollapsingAll += New EventHandler(editControl_CollapsingAll)

' Call the CollapseAll method.
Me.editControl.CollapseAll()

Private Sub editControl_CollapsingAll(ByVal sender As Object, ByVal e As CancelEventArgs)
    ' The below given line will be displayed in the output window at runtime.
    Console.WriteLine(" CollapsingAll event is raised ")

    ' Cancels the event.
    e.Cancel = True
End Sub
```

### 4.14.6 ContextChoice Events

This section discusses the below given context choice events.

#### 4.14.6.1 ContextChoiceBeforeOpen Event

This event is discussed in the **Context Choice** topic.

---

## Page-level Navigation/TOC (if applicable)

- Overview
  - Essential Edit for Windows Forms
    - Handling the `CollapsingAll` Event
      - C#
      - VB.NET
    - ContextChoice Events
      - 4.14.6.1 ContextChoiceBeforeOpen Event

## Cross References

- **Context Choice** topic (referenced in the ContextChoiceBeforeOpen Event section)

## RAG Annotations

<!-- tags: [syncfusion, windows forms, event handling, collapsing, context choice events] keywords: [CollapsingAll event, CollapseAll method, cancel event, context choice, ContextChoiceBeforeOpen, EventHandler, editControl] -->
```