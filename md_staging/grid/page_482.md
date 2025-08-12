```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_482.jpeg
document_name: grid
page_number: 482
page_id: grid#page_482
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:19:16Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Code Example

```csharp
return size;
}
}
```

## Using VB.NET

### [VB.NET]

```vb
' Override this method to calculate proper control size and return the same.
Protected Overrides Function OnQueryPrefferedClientSize(ByVal g As Graphics, ByVal rowIndex As Integer, ByVal colIndex As Integer, ByVal style As GridStyleInfo, ByVal queryBounds As GridQueryBounds) As Size
    If Grid(rowIndex, colIndex).Tag Is Nothing Then
        Throw New Exception("No User Control is tagged")
    Else

        ' Get the type of the control from Style.Tag.
        Dim userControl As Control = TryCast(Grid(rowIndex, colIndex).Tag, Control)

        ' Calculate the size of the control.
        Dim size As Size = userControl.Size
        size.Height += 2

        ' Return the size.
        Return size
    End If
End Function
```

The following image shows how the cell resizes itself automatically to the size of the control, when a custom control is added to it.

## API Reference

## Page-level Navigation/TOC

## Cross References

## RAG Annotations
<!-- tags: [Grid, Windows Forms, Syncfusion, VB.NET, cell resizing, control size calculation, custom controls] keywords: [OnQueryPrefferedClientSize, GridStyleInfo, GridQueryBounds, TryCast, Control Tag] -->
```
