# WORKFLOW DEFINITION v2: IDEA GENERATION & REFINEMENT
*(Đã vá 8 lỗ hổng: Agent 2 vào lại vòng lặp, retry thay vì dừng cứng, mở rộng rubric Agent 3, định lượng Đạt/Chưa đạt, cấp lịch sử cho Agent 4, chuẩn hóa rubric cho Agent 5, xử lý hết vòng, chống nương tay của Agent 3)*

---

## 1. Danh sách Agent & Nhiệm vụ

| Agent | Nhiệm vụ | Thay đổi so với v1 |
|---|---|---|
| Agent 1 | Nhận thông tin cuộc thi, sinh ý tưởng ban đầu (hoặc sinh lại nếu bị Agent 2 từ chối) | Nhận thêm lý do bị từ chối nếu là lượt retry |
| Agent 2 | Tra cứu độc quyền/trùng lặp | Giờ được gọi ở **2 điểm**: (a) sau Agent 1 lần đầu, (b) kiểm tra lại sau Agent 6 trước khi gửi Agent 3 |
| Agent 3 | Đánh giá theo rubric đầy đủ (4 tiêu chí, có điểm số) | Rubric mở rộng, chấm điểm 0-10 thay vì Đạt/Chưa đạt cảm tính, **stateless** (không biết số vòng) |
| Agent 4 | Phân tích lỗi + đề xuất giải pháp cải tiến | Nhận **toàn bộ lịch sử** các phương án đã thử, không chỉ vòng gần nhất |
| Agent 5 | Phản biện giải pháp của Agent 4 | Dùng **cùng rubric + blacklist** với Agent 2/Agent 3, không phản biện tự do |
| Agent 6 | Tổng hợp, viết lại ý tưởng hoàn thiện | Thêm bước tự hỏi "còn giữ đúng góc khác biệt đã được Agent 2 xác nhận không?" |

---

## 2. Quy tắc điều phối (Control Flow — đã vá)

```
BẮT ĐẦU
  │
  ▼
Agent 1 sinh ý tưởng (lần 1) ──────────────────────────────┐
  │                                                          │
  ▼                                                          │
Agent 2: Kiểm tra độc quyền                                  │
  │                                                          │
  ├─ TRÙNG LẶP & còn lượt retry (< max_gen2_retry)           │
  │     → gửi lý do trùng về Agent 1 → sinh lại ─────────────┘
  │
  ├─ TRÙNG LẶP & HẾT lượt retry
  │     → DỪNG, báo cáo cho người dùng: lý do trùng + gợi ý pivot thủ công
  │
  └─ HỢP LỆ (chưa trùng, hoặc có khác biệt đủ rõ)
        │
        ▼
   Agent 3: Chấm điểm theo rubric đầy đủ (xem mục 3)
        │  [LƯU Ý: Agent 3 chấm KHÔNG biết đây là vòng lặp thứ mấy — xem mục 5]
        │
        ├─ ĐẠT (điểm TB ≥ ngưỡng VÀ không tiêu chí nào < mức tối thiểu)
        │     → Xuất báo cáo → KẾT THÚC
        │
        └─ CHƯA ĐẠT & còn vòng (< max_loop, mặc định 3)
              │
              ▼
        Agent 4: Nhận lỗi/rủi ro từ Agent 3 + TOÀN BỘ lịch sử các bản
                 đã thử trước đó (xem mục 4) → đề xuất giải pháp mới
              │
              ▼
        Agent 5: Phản biện giải pháp của Agent 4, dùng CÙNG rubric +
                 blacklist với Agent 2/3 (xem mục 6)
              │
              ├─ Phát hiện giải pháp mới VẪN phạm lỗi cũ (trùng lặp,
              │  hoặc không thực sự giải quyết điểm yếu Agent 3 nêu)
              │     → trả NGƯỢC về Agent 4, không qua Agent 6, tính là
              │       1 lần thử trong cùng vòng (không tốn thêm 1 vòng
              │       lặp chính nếu retry nội bộ < 2 lần)
              │
              └─ Giải pháp hợp lý
                    │
                    ▼
              Agent 6: Viết lại ý tưởng hoàn thiện
                    │  Tự hỏi: "So với bản đã qua Agent 2, còn giữ đúng
                    │  góc khác biệt đã xác nhận không, hay đã trôi về
                    │  hướng generic?"
                    │
                    ├─ Nghi ngờ đã trôi khỏi vùng an toàn về độc quyền
                    │     → gửi lại qua Agent 2 kiểm tra lại trước khi
                    │       tới Agent 3 (đúng nhánh trên cùng)
                    │
                    └─ Không nghi ngờ → gửi thẳng về Agent 3, TĂNG
                       biến đếm vòng lặp (+1)

        └─ CHƯA ĐẠT & HẾT vòng (= max_loop)
              → DỪNG, xuất BÁO CÁO KẾT THÚC KHÔNG THÀNH CÔNG (xem mục 7)
```

---

## 3. Cấu hình rubric cho Agent 3 — CHỈNH SỬA ĐƯỢC

> Vá lỗ hổng #3: rubric cũ chỉ có "gần gũi + giá trị", thiếu 2 điều kiện quan trọng của cuộc thi. Bảng dưới gộp đủ 4 khía cạnh; bạn chỉnh trọng số/ngưỡng theo ý muốn.

| # | Tiêu chí | Câu hỏi Agent 3 phải trả lời | Trọng số (mặc định) |
|---|---|---|---|
| 1 | **Khớp build direction** (gate, không tính điểm nếu fail) | Có khớp rõ 1 trong 3 hướng (Autonomous & Adaptive / AI-Native / Deep Domain) không, hay gắn nhãn hời hợt? | Pass/Fail — fail thì toàn bộ điểm = 0, không tính trung bình |
| 2 | Gần gũi & thiết thực với đời sống | Vấn đề có phải thứ người dùng thật (sinh viên, người bình thường) tự trải nghiệm/quan sát được không? | 30% |
| 3 | Giá trị mang lại | Giải quyết được gì cụ thể, cho ai, mức độ cải thiện so với hiện trạng ra sao? | 30% |
| 4 | Khả thi build trong 7 tiếng bằng Codex | Phạm vi có đủ hẹp, không cần data/tích hợp phức tạp, không cần scrape rủi ro? | 40% |

**Công thức:**
```
Nếu tiêu chí 1 = Fail → Kết quả = "CHƯA ĐẠT", điểm = 0, lý do = "Không khớp build direction"
Nếu tiêu chí 1 = Pass:
  Điểm tổng = (tiêu chí2 × 0.3) + (tiêu chí3 × 0.3) + (tiêu chí4 × 0.4)
  ĐẠT nếu: Điểm tổng ≥ [NGƯỠNG, mặc định 8.0] VÀ mỗi tiêu chí 2,3,4 ≥ [TỐI THIỂU, mặc định 6.0]
```

*Bạn có thể đổi trọng số (VD: nếu lo nhất về tính khả thi build, tăng tiêu chí 4 lên 50%), hoặc đổi ngưỡng 8.0/6.0 tùy độ khắt khe mong muốn.*

---

## 4. Cấu hình lịch sử cho Agent 4 — CHỈNH SỬA ĐƯỢC

> Vá lỗ hổng #4/#5 (đánh số theo yêu cầu của bạn — đây là "Agent 4 không có lịch sử").

Mỗi lần gọi Agent 4, payload bắt buộc phải chứa:

```json
{
  "current_version": {
    "idea": "...",
    "agent3_scores": {...},
    "weakest_criterion": "...",
    "weakest_reason": "..."
  },
  "history": [
    {
      "round": 1,
      "idea": "...",
      "agent3_scores": {...},
      "rejection_reason": "..."
    },
    {
      "round": 2,
      "idea": "...",
      "agent3_scores": {...},
      "rejection_reason": "..."
    }
  ],
  "instruction": "Đề xuất giải pháp mới. KHÔNG được đề xuất lại bất kỳ hướng nào đã xuất hiện trong history và bị từ chối vì cùng lý do. Nếu weakest_criterion là 'khớp build direction' hoặc liên quan độc quyền, giải pháp mới PHẢI khác về bản chất (đối tượng/cơ chế), không chỉ đổi câu chữ."
}
```

*Cấu hình bạn có thể chỉnh:* số lượng vòng lịch sử tối đa gửi kèm (mặc định: toàn bộ, nhưng nếu context quá dài có thể giới hạn 3 vòng gần nhất + tóm tắt các vòng cũ hơn).

---

## 5. Trạng thái "vô danh" của Agent 3 — chống nương tay

> Vá lỗ hổng #8.

Agent 3 **không được nhận** các trường sau trong payload: số thứ tự vòng lặp, số lần ý tưởng này đã bị từ chối trước đó, hoặc bất kỳ tín hiệu nào cho biết đây là bản đã sửa nhiều lần. Payload gửi tới Agent 3 luôn có format giống hệt nhau dù là lần chấm thứ 1 hay thứ 4:

```json
{
  "idea": "...",
  "rubric": "(bảng mục 3)",
  "instruction": "Chấm điểm ý tưởng này như thể đây là lần đầu tiên bạn thấy nó."
}
```

---

## 6. Cấu hình rubric cho Agent 5 — CHỈNH SỬA ĐƯỢC

> Vá lỗ hổng #6: Agent 5 cần phản biện đúng thứ Agent 3 sẽ chấm, không phản biện tự do.

Agent 5 nhận **cùng bảng rubric ở mục 3** + **cùng blacklist đã dùng ở Agent 2**, và phải trả lời checklist sau cho giải pháp của Agent 4 trước khi cho qua:

| Câu hỏi kiểm tra | Nếu "Có" → |
|---|---|
| Giải pháp mới có còn khớp build direction đã chọn không? | Nếu không → trả về Agent 4 |
| Giải pháp mới có trùng/gần giống bất kỳ mục nào trong blacklist không? | Nếu có → trả về Agent 4, kèm tên sản phẩm trùng |
| Giải pháp mới có thực sự khắc phục ĐÚNG `weakest_reason` mà Agent 3 nêu ở vòng trước không, hay né tránh sang vấn đề khác? | Nếu né tránh → trả về Agent 4 |
| Giải pháp mới có phát sinh rủi ro mới ở tiêu chí khác (VD: sửa cho khả thi hơn nhưng làm giảm giá trị) không? | Nếu có → ghi chú cảnh báo, chuyển tiếp Agent 6 kèm cảnh báo để cân đối |

*Bạn có thể thêm/bớt dòng trong checklist này tùy mức độ khắt khe muốn Agent 5 áp dụng.*

---

## 7. Xử lý khi hết vòng lặp (max_loop) mà vẫn "Chưa đạt"

> Vá lỗ hổng #7.

```
Khi vòng lặp = max_loop (mặc định 3) VÀ Agent 3 vẫn trả "CHƯA ĐẠT":
  → DỪNG workflow
  → Xuất "BÁO CÁO KẾT THÚC KHÔNG THÀNH CÔNG" gồm:
      - Toàn bộ lịch sử các phiên bản đã thử (idea + điểm số từng vòng)
      - Tiêu chí nào LIÊN TỤC là điểm yếu nhất qua các vòng (dấu hiệu lỗi
        cấu trúc, không phải lỗi diễn đạt)
      - Khuyến nghị: "Nên pivot sang ý tưởng gốc khác" hay "Nên nới ngưỡng
        đánh giá" — tùy vào việc điểm số có xu hướng tăng dần (gần đạt,
        thử thêm vòng) hay giậm chân tại chỗ (đổi hướng hẳn)
```

---

## 8. Bảng cấu hình tổng hợp (đặt ở đầu file khi triển khai thật)

```yaml
batch_size: 6             # số lượng ý tưởng sinh trong 1 lần chạy (mặc định: 6)
max_gen2_retry: 3        # số lần Agent 1 được sinh lại nếu Agent 2 báo trùng
max_loop: 3               # số vòng Agent 3 → Agent 4/5/6 → Agent 3
agent3_threshold_avg: 8.5
agent3_threshold_min_per_criterion: 7.0
agent3_weights:
  gan_gui_thiet_thuc: 0.4
  gia_tri: 0.4
  kha_thi_codex: 0.2
history_window: full      # hoặc số nguyên, VD: 3 (chỉ gửi 3 vòng gần nhất)
```

