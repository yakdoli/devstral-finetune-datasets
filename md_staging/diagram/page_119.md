```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_119.jpeg
document_name: diagram
page_number: 119
page_id: diagram#page_119
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:26Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### Overview
- Displays the essential diagram features specific to Windows Forms.
- Illustrates how to control the appearance of bridges in a diagram using properties.
- Focuses on programmatic configurations for enhancing diagram layout.

### Content

#### Diagram Illustration

![Diagram showing Line Bridging](#)
*Figure 70: Line Bridging*

The below table lists the properties which controls the appearance of the bridge.

| Property         | Description                                                                                                                                |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| LineBridgeSize   | Allows to set the size of the bridge when the links intersect each other. Default value is 16.                                           |
| BridgeStyle      | Specifies the type of bridge to be applied. Default value is 'Arc'. The value when set, applies to all the links that are drawn on the diagram. The links will bridge over the other link only when its ZOrder value is high. The options include the following: |
|                   | • Arc<br>• Gap<br>• Square<br>• Side2<br>• Side3<br>• Side4<br>• Side5<br>• Side6<br>• Side7                                              |

#### Programmatic Configuration

Programmatically it can be set as follows:

```csharp
// [C#]
```

## Conclusion
This chapter outlines the essential diagram features and how to configure bridging properties programmatically in Windows Forms applications using Syncfusion tools. 

### Tags and Keywords
<!-- tags: [Syncfusion Winforms, Essential Diagram, Line Bridging, ZOrder, BridgeStyle, LineBridgeSize] keywords: [diagram, windows forms, line bridging, z-order] -->
```