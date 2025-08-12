<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_785.jpeg
document_name: grid
page_number: 785
page_id: grid#page_785
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:39:47Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- This section explains the localization support provided by the GridGrouping control for customizing the display content of static elements.
- Demonstrates how to localize the compare operator list box options in a dynamic filter.

## Content

### 4.3.4.3.4.2.2.1 Localization Support for CompareOperatorListBox

The dynamic filter in the GridGrouping control provides support to customize the display content of the static element. Using this you can localize the static elements in the compare operator list box.

#### Use Case Scenarios

With this feature, you can localize the options in the compare operator list box to display the language specific to your locale.

#### Sample Link

A demo of this feature is available in the following location:

```
{Installed
Path}\Syncfusion\EssentialStudio\x.x.x.x\Windows\Grid.Grouping.Windows\Samples\2.0\Filters\Dynamic Filter Demo
```

### Adding Localization Support for CompareOperatorListBox

To localize the content, create a class file and add an interface as `ILocalizationProvider`. Assign the required content to be displayed to the `DynamicFilterResourceIdentifiers` of the `GetLocalizedString` method as illustrated in the following code:

#### Code Example

```csharp
public string GetLocalizedString(System.Globalization.CultureInfo culture, string name)
{
    if (str == "True")
    {
        switch (name)
        {
#region Menu Package
            case DynamicFilterResourceIdentifiers.StartsWith:
                return "empieza con";
            case DynamicFilterResourceIdentifiers.EndsWith:
                return "termina con";
            case DynamicFilterResourceIdentifiers.Equals:
                return "es igual a";
            case DynamicFilterResourceIdentifiers.GreaterThan:
                return "mayor que";
            case DynamicFilterResourceIdentifiers.GreaterThanOrEqualto:
                return "Mayor o igual a";
            case DynamicFilterResourceIdentifiers.LessThan:
                return "menos que";
            case DynamicFilterResourceIdentifiers.LessThanOrEqualTo:
                // Additional logic here
        }
    }
}
```

## RAG Annotations
<!-- tags: localization, GridGrouping, Windows Forms, Syncfusion, dynamic filter keywords: localization, static elements, compare operator list box, locale-specific languages, ILocalizationProvider, DynamicFilterResourceIdentifiers, GetLocalizedString, WinForms, Grid.Grouping.Windows -->
