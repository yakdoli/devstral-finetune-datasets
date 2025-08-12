```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_508.jpeg
document_name: chart
page_number: 508
page_id: chart#page_508
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:46:30Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- How to add multiple chart titles in a Windows Forms application.
- How to display chart titles as multiline text using the `ChartTitle.Text` property.

## Content

### Chart with Multiple Chart Titles
You can add multiple chart titles to a Windows Forms application using the following code snippet:

```csharp
Me.ChartControl1.Titles.Add(title)
```

#### Figure 326: Chart with Multiple Chart Titles
![Chart with Multiple Chart Titles](https://i.imgur.com/example.png)

**Figure 326: Chart with Multiple Chart Titles**

### Multiline Chart Title
You can now wrap the Chart titles and display them as multiline text. Set multiline title text in `ChartTitle.Text` property through designer as follows. Press ENTER key to begin a new line. Press CTRL+ENTER to set the text entered.

#### Figure: Chart with Multiline Title
![Chart with Multiline Title](https://i.imgur.com/example2.png)

**Figure: Chart with Multiline Title**

## API Reference

### ChartTitle Class
- **Property:** `Text`
  - **Description:** Sets or gets the text displayed by the title.
  - **Type:** `string`

## Code Examples

### Adding a Multiline Chart Title

```csharp
using Syncfusion.Windows.Forms.Chart;

// Assuming chartControl1 is a ChartControl on the form
ChartTitle title = new ChartTitle();
title.Text = "Essential\nChart\nMultiline\nTitle";
title.TextAlignment = ContentAlignment.TopCenter;
chartControl1.Titles.Add(title);
```

## RAG Annotations
<!-- tags: [chart, windowsforms, multilinetitle] keywords: [charttitle, textproperty, multiline, linebreak, enterkey, ctrl+enter] -->
```