# 🚀 Sea x OpenAI Regional Codex Hackathon — Multi-Agent Idea Incubator

Hệ thống điều phối đa tác nhân (Multi-Agent System) 6 bước chuyên sâu phục vụ cuộc thi **Sea x OpenAI Regional Codex Hackathon** (tổ chức tại văn phòng Shopee Việt Nam).

---

## 📌 Tổng quan dự án

Hệ thống tự động hóa quá trình sáng tạo, thẩm định, phản biện và đóng gói các ý tưởng sản phẩm AI-Native giải quyết các bài toán lớn trong hệ sinh thái **Sea (Shopee, SPX, SeaMoney, Garena)** tại Đông Nam Á.

Quy trình vận hành tuân thủ nghiêm ngặt theo tài liệu chuẩn hóa [`workflow.md`](./workflow.md), đảm bảo chất lượng ý tưởng đạt chuẩn trước Ban Giám Khảo (OpenAI & Shopee Leadership).

---

## 👥 Đội ngũ 6 Agents chuyên biệt

| Agent | Định danh | Vai trò & Nhiệm vụ | Đặc tính kỹ thuật |
|---|---|---|---|
| **Agent 1** | `agent1_ideator` | Khởi tạo & đề xuất ý tưởng | Nhận đề bài hackathon, phân tích bài toán thực tế ĐNA |
| **Agent 2** | `agent2_novelty_checker` | Thẩm định độc quyền & chống trùng lặp | Lọc generic wrappers, kích hoạt vòng retry nếu trùng |
| **Agent 3** | `agent3_rubric_evaluator` | Chấm điểm Rubric khắt khe | **100% Stateless**, chống thiên vị/nương tay qua các vòng |
| **Agent 4** | `agent4_problem_analyzer` | Mổ xẻ nguyên nhân & tái cấu trúc | Phân tích weakest criterion, tối ưu cho 7h coding window |
| **Agent 5** | `agent5_solution_critic` | Phản biện giải pháp tái cấu trúc | Áp dụng Checklist 4 câu hỏi chốt chặn |
| **Agent 6** | `agent6_synthesizer` | Tổng hợp hồ sơ & báo cáo chi tiết | Kiểm tra Novelty Drift (0% trôi dạt) & chuẩn hóa hồ sơ |

---

## 📁 Cấu trúc thư mục

```text
├── generated_ideas/                 # Thư mục lưu trữ các ý tưởng đã thẩm định (.md)
│   ├── idea_1_shopee_livestream_sentry.md
│   ├── idea_2_seamoney_microflow.md
│   ├── idea_3_crossborder_codex.md
│   ├── ...
│   └── idea_15_riderguard_ai.md
├── workflow.md                      # Đặc tả quy trình điều phối đa tác nhân (v2)
├── state.json                       # Trạng thái runtime & lịch sử chấm điểm qua các vòng
├── orchestrator.py                  # Kịch bản mô phỏng điều phối chu trình 6 Agents
├── batch_pipeline.py                # Pipeline tạo và cập nhật hồ sơ ý tưởng
├── hackathon_execution_report.md    # Báo cáo kết quả thẩm định mẫu COD-Shield
└── README.md                        # Giới thiệu dự án
```

---

## ⚙️ Cấu hình hệ thống (`workflow.md` & `state.json`)

- **`batch_size`**: Số lượng ý tưởng tự động sinh và xử lý trong mỗi lần chạy (mặc định: `6`).
- **`max_gen2_retry`**: 3 (Số lần Agent 1 được sinh lại nếu Agent 2 báo trùng lặp).
- **`max_loop`**: 3 (Số vòng thẩm định Agent 3 $\rightarrow$ Agent 4/5/6 $\rightarrow$ Agent 3).
- **`agent3_threshold_avg`**: 8.0 (Điểm trung bình tối thiểu để PASS).
- **`agent3_threshold_min`**: 6.0 (Điểm tối thiểu cho từng tiêu chí thành phần).

---

## 📋 Cấu trúc chuẩn của mỗi Hồ sơ Ý tưởng

Mỗi file trong thư mục `generated_ideas/` được cấu trúc theo 3 phần bắt buộc:
1. **Chi tiết diễn biến từng vòng**: Nhật ký phản biện và chấm điểm từ Agent 1 đến Agent 6.
2. **HỒ SƠ Ý TƯỞNG**:
   - Tên sản phẩm & Slogan
   - Build Direction (1 trong 3 hướng trọng tâm của cuộc thi)
   - Bối cảnh (thực trạng hiện nay tại ĐNA)
   - Hậu quả (nỗi đau tài chính/vận hành nếu không giải quyết)
   - Giải pháp và Kiến trúc giải pháp (Unified Split-Screen Operations Cockpit)
   - Kịch bản Demo 3 phút trước Ban Giám Khảo (180 giây)
3. **Trạng thái hệ thống cập nhật**: Schema JSON lưu vết trạng thái phê duyệt.
