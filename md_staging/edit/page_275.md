```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_275.jpeg
document_name: edit
page_number: 275
page_id: edit#page_275
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:17Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Describes events triggered upon finding hidden text in documents.
- Provides details on event handling for hidden text challenges and tooltip updates.

## Content

### Event: UnreachableTextFound

This event occurs when text in a hidden block is found and this block cannot be expanded due to the user's cancellation.

The event handler receives an argument of type **UnreachableTextFoundEventArgs**. The following **UnreachableTextFoundEventArgs** members provide information specific to this event.

| Member          | Description                                 |
|-----------------|---------------------------------------------|
| ContinueSearch  | Indicates whether the search must be continued. |
| Point           | Point of the location of unreachable text. |
| Text            | Searched text.                            |

#### Code Example

**C#**

```csharp
private void editControl1_UnreachableTextFound(object sender,
    Syncfusion.Windows.Forms.Edit.UnreachableTextFoundEventArgs e)
{
    Console.WriteLine(" UnreachableTextFound event is raised ");
}
```

**VB.NET**

```vb
Private Sub editControl1_UnreachableTextFound(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.UnreachableTextFoundEventArgs)
    Console.WriteLine(" UnreachableTextFound event is raised ")
End Sub
```

### Event: UpdateBookmarkTooltip

This event is fired when the bookmark tooltip text is updated.

The event handler receives an argument of type **UpdateBookmarkTooltipEventArgs**. The following **UpdateBookmarkTooltipEventArgs** members provide information specific to this event.

| Member       | Description                                  |
|--------------|----------------------------------------------|
| Bookmark     | Bookmark.                                   |
| HintedArea   | Rectangle that represents an object which has this tooltip. |

## Page-level Navigation/TOC (if applicable)
### 4.14.26 UpdateBookmarkTooltip Event

This event is fired when the bookmark tooltip text is updated.

The event handler receives an argument of type **UpdateBookmarkTooltipEventArgs**. The following **UpdateBookmarkTooltipEventArgs** members provide information specific to this event.

| Member       | Description                                  |
|--------------|----------------------------------------------|
| Bookmark     | Bookmark.                                   |
| HintedArea   | Rectangle that represents an object which has this tooltip. |

<!-- tags: [Syncfusion Winforms, UnreachableTextFoundEventArgs, UpdateBookmarkTooltipEventArgs, Event Handling, Windows Forms Editing] keywords: [unreachable text, hidden block, event, tooltip update, bookmark, editor, flags, event arguments] -->
```