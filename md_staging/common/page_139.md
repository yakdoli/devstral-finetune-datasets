```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_139.jpeg
document_name: common
page_number: 139
page_id: common#page_139
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:31Z
fidelity: lossless
-->

# Essential Common

```csharp
Thread.CurrentThread.CurrentUICulture = new
System.Globalization.CultureInfo("fr-FR");
Thread.CurrentThread.CurrentCulture = new
System.Globalization.CultureInfo("fr-FR");
)
```

At the end of this process, the application should contain the following to achieve localization:

- Your Application.exe file
- The en-US directory with Resources.dll
- The fr-CH directory with corresponding Resources.dll and Syncfusion Assemblies (if you have set `CopyLocal` to `True`).

## Calendar control in French language

The image below illustrates a Calendar control in the French language.

![](images/media/image140.png){#fig:131}
**Figure 131:** Calendar control localized to French

> **Note:** 
>
> - Localized strings will not be displayed in your application until the created satellite assembly is signed. Send us your newly created assemblies for signing. We will sign your assemblies and send them immediately.
> - It is not required to install satellite assemblies in the GAC or Assemblies folder.
> - Your en-US directory should contain the default satellite assembly, which is available in the Precompiled Assemblies or Assemblies folder.
> - Application culture change should be included before the `InitializeComponent()` method call in the application. It is better to include culture change in the App.xaml file.

## 4.7.2 Silverlight

In Silverlight, the easiest way to accomplish localization is to use a Resource (.resx) file. For each culture you wish to target, you will need a separate set of resources that match that specific culture.

The following are the primary steps for Localizing the Syncfusion Ribbon Control:
```markdown

The following are the primary steps for Localizing the Syncfusion Ribbon Control:
```

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations
<!-- tags: [syncfusion, winforms, localization, culture, satellite assembly, french, fr-fr, silverlight, resource file, app.xaml, calendar control] keywords: [localized strings, application localization, satellite assembly signing, GAC, Assemblies folder, Resource (.resx) file, Syncfusion Ribbon Control] -->
```