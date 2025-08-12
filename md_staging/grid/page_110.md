```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_110.jpeg
document_name: grid
page_number: 110
page_id: grid#page_110
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:29:18Z
fidelity: lossless
-->

##  Essential Grid for Windows Forms

![Editable Virtual Grid](attachment://image_2.png)

## Setting Properties in a Virtual Grid

So far you have seen that you can provide any GridStyleInfo property in a virtual manner by merely handling the Grid control's QueryCellInfo event. You can also provide the row count and column count in a virtual manner as well.

Here is a list of the other events that will allow virtual access to an Essential Grid.

- QueryRowHeight - This event allows you to dynamically provide row heights.
- QueryColWidth - This event allows you to dynamically provide column widths.
- QueryCoveredRange - This event allows you to dynamically provide covered cell ranges.

```csharp
[C#]

// Provide the row heights on demand - optional...
void GridQueryRowHeight(object sender, GridRowColSizeEventArgs e)
{
    if (e.Index % 2 == 0)
    {
        e.Size = 20;
        e.Handled = true;
    }
}
```
```html
```