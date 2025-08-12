```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_063.jpeg
document_name: schedule
page_number: 063
page_id: schedule#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:11:38Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview
- Demonstrates the essential components of the Schedule control with a Metro theme applied.
- Explains item dragging context and its detection using the `ItemChanging` event.
- Provides an example scenario using the `ItemDragHitContext` enumeration.

## Content

### Schedule Control with Metro Theme

![Schedule Control Applied with Metro Theme](#)
*Figure 28: Schedule Control Applied with Metro Theme*

#### Item Dragging Context in the ItemChanging Event

This feature provides support to detect the dragging context when an item is dropped in the schedule part or calendar part. It also enables the cancellation of the needed items through the `ItemChanging` event.

##### Use Case Scenario

In the `ItemChanging` event, through the `ItemDragHitContext` enumeration, you can detect the dragging context (Schedule or Calendar) and cancel the needed items.

##### Properties

| Property            | Description                                               | Data Type |
|---------------------|-----------------------------------------------------------|-----------|
| ItemDragHitContext  | Specifies where the mouse is during an appointment drag in a | enum      |

## API Reference

### Events
- **ItemChanging**
  - **Description**: Triggered when an item is about to change, providing the ability to detect the dragging context and cancel changes if necessary.
  - **Event Handler**: `ItemChangingEventHandler`

### Enumerations
- **ItemDragHitContext**
  - **Description**: Indicates the context where the mouse is during a drag operation.
  - **Values**:
    - **Schedule**: Dragging within the schedule view.
    - **Calendar**: Dragging within the calendar view.

## Code Examples

### Example: Handling Item Dragging Context

```csharp
private void Schedule_ItemChanging(object sender, ItemChangingEventArgs e)
{
    if (e.ItemDragHitContext == ItemDragHitContext.Calendar)
    {
        // Cancel the change if item is being dragged to the calendar
        e.Cancel = true;
    }
}
```

## Cross References

See also:
- [Syncfusion WinForms Documentation](https://www.syncfusion.com/products/windowsforms/documentation)
- Key features of the Schedule control: [Syncfusion Essentials](https://help.syncfusion.com/windowsforms/schedule)

<!-- tags: [schedule, itemchangingevent, itemdraghitcontext, metrotheme, windowsforms, syncfusion] keywords: [schedule control, item dragging, context detection, itemchanging event, itemdraghitcontext, metro theme, windows forms, .NET, item cancel, enumeration] -->
```