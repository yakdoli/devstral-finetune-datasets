```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: QTP
page_number: 067
page_id: QTP#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:21Z
fidelity: lossless
-->

# 6 Utilities

## 6.1 Configuring the SwfConfig file

An XML file in QTP called SwfConfig is the configuration file located at `(Installed location of Essential QuickTest Professional)\Config\<version-2.0, 3.5, or 4.0>\swfconfig`, which contains all the mapping information for QTP to recognize Syncfusion controls. Using the SwfConfig utility, users can easily configure the `SwfConfig.xml` file in HP QTP.

### Steps to Configure the SwfConfig.xml File

1. Open the Syncfusion Essential QTP Configurator located at `(Installed location of Essential QuickTest Professional)\Utilities\SwfConfigUtility\SwfConfigUtility.exe`.
   - Enter the QTP assemblies' location in the **QTP Assemblies Location** textbox.
   - Enter the Essential Studio version with framework in the **Product Version** textbox.
   - After entering the details, click **Check & Configure**. It will create the `swfconfig.xml` file for that particular version.

   ![Creating the SwfConfig.xml File for Essential Studio 10.3](attachment/SwfConfigUtility.png)

   **Figure 29: Creating the SwfConfig.xml File for Essential Studio 10.3**

2. Then Essential QTP Configurator shows the dialog box for appending the `swfconfig.xml` file. Click **Yes** to append the `swfconfig.xml` file in the QTP machine.

<!-- tags: [Essential QuickTest Professional, SwfConfig, Syncfusion controls, QTP, HP, XML configuration, Essential QTP Configurator, SwfConfigUtility. ] keywords: [Essential QuickTest Professional, SwfConfig, Syncfusion controls, QTP, HP, XML configuration, Essential QTP Configurator, SwfConfigUtility, product version, QTP assemblies, creating XML files, appending, verification utility, Essential Studio] -->
```