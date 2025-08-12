```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_296.jpeg
document_name: XlsIO
page_number: 296
page_id: XlsIO#page_296
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:09:32Z
fidelity: lossless
--> 

# Essential XlsIO

This section lists the following topics:

## List of Properties

The following table lists the properties available.

| Name of the Property | Type  | Value Accepted        | Description                                                                                                   |
|----------------------|-------|-----------------------|---------------------------------------------------------------------------------------------------------------|
| DisplayAsIcon       | Normal| Boolean               | Gets or sets value indicating whether to display the OLE object as icon.                                      |
| Location            | Normal| IRange                | Gets or sets the location of the OLE object in the sheet.                                                     |
| Picture             | Normal| Image                 | Gets or sets the picture to display to represent the OLE object.                                               |
| Shape               | Normal| IPictureShape         | Gets or sets picture shape object that defines look and position of the OLE Object inside the parent worksheet. |
| Size                | Normal| System.Drawing.Size   | Gets or sets the size of the OLE object.                                                                     |
| OleObjectType       | Normal| OleObjectType         | Gets or sets the value indicating the type of OLE object.                                                     |

### Displaying an Object as Icon

The following set of code sample illustrates the condition when the property is set to True.

```csharp
oleObject1.DisplayAsIcon = true;
```

```vb.net
oleObject1.DisplayAsIcon = True
```

## Code Examples

- C#:
  ```csharp
  oleObject1.DisplayAsIcon = true;
  ```

- VB.NET:
  ```vb.net
  oleObject1.DisplayAsIcon = True
  ```

<!-- tags: [xlsio, properties, oleobject, syncfusion winforms] keywords: [properties, oleobject, displayasicon, location, picture, shape, size, olEObjectType] -->
``` 
