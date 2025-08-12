```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_322.jpeg
document_name: DocIo
page_number: 322
page_id: DocIo#page_322
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:48:25Z
fidelity: lossless
-->

# Essential DocIO

```csharp
// any more information
if (read == buffer.Length)
{
    int nextByte = stream.ReadByte();
    // End of stream? If so, we're done
    if (nextByte == -1)
    {
        return buffer;
    }
    // Nope. Resize the buffer, put in the byte we've just
    // read, and continue
    byte[] newBuffer = new byte[buffer.Length * 2];
    Array.Copy(buffer, newBuffer, buffer.Length);
    newBuffer[read] = (byte)nextByte;
    buffer = newBuffer;
    read++;
}
}
// Buffer is now too big. Shrink it.
byte[] ret = new byte[read];
Array.Copy(buffer, ret, read);
return ret;
}
```

## VB.NET

```vb
Protected Sub Button1_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles Button1.Click
    Dim request As HttpWebRequest = CType(WebRequest.Create("http://www.nfpa.org/assets/files//PDF/Forms/EvacuationGuide.doc"), HttpWebRequest)
    Dim response1 As HttpWebResponse = CType(request.GetResponse(), HttpWebResponse)
    Dim stream As Stream = response1.GetResponseStream()
    Dim buffer As Byte() = ReadFully(stream, 32768)
    Dim ms As MemoryStream = New MemoryStream()
    ms.Write(buffer, 0, buffer.Length)
    ms.Seek(0, SeekOrigin.Begin)
    stream.Close()
    
    ' Creating a new document.
    Dim doc As WordDocument = New WordDocument()
    ' Open the template document from the filestream.
    doc.Open(ms, FormatType.Doc)
    doc.Save("Sample.doc", FormatType.Doc, response)
End Sub
```

## API Reference

### Methods
- `ReadFully(stream, bufferLength)`
- `Open(memoryStream, formatType)`
- `Save(filename, formatType, options)`

### Properties
- `WordDocument`

## Code Examples

### C#

```csharp
// Not applicable in this context, as VB.NET example is provided.
```

### VB.NET

```vb
Protected Sub Button1_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles Button1.Click
    Dim request As HttpWebRequest = CType(WebRequest.Create("http://www.nfpa.org/assets/files//PDF/Forms/EvacuationGuide.doc"), HttpWebRequest)
    Dim response1 As HttpWebResponse = CType(request.GetResponse(), HttpWebResponse)
    Dim stream As Stream = response1.GetResponseStream()
    Dim buffer As Byte() = ReadFully(stream, 32768)
    Dim ms As MemoryStream = New MemoryStream()
    ms.Write(buffer, 0, buffer.Length)
    ms.Seek(0, SeekOrigin.Begin)
    stream.Close()
    
    ' Creating a new document.
    Dim doc As WordDocument = New WordDocument()
    ' Open the template document from the filestream.
    doc.Open(ms, FormatType.Doc)
    doc.Save("Sample.doc", FormatType.Doc, response)
End Sub
```

<!-- tags: [DocIo, Syncfusion Winforms, Essential DocIO, API Reference, VB.NET, C#] keywords: [httprequest, httpwebresponse, worddocument, memorystream, readfully, save] -->
```