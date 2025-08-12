# Introduction to SQL JOIN

A **JOIN** in SQL is used to combine rows from two or more tables based on a related column between them. The primary reason for using joins is to retrieve data that is distributed across multiple tables in a relational database.

## Why Use JOINs?

* Databases often store related information in separate tables for normalization and organization.
* JOINs allow you to query and analyze data in a way that reconstructs these relationships.

## Common Types of SQL JOINs

## 1. INNER JOIN

* Returns rows where there is a match in both tables.
* Only the records with matching values in both tables are included.

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span></span><span class="token token operator">*</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> table1
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">INNER</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> table2
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">ON</span><span> table1</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">column</span><span></span><span class="token token operator">=</span><span> table2</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">column</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

## 2. LEFT JOIN (or LEFT OUTER JOIN)

* Returns all records from the left table, and the matched records from the right table.
* If there is no match, NULL values are returned for columns from the right table.

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span></span><span class="token token operator">*</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> table1
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">LEFT</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> table2
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">ON</span><span> table1</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">column</span><span></span><span class="token token operator">=</span><span> table2</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">column</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

## 3. RIGHT JOIN (or RIGHT OUTER JOIN)

* Returns all records from the right table, and the matched records from the left table.
* If there is no match, NULL values are returned for columns from the left table.

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span></span><span class="token token operator">*</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> table1
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">RIGHT</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> table2
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">ON</span><span> table1</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">column</span><span></span><span class="token token operator">=</span><span> table2</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">column</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

## 4. FULL JOIN (or FULL OUTER JOIN)

* Returns records when there is a match in one of the tables.
* All records from both tables are returned, with NULL values where the join condition is not met.

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span></span><span class="token token operator">*</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> table1
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FULL</span><span></span><span class="token token" data-darkreader-inline-color="">OUTER</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> table2
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">ON</span><span> table1</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">column</span><span></span><span class="token token operator">=</span><span> table2</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">column</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

## 5. CROSS JOIN

* Returns the Cartesian product of both tables (every row of table1 paired with every row of table2).
* Does not require a join condition.

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span></span><span class="token token operator">*</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> table1
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">CROSS</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> table2</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

## 6. SELF JOIN

* A table joined with itself to compare rows within the same table.

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span> a</span><span class="token token punctuation">.</span><span class="token token operator">*</span><span class="token token punctuation">,</span><span> b</span><span class="token token punctuation">.</span><span class="token token operator">*</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> table1 a
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> table1 b
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">ON</span><span> a</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">column</span><span></span><span class="token token operator">=</span><span> b</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">column</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

---

## Summary Table

| JOIN Type       | Returns                                                      |
| --------------- | ------------------------------------------------------------ |
| INNER JOIN      | Matching rows from both tables                               |
| LEFT JOIN       | All rows from left table, matching from right (NULL if none) |
| RIGHT JOIN      | All rows from right table, matching from left (NULL if none) |
| FULL OUTER JOIN | All rows from both tables (NULL where no match)              |
| CROSS JOIN      | Cartesian product (all combinations)                         |
| SELF JOIN       | Table joined to itself                                       |

# Data table setup

-- Customers Table

```
CREATE TABLE Customers (    CustomerID INT PRIMARY KEY,    CustomerName VARCHAR(100),    Country VARCHAR(50));
```

-- Orders Table

```
CREATE TABLE Orders (    OrderID INT PRIMARY KEY,    OrderDate DATE,    CustomerID INT,    ProductID INT,    Quantity INT,    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID));
```

-- Products Table

```
CREATE TABLE Products (    ProductID INT PRIMARY KEY,    ProductName VARCHAR(100),    Price DECIMAL(10,2));
```

-- Insert Customers

INSERT INTO Customers (CustomerID, CustomerName, Country) VALUES

(1, 'John Smith', 'USA'),

(2, 'Emma Johnson', 'UK'),

(3, 'Raj Kumar', 'India'),

(4, 'Sophia Lee', 'Canada'),

(5, 'Carlos Santos', 'Brazil');

-- Insert Products

INSERT INTO Products (ProductID, ProductName, Price) VALUES

(101, 'Laptop', 800.00),

(102, 'Mouse', 20.00),

(103, 'Keyboard', 35.00),

(104, 'Monitor', 150.00),

(105, 'USB Cable', 5.00);

-- Insert Orders

INSERT INTO Orders (OrderID, OrderDate, CustomerID, ProductID, Quantity) VALUES

(1001, '2025-08-01', 1, 101, 1),

(1002, '2025-08-02', 2, 102, 2),

(1003, '2025-08-03', 1, 103, 1),

(1004, '2025-08-04', 3, 104, 1),

(1005, '2025-08-05', 2, 105, 5),

(1006, '2025-08-06', 4, 101, 1),

(1007, '2025-08-07', 5, 103, 2);

## **1. INNER JOIN example**

Only returns rows where there’s a match in **all** tables.

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span> Customers</span><span class="token token punctuation">.</span><span>CustomerName</span><span class="token token punctuation">,</span><span> Products</span><span class="token token punctuation">.</span><span>ProductName</span><span class="token token punctuation">,</span><span> Orders</span><span class="token token punctuation">.</span><span>Quantity
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> Orders
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">INNER</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> Customers </span><span class="token token" data-darkreader-inline-color="">ON</span><span> Orders</span><span class="token token punctuation">.</span><span>CustomerID </span><span class="token token operator">=</span><span> Customers</span><span class="token token punctuation">.</span><span>CustomerID
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">INNER</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> Products </span><span class="token token" data-darkreader-inline-color="">ON</span><span> Orders</span><span class="token token punctuation">.</span><span>ProductID </span><span class="token token operator">=</span><span> Products</span><span class="token token punctuation">.</span><span>ProductID</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

**Result (example output):**

| CustomerName  | ProductName | Quantity |
| ------------- | ----------- | -------- |
| John Smith    | Laptop      | 1        |
| Emma Johnson  | Mouse       | 2        |
| John Smith    | Keyboard    | 1        |
| Raj Kumar     | Monitor     | 1        |
| Emma Johnson  | USB Cable   | 5        |
| Sophia Lee    | Laptop      | 1        |
| Carlos Santos | Keyboard    | 2        |

🔹 Here, **every row** has a valid customer **and** a valid product.

Orders with missing customer/product don’t appear at all.

---

## **2. LEFT JOIN example**

Shows  **all Customers** , even if they haven’t placed any orders. Missing order/product data becomes `NULL`.

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span> Customers</span><span class="token token punctuation">.</span><span>CustomerName</span><span class="token token punctuation">,</span><span> Products</span><span class="token token punctuation">.</span><span>ProductName</span><span class="token token punctuation">,</span><span> Orders</span><span class="token token punctuation">.</span><span>Quantity
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> Customers
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">LEFT</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> Orders </span><span class="token token" data-darkreader-inline-color="">ON</span><span> Customers</span><span class="token token punctuation">.</span><span>CustomerID </span><span class="token token operator">=</span><span> Orders</span><span class="token token punctuation">.</span><span>CustomerID
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">LEFT</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> Products </span><span class="token token" data-darkreader-inline-color="">ON</span><span> Orders</span><span class="token token punctuation">.</span><span>ProductID </span><span class="token token operator">=</span><span> Products</span><span class="token token punctuation">.</span><span>ProductID</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

**Result (example output):**

| CustomerName           | ProductName    | Quantity       |
| ---------------------- | -------------- | -------------- |
| John Smith             | Laptop         | 1              |
| John Smith             | Keyboard       | 1              |
| Emma Johnson           | Mouse          | 2              |
| Emma Johnson           | USB Cable      | 5              |
| Raj Kumar              | Monitor        | 1              |
| Sophia Lee             | Laptop         | 1              |
| Carlos Santos          | Keyboard       | 2              |
| **New Customer** | **NULL** | **NULL** |

🔹 Notice the last row – this is a  **customer with no orders** .

They show up because `LEFT JOIN` keeps  *all records from the left table (`Customers`)* , and uses `NULL` for missing matches.

---

## **Key Difference**

* **INNER JOIN** ➡ Only where matches exist in both tables.
* **LEFT JOIN** ➡ All from left table + matches from right table (NULL if no match).

---

# What Is a RIGHT JOIN in SQL?

A **RIGHT JOIN** (also called RIGHT OUTER JOIN) is a SQL operation that retrieves all records from the right table and only the matching records from the left table. If there is no match in the left table, the result will include NULL values for those columns, but the row from the right table will still appear.

## RIGHT JOIN Syntax

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span> column_list
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> left_table
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">RIGHT</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> right_table
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">ON</span><span> left_table</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">key</span><span></span><span class="token token operator">=</span><span> right_table</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">key</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

* `left_table`: The first table listed in the query.
* `right_table`: The second table listed, whose records will all show up in the result.

## When to Use RIGHT JOIN

* When you want to make sure you return every row from the right table, even if there are no matches in the left table.
* To identify records in the right table that have no relationships in the left table.
* For handling optional relationships and ensuring completeness of data from the right table.[w3schools**+2**](https://www.w3schools.com/sql/sql_join_right.asp)

## Example Based on Our Customers, Orders, Products Scenario

Let's say we want to list every product, showing details of any orders placed for them (including products with no orders):

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span> Products</span><span class="token token punctuation">.</span><span>ProductName</span><span class="token token punctuation">,</span><span> Orders</span><span class="token token punctuation">.</span><span>OrderID</span><span class="token token punctuation">,</span><span> Orders</span><span class="token token punctuation">.</span><span>Quantity
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> Orders
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">RIGHT</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> Products </span><span class="token token" data-darkreader-inline-color="">ON</span><span> Orders</span><span class="token token punctuation">.</span><span>ProductID </span><span class="token token operator">=</span><span> Products</span><span class="token token punctuation">.</span><span>ProductID</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

* This query will list all products from the `Products` table.
* If a product has been ordered, you see `OrderID` and `Quantity` from the `Orders` table.
* If a product has  **never been ordered** , you’ll still see the product’s name, but `OrderID` and `Quantity` will be `NULL`.

## Sample Output

| ProductName | OrderID | Quantity |
| ----------- | ------- | -------- |
| Laptop      | 1001    | 1        |
| Mouse       | 1002    | 2        |
| Keyboard    | 1003    | 1        |
| Monitor     | 1004    | 1        |
| USB Cable   | 1005    | 5        |
| NewProduct  | NULL    | NULL     |

* *NewProduct* appears even though it has no order, with `NULL` for order fields.

## Visual Explanation

RIGHT JOIN is essentially the mirror opposite of LEFT JOIN:

* LEFT JOIN: All rows from left table, plus matches from right.
* RIGHT JOIN: All rows from right table, plus matches from left.


## FULL JOIN (FULL OUTER JOIN)

* A **FULL JOIN** returns all records when there is a match in either the left or right table.
* It combines the results of both LEFT JOIN and RIGHT JOIN.
* If a row in one table does not have a match in the other, the result includes the row with `NULL` in columns of the table without the match.

**Syntax:**

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span></span><span class="token token" data-darkreader-inline-color="">columns</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> table1
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FULL</span><span></span><span class="token token" data-darkreader-inline-color="">OUTER</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> table2
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">ON</span><span> table1</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">key</span><span></span><span class="token token operator">=</span><span> table2</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">key</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

**Use case:** When you want to keep all data from both tables and include unmatched rows from either side.

**Example:** List all customers and all orders, showing matched records and also customers without orders and orders without customers.

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span> Customers</span><span class="token token punctuation">.</span><span>CustomerName</span><span class="token token punctuation">,</span><span> Orders</span><span class="token token punctuation">.</span><span>OrderID
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> Customers
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FULL</span><span></span><span class="token token" data-darkreader-inline-color="">OUTER</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> Orders </span><span class="token token" data-darkreader-inline-color="">ON</span><span> Customers</span><span class="token token punctuation">.</span><span>CustomerID </span><span class="token token operator">=</span><span> Orders</span><span class="token token punctuation">.</span><span>CustomerID</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

---

## CROSS JOIN

* A **CROSS JOIN** returns the Cartesian product of the two tables: every row from the first table combined with every row from the second table.
* It does not require a join condition.
* Result size is the product of row counts of the two tables, so it can grow very large.

**Syntax:**

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span></span><span class="token token" data-darkreader-inline-color="">columns</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> table1
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">CROSS</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> table2</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

**Use case:** When you want to combine all possibilities of rows between two tables without filtering or matching.

**Example:** If you want to see every possible customer-product combination, regardless of whether an order was placed.

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span> Customers</span><span class="token token punctuation">.</span><span>CustomerName</span><span class="token token punctuation">,</span><span> Products</span><span class="token token punctuation">.</span><span>ProductName
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> Customers
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">CROSS</span><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> Products</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

---

## SELF JOIN

* A **SELF JOIN** is when a table is joined with itself.
* Useful to compare rows within the same table or find relationships like hierarchical data.
* Requires table aliasing to distinguish the two instances of the same table.

**Syntax:**

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span> a</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">column</span><span class="token token punctuation">,</span><span> b</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">column</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span></span><span class="token token" data-darkreader-inline-color="">table</span><span> a
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span></span><span class="token token" data-darkreader-inline-color="">table</span><span> b </span><span class="token token" data-darkreader-inline-color="">ON</span><span> a</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">key</span><span></span><span class="token token operator">=</span><span> b</span><span class="token token punctuation">.</span><span class="token token" data-darkreader-inline-color="">key</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

**Use case:** When you want to compare data within the same table, e.g., find employees and their managers in the same Employees table.

**Example:** Suppose you want to find customers who share the same country:

<pre class="not-prose w-full rounded font-mono text-sm font-extralight"><div class="codeWrapper text-light selection:text-super selection:bg-super/10 bg-offset my-md relative flex flex-col rounded font-mono text-sm font-normal"><div class="translate-y-xs -translate-x-xs bottom-xl mb-xl sticky top-0 flex h-0 items-start justify-end"><button data-testid="copy-code-button" type="button" class="focus-visible:bg-offsetPlus hover:bg-offsetPlus text-quiet  hover:text-foreground dark:hover:bg-offsetPlus font-sans focus:outline-none outline-none outline-transparent transition duration-300 ease-out font-sans  select-none items-center relative group/button  justify-center text-center items-center rounded-full cursor-pointer active:scale-[0.97] active:duration-150 active:ease-outExpo origin-center whitespace-nowrap inline-flex text-sm h-8 aspect-square"><div class="flex items-center min-w-0 font-medium gap-1.5 justify-center"><div class="flex shrink-0 items-center justify-center size-4"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7999999999999998" stroke-linecap="round" stroke-linejoin="round" class="tabler-icon tabler-icon-copy " data-darkreader-inline-stroke=""><path d="M7 7m0 2.667a2.667 2.667 0 0 1 2.667 -2.667h8.666a2.667 2.667 0 0 1 2.667 2.667v8.666a2.667 2.667 0 0 1 -2.667 2.667h-8.666a2.667 2.667 0 0 1 -2.667 -2.667z"></path><path d="M4.012 16.737a2.005 2.005 0 0 1 -1.012 -1.737v-10c0 -1.1 .9 -2 2 -2h10c.75 0 1.158 .385 1.5 1"></path></svg></div></div></button></div><div class="-mt-xl"><div><div data-testid="code-language-indicator" class="text-quiet bg-offsetPlus py-xs px-sm inline-block rounded-br rounded-tl-[3px] font-thin">sql</div></div><div class="pr-lg"><span data-darkreader-inline-bgimage="" data-darkreader-inline-bgcolor="" data-darkreader-inline-color=""><code><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span class="token token" data-darkreader-inline-color="">SELECT</span><span> a</span><span class="token token punctuation">.</span><span>CustomerName </span><span class="token token" data-darkreader-inline-color="">AS</span><span> Customer1</span><span class="token token punctuation">,</span><span> b</span><span class="token token punctuation">.</span><span>CustomerName </span><span class="token token" data-darkreader-inline-color="">AS</span><span> Customer2</span><span class="token token punctuation">,</span><span> a</span><span class="token token punctuation">.</span><span>Country
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">FROM</span><span> Customers a
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""><span></span><span class="token token" data-darkreader-inline-color="">JOIN</span><span> Customers b </span><span class="token token" data-darkreader-inline-color="">ON</span><span> a</span><span class="token token punctuation">.</span><span>Country </span><span class="token token operator">=</span><span> b</span><span class="token token punctuation">.</span><span>Country </span><span class="token token operator">AND</span><span> a</span><span class="token token punctuation">.</span><span>CustomerID </span><span class="token token operator"><></span><span> b</span><span class="token token punctuation">.</span><span>CustomerID</span><span class="token token punctuation">;</span><span>
</span></span><span data-darkreader-inline-color="" data-darkreader-inline-bgcolor=""></span></code></span></div></div></div></pre>

This shows pairs of customers from the same country.

---

Let me know if you want sample tables and data to try out these JOIN types or practical queries for them!
