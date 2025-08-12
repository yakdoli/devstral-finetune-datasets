```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_445.jpeg
document_name: chart
page_number: 445
page_id: chart#page_445
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:42:18Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```vb
legendItem1.Text = "Legend Item"

'Adding the custom Legend item to the chart
Me.chartControl1.Legends[1].CustomItems = New ChartLegendItem()
{legendItem1}
```

![Figure 283: Custom Legend Item](https://i.imgur.com/7IUjM2B.png)

## Customizing items through event

There is also a way to specify custom legend item via events right before they get rendered.

In this example, we reverse the order in which the legend items are rendered through the **FilterItems** event.

### [C#]

```csharp
private void Legend_FilterItems(object sender, ChartLegendFilterItemsEventArgs e)
{
    // This creates an new instance of the ChartLegendItemCollection
    ChartLegendItemsCollection items = new ChartLegendItemsCollection();
    for (int i = e.Items.Count - 1; i >= 0; i--)
        items.Add(e.Items[i]);
    e.Items = items;
}
```

### [VB.NET]

```vb
Private Sub Legend_FilterItems(ByVal sender As Object, ByVal e As ChartLegendFilterItemsEventArgs)
    ' This creates an new instance of the ChartLegendItemCollection
    Dim item As New ChartLegendItemsCollection()
    For i As Integer = e.Items.Count - 1 To 0 Step -1
        item.Add(e.Items(i))
    Next
    e.Items = item
End Sub
```
```