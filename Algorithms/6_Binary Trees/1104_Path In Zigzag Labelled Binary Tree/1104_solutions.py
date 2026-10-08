#20261008

#答案
class Solution:

    def pathInZigZagTree(self, label: int) -> list[int]:
        # 1. 计算 label 所在的层数 level (从 1 开始)
        level = 1
        while (1 << level) <= label:
            level += 1

        path = []

        # 2. 自底向上寻找父节点，循环条件改为 level > 1
        while level > 1:
            path.append(label)

            # 父节点所在层的范围 [parent_min, parent_max]
            parent_min = 1 << (level - 2)
            parent_max = (1 << (level - 1)) - 1

            # 计算镜像翻转后的真正父节点
            label = parent_min + parent_max - (label // 2)

            level -= 1

        # 3. 把根节点 1 加入路径
        path.append(1)

        # 4. 反转路径（从根到叶）
        return path[::-1]