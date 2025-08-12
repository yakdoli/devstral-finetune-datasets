```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_998.jpeg
document_name: grid
page_number: 998
page_id: grid#page_998
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:57:34Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Group and categorize data dynamically using a custom categorizer and comparer for advanced grouping options.
- Handle the QueryCellStyleInfo event to customize the display of group captions for enhanced user交互和理解.

## Content

### Grouping with Custom Categorizer and Comparer

In this section, we demonstrate how to group data in a specific column ("Col2") using a custom categorizer and comparer. The code below shows how to configure this setup in Visual Basic.NET (VB.NET).

```vb
' Group "Col2" by using a Custom Categorizer and Comparer.
Dim cd As New Syncfusion.Grouping.SortColumnDescriptor("Col2")
cd.Categorizer = New CustomCategorizer()
cd.Comparer = New CustomComparer()
Me.gridGroupingControl1.TableDescriptor.GroupedColumns.Add(cd)
```

### Customizing Group Captions

To display customized group captions, the QueryCellStyleInfo event can be handled. This event allows you to modify the appearance or content of table cells, including group headers. Below is an example implementation in C#:

```csharp
// Subscribe to QueryCellStyleInfo event to display custom group caption.
this.gridGroupingControl1.QueryCellStyleInfo += new GridTableCellStyleInfoEventHandler(gridGroupingControl1_QueryCellStyleInfo);

private void gridGroupingControl1_QueryCellStyleInfo(object sender, GridTableCellStyleInfoEventArgs e)
{
    if (e.TableCellIdentity.GroupedColumn != null &&
        e.TableCellIdentity.DisplayElement.ParentGroup != null &&
        e.TableCellIdentity.DisplayElement.ParentGroup.Category is int)
    {
        if (e.TableCellIdentity.DisplayElement is CaptionRow &&
            e.TableCellIdentity.GroupedColumn.Name == "Col2")
        {
            int cat = (int)e.TableCellIdentity.DisplayElement.ParentGroup.Category;
            string ret = "";
            switch (cat)
            {
                case 1:
                    ret = "< 10";
                    break;
                case 2:
                    ret = "10 - 19";
                    break;
                case 3:
                    ret = "20 - 29";
                    break;
                case 4:
                    ret = "30 - 39";
                    break;
                case 5:
            }
        }
    }
}
```

### Explanation

- **Custom Categorizer and Comparer**: In the first part, we create a `SortColumnDescriptor` for the column "Col2" and assign custom categorizer and comparer objects to it. This allows for custom grouping logic based on your specific requirements.
- **Handling QueryCellStyleInfo Event**: In the second part, we handle the `QueryCellStyleInfo` event to customize the display of group captions. By checking specific conditions, we determine when a group caption should be formatted differently based on the group's category.

### Custom Group Caption Logic

- The `switch` statement in the `QueryCellStyleInfo` handler is used to map integer categories to different range labels.
- This allows for clear and meaningful group captions that reflect the underlying data in a human-readable format.

### See also
- [Syncfusion Grid Documentation](https://help.syncfusion.com/windowsforms/grid)
- [Custom Grouping and Sorting](https://help.syncfusion.com/windowsforms/grid/grouping-and-sorting)
- [Handling Cell Style Information](https://help.syncfusion.com/windowsforms/grid/cell-style-information)

## RAG Annotations

<!-- tags: [Syncfusion, WinForms, Grid, Grouping, Customization, QueryCellStyleInfo, Categorizer, Comparer] keywords: [group captions, custom grouping, data categorization, column sorting, UI customization, event handling] -->
```