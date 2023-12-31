#### GlobalExceptionHandler
```java
@ControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(NotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFoundException(NotFoundException ex) {
	     ErrorResponse errorResponse = new ErrorResponse(
									     HttpStatus.NOT_FOUND.value(), ex.getMessage());
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(errorResponse);
    }   
 }
```

#### NotFoundException
```java
public class NotFoundException extends RuntimeException {
    private final int errorCode;
    public NotFoundException(String message) {
        super(message);
        this.errorCode = 404;
    }
    
    public int getErrorCode() {
        return errorCode;
    }
}
```

#### ErrorResponse
```java
public class ErrorResponse {

    private int status;
    private String message;

    public ErrorResponse(int status, String message) {
        this.status = status;
        this.message = message;
    }

    public ErrorResponse(String message) {
        this.message = message;
    }

    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
}
```