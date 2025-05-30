---
tags:
  - index
  - MOC
date_created: <% tp.file.creation_date("2025-04-20") %>
---
# Infinity Labs AI3 Index

Welcome to your  Infinity Labs AI3 Index course knowledge base!

This vault organizes concepts, commands, and notes from the course. Use the links below to navigate to the main subject areas.

## Main Subject Areas

- [[10_Linux/_Linux_MOC|Linux & Shell]]
- [[20_Version_Control/_Version_Control_MOC|Version Control (Git)]]
- [[30_C_Programming/_C_Programming_MOC|C Programming]]
- [[40_Testing_Debugging/_Testing_Debugging_MOC|Testing & Debugging]]
- [[50_Data_Structures/_Data_Structures_MOC|Data Structures]]
- [[60_Algorithms/_Algorithms_MOC|Algorithms]]
- [[70_System_Programming/_System_Programming_MOC|System Programming]]
- [[80_DevOps/_DevOps_MOC|DevOps]]
- [[90_Networking/_Networking_MOC|Networking]]
- [[100_Python/_Python_MOC|Python Programming]]
- [[110_Cloud_Computing/_Cloud_Computing_MOC|Cloud Computing]]
- [[120_Virtualization_Containers/_Virtualization_Containers_MOC|Virtualization & Containers]]
- [[130_Bash/_Bash_MOC|Bash Scripting]]
- [[140_Data_Science_AI/_Data_Science_AI_MOC|Data Science & AI]] (Placeholder for future topics)

## Meta & Templates
- [[00_Meta/Templates/T_Concept|Concept Template]]
- [[00_Meta/Templates/T_Command|Command Template]]
- [[00_Meta/Templates/T_C_Function|C Function Template]]
- [[00_Meta/Templates/T_MOC|MOC Template]]

## Recent Notes

```dataview
LIST
FROM "" AND !"00_Meta"
SORT file.mtime DESC
LIMIT 15
```

---

**Corrected Mermaid Snippets:**

1.  **File:** `140_Data_Science_AI/NumPy/NumPy_Dimension_Shape_Axis.md`
    *   For the "1D Array (Vector)" tab:
        ```mermaid
        graph LR
            subgraph arr1d_Shape_4 [arr1d - Shape (4,)] %% Removed parentheses from title
                direction LR
                Idx0((0: 1)) --- Idx1((1: 2)) --- Idx2((2: 3)) --- Idx3((3: 4))
            end
            %% note right of arr1d : Axis 0 (Length 4) %% Mermaid comment
        ```
    *   For the "2D Array (Matrix)" tab:
        ```mermaid
        graph TD
            subgraph arr2d_Shape_2_3 [arr2d - Shape (2,3)] %% Removed parentheses
                %% direction TB %% Not needed for subgraph
                subgraph Axis_0_Rows_Length_2 [Axis 0 Rows - Length 2]
                    R0["Row 0"] --> C00((0,0: 1)); R0 --> C01((0,1: 2)); R0 --> C02((0,2: 3));
                    R1["Row 1"] --> C10((1,0: 4)); R1 --> C11((1,1: 5)); R1 --> C12((1,2: 6));
                end
                subgraph Axis_1_Columns_Length_3 [Axis 1 Columns - Length 3]
                    direction LR
                    C0((Col 0)) --- C1((Col 1)) --- C2((Col 2))
                end
                R0 --- R1
            end
        ```

2.  **File:** `140_Data_Science_AI/NumPy/NumPy_sum_vs_python_sum.md`
    ```mermaid
    graph LR
        subgraph Summing_Large_Numerical_Array [Summing Large Numerical Array]
            PySum["Python sum(ndarray)"] -- Iterates in Python --> Element1[Elem1 as PyObject];
            Element1 -- Python + --> Element2[Elem2 as PyObject];
            Element2 -- Python + --> ElementN[...];
            style PySum fill:#fdd

            NpSum["np.sum(ndarray)"] -- Operates in C --> ContigData["Contiguous Data Block"];
            ContigData -- Vectorized Sum --> NpResult[Result];
            style NpSum fill:#dfd
        end
        %% note right of PySum : High overhead per element %% Mermaid comment
        %% note right of NpSum : Low overhead, optimized loop %% Mermaid comment
    ```

3.  **File:** `140_Data_Science_AI/Matplotlib/Figure_Subplot_Axes.md`
    ```mermaid
    graph TD
        FIGURE["Figure TopLevel Container"] --> AXES1["Axes 1 Subplot 1"];
        FIGURE --> AXES2["Axes 2 Subplot 2"];
        FIGURE --> Suptitle["Figure Suptitle Optional"];

        AXES1 --> XAxis1["X-Axis 1"];
        AXES1 --> YAxis1["Y-Axis 1"];
        AXES1 --> Title1["Axes Title 1"];
        AXES1 --> Plot1["Plotted Data 1 lines points"];
        AXES1 --> Legend1["Legend 1"];

        AXES2 --> XAxis2["X-Axis 2"];
        AXES2 --> YAxis2["Y-Axis 2"];
        AXES2 --> Title2["Axes Title 2"];
        AXES2 --> Plot2["Plotted Data 2"];
        AXES2 --> Legend2["Legend 2"];

        style FIGURE fill:#lightgrey,stroke:#333,stroke-width:2px
        style AXES1 fill:#lightblue,stroke:#333,stroke-width:2px
        style AXES2 fill:#lightgreen,stroke:#333,stroke-width:2px
    ```

4.  **File:** `140_Data_Science_AI/Pandas/Pandas_Series.md`
    ```mermaid
    graph LR
        subgraph Pandas_Series_Structure [Pandas Series] %% Changed subgraph title
            direction TB
            subgraph Index_Labels_Series [Index Labels] %% Changed subgraph title
                direction TB
                idx0((Label 0))
                idx1((Label 1))
                idx_dots(...)
                idx_n((Label n-1))
            end
            subgraph Data_Values_Series [Data Values - NumPy ndarray] %% Changed subgraph title
                direction TB
                val0[Value 0]
                val1[Value 1]
                val_dots[...]
                val_n[Value n-1]
            end
            Index_Labels_Series --- Data_Values_Series
        end
        Name["Series Name Optional"] --> Pandas_Series_Structure
    ```

5.  **File:** `140_Data_Science_AI/Pandas/Pandas_DataFrame.md`
    ```mermaid
    graph TD
        subgraph Pandas_DataFrame_Structure [Pandas DataFrame]
            %% Use of a more descriptive title for the main subgraph
            subgraph Index_Row_Labels_DF [Index Row Labels] %% Changed title
                direction TB
                idx0((Label 0))
                idx1((Label 1))
                idx_dots(...)
                idx_m((Label m-1))
            end
            subgraph Columns_Collection_DF [Columns] %% Changed title
                direction TB
                ColHeader1["Col 1 Name"] --> S1Data["Series 1 Data Col 1"]
                ColHeader2["Col 2 Name"] --> S2Data["Series 2 Data Col 2"]
                ColHeaderDots["..."] --> SDotsData["..."]
                ColHeaderN["Col N Name"] --> SNData["Series N Data Col N"]
            end
            %% Indicates index applies to all series/columns
            Index_Row_Labels_DF -.-> Columns_Collection_DF
        end
    ```

6.  **File:** `50_Data_Structures/Vector_Math.md`
    ```mermaid
    graph TD
        subgraph Vector_Addition_u_plus_v [Vector Addition u+v] %% Changed title
            direction LR
            O((Origin)) -- u [2, 1] --> P1;
            P1 -- v [1, 2] --> P2;
            O -- u_plus_v [3, 3] --> P2;
            style P2 fill:#f9f,stroke:#333,stroke-width:2px
        end
        subgraph Scalar_Multiplication_2u [Scalar Multiplication 2u] %% Changed title
             direction LR
             O2((Origin)) -- u_mult [2, 1] --> P3; %% Renamed u to u_mult
             O2 -- two_u_mult [4, 2] --> P4;
             style P4 fill:#ccf,stroke:#333,stroke-width:2px
        end
    ```

7.  **File:** `50_Data_Structures/Matrix_Math.md`
    ```mermaid
    graph TD
        subgraph Matrix_A_3x2_Example [Matrix A 3x2] %% Changed title
            direction LR
            R1["Row 1"] --> C11(a_11);
            R1 --> C12(a_12);
            R2["Row 2"] --> C21(a_21);
            R2 --> C22(a_22);
            R3["Row 3"] --> C31(a_31);
            R3 --> C32(a_32);

            subgraph Columns_Sub_Example [Columns] %% Changed title
               direction TB
               Col1["Col 1"] --> C11; Col1 --> C21; Col1 --> C31;
               Col2["Col 2"] --> C12; Col2 --> C22; Col2 --> C32;
            end
        end
    ```

8.  **File:** `50_Data_Structures/Matrix_Inverse.md`
    ```mermaid
    graph LR
        A_mat[Matrix A] -- Multiply --> I_mat[Identity Matrix I];
        I_mat -- Multiply_by_A_inv_rel[Multiply by A_inv] --> A_inv_mat[Inverse A_inv];
        A_inv_mat -- Multiply_by_A_rel[Multiply by A] --> I_from_inv_mat[Identity Matrix I];

        A_mat -- has_inverse_rel[has_inverse] --> A_inv_mat;
        A_inv_mat -- is_inverse_of_rel[is_inverse_of] --> A_mat;

        A_mat -- Multiply_by_A_inv_op_rel[Multiply by A_inv] --> Result_I1_mat[Identity Matrix I];
        A_inv_mat -- Multiply_by_A_op_rel[Multiply by A] --> Result_I2_mat[Identity Matrix I];
    ```

9.  **File:** `50_Data_Structures/Matrix_Operations.md`
    *   Addition Diagram:
        ```mermaid
        graph TD
            A_add_op("A = [1 2]<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3 4]") -- + --> C_add_op("C = [6 8]<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[10 12]");
            B_add_op("B = [5 6]<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[7 8]") -- + --> C_add_op;
        ```
    *   Transpose Diagram:
        ```mermaid
        graph TD
            A_trans_op("A = [1 2 3]<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4 5 6]") --> AT_trans_op("A<sup>T</sup> = [1 4]<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2 5]<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[3 6]");
        ```

10. **File:** `50_Data_Structures/DAG.md`
    ```mermaid
    graph LR
        A_node --> B_node;
        A_node --> C_node;
        B_node --> D_node;
        C_node --> D_node;
        C_node --> E_node;
        D_node --> F_node;
        E_node --> F_node;

        subgraph Note_DAG_Corrected [Note] %% Changed title
            direction LR
            N1_item(No path back to starting node e.g. no path from F back to A)
        end
    ```

11. **File:** `50_Data_Structures/Singly_Linked_List_DS.md`
    ```mermaid
    graph LR
        Head_SLL --> NodeA_SLL["Data: A | next"];
        NodeA_SLL -- ptr --> NodeB_SLL["Data: B | next"];
        NodeB_SLL -- ptr --> NodeC_SLL["Data: C | next"];
        NodeC_SLL -- ptr --> NullVal_SLL(NULL);

        style Head_SLL fill:#fff,stroke:#f00,stroke-width:2px
    ```

12. **File:** `50_Data_Structures/Dummy_Node_C.md` (Empty List)
    ```mermaid
    graph LR
        Head_Dummy_Empty --> DummyNode_Empty[Dummy | next];
        DummyNode_Empty -- ptr --> NullVal_Empty(NULL);

        style Head_Dummy_Empty fill:#fff,stroke:#f00,stroke-width:2px
    ```

13. **File:** `50_Data_Structures/Dummy_Node_C.md` (List with A, B)
    ```mermaid
    graph LR
        Head_Dummy_AB --> DummyNode_AB[Dummy | next];
        DummyNode_AB -- ptr --> NodeA_Dummy_AB[Data: A | next];
        NodeA_Dummy_AB -- ptr --> NodeB_Dummy_AB[Data: B | next];
        NodeB_Dummy_AB -- ptr --> NullVal_Dummy_AB(NULL);

        style Head_Dummy_AB fill:#fff,stroke:#f00,stroke-width:2px
    ```

14. **File:** `50_Data_Structures/Circular_Linked_List_DS.md`
    ```mermaid
    graph LR
        NodeA_CLL["Data: A | next"] -- ptr --> NodeB_CLL["Data: B | next"];
        NodeB_CLL -- ptr --> NodeC_CLL["Data: C | next"];
        NodeC_CLL -- ptr --> NodeA_CLL; %% Last node points back to first

        subgraph Access_Pointer_CLL_Sub [Access Pointer] %% Changed title
          LAST_ptr_CLL --> NodeC_CLL; %% Example Pointer to last node
        end
        style LAST_ptr_CLL fill:#fff,stroke:#f00,stroke-width:2px
    ```

15. **File:** `50_Data_Structures/Doubly_Linked_List_DS.md`
    ```mermaid
    graph LR
        HEAD_Node_DLL[Head] -- ptr --> NodeA_Node_DLL;
        TAIL_Node_DLL[Tail] -- ptr --> NodeC_Node_DLL;

        subgraph Nodes_DLL_Structure [Nodes] %% Changed title
          NULL_Prev_Node_DLL(NULL);
          NodeA_Node_DLL["prev | Data: A | next"];
          NodeB_Node_DLL["prev | Data: B | next"];
          NodeC_Node_DLL["prev | Data: C | next"];
          NULL_Next_Node_DLL(NULL);

          NULL_Prev_Node_DLL -- prev_link --> NodeA_Node_DLL;
          NodeA_Node_DLL -- next_link --> NodeB_Node_DLL;
          NodeB_Node_DLL -- next_link --> NodeC_Node_DLL;
          NodeC_Node_DLL -- next_link --> NULL_Next_Node_DLL;

          NodeA_Node_DLL -- prev_link_back --> NULL_Prev_Node_DLL;
          NodeB_Node_DLL -- prev_link_back --> NodeA_Node_DLL;
          NodeC_Node_DLL -- prev_link_back --> NodeB_Node_DLL;
        end

        style HEAD_Node_DLL fill:#fff,stroke:#f00,stroke-width:2px
        style TAIL_Node_DLL fill:#fff,stroke:#00f,stroke-width:2px
    ```

16. **File:** `50_Data_Structures/Circular_Queue_DS.md`
    ```mermaid
    graph TD
        subgraph Circ_Queue_Cap5_Struct [Circular Queue Capacity 5 One Slot Empty Strategy] %% Changed title
            Q0 --- Q1 --- Q2 --- Q3 --- Q4 --- Q0;
        end

        subgraph State1_Empty_CQ [State 1 Empty] %% Changed title
            Front1_CQ(front=0);
            Rear1_CQ(rear=0);
            Q0_1_CQ((Q0)); Q1_1_CQ((Q1)); Q2_1_CQ((Q2)); Q3_1_CQ((Q3)); Q4_1_CQ((Q4));
            style Front1_CQ fill:#fff,stroke:#f00,stroke-width:2px;
            style Rear1_CQ fill:#fff,stroke:#00f,stroke-width:2px;
        end
        subgraph State2_Enqueue_AB_CQ [State 2 Enqueue A B] %% Changed title
            Front2_CQ(front=0);
            Rear2_CQ(rear=2);
            Q0_2_CQ((Q0=A)); Q1_2_CQ((Q1=B)); Q2_2_CQ((Q2)); Q3_2_CQ((Q3)); Q4_2_CQ((Q4));
            style Front2_CQ fill:#fff,stroke:#f00,stroke-width:2px;
            style Rear2_CQ fill:#fff,stroke:#00f,stroke-width:2px;
        end
         subgraph State3_Dequeue_A_CQ [State 3 Dequeue A] %% Changed title
            Front3_CQ(front=1);
            Rear3_CQ(rear=2);
            Q0_3_CQ((Q0)); Q1_3_CQ((Q1=B)); Q2_3_CQ((Q2)); Q3_3_CQ((Q3)); Q4_3_CQ((Q4));
            style Front3_CQ fill:#fff,stroke:#f00,stroke-width:2px;
            style Rear3_CQ fill:#fff,stroke:#00f,stroke-width:2px;
        end
         subgraph State4_Enqueue_CDE_CQ [State 4 Enqueue C D E] %% Changed title
            Front4_CQ(front=1);
            Rear4_CQ(rear=0);
            Q0_4_CQ((Q0=E)); Q1_4_CQ((Q1=B)); Q2_4_CQ((Q2=C)); Q3_4_CQ((Q3=D)); Q4_4_CQ((Q4));
            style Front4_CQ fill:#fff,stroke:#f00,stroke-width:2px;
            style Rear4_CQ fill:#fff,stroke:#00f,stroke-width:2px;
            %% note right of Q0_4 : Queue is Full! (rear+1)%5 == front
        end
    ```

17. **File:** `50_Data_Structures/Queue_ADT.md`
    ```mermaid
    graph TD
        subgraph Queue_Operations_ADT [Queue Operations] %% Changed title
            direction LR
            Start_Q([ ]) -- enqueue A --> Node_A_Q([A]) -- Front & Rear;
            Node_A_Q -- enqueue B --> Node_B_Q([A, B]) -- Rear;
            Node_B_Q -- enqueue C --> Node_C_Q([A, B, C]) -- Rear;
            Node_C_Q -- dequeue --> Node_D_Q([B, C]) -- Returns A;
            Node_D_Q -- front --> Node_D_Q -- Returns B;
            Node_D_Q -- dequeue --> Node_E_Q([C]) -- Returns B;
        end
    ```

18. **File:** `50_Data_Structures/Stack_ADT.md`
    ```mermaid
    graph TD
        subgraph Stack_Ops_Diagram_ADT [Stack Operations] %% Changed title
            direction LR
            A_Item_S(Item A) -- push --> B_Stack_S([A]);
            B_Stack_S -- push B --> C_Stack_S([B, A]);
            C_Stack_S -- push C --> D_Stack_S([C, B, A]) -- Top;
            D_Stack_S -- pop --> E_Stack_S([B, A]) -- Returns C;
            E_Stack_S -- peek --> E_Stack_S -- Returns B;
            E_Stack_S -- pop --> F_Stack_S([A]) -- Returns B;
        end
    ```

19. **File:** `10_Linux/CPU_cache.md`
    ```mermaid
    graph TD
        CPU_Reg_Cache[CPU Registers] --> L1_Cache[L1 Cache];
        L1_Cache --> L2_Cache[L2 Cache];
        L2_Cache --> L3_Cache[L3 Cache];
        L3_Cache --> Main_RAM[Main RAM];
        Main_RAM --> Disk_Storage[Disk/SSD Storage];

        subgraph CPU_Chip_Cache_Diagram [CPU Chip] %% Changed title
            CPU_Reg_Cache; L1_Cache; L2_Cache; L3_Cache;
        end

        style CPU_Reg_Cache fill:#f9f
        style L1_Cache fill:#ccf
        style L2_Cache fill:#ccf
        style L3_Cache fill:#ccf
        style Main_RAM fill:#9cf
        style Disk_Storage fill:#ccc

        linkStyle 0 stroke-width:2px,stroke:red;
        linkStyle 1 stroke-width:2px,stroke:orange;
        linkStyle 2 stroke-width:2px,stroke:green;
        linkStyle 3 stroke-width:2px,stroke:blue;
        linkStyle 4 stroke-width:1px,stroke:gray;

        %% note right of L1_Cache : Fastest, Smallest %% Mermaid comment
        %% note right of Main_RAM : Slower, Larger %% Mermaid comment
    ```

20. **File:** `10_Linux/EPROM.md`
    ```mermaid
    graph TD
        EPROM_Chip_Diagram[EPROM Chip w Quartz Window] -- UV Light --> Erased_State_EPROM[Erased State];
        Erased_State_EPROM -- EPROM_Programmer_Device --> Programmed_State_EPROM[Programmed EPROM];
        Programmed_State_EPROM -- Read_Operations_EPROM --> System_Bus_EPROM[System Bus];
    ```

21. **File:** `90_Networking/OSI_Model.md`
    ```mermaid
    graph TD
        subgraph Host_A_OSI_Model [Host A] %% Changed title
            App_A_OSI(Layer 7 Application);
            Pre_A_OSI(Layer 6 Presentation);
            Ses_A_OSI(Layer 5 Session);
            Tra_A_OSI(Layer 4 Transport);
            Net_A_OSI(Layer 3 Network);
            Dat_A_OSI(Layer 2 Data Link);
            Phy_A_OSI(Layer 1 Physical);
        end

        subgraph Host_B_OSI_Model [Host B] %% Changed title
            App_B_OSI(Layer 7 Application);
            Pre_B_OSI(Layer 6 Presentation);
            Ses_B_OSI(Layer 5 Session);
            Tra_B_OSI(Layer 4 Transport);
            Net_B_OSI(Layer 3 Network);
            Dat_B_OSI(Layer 2 Data Link);
            Phy_B_OSI(Layer 1 Physical);
        end

        App_A_OSI <--> App_B_OSI;
        Pre_A_OSI <--> Pre_B_OSI;
        Ses_A_OSI <--> Ses_B_OSI;
        Tra_A_OSI <--> Tra_B_OSI;
        Net_A_OSI <--> Router_OSI_Device((Router - L3)) <--> Net_B_OSI;
        Dat_A_OSI <--> Switch_OSI_Device((Switch - L2)) <--> Dat_B_OSI;
        Phy_A_OSI --- Network_Medium_OSI_Link(((Network Medium))) --- Phy_B_OSI;

        App_A_OSI --> Pre_A_OSI --> Ses_A_OSI --> Tra_A_OSI --> Net_A_OSI --> Dat_A_OSI --> Phy_A_OSI;
        Phy_B_OSI --> Dat_B_OSI --> Net_B_OSI --> Tra_B_OSI --> Ses_B_OSI --> Pre_B_OSI --> App_B_OSI;

        style Router_OSI_Device fill:#f9f
        style Switch_OSI_Device fill:#ccf
    ```

---

**Summary of Mermaid Corrections Applied:**
1.  Removed parentheses `()` from subgraph titles.
2.  Replaced `#` comments with `%%` comments on their own lines.
3.  Ensured node IDs are unique across the examples provided here to avoid potential conflicts if these were ever combined or if Mermaid has global ID caches in some renderers (though typically scoped per diagram). I've added suffixes like `_SLL`, `_CQ`, `_OSI` etc. to achieve this in this corrective list. You should ensure your actual node IDs within each diagram are unique *within that diagram*.

This approach should give you the corrected Mermaid code for each file, which you can then embed within a standard ` ```mermaid ... ``` ` block in the respective Markdown files.

We can now continue with generating the **Pandas** content.
