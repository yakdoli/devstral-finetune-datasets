```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_078.jpeg
document_name: QTP
page_number: 078
page_id: QTP#page_078
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:30Z
fidelity: lossless
-->

## Why are Syncfusion controls not recognized even after adding the custom libraries?

The following are the troubleshooting steps to get the Syncfusion controls recognized in the QTP environment.

1. Make sure that the DLL path of the custom libraries is properly written in the SwfConfig.xml file. Refer to the Configuring Essential QuickTest Professional topic in this user guide for more details.
2. There are chances for typing errors to occur in the SwfConfig.xml. Ensure that there are no typing errors in the file and try replacing SwfConfig.xml at the correct location and restart QTP.
3. Sometimes the Syncfusion controls may not be recognized due to differences in the version numbers of Essential Studio and Essential QuickTest Professional, or .NET framework and Essential QuickTest Professional that are being used. Check if the version numbers of the assembly that is used to build the application and the Essential QuickTest Professional assembly are the same. If not, this can be solved by rebuilding the Custom Libraries with the required Syncfusion references and .NET framework. If you do not have the corresponding versions of Essential QuickTest Professional and Essential Studio, please contact us specifying the version of Essential QuickTest Professional that is required.
4. If the DLLs are the right version and are mapped correctly, and if the SwfConfig.xml is perfect, but there is still an issue of recognizing Syncfusion controls, then reinstall the .NET add-in for QTP. If the AUT (Application Under Test) is recorded as a WinObject (object in the Windows Environment), make a cross check with a small .NET application using a non-Syncfusion control to see if this control is also not recognized. If so, the problem is with the QTP or .NET add-in installed. Thus, we can isolate the problem with the .NET controls being recognized. SwfObject would be the right way to be recognized after the .NET add-in install.

## How do I know that Essential QuickTest Professional works as expected?

When Syncfusion control events are recorded, they should be able to record with the method that is handled in the custom library (DLL). This will not occur if the mapping is not correct. If the mapping in the DLLName tag of the SwfConfig.xml does not point to the required DLL, the recording would be seen as in the sample script below, which is a low-level recording already explained in the document.

```csharp
[QTP]
SwfWindow("GridDataBoundGrid CellTypes").SwfObject("gridDataBoundGrid2").SetCurrentCell 1,2
```
```