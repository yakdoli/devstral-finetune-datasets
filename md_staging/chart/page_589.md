```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_589.jpeg
document_name: chart
page_number: 589
page_id: chart#page_589
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:51:49Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

- ChartTemplate has a static method to save the data programmatically. We need to pass ChartControl instance and a file name (it can accept stream file also.), through this save method.

### Saving Chart Templates

```csharp
ChartTemplate.Save(this.chartControl1, "TemplateName.xml");
```

```vb
ChartTemplate.Save(Me.chartControl1, "TemplateName.xml")
```

## Load Template

Essential Chart provides support to load the saved Chart template into a new chart control. This loads the eries properties and the point properties, which were saved in a XML file and applies these properties into the new chart control.

- At the design time, by selecting the **Load Template** from the context menu.
- By clicking the **Load Template** designer verb, in the Visual Studio property browser.

ChartTemplate has static method, to load the template data programmatically. We need to pass the ChartControl, that will be applied with the loaded template data.

## Reset Template

The ChartControl, which when loaded with a template will be applied with the appearance and other settings that were stored in the template. These settings can be reset and the Chart can be reverted back to its original appearance by using the below two methods.

- At the design time, by selecting the "Reset Template.." from the context menu.
- By clicking the "Reset Template" link in the Visual Studio property browser.

ChartTemplate can be reset using the following simple statements,

### Resetting Chart Templates

```csharp
ChartTemplate ct = new ChartTemplate();
ct.Reset(this.chartControl1);
```

```vb
ChartTemplate ct = New ChartTemplate()
```

## Notes
- The ChartTemplate feature allows for saving, loading, and resetting chart templates, providing flexibility in managing chart designs and styles programmatically.
<!-- tags: [Syncfusion, Chart, ChartTemplate, Save, Load, Reset] keywords: [ChartTemplate, Save, Load, Reset, ChartControl] -->
```