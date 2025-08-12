```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_907.jpeg
document_name: grid
page_number: 907
page_id: grid#page_907
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:49:01Z
fidelity: lossless
-->

### Essential Grid for Windows Forms

#### Overview
- Details the events related to the FieldChooser DialogBox.
- Provides a comprehensive explanation of the FieldChooser events: FieldChooserShowing, FieldChooserShown, FieldChooserClosing, and FieldChooserClosed.
- Includes an example code handling the FieldChooserShowing event.

#### Content

| Event               | Description                                                        | Arguments                                                         | Type   |
|---------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|--------|
| FieldChooserShowing | This event is handled before the FieldChooser DialogBox is shown either in the stacked header or column header. This event is generally used to change the caption of the DialogBox, get and set the control of the TreeViewAdv or Grid controls, and also used to cancel showing the FieldChooser dialog. | public FieldChooserShowingEventArgs(string caption, object fieldList); | Event  |
| FieldChooserShown   | This event is handled after the FieldChooser dialog is shown. This event is generally used to get the caption name of the FieldChooser dialog box and get the control of the TreeViewAdv or Grid controls. | public FieldChooserShownEventArgs(string caption, object fieldList); | Event  |
| FieldChooserClosing | This event is generally used to change the caption name of the dialog, get and set the control of the TreeViewAdv or Grid controls, and also used to cancel closing the FieldChooser dialog. | public FieldChooserClosingEventArgs(string caption, object fieldList); | Event  |
| FieldChooserClosed  | This event is handled after the FieldChooser Dialog Box is closed. This event is generally used to get the caption name of the FieldChooser dialog, and get the control of the TreeViewAdv or Grid controls after closing the FieldChooser dialog. | public FieldChooserClosedEventArgs(string caption, object fieldList); | Event  |

#### Code Examples

The following code sample illustrates handling the FieldChooserShowing event. It is used to change the caption of the FieldChooser dialog and cancel the FieldChooser dialog showing.

```csharp
// FieldChooserShowing Event
void gridGroupingControl_FieldChooserShowing(object sender, FieldChooserShowingEventArgs e)
{
    e.Caption = "Syncfusion";
    e.Cancel = true;
}
```

#### API Reference

- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Event**: FieldChooserShowing, FieldChooserShown, FieldChooserClosing, FieldChooserClosed
- **Parameters**:
  - `caption`: string
  - `fieldList`: object
- **Returns**: None
- **Exceptions**: None mentioned in the context.

#### RAG Annotations

<!-- tags: [Essential Grid, Windows Forms, FieldChooser, Events, Syncfusion, Version 11.4.0.26] keywords: [FieldChooser, Grid control, TreeViewAdv, DialogBox, Showing event, Shown event, Closing event, Closed event, Caption, FieldList] -->
```