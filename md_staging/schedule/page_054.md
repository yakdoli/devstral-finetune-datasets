```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_054.jpeg
document_name: schedule
page_number: 054
page_id: schedule#page_054
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:11:28Z
fidelity: lossless
-->

# Essential Schedule for Windows Forms

## Overview
- Defines items that can be included in an `ILookUpObjectList`.
- Choice lists within the `ScheduleControl` are used to provide possible schedule item information like location or a reminder.
- `ILookUpObject` allows such list items to have a `ValueMember` and `DisplayMember` associated with the choices, as well as a color for display in drop-down lists.
- Value members are typically serialized to data stores for persistence.

## Content

### ILookUpObject Interface

```csharp
[C#]

/// <summary>
/// Defines items that can be included in a ILookUpObjectList.
/// Choice lists within the ScheduleControl are used to provide possible
/// schedule item information like location or a reminder.
/// ILookUpObject allows such list items to have a ValueMember / DisplayMember
/// associated with
/// the choices as well as a color that will be used in drop-down
/// lists. Value members are normally the values serialized to data
/// stores.
/// </summary>
public interface ILookUpObject
{
    /// <summary>
    /// The value member associated with this item.
    /// </summary>
    int ValueMember { get; set; }

    /// <summary>
    /// The display member associated with this item.
    /// </summary>
    string DisplayMember { get; set; }

    /// <summary>
    /// A color associated with this item.
    /// </summary>
    Color ColorMember { get; set; }
}
```

### ILookUpObjectList Interface

```csharp
[C#]

/// <summary>
/// Collection of <see cref="ILookUpObject"/> items.
/// </summary>
public interface ILookUpObjectList
{
    /// <summary>
    /// Indexer that returns a ILookUpObject object.
    /// </summary>
    ILookUpObject this[int i] { get; set; }
}
```

## Summary
- The `ILookUpObject` interface provides structure for items that can be part of a droplist in a `ScheduleControl`, enabling the association of value and display members along with a color.
- The `ILookUpObjectList` interface serves as a wrapper for a collection of `ILookUpObject` items, enabling indexed access to these droplist items.

<!-- tags: [schedule, iLookUpObject, iLookUpObjectList] keywords: [scheduleControl, choice list, value member, display member, color, droplist] -->
```