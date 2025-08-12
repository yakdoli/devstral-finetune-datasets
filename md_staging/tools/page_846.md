```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_846.jpeg
document_name: tools
page_number: 846
page_id: tools#page_846
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:38:26Z
fidelity: lossless
-->

# Essentials Tools for Windows Forms

## Overview

- The document discusses the alignment of control groups in Windows Forms.
- It explains the use of the `MaskEditDataGroupInfo.Value` property to retrieve the value of specific groups without parsing.
- Demonstrates how to define and use `DataGroups` in a `MaskedEditBox`.

## Content

### Group Alignment

The group alignments will only be enforced after the control has lost focus.

### MaskedEditDataGroupInfo.Value Property

The `MaskedEditDataGroupInfo.Value` property can be used to get the value of a group without any parsing. For example, if the mask is given as follows:

```
(###) - ### #### Extn #####
```

#### Group Definitions

3 groups can be defined as follows:

- Group1 - (###)
- Group2 - ### ####
- Group3 Extn - #####

The value of Group 1 will be the area code, Group 2 will be the phone number, and Group 3 will be the extension.

### Code Snippet Using Groups

The following code snippet uses two groups.

#### C#

```csharp
// Adding DataGroups.
this.maskedEditBox1.DataGroups.Add(this.maskedEditDataGroupInfo1);
this.maskedEditBox1.DataGroups.Add(this.maskedEditDataGroupInfo2);

// Defining maskedEditDataGroupInfo1.
this.maskedEditDataGroupInfo1.DataGroupAlignment =
    Syncfusion.Windows.Forms.Tools.MaskGroupAlignment.Left;
this.maskedEditDataGroupInfo1.DataGroupName = "One";
this.maskedEditDataGroupInfo1.DataGroupSize = 3;

// Defining maskedEditDataGroupInfo2.
this.maskedEditDataGroupInfo2.DataGroupAlignment =
    Syncfusion.Windows.Forms.Tools.MaskGroupAlignment.None;
this.maskedEditDataGroupInfo2.DataGroupName = "Two";
this.maskedEditDataGroupInfo2.DataGroupSize = 4;
```

#### VB.NET

```vb
' Adding DataGroups.
Me.maskedEditBox1.DataGroups.Add(Me.maskedEditDataGroupInfo1)
```

## API Reference

### Namespace

- `Syncfusion.Windows.Forms.Tools`

### Class Members

- **DataGroups** (`System.Collections.ArrayList`): Represents the collection of `DataGroupInfo` objects.
- **DataGroupName** (`System.String`): Gets or sets the name of the data group.
- **DataGroupSize** (`System.Int32`): Gets or sets the size of the data group.
- **DataGroupAlignment** (`MaskGroupAlignment`): Gets or sets the alignment of the group.

#### MaskGroupAlignment Enum

- **Left**: Aligns the group to the left.
- **None**: No specific alignment is applied.

## Code Examples

### Example: Defining DataGroups in a MaskedEditBox

```csharp
// Creating MaskEditDataGroupInfo objects.
MaskEditDataGroupInfo group1 = new MaskEditDataGroupInfo();
group1.DataGroupName = "AreaCode";
group1.DataGroupSize = 3;
group1.DataGroupAlignment = MaskGroupAlignment.Left;

MaskEditDataGroupInfo group2 = new MaskEditDataGroupInfo();
group2.DataGroupName = "PhoneNumber";
group2.DataGroupSize = 7;
group2.DataGroupAlignment = MaskGroupAlignment.Right;

// Adding groups to MaskedEditBox.
maskedEditBox1.DataGroups.Add(group1);
maskedEditBox1.DataGroups.Add(group2);
```

### Example: Retrieving Group Values Without Parsing

```csharp
string groupValue = maskedEditBox1.MaskEditDataGroupInfo.Value;
```

## Cross References

See also:
- [Syncfusion Windows Forms Documentation](https://help.syncfusion.com/windowsforms/)
- [MaskedEditBox Control](https://help.syncfusion.com/windowsforms/maskeditbox)

<!-- tags: [syncfusion, winforms, maskededitbox, maskeditdatagroupinfo, datagroups] keywords: [group alignment, mask edit, data groups, alignment, control focus, value retrieval, area code, phone number, extension, csharp, vb.net] -->
```