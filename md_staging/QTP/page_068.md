```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: QTP
page_number: 068
page_id: QTP#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:35Z
fidelity: lossless
-->

## Essential QuickTest Professional

### Overview
- This page provides instructions on configuring the Essential QTP Configurator and appending the swfconfig.xml file.

## Content

### Configuring SwfConfig File

#### Figure 30: Appending the SwfConfig File

The Essential QTP Configurator tool allows you to configure and append the swfconfig.xml file. Here is the process explained:

1. **Access the Configurator**:
   - Open the Essential QTP Configurator.
   - Navigate to the "Configure SwfConfig file" section.

2. **Locate and Enter the QTP Assemblies**:
   - In the QTP Assemblies Location field, specify the path to your QTP assemblies, for example: `Files (x86)\Syncfusion\Essential QTP\10.4.0.53\bin\3.5`.

3. **Enter the Product Version**:
   - Enter the product version in the designated field. For example, `10.403.0.53`.

4. **Check and Configure**:
   - Click the "Check & Configure" button to verify the configuration.

5. **Save Report**:
   - Optionally, save the configuration report using the "Save Report" button.

6. **Review the Assembly List**:
   - A list of assembly names and their corresponding product versions will be displayed, such as:
     - `ButtonAdv.dll` - `10.403.0.53`
     - `CalculatorControl.dll` - `10.403.0.53`
     - `ChartControl.dll` - `10.403.0.53`
     - `ColorPickerUIAdv.dll` - `10.403.0.53`
     - `ComboBoxAutoComplete.dll` - `10.403.0.53`
     - `CommandBar.dll` - `10.403.0.53`
     - And others.

7. **Append the swfconfig.xml File**:
   - If your system already has a swfconfig.xml file, a dialog box will appear asking you whether to append or replace the existing file.
   - **Replace Existing File**:
     - Click **Yes** to replace the old swfconfig.xml file with the current framework swfconfig.xml file.
   - **Keep Both Files**:
     - Click **No** if you wish to keep both files in the same folder.

### Do You Want to Append the Swfconfig.xml File?
A dialog box will prompt you with the following message:  
"**Do you want to append the swfconfig.xml file?**"  
Click **Yes** or **No** based on your requirements.

## API Reference (if applicable)

None specified in this section.

## Code Examples (multi-language supported)

None applicable in this section.

## Page-level Navigation/TOC (if applicable)

None additional content provided in this section.

## Cross References

None relevant cross-references in this section.

## RAG Annotations
<!-- tags: [QTP Configurator, swfconfig.xml, QTP assemblies, version configuration] keywords: [append, replace, configuration, dialog box, assembly names, product versions] -->
```