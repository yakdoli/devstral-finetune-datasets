```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_185.jpeg
document_name: diagram
page_number: 185
page_id: diagram#page_185
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:20:21Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Introduces the `GroupNodePosition` property for positioning child nodes within a group.
- Explains the two positioning options: `Absolute` and `Relative`.
- Provides code examples in C# and VB for setting the `GroupNodePosition` property to `Absolute`.

## Content

### GroupNodePosition Property

Group Node has an enum property called `GroupNodePosition` of type `GroupNodePositions` to position its child nodes. GroupNodePositions has two values: `Absolute` and `Relative`.

- **Absolute**: Places the nodes inside a group based on their actual pinpoint.
- **Relative**: Places the nodes based on their default pinpoint.
- **Default value**: `Relative`.

#### Code Examples

**C#**
```csharp
//Group
Group group = new Group();
//Absolute positioning
group.GroupNodePosition = GroupNodePositions.Absolute;
```

**VB**
```vb
'Group
Dim group As Group = New Group()
'Absolute positioning
group.GroupNodePosition = GroupNodePositions.Absolute
```

### Positioning Diagrams

#### Figure 114: Group Node Absolute positioning
![Figure 114: Group Node Absolute positioning](https://i.imgur.com/example_image_114.png)

#### Figure 115: Group Node Relative positioning
![Figure 115: Group Node Relative positioning](https://i.imgur.com/example_image_115.png)

## Properties

## API Reference (if applicable)
- **Namespace**: Syncfusion.Windows.Forms.Diagram
- **Class**: Group
- **Enum**: GroupNodePositions
- **Property**: `GroupNodePosition`
- **Parameters**:
  - **Name**: GroupNodePosition
  - **Type**: GroupNodePositions
  - **Description**: Determines how child nodes are positioned within the group.
  - **Default**: Relative
  - **Required**: No

### Returns
- **Type**: GroupNodePositions
- **Description**: The current positioning method of the child nodes.

### Exceptions
- No exceptions are thrown for setting the `GroupNodePosition` property.

## Code Examples
- Refer to the C# and VB examples provided above.

## Cross References
- See also: [unclear]

<!-- tags: [groupnodeposition, absolutepositioning, relativelpositioning, diagrampositioning, windowsforms, groupnode, syncfusionwinforms, enum, positioning, softnodeposition] keywords: [GroupNodePosition, GroupNodePositions, Absolute, Relative, diagram, positioning, windows forms, Syncfusion WinForms] -->
```