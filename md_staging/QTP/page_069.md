```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_069.jpeg
document_name: QTP
page_number: 069
page_id: QTP#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:01Z
fidelity: lossless
-->

## Overview
- Configuring Syncfusion assemblies with QTP (QuickTest Professional).
- Steps to replace the SwfConfig.xml file in HP QTP.
- Verifying and saving the new configuration for Syncfusion assembly integration.

## Content

### Essential QTP Configurator
When setting up the configuration for Syncfusion assemblies in QTP, the Essential QTP Configurator provides a visual interface for specifying the QTP Assemblies Location and Product Version. This tool assists in configuring the swfconfig.xml file, which dictates the integration of Syncfusion components with QTP.

#### Section: Configuring Syncfusion Assemblies
The **Configure SwfConfig File** interface allows users to:
- **QTP Assemblies Location**: Specify the directory containing the necessary libraries, such as `Files (x86)\Syncfusion\Essential QTP\10.4.0.53\bin\3.5`.
- **Product Version**: Enter the version of the product (10.403.0.53 in this example).
- After entering the required details, users can click the **Check & Configure** button to verify the configuration and generate the swfconfig.xml file.

#### Section: Assembly List
The listed assemblies include:
- ButtonAdv.dll
- CalculatorControl.dll
- ChartControl.dll
- CheckBoxAdv.dll
- ColorPickerUIAdv.dll
- ComboBoxAutoComplete.dll
- ComboBoxDropDown.dll
- CommandBar.dll
- Among others, ensuring all essential controls are included for automation.

#### Warning Dialog for Overwriting Configuration
Upon generating the swfconfig.xml file, a dialog prompts the user to confirm whether to replace the existing configuration:
- **You have Syncfusion assemblies configured already in the SwfConfig.xml file of HP QTP. Do you want to replace that?**
- **Select 'No' to skip the replacing and select 'Cancel' to abort.**

**Action Required**: Click **Yes** to save and open the new swfconfig.xml file, effectively replacing the existing configuration.

## Important Instructions
4. **After generating the swfconfig.xml file**, the system will ask whether you want to open it. **Click Yes** to save and open the new swfconfig.xml file.

## Cross References
See also: SwfConfig.xml file configuration in HP QTP for detailed instructions on Synfusion assembly integration.

<!-- tags: [QTP, swfconfig, Syncfusion, assembly configuration, HP QTP] keywords: [QTP, swfconfig, Syncfusion, assembly integration, configuration tool] -->
```