```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_120.jpeg
document_name: common
page_number: 120
page_id: common#page_120
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:05:09Z
fidelity: lossless
-->

# 4 Frequently Asked Questions

This section covers frequently asked questions related to Essential Studio.

## 4.1 How to Configure the Toolbox of Visual Studio Manually

The following are the steps to load the Syncfusion controls in toolbox of visual studio by configuring the toolbox:

### 4.1.1 Toolbox Configuration Utility

To configure the toolbox using Toolbox Configuration Utility, refer to Toolbox Configuration.

### 4.1.2 Manually Configuring VS Toolbox

The following are the steps to configure VS Toolbox manually for Syncfusion tools:

1. **Close all Visual Studio running instances.**
2. **Remove the *.tbd files except the toolbox.tbd from the following location:**

   - **Windows XP:**

     ```
     C:\Documents and Settings\(user name)\Local Settings\Application Data\Microsoft\VisualStudio\10.0
     ```

   - **Vista/Windows 7:**

     ```
     C:\Users\(user name)\AppData\Local\Microsoft\VisualStudio\10.0
     ```

   <img src="safe_note.png" alt="Note: It will take some time to configure the toolbox and create tbd files when initially loading the toolbox in VS2010.">

   3. Re-open the Visual Studio environment. The VS toolbox will be configured.

### Adding Syncfusion controls in the customized toolbox

The following are the steps to add the Syncfusion controls in the user customized toolbox:

1. Open Visual Studio and then create a new tab named **Syncfusion** in the toolbox.
```