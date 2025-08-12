```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_137.jpeg
document_name: common
page_number: 137
page_id: common#page_137
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:06:27Z
fidelity: lossless
-->

# Essential Common

You can use this satellite assembly to utilize the localization support for your culture. The following steps will help you to extract the resource strings to a .csv file using the LocBaml.exe file, as a major part of enabling localization.

## Overview
- Utilizing satellite assemblies for localization support.
- Extracting resource strings to a .csv file using LocBaml.exe.
- Steps to extract and customize resource strings.

## Content

The Syncfusion.Tools.WPF.Resources.dll is sufficient to generate the localization support for the Syncfusion controls. This assembly will be available in the following installation location:

### Installation Location

```
(Installed_location)\Syncfusion\Essential Studio\<Version Number>\Assemblies\3.5
```

### Steps to Enable Localization

1. **Download the LocBaml.exe file**  
   From the following location:  
   ```
   http://files.syncfusion.com/support/Tools.WPF/UG/LocBaml.zip
   ```

2. **Copy the exe file and Syncfusion.Tools.WPF.Resources.dll**  
   To the following location:  
   ```
   <Your Application>\bin\Debug\en-US
   ```

3. **Open the command prompt**  
   Navigate to the same directory as mentioned above.

4. **Generate the .csv file**  
   Use the following command to generate the .csv file from the existing Syncfusion.Tools.WPF.Resources.dll:  
   ```
   (Your Application)\bin\Debug\en-US LocBaml /parse Syncfusion.Tools.WPF.Resources.dll /out:resourceStrings.csv
   ```

5. **Edit the .csv file**  
   - The .csv files can be edited via MS Excel or Notepad.  
   - This file contains string resources with the default text in the English language.  

   Open the .csv file using MS Excel or Notepad, and change the texts based on your culture.

### Example Customization: English to French

The following illustrates customization from English to French.

<!-- tags: [Syncfusion Winforms, localization, resource strings, .csv file, LocBaml, string localization, satellite assembly] -->
```