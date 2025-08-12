```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_074.jpeg
document_name: QTP
page_number: 074
page_id: QTP#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:12Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Configuring QTP assemblies and swfconfig file settings.
- Entering the location of QTP assemblies and product version details.
- Validating swfconfig file references and saving the configuration.

## Content

### Configuring QTP Assemblies

1. Open the "Essential QTP Configurator" window.
   - The window provides fields to configure the swfconfig file along with QTP Assemblies Location and Product Version.
   - Below is an example screenshot of the configurator:

   ![Essential QTP Configurator Window](image)

2. Enter the QTP assemblies' location in the **QTP Assemblies Location** textbox.
   - Example path: `Files (x86)\Syncfusion\Essential QTP\10.4.0.53\bin\3.5`

3. Enter the Essential Studio version with framework in the **Product Version** textbox.
   - Example version: `10.403.0.53`

4. After entering the details, click **Check & Configure**.
   - This step will validate the swfconfig file.

5. If the swfconfig file holds the valid reference path, the swfconfig utility shows the dialog box to save the `swfconfig.xml` file.

### Step-by-Step Configuration

Here's the step-by-step process for configuring QTP assemblies:

1. **Open the Configurator:**
   - Launch the "Essential QTP Configurator".

2. **Enter the QTP Assemblies Location:**
   - In the **QTP Assemblies Location** textbox, input the path to the QTP assemblies.
     - Example: `Files (x86)\Syncfusion\Essential QTP\10.4.0.53\bin\3.5`

3. **Enter the Product Version:**
   - In the **Product Version** textbox, input the version of the Essential Studio framework.
     - Example: `10.403.0.53`

4. **Check Configuration:**
   - Click the **Check & Configure** button to validate the swfconfig file.

5. **Save the Configuration:**
   - If the configuration is valid, the swfconfig utility will display a dialog to save the `swfconfig.xml` file.

   ![Final Configurator Window](image)

## API Reference

- **Configure SwfConfig file**
- **QTP Assemblies Location** 
- **Product Version**

## Code Examples

```xml
<AssemblyInfo>
    <AssemblyLocation>Files (x86)\Syncfusion\Essential QTP\10.4.0.53\bin\3.5</AssemblyLocation>
    <ProductVersion>10.403.0.53</ProductVersion>
</AssemblyInfo>
```

## Tags and Keywords
<!-- tags: [QTP, swfconfig, Essential Studio, WinForms, product version] keywords: [Essential QTP Configurator, QTP Assemblies Location, Product Version, swfconfig.xml, swfconfig file] -->
```