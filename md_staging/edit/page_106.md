```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_106.jpeg
document_name: edit
page_number: 106
page_id: edit#page_106
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:00:45Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

| Event | Description |
|-------|-------------|
| CollapsingAll | Occurs when CollapseAll method is called. |
| ExpandingAll | Occurs when ExpandAll method is called. |

The above events can be canceled, and can be used to optionally cancel the Outlining Collapse and Expand operations respectively. They are discussed in detail in the Edit Control Events section.

The Custom Outlining Demo sample demonstrates how the outlining feature can be used on any custom file or plain text, and not necessarily on programming language code samples. This sample is available in the following location.

`..\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Edit.Windows\Samples\2.0\Text Formatting\CustomOutliningDemo`

## 4.4.11.5.1 Outlining Tooltip

Outlining Tooltip is displayed for each collapsed outlining block, and it shows the contents of the collapsed block. This feature is similar to the one available in Visual Studio.NET editor.

The Outlining Tooltip can be optionally shown / hidden by using the ShowOutliningTooltip property in the Edit Control.

```csharp
this.editControl1.ShowOutliningTooltip = true;
```

```vb.net
Me.editControl1.ShowOutliningTooltip = True
```

<!-- tags: [winforms, syncfusion, edit control, outlining, tooltip, custom demo] keywords: [collapseall, expandall, outlining feature, ShowOutliningTooltip, custom outlinging demo, visual studio.net] -->
```