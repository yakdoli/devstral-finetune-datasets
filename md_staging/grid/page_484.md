```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_484.jpeg
document_name: grid
page_number: 484
page_id: grid#page_484
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:19:33Z
fidelity: lossless
-->

## Use Case Scenarios

You can use this property to change the navigation direction of Enter key behavior in the grid. The EnterKeyBehavior property works based on **WrapCellBehavior**. Enter key behavior navigates to the first column in the next row when at the end of a row and moving to the right.

## Properties

| Property           | Description                                                                                                                                                        | Type                      | Data Type |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|-----------|
| EnterKeyBehavior   | Navigate to other cells when Enter is pressed.                                                                                                                    | GridDirectionType         | Enum      |
| WrapCellBehavior   | Go to first column in next row or last column in previous row when at end or beginning of a row and moving based on Enter key behavior.                         | GridWrapCellBehavior      | Enum      |

## Example

The following code illustrates how to set the **EnterKeyBehavior** property for Syncfusion Windows Forms Grid controls.

### For the Grid Control

#### [C#]
```csharp
this.gridControl1.EnterKeyBehavior = GridDirectionType.Top;

this.gridControl1.Model.Options.WrapCellBehavior = GridWrapCellBehavior.WrapGrid;
```

#### [VB.NET]
```vb
Me.gridControl1.EnterKeyBehavior = GridDirectionType.Top

Me.gridControl1.Model.Options.WrapCellBehavior=GridWrapCellBehavior.WrapGrid;
```
```


<!-- tags: [Essential Grid for Windows Forms, EnterKeyBehavior, WrapCellBehavior, GridDirectionType, GridWrapCellBehavior] keywords: [navigation, behavior, enter key, row, column, next, previous, grid, Syncfusion, Windows Forms, C#, VB.NET] -->
```