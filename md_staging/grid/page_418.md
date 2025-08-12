```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_418.jpeg
document_name: grid
page_number: 418
page_id: grid#page_418
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:15:18Z
fidelity: lossless
-->

## Content

This event is used to return row heights that are in demand.

### Sample Code for Row Height

**[C#]**

```csharp
void GridQueryRowHeight(object sender, GridRowColSizeEventArgs e)
{
    if (e.Index % 2 == 0)
    {
        // Determine Row Height.
        e.Size = 20;
        e.Handled = true;
    }
}
```

**[VB.NET]**

```vb
Private Sub GridQueryRowHeight(ByVal sender As Object, ByVal e As GridRowColSizeEventArgs)
    If ((e.Index Mod 2) = 0) Then
        ' Determine Row Height.
        e.Size = 20
        e.Handled = True
    End If
End Sub
```

### QueryColWidth

**4.1.4.11.2.3 QueryColWidth**

This event is used to return column widths that are in demand. Here is a sample handler.

**[C#]**

```csharp
void GridQueryColWidth(object sender, GridRowColSizeEventArgs e)
{
    if (e.Index % 3 == 0)
    {
        // Assign Column Width.
        e.Size = 40;
        e.Handled = true;
    }
}
```

## API Reference

This section describes the API used for handling row and column size queries.

### GridRowColSizeEventArgs

This class contains the event arguments for querying row and column sizes.

#### Properties
- **Index**: The index of the row or column being queried.
- **Size**: The size value that can be set.
- **Handled**: A flag indicating whether the event has been handled.

### Event Handling

#### GridQueryRowHeight
- **Parameters**:
  - `sender`: The source of the event.
  - `e`: The event arguments of type `GridRowColSizeEventArgs`.

#### GridQueryColWidth
- **Parameters**:
  - `sender`: The source of the event.
  - `e`: The event arguments of type `GridRowColSizeEventArgs`.

## Code Examples

### Example 1: Handling Row Height Query

This example demonstrates how to handle the `GridQueryRowHeight` event to set specific row heights.

```csharp
void GridQueryRowHeight(object sender, GridRowColSizeEventArgs e)
{
    if (e.Index % 2 == 0)
    {
        e.Size = 20;
        e.Handled = true;
    }
}
```

### Example 2: Handling Column Width Query

This example shows how to handle the `GridQueryColWidth` event to set specific column widths.

```csharp
void GridQueryColWidth(object sender, GridRowColSizeEventArgs e)
{
    if (e.Index % 3 == 0)
    {
        e.Size = 40;
        e.Handled = true;
    }
}
```

## See also
- `GridRowColSizeEventArgs`
- `GridQueryRowHeight`
- `GridQueryColWidth`

<!-- tags: [syncfusion-winforms, grid, row-height, column-width, event-handling] keywords: [GridQueryRowHeight, GridQueryColWidth, GridRowColSizeEventArgs, row-heights, column-widths, demand, handler] -->
```