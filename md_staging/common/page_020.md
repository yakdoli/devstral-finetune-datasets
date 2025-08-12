```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_020.jpeg
document_name: common
page_number: 020
page_id: common#page_020
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:59:34Z
fidelity: lossless
-->

## Essential Common

### Installation Steps

1. Copy the `SyncfusionEssentialStudio_(version).exe` file in local drive. Example: `D:\temp`
2. Cancel the wizard.
3. Open the command prompt in administrator mode and pass the following arguments:

    ```
    "Setup file path\SyncfusionEssentialStudio(platform)_(version).exe" Install
    /PIDKEY:“(product unlock key)” /InstallPath:C:\Program Files\Syncfusion\x.x.x
    ```
    
    Example:
    ```
    "D:\Temp\SyncfusionEssentialStudio(platform) _11.1.0.1.exe" Install
    /PIDKEY:“product unlock key” /InstallPath:C:\Syncfusion\x.x.x
    ```

4. Setup will be installed.

**Note:** `x.x.x` needs to be replaced with the Essential Studio version installed in your machine and the product unlock key needs to be replaced with the unlock key for that version. Platform should be replaced with aspnet, aspnetmvc, mobilemvc, silverlight, windowsforms, windowsphone, winrt, or wpf.

### Command Line Uninstall Options

Syncfusion Essential Studio supports uninstalling the setup through command line in silent mode. The following steps illustrate this:

1. If you don’t have the extracted setup (`SyncfusionEssentialStudio(platform)_(version).exe`), then follow the steps from 2 to 7.
2. Double-click the Syncfusion Essential Studio platform Setup file. The self-Extractor wizard opens and extracts the package automatically.
3. The `SyncfusionEssentialStudio(platform)_(version).exe` file will be extracted into the Temp folder.
4. Run `%temp%`. The Temp folder will open. The `SyncfusionEssentialStudio(platform)_(version).exe` file will be available in one of the folders.
5. Copy the `SyncfusionEssentialStudio(platform)_(version).exe` file in local drive. Example: `D:\temp`
6. Cancel the wizard.
7. Open the command prompt in administrator mode and pass the following arguments:

    ```
    “Setup file path\SyncfusionEssentialStudio(platform) _(version).exe” /uninstall true
    ```
    
    Example:
    ```
    “D:\Temp\SyncfusionEssentialStudio(platform)_11.1.0.1.exe” /uninstall true
    ```

8. Setup will be uninstalled.

**Note:** `x.x.x` needs to be replaced with the Essential Studio version installed in your machine and Product unlock key needs to be replaced with the unlock key for that version. Platform should be replaced with aspnet, aspnetmvc, mobilemvc, silverlight, windowsforms, windowsphone, winrt, or wpf.
```