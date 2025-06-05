---
tags:
  - numpy
  - python
  - linear_algebra
  - matrix_operations
  - concept
  - example
aliases:
  - NumPy Matrix Math Examples
related:
  - "[[NumPy_ndarray]]"
  - "[[NumPy_Transpose]]"
  - "[[Dot_Product]]" # General math concept
  - "[[np.dot]]"
  - "[[Matrix_Multiplication_NumPy]]" # Placeholder for `@` operator
  - "[[NumPy_linalg_norm]]"
  - "[[NumPy_Softmax]]"
  - "[[NumPy_Dimension_Shape_Axis]]"
  - "[[NumPy_Broadcasting]]"
worksheet: [WS_NumPy] # For the "Let a and b be two 2x2x2 ndarrays" questions
date_created: <% tp.file.creation_date("YYYY-MM-DD") %>
---
# NumPy Matrix & Vector Operations Examples (WS_NumPy Q&A)

This note addresses the NumPy worksheet question regarding operations on `ndarray`s, specifically focusing on `2x2x2` and `2x3x2` arrays.

## Scenario 1: `a` and `b` are two `2x2x2` ndarrays

Let's define example arrays:
```python
import numpy as np

a = np.arange(8).reshape((2, 2, 2))
# a = [[[0, 1],
#       [2, 3]],
#      [[4, 5],
#       [6, 7]]]

b = np.arange(8, 16).reshape((2, 2, 2))
# b = [[[ 8,  9],
#       [10, 11]],
#      [[12, 13],
#       [14, 15]]]
```

Shape of `a` and `b`: `(2, 2, 2)` - This means 2 "layers" (or "matrices"), each layer being a 2x2 matrix.

[list2tab]

-  "a @ b (Matrix Multiplication)"
	tabs: 2x2x2 Array Operations
	title: "a @ b (Matrix Multiplication)"
	content: |
	The `@` operator performs matrix multiplication. For N-D arrays (N > 2), it treats the **last two axes** as the matrices to be multiplied and **broadcasts** over the preceding axes.
	- `a` shape: `(2, 2, 2)`
	- `b` shape: `(2, 2, 2)`
	- The last two axes define 2x2 matrices. The first axis (size 2) is the "stack" of matrices.
	- The operation will perform element-wise matrix multiplication for each corresponding 2x2 matrix in the stack.
		```python
	      result_ab = a @ b
	      result_ab[0] = a[0] @ b[0]
	      result_ab[1] = a[1] @ b[1]
	            
		  a[0] = [[0, 1], [2, 3]]
	      b[0] = [[8, 9], [10, 11]]
	      a[0] @ b[0] = [[(0*8+1*10), (0*9+1*11)],
	                     [(2*8+3*10), (2*9+3*11)]]
	                  = [[10, 11],
	                     [46, 51]]
	            a[1] = [[4, 5], [6, 7]]
	      b[1] = [[12, 13], [14, 15]]
	      a[1] @ b[1] = [[(4*12+5*14), (4*13+5*15)],
	                     [(6*12+7*14), (6*13+7*15)]]
	                  = [[118, 127],
	                     [170, 183]]
	            # result_ab will have shape (2, 2, 2)
	      result_ab = [[[ 10,  11],
	                    [ 46,  51]],
	                   [[118, 127],
	                    [170, 183]]]
	      ```
      **Returns:** A new `ndarray` of shape `(2, 2, 2)` where each 2x2 slice is the matrix product of the corresponding 2x2 slices from `a` and `b`.
  - title: "a @ b[1] (Matrix-Matrix Product)"
    content: |
      - `a` shape: `(2, 2, 2)`
      - `b[1]` shape: `(2, 2)` (This selects the second 2x2 matrix from `b`)
      - NumPy will attempt to broadcast `b[1]` to match `a` for matrix multiplication.
      - `a` is a stack of two 2x2 matrices: `a[0]` and `a[1]`.
      - `b[1]` is a single 2x2 matrix.
      - The operation will perform `a[0] @ b[1]` and `a[1] @ b[1]`.
      ```python
      # result_ab1 = a @ b[1]
      # result_ab1[0] = a[0] @ b[1]
      # result_ab1[1] = a[1] @ b[1]
      #
      # b[1] = [[12, 13], [14, 15]]
      #
      # a[0] @ b[1] = [[(0*12+1*14), (0*13+1*15)],
      #                [(2*12+3*14), (2*13+3*15)]]
      #             = [[14, 15],
      #                [66, 71]]
      #
      # a[1] @ b[1] (calculated in previous tab)
      #             = [[118, 127],
      #                [170, 183]]
      #
      # result_ab1 will have shape (2, 2, 2)
      # result_ab1 = [[[ 14,  15],
      #                [ 66,  71]],
      #               [[118, 127],
      #                [170, 183]]]
      ```
      **Returns:** A new `ndarray` of shape `(2, 2, 2)`. `b[1]` is broadcast to be multiplied with each 2x2 matrix in `a`.
  - title: "a[1] @ b[1] (Matrix-Matrix Product)"
    content: |
      - `a[1]` shape: `(2, 2)`
      - `b[1]` shape: `(2, 2)`
      - This is a standard 2x2 matrix multiplication.
      ```python
      # result_a1b1 = a[1] @ b[1]
      # a[1] = [[4, 5], [6, 7]]
      # b[1] = [[12, 13], [14, 15]]
      # result_a1b1 (calculated in first tab as part of a @ b)
      #             = [[118, 127],
      #                [170, 183]]
      ```
      **Returns:** A new `ndarray` of shape `(2, 2)`.
  - title: "a.T (Transpose)"
    content: |
      - `a` shape: `(2, 2, 2)`
      - The `.T` attribute (or `np.transpose(a)`) reverses the order of axes by default.
      - Original axes: `(axis 0, axis 1, axis 2)`
      - Transposed axes: `(axis 2, axis 1, axis 0)`
      - So, if `a[i,j,k]` was an element, in `a.T` it will be at `a.T[k,j,i]`.
      - The shape will also be `(2, 2, 2)`.
      ```python
      # a = [[[0, 1], [2, 3]],
      #      [[4, 5], [6, 7]]]
      # a_T = a.T
      # a_T[0,0,0] = a[0,0,0] = 0
      # a_T[0,0,1] = a[1,0,0] = 4
      # a_T[0,1,0] = a[0,1,0] = 2
      # a_T[0,1,1] = a[1,1,0] = 6
      # a_T[1,0,0] = a[0,0,1] = 1
      # ...
      # a_T = [[[0, 4], [2, 6]],
      #        [[1, 5], [3, 7]]]
      ```
      **Returns:** A new `ndarray` (usually a view) of shape `(2, 2, 2)` with axes permuted.
  - title: "np.dot(a, b)"
    content: |
      For N-D arrays, `np.dot(a, b)` behaves differently from `@`.
      - If `a` is N-D and `b` is M-D, it's a sum product over the **last axis of `a`** and the **second-to-last axis of `b`**.
      - `a` shape: `(2, 2, 2)` (N=3)
      - `b` shape: `(2, 2, 2)` (M=3)
      - Last axis of `a` is axis 2 (size 2).
      - Second-to-last axis of `b` is axis 1 (size 2). These match, so product is possible.
      - Result shape will be `a.shape[:-1] + b.shape[:-2] + b.shape[-1:]`
        ` = ( 2, 2 ) + (2, ) + (2, ) = (2,2,2,2)` (This is more complex than often assumed)

      Let's simplify with a common interpretation for `np.dot` with higher dimensions: If `N=M` and last dim of `a` matches second-to-last of `b`, it's like a stack of dot products.
      More commonly, `np.dot` is used for vector dot products or matrix-vector / matrix-matrix products.
      **If `a` and `b` were 2D matrices, `np.dot(a,b)` is matrix multiplication.**

      Given the complexity and common use of `@` for matrix multiplication of stacks of matrices, `np.dot` with two 3D arrays is less intuitive and might produce a higher-dimensional array based on tensor dot product rules. It would sum over `a`'s last axis and `b`'s second-to-last axis.
      `result[i,j,k,l] = sum(a[i,j,:] * b[k,:,l])`
      Shape of result: `(2, 2, 2, 2)`
      **Returns:** A new `ndarray` of shape `(2, 2, 2, 2)`.
      > [!NOTE]
      > `np.dot` with arrays of `ndim > 2` can be confusing. `@` (`np.matmul`) is generally preferred for "stacks of matrices" multiplication. `np.tensordot` provides more explicit control over which axes are summed over.
  - title: "a[:, 0] @ b"
    content: |
      - `a[:, 0]` shape: `(2, 2)`. This selects the first "column slice" across the first dimension.
        `a[:, 0]` is `[[0, 1], [4, 5]]`
      - `b` shape: `(2, 2, 2)`
      - Here, `(2, 2) @ (2, 2, 2)` is attempted.
      - `b`'s last two dimensions are `(2,2)`. `a[:,0]`'s last two (and only) dimensions are `(2,2)`.
      - `a[:,0]` (a single 2x2 matrix) will be broadcast to multiply with each of the 2x2 matrices in `b`.
      ```python
      # let A_slice = a[:, 0]
      # result = A_slice @ b
      # result[0] = A_slice @ b[0]
      # result[1] = A_slice @ b[1]
      #
      # A_slice = [[0, 1], [4, 5]]
      # b[0] = [[8, 9], [10, 11]]
      # A_slice @ b[0] = [[10, 11], [82, 91]]
      #
      # b[1] = [[12, 13], [14, 15]]
      # A_slice @ b[1] = [[14, 15], [118, 127]]
      #
      # Result shape will be (2, 2, 2)
      ```
      **Returns:** A new `ndarray` of shape `(2, 2, 2)`.
  - title: "a @ b[:, 0, 0]"
    content: |
      - `a` shape: `(2, 2, 2)`
      - `b[:, 0, 0]` selects elements `b[0,0,0]` and `b[1,0,0]`. Shape: `(2,)`. This is a 1D vector.
        `b[:, 0, 0]` is `[8, 12]`
      - This is `(2, 2, 2) @ (2,)`. Matrix multiplication rules:
        - The last dimension of `a` (size 2) must match the second-to-last (or only, if 1D) dimension of the vector `b[:,0,0]` (size 2). They match.
        - The operation effectively multiplies each 2x2 matrix in `a` by the vector `b[:,0,0]`.
      ```python
      # let B_vec = b[:, 0, 0]  (which is [8, 12])
      # result = a @ B_vec
      # result[0] = a[0] @ B_vec
      # result[1] = a[1] @ B_vec
      #
      # a[0] = [[0, 1], [2, 3]]
      # B_vec = [8, 12]
      # a[0] @ B_vec = [(0*8+1*12), (2*8+3*12)] = [12, 52]
      #
      # a[1] = [[4, 5], [6, 7]]
      # a[1] @ B_vec = [(4*8+5*12), (6*8+7*12)] = [92, 132]
      #
      # Result shape will be (2, 2)
      # result = [[12, 52],
      #           [92, 132]]
      ```
      **Returns:** A new `ndarray` of shape `(2, 2)`.
  - title: "a - b[:, 0]"
    content: |
      - `a` shape: `(2, 2, 2)`
      - `b[:, 0]` shape: `( 2, 2 )`. This selects the first 2x2 matrix from each "layer" of `b`, effectively `[[b[0,0,0], b[0,0,1]], [b[1,0,0], b[1,0,1]]]`, which is `[[8,9], [12,13]]`. No, this is incorrect.
      - `b[:, 0]` selects the first row from *each* 2x2 matrix within `b`.
        `b[:, 0]` is `[[8, 9], [12, 13]]`. Shape is `(2, 2)`.
      - Operation: `(2, 2, 2) - (2, 2)`
      - For broadcasting, `b[:,0]` (shape `(2,2)`) is conceptually padded to `(1,2,2)`.
      - Comparing shapes `(2,2,2)` and `(1,2,2)`:
        - Trailing: `2` vs `2` (equal)
        - Middle: `2` vs `2` (equal)
        - Leading: `2` vs `1` (one is 1, compatible)
      - `b[:,0]` will be broadcast across the first dimension of `a`.
      ```python
      # let B_slice = b[:, 0]  which is [[ 8,  9], [12, 13]]
      # result = a - B_slice (broadcasted)
      # result[0] = a[0] - B_slice
      # result[1] = a[1] - B_slice
      #
      # a[0] = [[0, 1], [2, 3]]
      # result[0] = [[0-8, 1-9], [2-12, 3-13]] = [[-8, -8], [-10, -10]]
      #
      # a[1] = [[4, 5], [6, 7]]
      # result[1] = [[4-8, 5-9], [6-12, 7-13]] = [[-4, -4], [ -6,  -6]]
      #
      # Result shape will be (2, 2, 2)
      # result = [[[-8, -8], [-10, -10]],
      #           [[-4, -4], [ -6,  -6]]]
      ```
      **Returns:** A new `ndarray` of shape `(2, 2, 2)`
---

## Scenario 2: `a` and `b` are two `2x3x2` ndarrays

Let's define new example arrays:
```python
a_new = np.arange(12).reshape((2, 3, 2))
# a_new = [[[ 0,  1],
#           [ 2,  3],
#           [ 4,  5]],
#          [[ 6,  7],
#           [ 8,  9],
#           [10, 11]]]

b_new = np.arange(12, 24).reshape((2, 3, 2))
# b_new = [[[12, 13],
#           [14, 15],
#           [16, 17]],
#          [[18, 19],
#           [20, 21],
#           [22, 23]]]
```
Shape of `a_new` and `b_new`: `(2, 3, 2)` (2 layers, each layer is a 3x2 matrix)

### Which operations still work and "make sense"?

1.  **`a_new @ b_new`**:
    -   `a_new` last two axes: `(3, 2)`
    -   `b_new` last two axes: `(3, 2)`
    -   For matrix multiplication `M1 @ M2`, inner dimensions must match (`M1_cols == M2_rows`). Here, `2 != 3`.
    -   **Will FAIL.** `ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 3 is different from 2)`
    -   Does not "make sense" as a direct stack of matrix multiplications.

2.  **`a_new @ b_new[1]`**:
    -   `a_new` shape: `(2, 3, 2)`
    -   `b_new[1]` shape: `(3, 2)` (This is the second 3x2 matrix from `b_new`)
    -   Operation: `(2, 3, 2) @ (3, 2)`
    -   `a_new`'s "matrices" are `3x2`. `b_new[1]` is `3x2`.
    -   `a_new[0] @ b_new[1]` would be `(3,2) @ (3,2)` -> Fails.
    -   **Will FAIL.**
    -   Does not "make sense" as matrix multiplication.

3.  **`a_new[1] @ b_new[1]`**:
    -   `a_new[1]` shape: `(3, 2)`
    -   `b_new[1]` shape: `(3, 2)`
    -   Operation: `(3,2) @ (3,2)` -> Fails (inner dimensions `2 != 3`).
    -   **Will FAIL.**
    -   Does not "make sense" as matrix multiplication.

4.  **`a_new.T`**:
    -   `a_new` shape: `(2, 3, 2)`
    -   `a_new.T` shape: `(2, 3, 2)` (reverses axes `(2,1,0)` -> `(axis2_size, axis1_size, axis0_size)`)
    -   **Will WORK.**
    -   "Makes sense" as a permutation of axes.

5.  **`np.dot(a_new, b_new)`**:
    -   `a_new` shape: `(2, 3, 2)` (N=3)
    -   `b_new` shape: `(2, 3, 2)` (M=3)
    -   Last axis of `a_new` (size 2). Second-to-last axis of `b_new` (size 3). These do **not** match.
    -   **Will FAIL.** `ValueError: shapes (2,3,2) and (2,3,2) not aligned: 2 (dim 2) != 3 (dim 1)` (if interpreting as sum product over last of A and second-to-last of B)
    -   Does not "make sense" in the standard matrix multiplication sense due to incompatible dimensions for the typical dot product generalization.

6.  **`a_new[:, 0] @ b_new`**:
    -   `a_new[:, 0]` shape: `(2, 2)` (selects `[[0,1], [6,7]]`)
    -   `b_new` shape: `(2, 3, 2)`
    -   Operation: `(2,2) @ (2,3,2)`
    -   `a_new[:, 0]` is a `2x2` matrix. `b_new` is a stack of two `3x2` matrices.
    -   Cannot broadcast `a_new[:,0]` to perform matrix multiplication with `3x2` matrices. Inner dimensions `2` (from `a_new[:,0]`) and `3` (from `b_new` matrices) mismatch.
    -   **Will FAIL.**
    -   Does not "make sense" as direct matrix multiplication.

7.  **`a_new @ b_new[:, 0, 0]`**:
    -   `a_new` shape: `(2, 3, 2)`
    -   `b_new[:, 0, 0]` shape: `(2,)` (This is `[12, 18]`)
    -   Operation: `(2, 3, 2) @ (2,)`
    -   `a_new`'s "matrices" are `3x2`. Vector is `(2,)`.
    -   Last dim of `a_new` (size 2) matches dim of vector (size 2).
    -   This performs matrix-vector product for each 3x2 matrix in `a_new` with the vector `b_new[:,0,0]`.
    -   `result[i,j] = sum(a_new[i,j,:] * b_new[:,0,0])` -> This interpretation is wrong.
    -   Correct: `result[i,k] = sum(a_new[i,k,:] * b_new[:,0,0])` -> Not this either.
    -   It will be `a_new[0] @ b_new[:,0,0]` and `a_new[1] @ b_new[:,0,0]`.
        - `a_new[0]` (3x2) @ `vector` (2,) -> results in (3,).
        - `a_new[1]` (3x2) @ `vector` (2,) -> results in (3,).
    -   Result shape: `(2, 3)`
    -   **Will WORK.**
    -   "Makes sense" as applying matrix-vector product to each "matrix page" of `a_new`.

8.  **`a_new - b_new[:, 0]`**:
    -   `a_new` shape: `(2, 3, 2)`
    -   `b_new[:, 0]` shape: `(2, 2)` (This is `[[12,13], [18,19]]`)
    -   Operation: `(2, 3, 2) - (2, 2)`
    -   For broadcasting, `b_new[:,0]` (shape `(2,2)`) needs to be made compatible with the last two dimensions of `a_new` which are `(3,2)`. It cannot.
    -   `b_new[:,0]` is padded to `(1,2,2)`.
    -   Comparing `a_new(2,3,2)` with broadcasted `b_new[:,0](1,2,2)`:
        - Trailing: `2` vs `2` (OK)
        - Middle: `3` vs `2` (**FAIL** - not equal, neither is 1)
    -   **Will FAIL.** `ValueError: operands could not be broadcast together with shapes (2,3,2) (2,2)`
    -   Does not "make sense" due to incompatible shapes for element-wise subtraction after broadcasting.

### How would you fix these operations so they would work and "make sense"?

*(This requires assumptions about the *intended* operation if the direct one fails.)*

1.  **`a_new @ b_new`**:
    -   To make matrix multiplication work, the inner dimensions must match. We could transpose one of them on its last two axes.
    -   Option 1: `a_new @ b_new.transpose(0, 2, 1)` -> `(2,3,2) @ (2,2,3)`. Result shape `(2,3,3)`. This multiplies each `3x2` matrix in `a_new` with each `2x3` (transposed) matrix in `b_new`.
    -   Option 2: `a_new.transpose(0,2,1) @ b_new` -> `(2,2,3) @ (2,3,2)`. Result shape `(2,2,2)`.
    -   To make it like the `2x2x2` case (element-wise matrix product on "pages"), this operation is fundamentally not designed for `3x2 @ 3x2`. You'd need to select compatible sub-matrices or restructure.

2.  **`a_new @ b_new[1]`**:
    -   `a_new` (stack of `3x2` matrices), `b_new[1]` (a single `3x2` matrix).
    -   To multiply, `b_new[1]` needs to be `2xk`. So, `b_new[1].T` would be `(2,3)`.
    -   Then `a_new @ b_new[1].T` means `(2,3,2) @ (2,3)`. Each `3x2` matrix in `a_new` is multiplied by `b_new[1].T` (a `2x3` matrix). Result `(2,3,3)`.
    ```python
    # Fixed
    b_slice_transposed = b_new[1].T # Shape (2,3)
    result = a_new @ b_slice_transposed # Shape (2,3,3)
    ```

3.  **`a_new[1] @ b_new[1]`**:
    -   `a_new[1]` (3x2), `b_new[1]` (3x2).
    -   Fix: `a_new[1] @ b_new[1].T` -> `(3,2) @ (2,3)`. Result shape `(3,3)`.
    -   Or: `a_new[1].T @ b_new[1]` -> `(2,3) @ (3,2)`. Result shape `(2,2)`.
    ```python
    # Fixed option 1
    result1 = a_new[1] @ b_new[1].T
    # Fixed option 2
    result2 = a_new[1].T @ b_new[1]
    ```

4.  **`np.dot(a_new, b_new)`**:
    -   Failed due to last axis of `a_new` (size 2) not matching second-to-last of `b_new` (size 3).
    -   To make it work like sum product over specific axes, `np.tensordot` is better.
    -   If intended like `matmul` for stacks of matrices, one needs transposition:
        `np.dot(a_new, b_new.transpose(0,2,1))` if you consider `np.dot` for N-D to behave like `matmul` (which it doesn't perfectly). The most "sensible" fix is to use `@` with appropriate transposes if matrix multiplication is intended.
    ```python
    # If trying to achieve element-wise matrix products on "pages"
    # but dimensions are 3x2 @ 3x2, it's still a conceptual problem for direct @
    # One might do:
    result_dot_fixed = np.zeros((2,3,3)) # Assuming a (3x2) @ (2x3) product
    for i in range(a_new.shape[0]): # Iterate through the "layers"
        result_dot_fixed[i] = a_new[i] @ b_new[i].T
    ```

5.  **`a_new[:, 0] @ b_new`**:
    -   `a_new[:, 0]` is `(2,2)`. `b_new` is `(2,3,2)`. Fails due to `(2,2) @ (3,2)` inner mismatch.
    -   Fix: Transpose the matrices within `b_new`.
        `a_new[:, 0] @ b_new.transpose(0,2,1)` -> `(2,2) @ (2,2,3)`. Result shape `(2,2,3)`.
        Each `2x2` matrix from `b_new` (after transpose) is multiplied by `a_new[:,0]`.
    ```python
    # Fixed
    result = a_new[:, 0] @ b_new.transpose(0, 2, 1)
    ```

6.  **`a_new - b_new[:, 0]`**:
    -   `a_new` (2,3,2), `b_new[:,0]` (2,2). Fails due to broadcasting incompatibility (middle dimensions `3` vs `2`).
    -   To make sense, `b_new[:,0]` would need to be broadcastable to the last two dimensions of `a_new` `(3,2)`.
    -   If the intent was to subtract a vector (derived from `b_new[:,0]`) from each "row" of the "matrices" in `a_new`, the selection of `b_new[:,0]` needs rethinking or explicit broadcasting/tiling.
    -   Example fix if `b_new[:,0]` was meant to be compatible with the *last* dimension of `a_new` (size 2):
        Suppose we want to subtract `b_new[0,0,:]` (shape `(2,)`) from every `(3,2)` matrix in `a_new`.
        ```python
        b_vector_to_subtract = b_new[0, 0, :] # Shape (2,) e.g. [12, 13]
        # This will broadcast b_vector_to_subtract to each of the 3 rows in each of the 2 layers.
        result = a_new - b_vector_to_subtract # (2,3,2) - (2,) -> (2,3,2)
        ```
    -   If the intent was to subtract the `(2,2)` matrix `b_new[:,0]` from corresponding parts of `a_new`, then `a_new` would need to be sliced to match:
        `a_new[:, :2, :] - b_new[:, 0][:, np.newaxis, :]` (This gets complicated and depends heavily on intent).
        A simpler fix if you want to subtract the elements of `b_new[:,0]` from the *first two rows* of each matrix in `a_new`:
        ```python
        # Assume we want to subtract b_new[:,0] from a_new[:,0:2,:]
        # b_new[:,0] shape is (2,2)
        # a_new[:,0:2,:] shape is (2,2,2)
        # We need to make b_new[:,0] broadcastable, e.g. by adding a new axis
        # result = a_new[:, 0:2, :] - b_new[:, 0][:, :, np.newaxis] # This would be (2,2,1)
        # This specific subtraction remains tricky to make "sensible" without more context.
        # A direct element-wise subtraction implies compatible shapes.
        # If we take b_new[0,:,:] which is (3,2), and subtract it from a_new[0,:,:], it works.
        # If we want to subtract b_new[:,0,:] (shape (2,2)) from each 2x2 sub-part of a_new:
        # This is not directly possible without reshaping 'a_new' or tiling 'b_new[:,0]'.
        ```
        Given the original `b_new[:,0]` is `(2,2)`, to make it subtract from `a_new (2,3,2)` element-wise after broadcasting, there isn't a straightforward general fix unless `a_new` is sliced to match `b_new[:,0]`'s broadcastable form or vice-versa, which changes the problem.

---
**Source:** Worksheet WS_NumPy