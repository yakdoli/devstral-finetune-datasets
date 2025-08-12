```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_066.jpeg
document_name: edit
page_number: 066
page_id: edit#page_066
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:57:54Z
fidelity: lossless
-->

# Content Dividers in Windows Forms

## Overview

- Enables content dividers to separate sections into distinct blocks within the Edit Control.
- The Content Dividers feature can be customized in the configuration file to define how sections are handled.

## Content

### Implementing Content Dividers

The feature can be enabled for sections of the Edit Control contents by setting the `ContentDivider` field to `True` within its lexem definition in the configuration file.

#### Example Configuration

```xml
<!-- Enable content dividers within its lexem definition in the configuration file. -->
<lexem BeginBlock="Function" EndBlock="End Function" Type="KeyWord"
       IsComplex="true" IsCollapsable="true" Indent="true"
       CollapseName="{Function...End Function}"
       AutoNameExpression='.+Function.*${\s+([?&lt;text&gt;\w+)]}'
       AutoNameTemplate="Function [${text}]"
       IsCollapseAutoNamed="true" ContentDivider="true">
  <References>
    <reference RefID="777"/>
  </References>
  <SubLexems>
    <lexem BeginBlock="\n" IsBeginRegex="true" />
  </SubLexems>
</lexem>
```

### Visual Representation

The following figure shows how Content Dividers separate event contents into sections within the Edit Control.

![Content Dividers separating the Event Contents into Sections](https://example.com/image.png)

Figure 17: Content Dividers separating the Event Contents into Sections

This feature is particularly useful for organizing and managing large blocks of code or content within the Edit Control, providing better navigation and readability.

---

## API Reference

### Configuration Settings

- **ContentDivider**: A boolean property that when set to `True`, enables the separation of sections within the Edit Control, improving content organization and navigation.

## Code Examples

The following demonstrates how to configure Content Dividers in the Edit Control:

```vb
Private Sub menuItem2_Click(sender As Object, e As EventArgs) Handles menuItem2.Click
    Me.editControl.NewFile()
End Sub

Private Sub menuItem3_Click(sender As Object, e As EventArgs) Handles menuItem3.Click
    Me.editControl.LoadFile()
End Sub

Private Sub menuItem5_Click(sender As Object, e As EventArgs) Handles menuItem5.Click
    Me.editControl.Save()
End Sub
```

### Configuration File Example

The configuration file includes lexem definitions to enable fine-tuned control over how different blocks of code or content are managed:

```xml
<lexem BeginBlock="Function" EndBlock="End Function" Type="KeyWord"
       IsComplex="true" IsCollapsable="true" Indent="true"
       CollapseName="{Function...End Function}"
       AutoNameExpression='.+Function.*${\s+([?&lt;text&gt;\w+)]}'
       AutoNameTemplate="Function [${text}]"
       IsCollapseAutoNamed="true" ContentDivider="true">
  ...
</lexem>
```

## Page-level Navigation/TOC (if applicable)

This section explains how to configure and utilize Content Dividers in the Edit Control to separate content into sections, providing improved organization and navigation.

## Cross References

- **Related Topic**: For more information on enhancing navigation and organization in the Edit Control, refer to the documentation on [Edit Control Features](#edit-control-features).

<!-- tags: [syncfusion, windows-forms, content-dividers, edit-control, configuration, seamless-organization] keywords: [content divider, edit control, lexem definition, configuration file, section separation, organization] -->
```