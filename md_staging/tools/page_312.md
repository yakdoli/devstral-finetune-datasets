```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_312.jpeg
document_name: tools
page_number: 312
page_id: tools#page_312
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:04:52Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

This event will be raised when a new item is about to be added. New items can be added by calling `AutoComplete.AddHistoryItem()` method. The event handler receives an argument of type `AutoCompleteAddItemCancelEventArgs` containing data related to this event. The following are the properties associated with `AutoCompleteAddItemCancelEventArgs` argument.

## Properties of AutoCompleteAddItemCancelEventArgs

| **Members**         | **Description**                                                                 |
|---------------------|---------------------------------------------------------------------------------|
| **Cancel**          | Gets/Sets a value indicating whether the event should be canceled.             |
| **ImageColumnIndex** | Gets/Sets the ColumnIndex into the AutoComplete.ImageList property.           |
| **RowItem**         | It is the System.Data.DataRow object that contains the value that is to be added to the history list. |

## Handling the AutoCompleteAddItem Event

### C#

```csharp
private void autoComplete1_BeforeAddItem(object sender, AutoCompleteAddItemCancelEventArgs e)
{
    // Cancels the item that is going to be added.
    e.Cancel = true;
}
```

### VB.NET

```vb
Private Sub autoComplete1_BeforeAddItem(ByVal sender As Object, ByVal e As AutoCompleteAddItemCancelEventArgs)
    ' Cancels the item that is going to be added.
    e.Cancel = True
End Sub
```

### 3.5.1.1.4.3 AutoCompleteItemBrowsed Event

This event will be raised when the user selects an item from the list of possible matches when the AutoComplete is set to AutoSuggest. The event handler receives an argument of type `AutoCompleteItemEventArgs`. The event properties associated with the `AutoCompleteItemEventArgs` are as follows.

## Properties of AutoCompleteItemEventArgs

| **Members**       | **Description**                           |
|-------------------|-------------------------------------------|
| **SelectedValue** | Gets/Sets the value selected.             |

<!-- tags: [syncfusion-winforms, event-handling, autocomplete, add-item, browsed-event] keywords: [auto-complete, add-item-event, browsed-event, event-arguments, selected-value] -->
```