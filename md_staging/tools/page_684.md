```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_684.jpeg
document_name: tools
page_number: 684
page_id: tools#page_684
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:28:16Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes the properties that control the behavior of the splitter in a SplitContainerAdv control.
- Explains how to configure splitter settings through SplitContainerAdv properties.

## Content

### 3.5.6.4.3.1.2 Splitter Settings

The properties which change the behavior of the Splitter in a SplitContainerAdv control are discussed in this section.

#### Splitter Settings

The below table describes the properties to control the behavior of the splitter.

| SplitContainerAdv Properties          | Description                                                                 |
|---------------------------------------|-----------------------------------------------------------------------------|
| IsSplitterFixed                       | Gets / sets whether the user is allowed to move the splitter or not. Default value is false. |
| SplitterDistance                      | Indicates the distance from the left top border. |
| SplitterIncrement                     | Determines the number of pixels the splitter moves in each increment. |
| SplitterWidth                         | Indicates the width of the splitter. |

#### C# Code Example

```csharp
this.SplitContainerAdv1.IsSplitterFixed = true;
this.SplitContainerAdv1.SplitterDistance = 25
this.SplitContainerAdv1.SplitterIncrement = 5
this.SplitContainerAdv1.SplitterWidth = 20
```

#### VB.NET Code Example

```vb
Me.SplitContainerAdv1.IsSplitterFixed = True
Me.SplitContainerAdv1.SplitterDistance = 25
Me.SplitContainerAdv1.SplitterIncrement = 5
Me.SplitContainerAdv1.SplitterWidth = 20
```

### Example Image
![image](https://i.imgur.com/example.png)

This image shows the visual representation of a split container with a splitter.
```