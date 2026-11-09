# ARCHITECTURE_CHANGE

**المسار:** `architecture-change` · **مستوى المخاطر:** `high`

يشرح هذا الدليل تسلسل العمل؛ يظل [السجل المركزي](../registry/registry.yaml) المرجع الوحيد لترتيب المراحل وشروطها. توثيق المسار الأصلي: [workflows/architecture-change.md](./architecture-change.md).

## متى نستخدمه؟

نختار هذا المسار فقط عندما يكون أصغر مسار مخوّل يناسب المهمة. تتطلب القرارات المؤثرة في المسارات عالية المخاطر موافقة صريحة. تُشغّل المهارات الاختيارية فقط إذا تحققت شروطها المسجلة.

## ترتيب المهارات

1. [`grill`](../skills/grill/README.ar.md) — أساسية
2. [`architecture-decision`](../skills/architecture-decision/README.ar.md) — أساسية
3. [`threat-model`](../skills/threat-model/README.ar.md) — اختيارية عندما تتحقق شروطها
4. [`review-design`](../skills/review-design/README.ar.md) — اختيارية عندما تتحقق شروطها
5. [`resolve-findings`](../skills/resolve-findings/README.ar.md) — اختيارية عندما تتحقق شروطها
6. [`doc-impact`](../skills/doc-impact/README.ar.md) — أساسية
7. [`to-spec`](../skills/to-spec/README.ar.md) — أساسية
8. [`to-tickets`](../skills/to-tickets/README.ar.md) — اختيارية عندما تتحقق شروطها
9. [`implement`](../skills/implement/README.ar.md) — أساسية
10. [`security-audit`](../skills/security-audit/README.ar.md) — اختيارية عندما تتحقق شروطها
11. [`accessibility-audit`](../skills/accessibility-audit/README.ar.md) — اختيارية عندما تتحقق شروطها
12. [`performance-audit`](../skills/performance-audit/README.ar.md) — اختيارية عندما تتحقق شروطها
13. [`verify`](../skills/verify/README.ar.md) — أساسية
14. [`code-review`](../skills/code-review/README.ar.md) — أساسية
15. [`detect-drift`](../skills/detect-drift/README.ar.md) — اختيارية عندما تتحقق شروطها
16. [`decision-capture`](../skills/decision-capture/README.ar.md) — أساسية
17. [`doc-sync`](../skills/doc-sync/README.ar.md) — أساسية
18. [`handoff`](../skills/handoff/README.ar.md) — أساسية

## إتمام العمل

يجب تقديم الملفات الناتجة والأدلة الفعلية والاختبارات والعوائق والموافقات والخطوة التالية. لا يحق للوكيل النشر أو الإنفاق أو إجراء تغييرات إنتاجية دون تفويض.
