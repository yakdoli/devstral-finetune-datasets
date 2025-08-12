```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_323.jpeg
document_name: DocIo
page_number: 323
page_id: DocIo#page_323
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:48:43Z
fidelity: lossless
-->

### Essential DocIO

```vb
HttpContentDisposition.InBrowser())
End Sub
Public Shared Function ReadFully(ByVal stream As Stream, ByVal initialLength As Integer) As Byte()
    ' If we've been passed an unhelpful initial length, just
    ' use 32K.
    If initialLength < 1 Then
        initialLength = 32768
    End If

    Dim buffer As Byte() = New Byte(initialLength - 1) {}
    Dim read As Integer = 0

    Dim chunk As Integer

    chunk = stream.Read(buffer, read, buffer.Length - read)
    Do While (chunk > 0)
        read += chunk

        ' If we've reached the end of our buffer, check to see if there's
        ' any more information
        If read = buffer.Length Then
            Dim nextByte As Integer = stream.ReadByte()

            ' End of stream? If so, we're done
            If nextByte = -1 Then
                Return buffer
            End If

            ' Nope. Resize the buffer, put in the byte we've just
            ' read, and continue
            Dim newBuffer As Byte() = New Byte(buffer.Length * 2 - 1) {}
            Array.Copy(buffer, newBuffer, buffer.Length)
            newBuffer(read) = CByte(nextByte)
            buffer = newBuffer
            read += 1
        End If
        chunk = stream.Read(buffer, read, buffer.Length - read)
    Loop

    ' Buffer is now too big. Shrink it.
    Dim ret As Byte() = New Byte(read - 1) {}
    Array.Copy(buffer, ret, read)
    Return ret
End Function
```

## Overview
- Comprehensive function to read a stream fully into a byte array.
- Handles dynamic resizing of the buffer to accommodate variable stream sizes.
- Ensures efficient memory usage by shrinking the buffer to fit the actual data read.

## Content
This section details the `ReadFully` function, which is designed to read an entire stream into a byte array. The function dynamically manages the size of the buffer to handle streams of any length, ensuring optimal memory usage and efficiency.

### Implementation Details
- **Input Parameters**:
  - `stream`: The input stream to read.
  - `initialLength`: The initial buffer size. If provided as an unhelpful length (e.g., less than 1), the function defaults to a buffer size of 32KB.
  
- **Process**:
  1. **Buffer Initialization**: 
     - The buffer is initialized with a size based on the `initialLength`. If `initialLength` is unhelpful, it is set to 32KB.
  
  2. **Reading Data**:
     - The function reads data from the stream into the buffer until the end of the stream is reached.
     - If the buffer becomes full, it is resized to accommodate additional data.
  
  3. **Buffer Resizing**:
     - When the buffer is full, but more data is available, the buffer is doubled in size.
     - The existing data is copied to the new buffer, and the new byte is added.
  
  4. **Final Shrinking**:
     - After all data has been read, the final buffer is shrunk to match the exact size of the data read, ensuring no unnecessary memory allocation.

### Example Usage

The `ReadFully` function can be utilized in scenarios where a complete stream representation as a byte array is required, such as file downloads or data processing tasks.

### Code Example

```vb
Dim stream As Stream = ' Your Stream Object
Dim bytes As Byte() = ReadFully(stream, 1024)
```

## API Reference
- **Namespace**: `Syncfusion.DocIO`
- **Function Definition**:
  ```vb
  Public Shared Function ReadFully(ByVal stream As Stream, ByVal initialLength As Integer) As Byte()
  ```
- **Parameters**:
  - `stream`: The `Stream` object to read data from.
  - `initialLength`: The initial size of the buffer. Defaults to 32KB if provided as unhelpful.
- **Return Value**: A `Byte()` array containing the complete data read from the stream.

## Cross References
- For further information on stream handling and buffer management, refer to [Syncfusion Winforms Stream Operations Guide](https://www.syncfusion.com/documentation)

<!-- tags: [DocIO, stream handling, buffer management, byte arrays] keywords: [ReadFully, dynamic resizing, buffer, stream, memory management] -->
```