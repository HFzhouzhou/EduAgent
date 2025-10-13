"""
Word 模板填充功能演示
Template Filler Demo

演示如何使用智能标签填充Word模板
"""

from utils.template_filler import WordTemplateFiller
from pathlib import Path


def main():
    print("=" * 60)
    print("🎓 Word 模板智能填充功能演示")
    print("=" * 60)
    print()
    
    filler = WordTemplateFiller()
    
    # 1. 创建示例模板
    print("📝 步骤 1: 创建示例模板")
    print("-" * 60)
    
    template_path = "教案模板_智能标签版.docx"
    if filler.create_sample_template(template_path):
        print(f"✅ 示例模板已创建：{template_path}")
        print("   您可以用 Word 打开查看标签格式")
    print()
    
    # 2. 显示标签使用指南
    print("📖 步骤 2: 标签使用指南")
    print("-" * 60)
    print(filler.get_tag_guide())
    print()
    
    # 3. 检查模板标签
    print("🔍 步骤 3: 检查模板标签")
    print("-" * 60)
    
    result = filler.check_template_tags(template_path)
    if result['success']:
        print(f"✅ 找到 {result['total_tags']} 个标签")
        print(f"   识别的标签：{', '.join(result['recognized_tags'])}")
        if result['unrecognized_tags']:
            print(f"   ⚠️  未识别的标签：{', '.join(result['unrecognized_tags'])}")
    print()
    
    # 4. 准备教案数据
    print("📚 步骤 4: 准备教案数据")
    print("-" * 60)
    
    lesson_data = {
        'lesson_number': '1',
        'lesson_title': '数据结构概述',
        'teaching_hours': '2',
        'teaching_objectives': {
            '知识目标': [
                '掌握数据结构的基本概念、术语和表示方法',
                '理解数据结构的分类及各类特点',
                '了解算法的基本概念及复杂度分析方法',
            ],
            '能力目标': [
                '能够分析实际问题中的数据结构特点',
                '能够根据问题选择合适的数据结构',
            ],
            '素质目标': [
                '培养抽象思维能力和逻辑分析能力',
                '养成科学严谨的工作态度',
            ]
        },
        'teaching_focus': [
            '数据结构的定义与分类',
            '逻辑结构与存储结构的关系',
            '算法复杂度的概念',
        ],
        'teaching_difficulty': [
            '数据结构的抽象表示方法',
            '时间复杂度和空间复杂度的分析',
        ],
        'teaching_methods': [
            '讲授法 - 讲解基本概念',
            '案例分析法 - 分析实际应用',
            '讨论法 - 小组讨论问题',
            '演示法 - 展示数据结构示例',
        ],
        'teaching_process': {
            '导入环节（10分钟）': [
                '回顾程序设计课程的基础知识',
                '提出问题：为什么需要研究数据结构？',
                '展示生活中的数据结构实例（图书馆书架、超市排队等）',
            ],
            '新课讲授（60分钟）': [
                '1. 数据结构的基本概念（20分钟）',
                '   - 数据、数据元素、数据项',
                '   - 数据对象、数据结构',
                '   - 逻辑结构：线性、树形、图形、集合',
                '2. 存储结构（20分钟）',
                '   - 顺序存储',
                '   - 链式存储',
                '   - 索引存储',
                '   - 散列存储',
                '3. 算法与复杂度（20分钟）',
                '   - 算法的定义和特性',
                '   - 时间复杂度分析',
                '   - 空间复杂度分析',
            ],
            '课堂练习（15分钟）': [
                '案例分析：学生成绩管理系统的数据结构设计',
                '小组讨论：如何选择合适的数据结构？',
                '分享讨论结果',
            ],
            '总结回顾（5分钟）': [
                '回顾本节课重点内容',
                '预告下节课内容：线性表',
                '布置课后作业',
            ],
        },
        'homework': '''
1. 复习教材第一章，理解数据结构的基本概念
2. 完成课后习题：1-3, 1-5, 1-7
3. 思考题：分析以下场景应该使用什么数据结构？
   - 浏览器的前进后退功能
   - 手机通讯录
   - 社交网络的好友关系
4. 预习下一章：线性表
''',
        'reflection': '（本栏由教师课后填写）',
    }
    
    course_data = {
        'course_name': '数据结构',
        'teacher_name': '张老师',
        'class_name': '计算机2021级1班',
    }
    
    print("课程信息：")
    print(f"  • 课程：{course_data['course_name']}")
    print(f"  • 教师：{course_data['teacher_name']}")
    print(f"  • 班级：{course_data['class_name']}")
    print()
    print("教案信息：")
    print(f"  • 课次：第 {lesson_data['lesson_number']} 次课")
    print(f"  • 课题：{lesson_data['lesson_title']}")
    print(f"  • 学时：{lesson_data['teaching_hours']} 学时")
    print()
    
    # 5. 填充模板
    print("✨ 步骤 5: 填充模板")
    print("-" * 60)
    
    output_path = f"教案_第{lesson_data['lesson_number']}次课.docx"
    if filler.fill_lesson_plan(
        template_path=template_path,
        output_path=output_path,
        lesson_plan=lesson_data,
        course_info=course_data
    ):
        print(f"✅ 教案生成成功：{output_path}")
        print("   您可以用 Word 打开查看效果")
    print()
    
    # 6. 使用说明
    print("💡 使用说明")
    print("-" * 60)
    print("""
1. 自定义模板
   - 打开生成的模板文件
   - 按需修改格式和布局
   - 在需要填充的位置插入 {{标签名}}
   - 保存模板

2. 标签语法
   - 简单变量：{{course_name}}
   - 条件判断：{% if homework %}...{% endif %}
   - 循环列表：{% for item in items %}...{% endfor %}

3. 批量生成
   - 可以使用同一个模板
   - 批量生成多个课次的教案
   - 每个教案使用不同的数据

4. 高级功能
   - 支持表格中使用标签
   - 支持文本框中使用标签
   - 支持页眉页脚中使用标签
   - 支持多级列表和编号

完整文档：https://docxtpl.readthedocs.io/
""")
    
    print("=" * 60)
    print("🎉 演示完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()

