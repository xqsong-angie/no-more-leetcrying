1.Given the task of finding words that share a common prefix with a given word, which data structure would have the optimal expected asymptotic runtime performance?   

Select the correct answer:   
binary tree   
linked list   
trie   ✅
hash set 


2.Hash map implementations group key hashes into "buckets". In what situation would there be multiple key hashes in one bucket?   

Select the correct answer:   
When the same key has been inserted more than once.   
When multiple value objects reference the exact same object in memory.   
When there has been a hash collision.   ✅
When the Hash Map is optimized for look-up by concurrent threads. 


3.A binary tree has a node n, which is reachable in 5 steps from the root of the tree. A level-order traversal is performed on the tree, and the nodes are stored in an array (with 0-based indexing) in the order in which they are visited. What will be the maximum possible index of n in this array?   

Select the correct answer:   
63   ✅ ❌  0-based indexing（索引从 $0$ 开始），前 $63$ 个节点的索引范围是 $0$ 到 $62$
65   
64   
62   正确答案


4.In complexity analysis, which of the following is used to describe an asymptotically tight bound?   

Select the correct answer:   
Big Theta (Big-Theta)   正确答案 渐进紧确界（Asymptotically Tight Bound）
Big Oh (Big-O)   ✅ ❌ 渐进上界（Asymptotic Upper Bound）
Little Oh (Little-o)   
Big Omega (Big-Omega)   渐进下界（Asymptotic Lower Bound）

5.Which techniques can be used to perform depth-first search and breadth-first search on a ternary tree?   

Select the correct answer:   
Successive left-right and right-left tree rotations, respectively   
Preorder and inorder traversals, respectively   
Preorder and level-order traversals, respectively   ✅
Depth-first search and breadth-first search can not be performed on ternary trees 


6.How many topologically distinct binary trees are there with 6 nodes?   E.g. There are 5 topologically distinct binary trees with 3 nodes.   
  .       .   .      .         .
 / \     /   /        \         \
.   .   .   .          .         .
       /     \        /           \
      .       .      .             .

Select the correct answer:   ？
11   
719   
132   正确答案 卡特兰数
10  


7.Which of the following number would end up being the largest as n increases indefinitely? ( googol is an extremely large number: 1 googol = 1.0 * 10^100 )   

Select the correct answer:   
googol * n * log n   
n!  ✅
e^n   
n^googol


8.Consider the function func and its inputs.
/* Inputs:
 * - vec: vector of integers
 * - low: integer
 * - high: integer
 */
function func(vec, low, high): #此代码是快排中的 Lomuto Partition 单趟分区过程，只分了第一次，没有排完，快排还需对左右部分递归调用函数
    pivot = vec[high]
    i = low - 1
    for j = low to high - 1:
        if vec[j] <= pivot:
            i += 1
            exchange vec[i] with vec[j]
    exchange vec[i + 1] with vec[high]
    return i
```

Now, consider the statements below about the function func:

I. This code snippet will have vec sorted at the end of the execution✅ ❌

II. Time complexity of this algorithm is \Theta(n) where n = high - low - 1 ✅

III. pivot will always be at the position floor((high + low)/2) at the end of the execution ✅ ❌

Which statements are TRUE?


9.Which of the following is true of greedy algorithms?   

Select the correct answer:   
At each step, a greedy algorithm evaluates all possible choices recursively and picks the best one.   
Greedy algorithms can't be used to solve problems where the optimal solution contains the optimal solutions to its sub-problems.   
At each step, a greedy algorithm picks the locally optimal choice in hopes of arriving at a globally optimal solution.   ✅
Greedy algorithms use memoization to cache and reuse previously computed values.   