```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_588.jpeg
document_name: chart
page_number: 588
page_id: chart#page_588
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:51:33Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Overview
- Explanation of saving, loading, and resetting templates through designer verbs.
- Description of how appearance settings for various Chart components can be managed using templates.

## Figure 359: Saving, Loading, and Resetting Templates through Designer Verbs

![Properties Window](https://chart.googleapis.com/chart?cht=gallery&chl=Properties%20window%20showing%20designer%20verbs:%20Save%20Template,%20Load%20Template,%20Reset%20Template)

### Save Template

The appearance settings for various components of a Chart like ChartSeries, ChartArea, Series properties, and Point properties can be stored in a template, which can be loaded into new Chart control when needed.

#### Template Behavior
A chart template can contain the properties of more than one data series. When such templates are loaded into a destination ChartControl, the appearance settings of the data series will be applied in a sequential order. For example:
- The first set of appearance settings of a data series will be applied to the destination Chart's first series.
- The second set of appearance properties of the data series will be applied to the destination Chart's second series, and so on.

If the destination collection's length is larger than the source collection, then the settings will repeat itself for these additional entries in the destination collection.

#### Saving Charts as Templates
These Charts can be saved as templates in the following two ways:
- **Selecting the Save Template option** from the context menu.
- **By clicking the Save Template designer verb** in the Visual Studio property browser.

## API Reference
- **Namespace**: `Syncfusion.Windows.Forms.Chart`
- **Class**: `ChartControl`
- **Properties**:
  - TabIndex
  - TabStop
  - Tag
  - Text
  - TextAlignment
  - TextPosition
  - TextRenderingHint

## Code Examples
```csharp
// Example of loading a template into a ChartControl
chartControl1.LoadTemplate("template.sfs");

// Example of saving a Chart as a template
chartControl1.SaveTemplate("new_template.sfs");
```

## Page-level Navigation/TOC
- Save Template
  - Template Behavior
  - Saving Charts as Templates

### Cross References
- See also: ChartControl, ChartSeries, ChartArea, Series properties, Point properties, Template Load/Save functionality.

<!-- tags: [charts, windows forms, templates, designer verbs, save template, load template, reset template] keywords: [chartcontrol, chartseries, chartarea, series properties, point properties, appearance settings, sequential order, template loading, template saving, features, windows forms, synchronization, data series] -->
```