```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_086.jpeg
document_name: common
page_number: 086
page_id: common#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:03:15Z
fidelity: lossless
-->

# Essential Common

## Overview
- Describes the configuration options for building assemblies in Syncfusion Winforms using .NET Framework versions.
- Details the Product, Platform Type, Assembly Type, Dependencies, Strong Key, and Output settings.
- Explains the default selections and how to customize these settings for specific build requirements.

## Content

### Framework Version
The Framework Version group box provides four option buttons: .NET 2.0, .NET 3.5, .NET 4.0, and .NET 4.5. If Visual Studio 2012 is not installed, the .NET 4.0 option is selected by default. If Visual Studio 2010 is not installed, .NET 3.5 is selected by default. If Visual Studio 2008 is not installed, .NET 2.0 is selected by default. You can change the default option by clicking another option button. The specified version of the .NET Framework is used to rebuild the assemblies.

### Product
The Product group box includes a drop-down list box where the default selection is "All." You can change the default option by selecting one of the products in the list box.

### Platform Type
Syncfusion products utilize a common base library forming the basis for Windows and Web variants. The library category for the build is specified using the Product Type. This frame offers eight option buttons, with "All" selected by default. You can select the required product's option button to perform the build operation.

**Note:** Assemblies that are not built and pre-compiled assemblies with the product will automatically be used.

### Assembly Type
This frame includes two option buttons: Debug and Release. Debug is selected by default. To choose the release mode for the assembly, select "Release." Here, the user can switch between Debug and Release modes for product configurations. Building the debug version allows stepping into Syncfusion assemblies during application debugging.

### Dependencies
This section allows you to specify whether dependent assemblies of the product need to be used. If the "Use PreBuilt Dependencies" check box is selected, the dependent assemblies from the selected Product frame will be taken from the "Pre-Compiled Assemblies" folder, which exists under the installed location. Rebuilding assemblies can be restricted to specific assemblies by enabling pre-built dependencies, in which case other assemblies would use precompiled variants installed with the product.

### Strong Key
This feature enables the installation of compiled assemblies in the Global Assembly Cache (GAC). Select the "Use Strong Key" check box and choose a `.snk` file to achieve this.

### Output

## API Reference (if applicable)
- Refer to the Syncfusion Winforms documentation for specific namespace and class references for configuration options and build parameters.

## Code Examples (multi-language supported)
- Implement configuration settings programmatically by utilizing the relevant namespaces and settings documented in the Syncfusion Winforms SDK.

## Page-level Navigation/TOC (if applicable)
- Refer to the table of contents or navigation within the Syncfusion Winforms documentation for further details on related topics.

## Cross References
- See also: Syncfusion documentation for detailed instructions on build configurations and assembly management.

<!-- tags: [Syncfusion, Winforms, assembly, configuration, build, .NET Framework] keywords: [Framework Version, Product, Platform Type, Assembly Type, Dependencies, Strong Key, Output] -->
```