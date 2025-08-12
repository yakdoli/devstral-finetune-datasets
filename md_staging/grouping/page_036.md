```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: grouping
page_number: 036
page_id: grouping#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:59:44Z
fidelity: lossless
-->

# Essential Grouping

## Overview

- Displays records grouped under the "c1" group.
- Demonstrates code for showing all records under the primary group.
- Explains how to implement the `ShowRecordsUnderGroup` method in the `Main` method.

## Content

### Displaying Grouped Records

The following figure shows the records from the "c1" group:

Figure: Last Section Shows the Records from the "c1" Group

#### Code Implementation

Similar code can be used to display all the records by passing the 'primary' group to your `ShowRecordsUnderGroup` method. To implement this, add the following code to the `Main` method.

```csharp
// Show all records under the TopLevelGroup.
ShowRecordsUnderGroup(groupingEngine.Table.TopLevelGroup);

// Pause
Console.ReadLine();
```

### Notes

- Ensure that the `groupingEngine` object is properly initialized and available in the `Main` method.
- The `ShowRecordsUnderGroup` method should be defined to handle the display logic for the grouped records.

---

This section details the display of records grouped under specific categories, focusing on the "c1" group, and provides a code example for showing all records under the main group.

## API Reference

- **Namespace**: (Not explicitly shown in the image; would require additional context or documentation)
- **Class**: `GroupingEngine`
- **Method**: `ShowRecordsUnderGroup`

### Parameters

| Name               | Type              | Description                                                                 |
|--------------------|-------------------|-----------------------------------------------------------------------------|
| `topLevelGroup`    | `GroupInfo`       | The primary group under which all records should be displayed. |

## Code Examples

Example: Showing all records under the top-level group.

```csharp
// Example code to display all records under the top-level group.
ShowRecordsUnderGroup(groupingEngine.Table.TopLevelGroup);
Console.ReadLine();
```

## Page-level Navigation/TOC (if applicable)

- [ ] Essential Grouping
  - [ ] Displaying Grouped Records
  - [ ] Code Implementation
  - [ ] Notes
  - [ ] API Reference
  - [ ] Code Examples

<!-- tags: [Syncfusion Winforms, Grouping, Records, GroupInfo, GroupingEngine, ShowRecordsUnderGroup, TopLevelGroup] keywords: [grouping, records, top level group, group, groupinfo, groupingengine, showrecordsundergroup, main method, pause, console.readline, display logic, implementation] -->
```