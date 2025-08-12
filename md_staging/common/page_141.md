```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_141.jpeg
document_name: common
page_number: 141
page_id: common#page_141
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:40Z
fidelity: lossless
-->

# Essential Common

## Overview
- Demonstrates how to apply cultural settings to the Ribbon Control in WinForms.
- Instructions to set the UI culture programmatically using C# code in `MainPage.xaml.cs` or `App.xaml.cs`.
- Visual examples showing the Ribbon Control under different culture settings.

## Content

### Setting the UI Culture in C# Code

#### In MainPage.xaml.cs
The UI culture can be set in the constructor of the `MainPage` class as follows:

```csharp
public MainPage()
{
    System.Threading.Thread.CurrentThread.CurrentUICulture = new
    System.Globalization.CultureInfo("fr-FR");

    InitializeComponent();
}
```

#### In App.xaml.cs
Alternatively, the UI culture can be set during the application startup in `App.xaml.cs`:

```csharp
private void Application_Startup(object sender, StartupEventArgs e)
{
    System.Threading.Thread.CurrentThread.CurrentUICulture = new
    System.Globalization.CultureInfo("fr-FR");

    this.RootVisual = new MainPage();
}
```

### Visual Illustrations

#### Figure 132: Ribbon Control for Invariant Culture

[![Figure 132: Ribbon Control for Invariant Culture](https://via.placeholder.com/800x400.png?text=Figure+132%3A+Ribbon+Control+for+Invariant+Culture)](./assets/image1.png)

**Description:** This figure shows the Ribbon Control without any specific cultural localization applied.

#### Figure 133: French Culture assigned as Current UI Culture

[![Figure 133: French Culture assigned as Current UI Culture](https://via.placeholder.com/800x400.png?text=Figure+133%3A+French+Culture+assigned+as+Current+UI+Culture)](./assets/image2.png)

**Description:** This figure illustrates the Ribbon Control after setting the culture to French (`fr-FR`), displaying labels and other elements in French.

## Cross References
- For more information on internationalization and localization using Syncfusion controls, refer to the relevant sections in the Syncfusion WinForms User Guide.

<!-- tags: [syncfusion, winforms, ribbon-control, ui-culture, localization, culture] keywords: [MainPage.xaml.cs, App.xaml.cs, CultureInfo, CurrentUICulture, French culture, invariant culture, Ribbon Control, WinForms] -->
```