# BÁO CÁO THẨM ĐỊNH Ý TƯỞNG: Shopee LiveStream Sentry: Real-Time Multimodal Flash-Bargain & Compliance Copilot

## 1. Chi tiết diễn biến từng vòng

### Vòng 1: Khởi tạo & Kiểm tra Độc quyền
- **Agent 1 (Ideator):** Đề xuất ý tưởng *Shopee LiveStream Sentry: Real-Time Multimodal Flash-Bargain & Compliance Copilot* thuộc nhóm *AI-Native Products & Operations*. Vấn đề cốt lõi: Livestream kéo dài 4-8 tiếng khiến host kiệt sức, không thể đọc kịp hàng nghìn bình luận xin giảm giá/hỏi size để chốt đơn đúng nhịp; đồng thời đối mặt rủi ro bị khóa phòng live tức thì do vô tình phát ngôn từ cấm hoặc vi phạm chính sách sàn.
- **Agent 2 (Novelty Checker):** Kết luận **HỢP LỆ (PASS)**. Khác biệt với tool quản lý chat hay bot tự chốt đơn tĩnh: Đây là AI-Native Copilot đa phương thức kết hợp giữa can thiệp chính sách (Compliance Guardrail) và định giá voucher theo thời gian thực (Dynamic Yield Management) cho Shopee Live.

### Vòng 2: Chấm điểm Rubric Vô danh (Agent 3 - Stateless)
- **Gate (Build Direction):** PASS
- **Tiêu chí 2 (Gần gũi & Thiết thực - 30%):** 9.2 / 10
- **Tiêu chí 3 (Giá trị mang lại - 30%):** 8.7 / 10
- **Tiêu chí 4 (Khả thi 7h Codex - 40%):** 8.4 / 10
- **Điểm tổng kết:** **8.73 / 10** $\rightarrow$ **ĐẠT** (Vượt ngưỡng 8.0/10).
- **Điểm yếu nhất:** Khả thi build 7h Codex (8.4/10) — *Cần đảm bảo dữ liệu audio giả lập được trích xuất text nhanh qua Whisper/OpenAI Audio API để không bị trễ khung hình khi demo live.*

### Vòng 3: Tinh chỉnh Cấu trúc & Tự phản chiếu (Agent 4, 5, 6)
- **Agent 4:** Chuẩn hóa giao diện thành kiến trúc *Unified Split-Screen Operations Cockpit* (Single 16:9 Dashboard) để Codex build trong 3.5h, loại bỏ nguy cơ phân tán UI.
- **Agent 5:** Duyệt giải pháp theo Checklist Mục 6, yêu cầu tích hợp chế độ 1-Click Auto-Pilot Demo.
- **Agent 6:** Tổng hợp hồ sơ dự thi hoàn chỉnh, xác nhận độ trôi dạt độc quyền là 0% (100% Safe).

---

## 2. HỒ SƠ Ý TƯỞNG

* **Tên sản phẩm**: **Shopee LiveStream Sentry: Real-Time Multimodal Flash-Bargain & Compliance Copilot**  
  *Slogan*: *"AI-Native Live Commerce Arbitrage — Transforming 4-Hour Live Sessions into Dynamic Autonomous Profit Engines."*
* **Build Direction**: **AI-Native Products & Operations (Primary) + Deep-Domain AI (Shopee Live Commerce)**
* **Bối cảnh (thực trạng hiện nay)**:  
  Tại Đông Nam Á (Việt Nam, Thái Lan, Indonesia), mô hình bán hàng qua Livestream (Shopee Live, TikTok Shop) đang bùng nổ chiếm từ 35% đến 40% tổng GMV toàn sàn. Hàng triệu nhà bán hàng và KOC/Host phải phát sóng trực tiếp từ 4 đến 8 tiếng mỗi ngày với hàng chục nghìn lượt người xem cùng lúc.
* **Hậu quả**:  
  1. **Thiệt hại doanh thu do lỡ nhịp 'thời điểm vàng' (Conversion Drop-off)**: Khi mắt xem tăng đột biến (ví dụ lúc có 5.000 người cùng xem), hàng nghìn bình luận dồn dập xin voucher, hỏi kích thước hoặc rủ nhau mua chung. Host live chỉ có 2 mắt 1 miệng, hoàn toàn bất lực trong việc đọc chat. Cơ hội chốt 200–300 đơn trong 60 giây trôi qua trong tích tắc, tỷ lệ thoát phòng live tăng 45% sau mỗi 2 phút chờ đợi.
2. **Nguy cơ 'chết kênh' tức thì do vi phạm chính sách (Sudden De-platforming Risk)**: Shopee và các sàn TMĐT áp dụng hệ thống quét AI kiểm duyệt ngày càng khắt khe. Chỉ cần host lỡ miệng nói các từ nhạy cảm ('chuyển khoản ngoài', 'qua Zalo', 'hàng rep', cam kết chữa bệnh, lộ số điện thoại), phòng live lập tức bị bóp tương tác, trừ điểm vận hành, hoặc bị ngắt sóng trực tiếp giữa chừng. Thiệt hại mỗi lần bị sập live ước tính từ 50.000.000 đến hàng trăm triệu đồng doanh thu cùng chi phí quảng cáo đổ sông đổ biển.
* **Giải pháp và Kiến trúc giải pháp**:  
  **Cơ chế giải pháp cốt lõi**:
Hệ thống là một **AI-Native Multimodal Copilot** tự hành chạy ngầm song song với buổi livestream, hoạt động theo mô hình *Listen -> Analyze -> Protect -> Monetize*:
- **Lắng nghe & Quan sát đa phương thức**: Đồng bộ luồng âm thanh host đang nói (STT qua Whisper/OpenAI Audio) và luồng tin nhắn bình luận (chat stream) thời gian thực.
- **Can thiệp vi phạm chủ động (Live Policy Guardrail)**: Tự động đối chiếu phát ngôn của host với bảng từ khóa cấm/chính sách cập nhật của Shopee theo thời gian thực (độ trễ < 0.8s). Nếu host chuẩn bị nói từ rủi ro, hệ thống lập tức nháy đèn đỏ trên màn hình nhắc nhở hoặc tự động mute micro 1 giây để cứu kênh.
- **Tự động kích hoạt Voucher chớp nhoáng (Autonomous Flash-Bargain Injection)**: Khi AI phát hiện lượng lớn bình luận có cùng ý định mua (Group Buying Intent, ví dụ: 'giảm 20k mua luôn', 'deal hời chốt ngay'), hệ thống tự động kích hoạt API sàn phát hành voucher độc quyền giới hạn 50 mã trong đúng 45 giây và ghim thẳng lên đầu giỏ hàng.

**Kiến trúc giải pháp (Unified Split-Screen Operations Cockpit)**:
Ứng dụng 1 màn hình tỷ lệ 16:9 duy nhất gồm 4 panels:
- **Panel 1 (Live Stream Intake Simulator)**: Mô phỏng video feed host đang livestream và luồng chat bình luận chạy tốc độ cao.
- **Panel 2 (Real-Time Intent & Compliance Sentry)**: Hiển thị bảng phân tích cảm xúc (Sentiment Analysis), radar phát hiện nhu cầu mua sắm tập thể, và cột đo rủi ro vi phạm từ cấm (Policy Violation Risk Gauge).
- **Panel 3 (Autonomous Action Engine)**: Hiển thị nhật ký gọi API tự động (`inject_flash_voucher`, `pin_product_to_cart`, `trigger_host_teleprompter_alert`).
- **Panel 4 (Live Financial Uplift Matrix)**: Biểu đồ tăng trưởng GMV thời gian thực, số lượng đơn chốt tức thì, và số lần ngăn chặn thành công nguy cơ bị phạt/khóa kênh.
* **Kịch bản Demo (rõ ràng)**:  
  **Kịch bản Demo 3 phút chuẩn chỉnh cho Ban Giám Khảo (180 giây)**:
- **00:00 - 00:45 (Hook & Problem)**: Mở giao diện Cockpit với 1 video livestream Shopee đang có 3.200 người xem. Chat cuộn chóng mặt với hàng trăm người hỏi: 'Mã giảm giá áo đâu shop?', 'Giảm thêm 30k mình lấy 3 chiếc'. Host đang bận giới thiệu sản phẩm khác và hoàn toàn không để ý.
- **00:45 - 01:30 (Action 1: Cứu kênh khỏi lệnh cấm)**: Host vô tình nói: 'Mọi người nhắn qua Zalo riêng để được ship rẻ...'. Panel 2 lập tức lóe đỏ cảnh báo `[CRITICAL: External Platform Redirection Violation]`. Panel 3 tự động kích hoạt lời nhắc khẩn cấp trên màn hình nhắc chữ (Teleprompter): 'ĐỔI LỜI: MUA NGAY TRÊN SHOPEE ĐƯỢC FREESHIP EXTRA'. Phòng live thoát án phạt trong gang tấc.
- **01:30 - 02:20 (Action 2: Chốt Flash-Sale tự động trong 45s)**: AI phát hiện 85 bình luận cùng hỏi mua mẫu áo khoác. Panel 3 tự động kích hoạt Tool Call `inject_flash_voucher(amount=25k, qty=50, duration=45s)`. Trên Panel 1, voucher lập tức được ghim lên giỏ hàng. Chat bùng nổ 'Đã chốt', 'Đã mua'. Panel 4 ghi nhận: *Chốt 50 đơn trong 38 giây, tăng thêm 12.500.000 VNĐ GMV*.
- **02:20 - 03:00 (Tech Stack & Codex Value)**: Trình bày cách Codex sinh toàn bộ giao diện Next.js + FastAPI WebSocket stream chỉ trong 3.5 tiếng, sử dụng Pydantic Structured Outputs đảm bảo logic voucher không bao giờ cấp vượt ngân sách của nhà bán hàng.

---

## 3. Trạng thái hệ thống cập nhật

```json
{
    "idea_id": 1,
    "title": "Shopee LiveStream Sentry: Real-Time Multimodal Flash-Bargain & Compliance Copilot",
    "build_direction": "AI-Native Products & Operations (Primary) + Deep-Domain AI (Shopee Live Commerce)",
    "final_score": 8.73,
    "verdict": "ĐẠT",
    "status": "APPROVED_FOR_HACKATHON",
    "generated_file": "generated_ideas/idea_1_shopee_livestream_sentry.md"
}
```
