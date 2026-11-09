# SECURITY_AUDIT

**المسار:** `security-audit` · **مستوى المخاطر:** `standard`

يشرح هذا الدليل تسلسل العمل؛ يظل [السجل المركزي](../registry/registry.yaml) المرجع الوحيد لترتيب المراحل وشروطها. توثيق المسار الأصلي: [workflows/security-audit.md](./security-audit.md).

## متى نستخدمه؟

نختار هذا المسار فقط عندما يكون أصغر مسار مخوّل يناسب المهمة. تتطلب القرارات المؤثرة في المسارات عالية المخاطر موافقة صريحة. تُشغّل المهارات الاختيارية فقط إذا تحققت شروطها المسجلة.

## ترتيب المهارات

1. [`threat-model`](../skills/threat-model/README.ar.md) — اختيارية عندما تتحقق شروطها
2. [`secrets-safety`](../skills/secrets-safety/README.ar.md) — اختيارية عندما تتحقق شروطها
3. [`dependency-audit`](../skills/dependency-audit/README.ar.md) — اختيارية عندما تتحقق شروطها
4. [`privacy-review`](../skills/privacy-review/README.ar.md) — اختيارية عندما تتحقق شروطها
5. [`security-audit`](../skills/security-audit/README.ar.md) — أساسية
6. [`verify`](../skills/verify/README.ar.md) — أساسية
7. [`handoff`](../skills/handoff/README.ar.md) — أساسية

## إتمام العمل

يجب تقديم الملفات الناتجة والأدلة الفعلية والاختبارات والعوائق والموافقات والخطوة التالية. لا يحق للوكيل النشر أو الإنفاق أو إجراء تغييرات إنتاجية دون تفويض.
