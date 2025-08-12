```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_012.jpeg
document_name: PDF Viewer
page_number: 012
page_id: PDF Viewer#page_012
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:50:21Z
fidelity: lossless
-->

## Overview
- Features supported by the Essential PDF Viewer for RGB, CMYK, Gray, ICC, and Indexed color modes.
- Compatibility with various compression filters like DCTDecode, CCITTFaxDecode, FlateDecode, LZWDecode, ASCII85Decode, ASCIIHexDecode, and JBIG2Decode.
- Support for specific interactive features, including Zoom, Page Navigation, and Search, but limited support for Actions, Annotations, Bookmarks, and Navigation Pane.

## Content

### Color Modes
| RGB   | Yes | Yes | Yes   |
| CMYK  | Yes | Yes | Yes*** |
| Gray  | Yes | Yes | Yes   |
| ICC   | Yes | Yes | Yes   |
| Indexed | Yes | Yes | Yes   |

### Compression Filters
| DCTDecode (Image, Content) | Yes | Yes | Yes   |
| CCITTFaxDecode (Image) | Yes | Yes | Yes   |
| FlateDecode (Image, Content) | Yes | Yes | Yes   |
| LZWDecode (Content only) | Yes | Yes | Yes   |
| ASCII85Decode (Content only) | Yes | Yes | Yes   |
| ASCIIHexDecode (Image) | Yes | Yes | Yes   |
| JBIG2Decode (Image) | Yes | Yes | Yes   |

### Interactive Features
| Actions | No | No | No   |
| Annotations | Yes**** | Yes**** | No   |
| Attachments | No | No | No   |
| Bookmarks | No | No | No   |
| Form | No | No | No   |
| Page Navigation | Yes | Yes | Yes   |
| Zoom | Yes | Yes | Yes   |
| Navigation Pane | No | No | No   |
| Selection (Keyboard & Mouse) | No | No | No   |
| Search | Yes | Yes | No   |
| Document Information | No | No | No   |
| Conformance | Yes | Yes | Yes   |
| Encrypted Documents | Yes | Yes | Yes   |

## API Reference (if applicable)
- **Namespace**: Syncfusion.Pdf
- **Class**: PdfDocument

### Members

#### Properties
- **Annotations**: Collection of annotations in the PdfDocument.
- **Bookmarks**: Collection of bookmarks in the PdfDocument.
- **Conformance**: Conformance level of the document (e.g., Pdf15, Pdf17).
- **Encrypted**: Boolean indicating if the document is encrypted.
- **Zoom**: Zoom factor for the viewer.

#### Methods
- **Decrypt()**: Decrypts the encrypted document.
- **SetSecurity(password, permissions)**: Sets security for the document with the specified password and permissions.

#### Events
- **PageLoaded**: Triggered when a page is loaded.

## Code Examples

### C# Example
```csharp
using Syncfusion.Pdf;
using System.IO;

// Load a PDF document
PdfDocument doc = new PdfDocument("input.pdf");

// Check if the document is encrypted
if (doc.Encrypted)
{
    // Decrypt the document
    doc.Decrypt("password");
}

// Enable zoom feature in the viewer
PdfViewer viewer = new PdfViewer();
viewer.Zoom = 1.5;

// Save the document
doc.Save("output.pdf");
doc.Close();
```

### VB Example
```vb
Imports Syncfusion.Pdf
Imports System.IO

' Load a PDF document
Dim doc As New PdfDocument("input.pdf")

' Check if the document is encrypted
If doc.Encrypted Then
    ' Decrypt the document
    doc.Decrypt("password")
End If

' Enable zoom feature in the viewer
Dim viewer As New PdfViewer()
viewer.Zoom = 1.5

' Save the document
doc.Save("output.pdf")
doc.Close()
```

<!-- tags: [Essential PDF Viewer, WinForms, PDF, Compression Filters, Interactive Features] keywords: [RGB, CMYK, Gray, ICC, Indexed, DCTDecode, CCITTFaxDecode, FlateDecode] -->
```