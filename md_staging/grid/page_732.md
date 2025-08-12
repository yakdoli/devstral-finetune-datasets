```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_732.jpeg
document_name: grid
page_number: 732
page_id: grid#page_732
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:36:57Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

```csharp
s(3).ParentGroup.Info
```

### 4.3.4.3.1.2.3 Events

This section discusses some of the important events that could be handled to catch the grouping actions. Below is a list of such events.

| Event                         | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| GroupedColumns_Changing       | Occurs before a property in the collection is changed.                      |
| GroupedColumns_Changed       | Occurs after a property in the collection was changed.                       |
| GroupExpanding                | Occurs before a group is expanded.                                         |
| GroupExpanded                 | Occurs after a group was expanded.                                         |
| GroupCollapsing               | Occurs before a group is collapsed.                                        |
| GroupCollapsed                | Occurs after a group was collapsed.                                        |
| SortingItemsInGroup           | Occurs before the records for a group are sorted.                          |
| SortedItemsInGroup            | Occurs after the records for a group were sorted.                          |

#### Example

The GroupedColumns Changing/Changed events get fired when the list is modified, i.e., when any item is added, removed or modified. It accepts an argument of type `ListPropertyChangedEventArgs` that lets you check the reason for a list change. The reason could be of `ItemAdded`, `ItemInserted`, `ItemRemoved`, `ItemModified`, `ItemMoved`, `ItemPropertyChanged`, or the whole collection is modified.

The following code examples show you how to capture the events.

```csharp
// Subscribe to the events.
```

## API Reference

This page does not contain any specific API reference details beyond the listed events.

## Code Examples

This page includes simple event subscription examples in C#, as shown in the provided code snippet.

## Cross References

See also: [Grouping Actions in Essential Grid](#grouping-actions-in-essential-grid)

<!-- tags: [syncfusion, winforms, grid, grouping, events] keywords: [GroupedColumns_Changing, GroupedColumns_Changed, GroupExpanding, GroupExpanded, GroupCollapsing, GroupCollapsed, SortingItemsInGroup, SortedItemsInGroup] -->
```