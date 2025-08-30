## 📑 **Topics**

1. Closures
2. Callbacks
3. Event Loop
4. Hoisting
5. Function Declarations vs Definitions
6. Promises & `Promise.all()`
7. Higher-Order Functions
8. Call Stack & Call Queue
9. Callback Hell
10. `let`, `var`, `const`
11. Array Methods
12. Destructuring
13. `map()` vs `reduce()`
14. Sync vs. Async
15. Spread Operator
16. Debouncing
17. Currying
18. Web APIs
19. First-Class Functions
20. How JavaScript Works

---

### **1. What are Closures?**

“A closure is when an inner function remembers variables from its outer function even after the outer function has finished executing.”

**Example:**

```jsx
function outer() {
  let x = 10;
  return function inner() {
    console.log(x);
  };
}
const fn = outer();
fn(); // 10

```

**Diagram:**

```
outer()
 └── inner() → remembers x=10

```

---

### **2. What are Callbacks?**

“A callback is a function passed as an argument to another function, executed after the parent function finishes.”

**Example:**

```jsx
function greet(name, cb) {
  console.log("Hello, " + name);
  cb();
}
greet("Alice", () => console.log("Callback executed"));

```

---

### **3. Explain Event Loop.**

“JS is single-threaded. The Event Loop manages async tasks by moving callbacks from Web APIs to the Call Stack when it’s free.”

**Diagram:**

```
Call Stack → Web APIs → Callback Queue → Event Loop → Call Stack

```

**Example:**

```jsx
console.log("Start");
setTimeout(() => console.log("Timeout"), 0);
console.log("End");
// Output: Start → End → Timeout

```

---

### **4. What is Hoisting?**

“Declarations are moved to the top before execution. Variables declared with `var` get `undefined`, while `let/const` stay in the Temporal Dead Zone.”

**Example:**

```jsx
console.log(a); // undefined
var a = 5;
```

---

### **5. Function Declarations vs Definitions**

- **Declaration:** Tells JS a function exists.
- **Definition:** Provides the body (logic).

**Example:**

```jsx
// Declaration (rare in JS alone)
function greet();

// Definition
function greet() { console.log("Hi"); }
```

---

### **6. What is a Promise? And `Promise.all()`?**

“A Promise represents a future value with states: pending, fulfilled, or rejected.”

“`Promise.all()` runs multiple promises in parallel, resolving when all succeed or rejecting if any fails.”

**Example:**

```jsx
Promise.all([
  fetch("/api/1"),
  fetch("/api/2")
])
.then(res => console.log("All done"))
.catch(err => console.log("Error", err));

```

---

### **7. Higher-Order Functions (HOFs)**

“HOFs are functions that take or return another function.”

**Example:**

```jsx
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2); // [2, 4, 6]

```

---

### **8. Call Stack & Call Queue**

“The Call Stack executes sync code (LIFO). Async tasks go to Callback Queue, waiting for Event Loop to push them into stack.”

---

### **9. What is Callback Hell?**

“Callback Hell is deeply nested callbacks, making code unreadable. We solve it using Promises or async/await.”

---

### **10. Difference Between `let`, `var`, and `const`**

- `var`: function-scoped, hoisted, re-declarable.
- `let`: block-scoped, not re-declarable.
- `const`: block-scoped, cannot be reassigned.

---

### **11. Array Methods (`map`, `filter`, `reduce`)**

- `map()`: transforms items.
- `filter()`: selects items.
- `reduce()`: accumulates to single value.

---

### **12. Destructuring**

“Destructuring extracts values from arrays or objects into variables.”

**Example:**

```jsx
const [a, b] = [1, 2];
const {name} = {name: "Ayush"};

```

---

### **13. `map()` vs `reduce()`**

- `map`: returns new array.
- `reduce`: returns single value.

---

### **14. Sync vs Async**

“Sync runs line by line. Async uses callbacks, promises, or async/await without blocking.”

- **Synchronous (Sync):** Code runs line by line. Next line waits for the previous one.
- **Asynchronous (Async):** Code doesn’t block execution. It uses **callbacks, promises, or async/await** to run in the background.

📌 Example:

```jsx
// Synchronous
console.log("A");
console.log("B");
console.log("C");
// Output: A B C

// Asynchronous
console.log("1");
setTimeout(() => console.log("2"), 1000);
console.log("3");
// Output: 1 3 2
```

> Async uses Event Loop + Callback Queue/Microtask Queue to run code later without blocking.
> 

---

### **15. Spread Operator**

“`...` expands arrays or objects.”

---

### **16. Debouncing**

“Debouncing delays function execution until user stops triggering it (useful for search inputs).”

```jsx
function debounce(fn, delay) {
  let timer;
  return function(...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

function searchQuery(query) {
  console.log("Fetching results for:", query);
}

const debouncedSearch = debounce(searchQuery, 500);

// Simulating typing
debouncedSearch("Ja");
debouncedSearch("Jav");
debouncedSearch("Java"); // ✅ Only this call executes after 500ms
```

---

### **17. Currying**

“Currying converts a function with multiple arguments into a sequence of functions each taking one argument.”

```jsx
// Normal function
function add(a, b, c) {
  return a + b + c;
}
console.log(add(1, 2, 3)); // 6

// Curried function
function curryAdd(a) {
  return function(b) {
    return function(c) {
      return a + b + c;
    };
  };
}

console.log(curryAdd(1)(2)(3)); // 6
```

---

### **18. Web APIs**

Web APIs are **features provided by the browser (or environment like Node.js)** that JavaScript alone doesn’t have. They allow JS to interact with the outside world.

👉 *Examples:*

`fetch`, `localStorage`, `setTimeout`, `DOM APIs`.

---

### **19. First-Class Functions**

“In JS, functions are first-class citizens — they can be stored, passed, and returned like variables.”

---

### **20. How JavaScript Works (Execution Flow)**

1. **Parser → Compiler → Execution**
2. **Code runs via**:
    - Call Stack
    - Global Execution Context
    - Callback Queue
    - Microtask Queue (Promises)
    - Event Loop
    - Web APIs
        
        ![image.png](attachment:c067a72f-f4c2-45d9-a0dc-14a41cd6a8aa:image.png)
        

### Ace Your Next JavaScript Interview!

Like this guide? Share it with a developer friend who has interviews coming up! 👩‍💻👨‍💻