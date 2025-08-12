```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_238.jpeg
document_name: edit
page_number: 238
page_id: edit#page_238
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:32Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Content

### 14. Specifying German Resources During Run Time

Finally, you should specify your application to fetch the German resources during run time. To change the UI culture of the current thread, add the following code in the Forms constructor before the `InitializeComponent()`:

```csharp
System.Threading.Thread.CurrentThread.CurrentUICulture = new System.Globalization.CultureInfo("de-DE");
```

### 15. Running the Application with German Localization

Now, run your application that contains the Syncfusion Edit Control, and open the Find dialog box. You will see the dialog box in German.

![Find dialog box localized to German](text/placeholder_image_path.png)

*Figure 81: Find dialog box localized to German*

### 4.14 Edit Control Events

This section discusses various events handled for the Edit control. The events are listed below:

#### 4.14.1 CanUndoRedoChanged Event

This event occurs when the CanUndoRedo state is changed. The CanUndo and CanRedo properties indicate whether it is possible to undo and redo the actions in Edit Control, respectively.

##### Event Handler

The event handler receives an argument of type `EventArgs`.

```csharp
[C#]
private void editControl_CanUndoRedoChanged(object sender, EventArgs e)
{
    Console.WriteLine(" CanUndoRedoChanged event is raised ");
}
```

## API Reference

The section above discusses the CanUndoRedoChanged event for the Edit control.

### Code Examples

The code example provided demonstrates how to handle the CanUndoRedoChanged event in C#.

```csharp
// Event handler for CanUndoRedoChanged event
private void editControl_CanUndoRedoChanged(object sender, EventArgs e)
{
    Console.WriteLine(" CanUndoRedoChanged event is raised ");
}
```

### See also

- Additional documentation on Windows Forms controls
- Events related to the Edit control

## RAG Annotations

<!-- tags: [Syncfusion Winforms, Edit Control, CanUndoRedoChanged Event] keywords: [Edit control, CanUndoRedo, CanUndoRedoChanged event, localization, Windows Forms] -->
```