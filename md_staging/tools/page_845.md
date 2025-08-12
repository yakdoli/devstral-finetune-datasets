```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_845.jpeg
document_name: tools
page_number: 845
page_id: tools#page_845
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:37:35Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates usage of the `DataGroups` property in a `MaskedEditBox` control.
- Explains how text can be split and aligned using data groups.
- Provides a detailed breakdown of the `DataGroups` property and its functionalities.

## Content

### Code Example (VB.NET)

```vb
Me.maskedEditBox1.PositionAt = Syncfusion.Windows.Forms.Tools.SpecialCursorPosition.Decimal
Me.maskedEditBox1.PositionAtDecimal = True
```

### DataGroups

Text can be split up and aligned using the options provided by the below given property.

| MaskedEditBox Property     | Description                                                                                     |
|----------------------------|-------------------------------------------------------------------------------------------------|
| DataGroups                 | Specifies the data groups that can be used for splitting up the text.                          |

The `DataGroups` property of the `MaskedEditBox` defines a virtual grouping of the mask value. Each group is defined by a `MaskedEditDataGroupInfo` object (the `DataGroups` property is a collection of these objects).

A data group is defined by its `GroupLength` property. For example, if the mask is given as follows,

```
######.######.######.#####
```

and there are 4 groups specified with group lengths of 4, 4, 4, 3 respectively, the groups will be defined as:

- Group1 ####.
- Group2 ####.
- Group3 ####.
- Group4 ####

The `DataAlignment` property of the `MaskedEditDataGroupInfo` object specifies the type of alignment to be used for the group. The data alignment behavior will be defined as given below:

- **Left**: All the filled-in mask fields in the group will be grouped to the left-most positions.
- **Right**: All the filled-in mask fields in the group will be grouped to the right-most positions.
- **Center**: All the filled-in mask fields in the group will be grouped to the center-most positions.

## Code Examples

### Expressions Usage Example
```vb
Me.maskedEditBox1.PositionAt = Syncfusion.Windows.Forms.Tools.SpecialCursorPosition.Decimal
Me.maskedEditBox1.PositionAtDecimal = True
```

This example demonstrates setting the cursor position to the decimal point in a `MaskedEditBox`.

---

<!-- tags: [Syncfusion Winforms, MaskedEditBox, DataGroups, DataAlignment, GroupLength, SpecialCursorPosition, Decimal] keywords: [mask groups, alignment, cursor position, text splitting, data grouping, windows forms, masked edit box, properties, group length, data alignment] -->
```