```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_035.jpeg
document_name: grouping
page_number: 035
page_id: grouping#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:50Z
fidelity: lossless
-->

# Essential Grouping

## Overview
- Demonstrates viewing records associated with a specific category after grouping.
- Utilizes the `ShowRecordsUnderGroup` method to display records under a selected group.

## Content

### Accessing Records Under Specific Groups

Once you have the `ShowRecordsUnderGroup` method, you only need to retrieve a specific group from the `Groups` collection and call the method. After grouping on property `C`, you can view all records whose `Category` is "c1" using the following code, similar to what is shown below the `Main` method.

#### C#

```csharp
// Get the Group associated with the value "c1".
Group g = groupingEngine.Table.TopLevelGroup.Groups["c1"];
ShowRecordsUnderGroup(g);

// Pause
Console.ReadLine();
```

#### VB.NET

```vb
' Get the Group associated with the value "c1".
Dim g As Group = groupingEngine.Table.TopLevelGroup.Groups("c1")
ShowRecordsUnderGroup(g)

' Pause
Console.ReadLine()
```

## API Reference

### Methods

- **ShowRecordsUnderGroup(g)**
  - **Purpose**: Displays records under the specified group `g`.
  - **Parameters**:
    - `g`: The group object to access records from.

### Properties

- **Groups**: Collection of groups within the `TopLevelGroup` to access specific groups by their category value.

## Page-level Navigation/TOC (if applicable)

- **Accessing Records Under Specific Groups**

## Cross References

See also:
- Chapter on Grouping Techniques in the Syncfusion Winforms User Guide.

<!-- tags: [Syncfusion, Winforms, Grouping, Records, ShowRecordsUnderGroup] keywords: [grouping, records, c1, groups, ShowRecordsUnderGroup, TopLevelGroup, categories] -->
```