```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_719.jpeg
document_name: tools
page_number: 719
page_id: tools#page_719
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:31:19Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- This section discusses the DomainUpDownExt control and its features, including how to create it programmatically and configure its text settings.

## Content

### 3.5.8.2.3 Concepts and Features

#### 3.5.8.2.3.1 Text Settings

The text for the DomainUpDownExt control can be specified in the String Collection Editor. This section deals with the properties related to this text.

#### DomainUpDownExt Property Descriptions

| DomainUpDownExt Property | Description |
|--------------------------|-------------|
| Items                    | Invokes the String Collection Editor. Text for the control can be specified in this editor. |
| TextAlign                | Specifies the alignment of the text in the text field. |
| MaxLength                | Indicates the maximum length of the text that can be entered into the editable portion of the control. Default value is 32767. |

#### Code Examples

##### C#

```csharp
this.domainUpDownExt2.Items.Add("Six");
this.domainUpDownExt1.TextAlign =
    System.Windows.Forms.HorizontalAlignment.Right;
this.domainUpDownExt2.MaxLength = 32768;
```

##### VB.NET

```vb
Me.domainUpDownExt2.Items.Add("Six")
Me.domainUpDownExt1.TextAlign =
    System.Windows.Forms.HorizontalAlignment.Right
Me.domainUpDownExt2.MaxLength = 32768
```

#### Figure

**Figure 447: DomainUpDownExt Created Programmatically**

### Page-level Navigation/TOC

- **3.5.8.2.3 Concepts and Features**
  - **3.5.8.2.3.1 Text Settings**

### Cross References

- **See also:**
  - [DomainUpDownExt control documentation](#)
  - [String Collection Editor usage](#)

<!-- tags: [Syncfusion Winforms, DomainUpDownExt, Text Settings, String Collection Editor, Control Properties] keywords: [DomainUpDownExt, text settings, String Collection Editor, TextAlign, MaxLength, C#, VB.NET, 3.5.8.2.3, 3.5.8.2.3.1, Programmatic Control Creation, HorizontalAlignment, Items Property] -->
```