# تشغيل المهارات الموحدة مع وكلاء البرمجة

تملك المهارات مصدراً أساسياً واحداً داخل `skills/` والسجل المركزي. تحتوي مسارات اكتشاف الوكلاء على روابط إلى المصدر نفسه، لا على حزم مختلفة أو نسخ متعارضة.

## تفعيل Codex وClaude Code داخل المشروع

```bash
python3 scripts/install-skills.py --target /path/to/project --dry-run
python3 scripts/install-skills.py --target /path/to/project
python3 scripts/activate-agents.py --target /path/to/project --host codex --host claude-code --dry-run
python3 scripts/activate-agents.py --target /path/to/project --host codex --host claude-code
```

## التفعيل على مستوى المستخدم لجميع مشاريعه

من نسخة موثوقة لهذا المستودع:

```bash
python3 scripts/activate-agents.py --scope user --host codex --host claude-code --dry-run
python3 scripts/activate-agents.py --scope user --host codex --host claude-code
```

ترتبط المهارات العالمية بالمستودع المحلي الموثوق؛ فإذا نُقل إلى مكان آخر أعد التفعيل بعد مراجعة الروابط. وعند تحديث المستودع الموثوق تتغير التعليمات التي تُحمّلها الروابط العالمية، لذا راجع التحديثات قبل اعتمادها.

## الحدود المهمة

- يعتمد التفعيل على الروابط الرمزية وقد يحتاج صلاحيات إضافية في Windows.
- التفعيل العالمي للمهارات لا يثبّت السجل الكامل داخل مجلد المستخدم؛ تحتاج المسارات متعددة المراحل إلى سياق المشروع وسجل يمكن الوصول إليه.
- لن نخترع مساراً خاصاً بـAntigravity دون التحقق من دعمه.
- لا يتم استبدال أي مهارة يملكها المستخدم.
- لا تُعتبر مراجعة التصميم مستقلة دون دعم فعلي لوكلاء بسياقات جديدة منفصلة.
