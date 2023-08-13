
```java
public class NativeMethodExample {
    // Load the shared object file
    static {
        System.loadLibrary("nativeLibrary");
    }

    // Declare the native method
    private native void nativeMethod();

    public static void main(String[] args) {
        NativeMethodExample example = new NativeMethodExample();
        example.nativeMethod();
    }
}
```

Compile the Java code:
```shell
javac NativeMethodExample.java
```

Generate the C/C++ header file:

```shell
javac -h . NativeMethodExample.java
```

This will generate a `NativeMethodExample.h` file.

Implement the native method in C/C++:

```cpp
#include <jni.h>
#include "NativeMethodExample.h"
#include <iostream>

JNIEXPORT void JNICALL Java_NativeMethodExample_nativeMethod(JNIEnv* env, jobject thisObject) {
    std::cout << "Hello from C++ !!" << std::endl;
}

```

### Compiling and Linking

Linux version 
```shell
> g++ -c -fPIC -I${JAVA_HOME}/include -I${JAVA_HOME}/include/linux NativeMethodExample.cpp -o NativeMethodExample.o
```

windows  version 
```shell
g++ -c -I%JAVA_HOME%\include -I%JAVA_HOME%\include\win32 com_baeldung_jni_HelloWorldJNI.cpp -o com_baeldung_jni_HelloWorldJNI.o
```

The G++ linker then links the C++ object files into our bridged library.

Linux  version:
```bash
g++ -shared -fPIC -o libnativeLibrary.so NativeMethodExample.o -lc
```

windows version:
```shell
g++ -shared -o native.dll com_baeldung_jni_HelloWorldJNI.o -Wl,--add-stdcall-alias
```
run  program from the command line
```bash
java -cp . -Djava.library.path=/NATIVE_SHARED_LIB_FOLDER NativeMethodExample
```