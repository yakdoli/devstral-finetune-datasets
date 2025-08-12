```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_075.jpeg
document_name: QTP
page_number: 075
page_id: QTP#page_075
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:55Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- The Essential QTP Configurator tool is used to configure QTP assemblies.
- It checks and configures the swfconfig file based on the specified QTP assemblies location and product version.
- A version conflict error can occur due to invalid assembly reference paths.

## Content

### Configuring SwfConfig File

The Essential QTP Configurator allows you to configure the swfconfig file. Here's a step-by-step guide on how to use it:

1. **Open the Configurator**: Launch the Essential QTP Configurator tool.
2. **Specify Assemblies Location**: Enter the location of the QTP assemblies in the "QTP Assemblies Location" field.
3. **Set Product Version**: Input the required product version in the "Product Version" field.
4. **Check & Configure**: Click the "Check & Configure" button to validate and update the swfconfig file.
5. **Save Report**: After checking and configuring, you can save the report for future reference.

#### Version Conflict Error
If a version conflict error occurs, it indicates that the swfconfig file contains an invalid assembly reference path. Here are the steps to handle this:

1. **Identify the Issue**: Upon encountering the error message box, verify the swfconfig file's contents.
2. **Correct Assembly Reference**: Update the swfconfig file to resolve any incorrect assembly references.
3. **Retry Configuration**: Repeat the configuration process after making necessary corrections.

#### Sample Configuration Interface

The figure below shows the Essential QTP Configurator interface.

![Essential QTP Configurator Interface](attachment)

#### Handling Version Conflicts

If you get the error message box with a version conflict error, the swfconfig file holds an invalid assembly reference path. The interface will prompt you with options to resolve the conflict.

![Version Conflict Dialog](attachment)

### Resolving Version Conflicts

- **Error Dialog**: The tool will display a dialog indicating a version conflict.
- **Action Required**: Address the invalid assembly reference paths in the swfconfig file.
- **Retry Configuration**: After correcting the issue, retry the configuration process.

## API Reference

The Essential QTP Configurator operates by manipulating the swfconfig file, which contains references to various assemblies. Below are the key components involved:

- **AssemblyName**: Lists the names of the assemblies referenced.
- **ProductVersion**: Specifies the version of each assembly.
- **DateModified**: Indicates the last modification date for each assembly.
- **Size**: Displays the size of each assembly.

### Example Table of Assemblies

| AssemblyName             | ProductVersion | DateModified   | Size    |
|--------------------------|----------------|----------------|---------|
| ButtonAdv.dll           | 10.403.0.53    | 1/23/2013      | 6.5 KB  |
| CalculatorControl.dll   | 10.403.0.53    | 1/23/2013      |         |
| ChartControl.dll        | 10.403.0.53    | 1/23/2013      |         |
| CheckBoxAdv.dll         | 10.403.0.53    | 1/23/2013      |         |
| ColorPickerUIAdv.dll    | 10.403.0.53    | 1/23/2013      |         |
| ComboBoxAutoComplete.dll | 10.403.0.53    | 1/23/2013      |         |
| ComboBoxDropDown.dll     | 10.403.0.53    | 1/23/2013      |         |
| CommandBar.dll          | 10.403.0.53    | 1/23/2013      |         |

## Code Examples

### C# Example

```csharp
// Configuring the swfconfig file programmatically
public void ConfigureSwfConfig()
{
    var configurator = new EssentialQTPConfigurator();
    configurator.AssembliesLocation = @"Files (x86)\Syncfusion\Essential QTP\10.4.0.53\bin\3.5";
    configurator.ProductVersion = "10.403.0.53";
    configurator.CheckAndConfigure();
    configurator.SaveReport();
}
```

### XML Configuration

```xml
<swfconfig>
    <assembly name="ButtonAdv.dll" version="10.403.0.53" />
    <assembly name="CalculatorControl.dll" version="10.403.0.53" />
    <!-- Add other assemblies as needed -->
</swfconfig>
```

## RAG Annotations

<!-- tags: [Essential QTP Configurator, swfconfig file, version conflict error, assembly reference path, Syncfusion Winforms] keywords: [QTP, assembly version, configuration tool, error handling, assembly list, product version] -->
```