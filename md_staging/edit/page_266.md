```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_266.jpeg
document_name: edit
page_number: 266
page_id: edit#page_266
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:58Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```vb
e.UserHandling = True
End Sub
```

## 4.14.20.2 SaveStreamWithDataLoss Event

This event is raised when the user tries to save streams with data loss.

The event handler receives an argument of type `SaveWithDataLosingEventArgs`. The following `SaveWithDataLosingEventArgs` members provide information specific to this event.

| Member           | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| SaveWithLoss     | Gets / sets value that indicates whether data has to be saved with loss. |
| UserHandling     | Gets / sets value that indicates whether the user handled the event.    |

### Example Code

#### [C#]

```csharp
private void editControl1_SaveStreamWithDataLoss(object sender, Syncfusion.Windows.Forms.Edit.SaveWithDataLosingEventArgs e)
{
    e.SaveWithLoss = true;
    e.UserHandling = true;
}
```

#### [VB.NET]

```vb
Private Sub editControl1_SaveStreamWithDataLoss(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.SaveWithDataLosingEventArgs)
    e.SaveWithLoss = True
    e.UserHandling = True
End Sub
```

## 4.14.21 Scroll Events

This section discusses the below given events that are generated when horizontal and vertical scrolling takes place.

---
```

<!-- tags: [Syncfusion Winforms, SaveStreamWithDataLoss, Scroll Events] keywords: [SaveWithDataLoss, UserHandling, event handler, data loss, horizontal, vertical, scrolling] -->
```