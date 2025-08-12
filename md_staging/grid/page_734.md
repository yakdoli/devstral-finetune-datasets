```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_734.jpeg
document_name: grid
page_number: 734
page_id: grid#page_734
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:39:11Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
If e.Action = ListPropertyChangedType.Remove Then
    Console.WriteLine("Column Removed - {0}" + scd.Name)
End If
End Sub
```

## Understanding Group Operations and Sorting

The `GroupExpanding/GroupExpanded` and `GroupCollapsing/GroupCollapsed` event handlers are ideal for performing actions when group operations such as GroupExpand and GroupCollapse occur.

The `SortingItemsInGroup` and `SortedItemsInGroup` events are triggered when the records for a group are sorted. These events require at least one group to occur and are unrelated to normal sorting. They specifically occur when a grouped column is sorted.

## Tracking Changes in Nested Tables

### Overview
- Listening to the `Engine.PropertyChanging` event
- Using the `GetNestedChildTableDescriptorEvent` method

It is possible to track changes in other table descriptors other than the default table by listening to the `Engine.PropertyChanging` event and using the `GetNestedChildTableDescriptorEvent` method. This method provides information about changes in the table descriptor of the nested child table. For instance, when a column in a nested table is modified, the above method supplies details such as the table descriptor of the affected table and the original `EventArgs` raised in response to the column changes (e.g., `ColumnsChanged` event). With the event data, you can check whether only the column width has changed or if other settings have been modified.

### Example Code for Using the Method

```csharp
protected override void Engine_PropertyChanging(object sender, DescriptorPropertyChangedEventArgs e)
{
    if (e.PropertyName == "TableDescriptor")
    {
        TableDescriptor tableDescriptor = ((Engine)sender).TableDescriptor;
        e = (DescriptorPropertyChangedEventArgs)e.Inner;

        if (e.PropertyName == "Relations")
            e = e.GetNestedChildTableDescriptorEvent(ref tableDescriptor);

        if (e.PropertyName == "Columns")
        {
            ListPropertyChangedEventArgs le = (ListPropertyChangedEventArgs)e.Inner;
        }
    }
}
```

## Summary

- The `GetNestedChildTableDescriptorEvent` method is crucial for monitoring changes in nested table descriptors.
- It provides details about changes in columns and their associated settings within nested tables.

<!-- tags: [Syncfusion Winforms, Essential Grid, Group Operations, Sorting, Nested Tables, PropertyChanging] keywords: [GroupExpand, GroupCollapse, SortingItemsInGroup, SortedItemsInGroup, NestedTables, TableDescriptor, ColumnsChanged, PropertyChanging, GetNestedChildTableDescriptorEvent] -->
```