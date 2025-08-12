```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_070.jpeg
document_name: QTP
page_number: 070
page_id: QTP#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:49Z
fidelity: lossless
-->

## Essential QuickTest Professional

### Overview
- An image showcasing the "Essential QTP Configurator" for configuring the SwfConfig.xml file.
- Steps to configure and save the SwfConfig.xml file and restart QTP for updated control mappings.
- Reference to the SwfConfig.xml file and its role in test setup.

### Content

#### QTP Configuration Setup
The "Essential QTP Configurator" is a tool used to configure the SwfConfig.xml file. This file is crucial for mapping controls in the test environment. Below is a step-by-step process to set up the configuration:

1. **Configure SwfConfig file**:  
   - **QTP Assemblies Location**:  
     ```
     Files (x86)\Syncfusion\Essential QTP\10.4.0.53\bin\3.5
     ```
   - **Product Version**:  
     ```
     10.403.0.53
     ```

2. **Assembly Details**:
   Below is a table listing assemblies and their details:
   | AssemblyName             | ProductVersion | Date Modified | Size   |
   |--------------------------|----------------|---------------|-------|
   | ButtonAdv.dll           | 10.403.0.53    | 1/23/2013     | 6.5 KB |
   | CalculatorControl.dll   | 10.403.0.53    | 1/23/2013     | 7.5 KB |
   | ChartControl.dll        | 10.403.0.53    | 1/23/2013     | 28 KB  |
   | CheckBoxAdv.dll         | 10.403.0.53    | 1/23/2013     | 6.5 KB |
   | ColorPickerUIAdv.dll    | 10.403.0.53    | 1/23/2013     | 7.5 KB |
   | ComboBoxAutoComplete.dll| 10.403.0.53    | 1/23/2013     | 16 KB  |
   | ComboBoxDropDown.dll    | 10.403.0.53    | 1/23/2013     | 16 KB  |
   | CommandBar.dll          | 10.403.0.53    | 1/23/2013     | 20 KB  |

3. **Configuration Report**:
   - Click **Check & Configure** to ensure all assemblies are correctly mapped.
   - Click **Save Report** to save the configuration details.

4. **File Confirmation Prompt**:
   Upon configuration completion, a dialog appears asking if you want to open the swfconfig.xml file:
   ```
   Swfconfig.Xml file configured.
   Do you want to open the swfconfig.xml file?
   Yes | No
   ```

#### Restart QTP for Updated Mappings
5. **Restart QTP**:  
   Restart QTP once the SwfConfig.xml file is saved to refresh the mappings to the required controls before starting the test.

### Figure Reference
- **Figure 32**: Opening the new SwfConfig.xml File
  This figure shows the dialog confirming the completion of the SwfConfig.xml file configuration and the option to open the file.

## See also
- Documentation on QTP test environments and control configurations
- Reference to product version and assembly details

<!-- tags: [syncfusion-qtp, winforms, essential-qtp-configurator] keywords: [swfconfig, qtp testing, controls mapping] -->
```